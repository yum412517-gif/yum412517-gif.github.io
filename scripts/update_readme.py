#!/usr/bin/env python3
"""Regenerate README.md from _posts front matter.

The GitHub README is an archive index. Post URLs follow the Jekyll permalink
in _config.yml: /:year/:month/:day/:title/
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

SITE_URL = "https://yum412517-gif.github.io"
REPO_URL = "https://github.com/yum412517-gif/yum412517-gif.github.io"
POST_FILENAME = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)$")
FRONT_MATTER_KEY = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
DATE_IN_VALUE = re.compile(r"(\d{4})-(\d{1,2})-(\d{1,2})")
CLOCK_IN_VALUE = re.compile(r"(\d{2}):(\d{2})(?::(\d{2}))?")
PRETTY_KEEP = set("._~!$&'()+,;=@")
MONTHS = (
    "",
    "一月",
    "二月",
    "三月",
    "四月",
    "五月",
    "六月",
    "七月",
    "八月",
    "九月",
    "十月",
    "十一月",
    "十二月",
)


@dataclass(frozen=True)
class Post:
    year: int
    month: int
    day: int
    sort_key: tuple
    title: str
    excerpt: str
    url: str


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_front_matter(text: str) -> dict[str, str]:
    """Read the scalar fields this index needs. Lists are ignored."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    data: dict[str, str] = {}
    index = 1
    while index < len(lines):
        line = lines[index]
        if line.strip() == "---":
            break
        match = FRONT_MATTER_KEY.match(line)
        if not match or line.startswith((" ", "\t")):
            index += 1
            continue
        key, raw = match.group(1), match.group(2).strip()
        if raw in {">", ">-", "|", "|-", "|+"}:
            index += 1
            chunks: list[str] = []
            while index < len(lines):
                nxt = lines[index]
                if nxt.strip() == "---":
                    break
                if nxt and not nxt.startswith((" ", "\t")):
                    break
                chunks.append(nxt.strip())
                index += 1
            data[key] = " ".join(part for part in chunks if part)
            continue
        if raw == "":
            index += 1
            continue
        data[key] = unquote(raw)
        index += 1
    return data


def pretty_slug(slug: str) -> str:
    """Match Jekyll's :title token: slugify(slug, mode='pretty', cased=True)."""
    pieces: list[str] = []
    pending_hyphen = False
    for char in slug:
        if char.isalnum() or char in PRETTY_KEEP:
            pieces.append(char)
            pending_hyphen = False
        elif pieces and not pending_hyphen:
            pieces.append("-")
            pending_hyphen = True
    return "".join(pieces).strip("-")


def calendar_date(value: str) -> tuple[int, int, int] | None:
    match = DATE_IN_VALUE.search(value or "")
    if not match:
        return None
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def one_line(value: str) -> str:
    return " ".join(value.replace("\r", " ").split())


def escape_link_text(value: str) -> str:
    return one_line(value).replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def load_posts(posts_dir: Path) -> list[Post]:
    posts: list[Post] = []
    if not posts_dir.is_dir():
        return posts

    for path in sorted(posts_dir.iterdir()):
        if not path.is_file() or path.suffix.lower() not in {".md", ".markdown"}:
            continue
        match = POST_FILENAME.match(path.stem)
        if not match:
            print(f"skip {path.name}: filename is not YYYY-MM-DD-slug", file=sys.stderr)
            continue

        file_year, file_month, file_day = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
        meta = parse_front_matter(path.read_text(encoding="utf-8"))
        dated = calendar_date(meta.get("date", "")) or (file_year, file_month, file_day)
        year, month, day = dated
        slug = pretty_slug(match.group(4))
        if not slug:
            print(f"skip {path.name}: empty slug", file=sys.stderr)
            continue
        title = one_line(meta.get("title", "")) or slug
        excerpt = one_line(meta.get("excerpt", ""))
        url = f"{SITE_URL}/{year:04d}/{month:02d}/{day:02d}/{slug}/"
        clock = CLOCK_IN_VALUE.search(meta.get("date", ""))
        clock_key = (
            int(clock.group(1)),
            int(clock.group(2)),
            int(clock.group(3) or 0),
        ) if clock else (0, 0, 0)
        posts.append(
            Post(
                year=year,
                month=month,
                day=day,
                sort_key=(year, month, day, clock_key, path.name),
                title=title,
                excerpt=excerpt,
                url=url,
            )
        )

    posts.sort(key=lambda post: post.sort_key, reverse=True)
    return posts


def format_entry(post: Post) -> str:
    date = f"{post.year:04d}-{post.month:02d}-{post.day:02d}"
    title = escape_link_text(post.title)
    line = f"- {date} [{title}]({post.url})"
    if post.excerpt:
        line += f"：{post.excerpt}"
    return line


def render_archive(posts: list[Post]) -> str:
    if not posts:
        return "还没有文章。\n"

    lines: list[str] = []
    current_year = None
    current_month = None
    for post in posts:
        if post.year != current_year:
            if lines:
                lines.append("")
            lines.append(f"## {post.year}")
            lines.append("")
            current_year = post.year
            current_month = None
        if post.month != current_month:
            if current_month is not None:
                lines.append("")
            lines.append(f"**{MONTHS[post.month]}**")
            lines.append("")
            current_month = post.month
        lines.append(format_entry(post))
    lines.append("")
    return "\n".join(lines)


def render_readme(posts: list[Post]) -> str:
    archive = render_archive(posts).rstrip() + "\n"
    return (
        "# AI 每日精选\n"
        "\n"
        "每天的 AI 新闻 + 对行业、公司和普通人的机会解读 + 实操教程。\n"
        "\n"
        f"站点：<{SITE_URL}>\n"
        "\n"
        f"RSS：[/feed.xml]({SITE_URL}/feed.xml)\n"
        "\n"
        f"**[Star 本仓库获取每日更新]({REPO_URL})**\n"
        "\n"
        "## 往期目录\n"
        "\n"
        f"{archive}"
        "\n"
        "文章格式见 [CONTRIBUTING.md](CONTRIBUTING.md)。"
        "往期目录由 `scripts/update_readme.py` 根据 `_posts` 的标题、日期和摘要生成。\n"
    )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    readme = render_readme(load_posts(root / "_posts"))
    destination = root / "README.md"
    destination.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
