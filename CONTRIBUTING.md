# 投稿说明

站点首页仍由 Jekyll 从 `_posts` 生成。仓库首页的「往期目录」不要手改，合并到 `main` 后，GitHub Actions 会在 `_posts` 有变动时运行 `scripts/update_readme.py` 并提交 `README.md`。

本地可以先生成一遍：

```bash
python3 scripts/update_readme.py
```

## 添加一篇新文章

1. 在 `_posts/` 新建 Markdown 文件。文件名必须是：

   ```text
   YYYY-MM-DD-英文短标题.md
   ```

   例如：`_posts/2026-10-21-prompt-checklist.md`

   - 文件名里的日期就是发布日期。首页、分类页和 README 往期目录都按这个日期**从新到旧**排列。
   - 日期和标题之间、单词之间用半角连字符 `-`。不要用空格，也不要在文件名里写中文。
   - 读者看到的标题写在 front matter 的 `title` 里，可以用中文。
   - 网址里的最后一段来自文件名里的短标题，例如上面的文件会发布到 `/2026/10/21/prompt-checklist/`。

2. 在文件最上面写 front matter。字段如下：

   ```yaml
   ---
   layout: post
   title: 文章标题
   date: 2026-10-21 09:00:00 +0800
   categories:
     - AI 新技术
   excerpt: 一句话摘要，会显示在首页和 README 往期目录里。
   ---
   ```

   | 字段 | 要求 |
   | --- | --- |
   | `layout` | 固定写 `post`。 |
   | `title` | 文章标题，可以用中文。 |
   | `date` | 带时区的发布时间，建议 `+0800`。应和文件名里的日期是同一天。 |
   | `categories` | YAML 列表。只能使用下面三个名称，必须逐字一致。 |
   | `excerpt` | 一句话摘要。README 往期目录直接使用这一行。 |

   三个栏目：

   - `AI 新技术`
   - `AI 最佳实践`
   - `AI 实用干货`

   一篇文章可以写一个或多个栏目。名称写错时，分类页不会把它算进对应栏目。

3. front matter 下面用 Markdown 写正文。代码块用围栏并标明语言，这样 Rouge 会做语法高亮：

   ````markdown
   ```python
   print("你好")
   ```
   ````

4. 把改动合并到 `main`。站点用 [Chirpy](https://github.com/cotes2020/chirpy-starter) 主题，由 GitHub Actions 工作流 `.github/workflows/pages-deploy.yml` 构建并发布（仓库 Settings → Pages → Source 必须是 **GitHub Actions**，不能再用 “Deploy from a branch”）。文章会出现在首页、对应分类和 [RSS](https://yum412517-gif.github.io/feed.xml)。若这次改动了 `_posts`，另一个 Actions 工作流会接着更新 README 往期目录。

示例见 `_posts/2026-10-20-welcome.md`。

## 本地预览

需要 Ruby 3.1 或更新版本。

```bash
bundle install
bundle exec jekyll serve
```

浏览器打开 <http://127.0.0.1:4000>。`Gemfile` 使用 `jekyll-theme-chirpy`，不使用 `github-pages` gem。Chirpy 依赖的插件不在 GitHub Pages 的内置白名单里，所以线上构建必须走 Actions。

文章里的 `excerpt` 会在构建时复制到 Chirpy 使用的 `description`，首页卡片和订阅摘要因此仍显示这一句。不要改 `_config.yml` 里文章的 `permalink`（`/:year/:month/:day/:title/`），否则已发布的地址和 README 往期目录会对不上。

不要在仓库里新增同名的 `_layouts` 或 `_includes` 去覆盖主题，除非确实要改 Chirpy 的版式。关于页在 `_tabs/about.md`，侧边栏其它页在 `_tabs/`。

## 页面

- `/` 文章列表，新文章在前
- `/about/` 关于
- `/categories/` 栏目（名称来自文章 front matter）
- `/archives/` 按时间归档
- `/feed.xml` Atom 订阅（RSS 阅读器可直接使用，主题自带，最近若干篇）
