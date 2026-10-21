#!/usr/bin/env python3
"""Checks for the README archive generator."""

import tempfile
import unittest
from pathlib import Path

from update_readme import load_posts, pretty_slug, render_readme


class UpdateReadmeTest(unittest.TestCase):
    def test_pretty_slug_matches_jekyll_title_token(self):
        self.assertEqual(pretty_slug("welcome"), "welcome")
        self.assertEqual(pretty_slug("Hello World"), "Hello-World")
        self.assertEqual(pretty_slug("--keep_me--"), "keep_me")

    def test_groups_newest_first_and_uses_front_matter(self):
        with tempfile.TemporaryDirectory() as tmp:
            posts = Path(tmp)
            (posts / "2026-09-02-older.md").write_text(
                "---\n"
                "title: 九月旧文\n"
                "date: 2026-09-02 09:00:00 +0800\n"
                "excerpt: 较早的一篇\n"
                "---\n",
                encoding="utf-8",
            )
            (posts / "2026-10-20-welcome.md").write_text(
                "---\n"
                "title: 欢迎来到 AI 每日精选\n"
                "date: 2026-10-20 08:00:00 +0800\n"
                "excerpt: 这里会用中文更新人工智能的新技术、最佳实践和实用干货。\n"
                "---\n",
                encoding="utf-8",
            )
            (posts / "2026-10-21-later.md").write_text(
                "---\n"
                "title: 后一篇\n"
                "date: 2026-10-21 08:00:00 +0800\n"
                "excerpt: >\n"
                "  跨行\n"
                "  摘要\n"
                "---\n",
                encoding="utf-8",
            )
            (posts / "notes.md").write_text("---\ntitle: skip\n---\n", encoding="utf-8")

            rendered = render_readme(load_posts(posts))

        october = rendered.split("**十月**", 1)[1].split("## 2026", 1)[0]
        self.assertLess(rendered.find("**十月**"), rendered.find("**九月**"))
        self.assertLess(october.find("后一篇"), october.find("欢迎来到 AI 每日精选"))
        self.assertIn(
            "- 2026-10-20 [欢迎来到 AI 每日精选]"
            "(https://yum412517-gif.github.io/2026/10/20/welcome/)："
            "这里会用中文更新人工智能的新技术、最佳实践和实用干货。",
            rendered,
        )
        self.assertIn("跨行 摘要", rendered)
        self.assertNotIn("skip", rendered)
        self.assertIn("Star 本仓库获取每日更新", rendered)
        self.assertIn("https://yum412517-gif.github.io/feed.xml", rendered)

    def test_same_day_later_clock_comes_first(self):
        with tempfile.TemporaryDirectory() as tmp:
            posts = Path(tmp)
            (posts / "2026-10-20-morning.md").write_text(
                "---\ntitle: 早上\ndate: 2026-10-20 08:00:00 +0800\nexcerpt: 早\n---\n",
                encoding="utf-8",
            )
            (posts / "2026-10-20-evening.md").write_text(
                "---\ntitle: 晚上\ndate: 2026-10-20 21:00:00 +0800\nexcerpt: 晚\n---\n",
                encoding="utf-8",
            )
            rendered = render_readme(load_posts(posts))
        self.assertLess(rendered.find("晚上"), rendered.find("早上"))


if __name__ == "__main__":
    unittest.main()
