# AI 每日精选

中文 AI 博客，使用 [Jekyll](https://jekyllrb.com/) 和 GitHub Pages 内置的 [minima](https://github.com/jekyll/minima) 主题。站点地址是 <https://yum412517-gif.github.io>。

合并到 `main` 后，GitHub Pages 会用仓库里已有的设置自动构建：源为 **Deploy from a branch**，分支 `main`，目录 `/`（根目录）。不需要改成 GitHub Actions。

## 添加一篇新文章

1. 在 `_posts/` 新建 Markdown 文件。文件名必须是：

   ```text
   YYYY-MM-DD-英文短标题.md
   ```

   例如：`_posts/2026-10-21-prompt-checklist.md`

   - 文件名里的日期就是发布日期。首页和分类页都按这个日期**从新到旧**排列。
   - 日期和标题之间、单词之间用半角连字符 `-`。不要用空格，也不要在文件名里写中文。
   - 读者看到的标题写在 front matter 的 `title` 里，可以用中文。

2. 在文件最上面写 front matter。字段如下：

   ```yaml
   ---
   layout: post
   title: 文章标题
   date: 2026-10-21 09:00:00 +0800
   categories:
     - AI 新技术
   excerpt: 一句话摘要，会显示在首页列表里。
   ---
   ```

   | 字段 | 要求 |
   | --- | --- |
   | `layout` | 固定写 `post`。 |
   | `title` | 文章标题，可以用中文。 |
   | `date` | 带时区的发布时间，建议 `+0800`。应和文件名里的日期是同一天。 |
   | `categories` | YAML 列表。只能使用下面三个名称，必须逐字一致。 |
   | `excerpt` | 可选。首页摘要；不写时会截取正文第一段。 |

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

4. 把改动合并到 `main`。GitHub Pages 构建完成后，文章会出现在首页、对应分类和 [RSS](https://yum412517-gif.github.io/feed.xml)。

示例见 `_posts/2026-10-20-welcome.md`。

## 本地预览

```bash
bundle install
bundle exec jekyll serve
```

浏览器打开 <http://127.0.0.1:4000>。`Gemfile` 使用 `github-pages` gem，版本与 GitHub Pages 构建环境一致。

## 页面

- `/` 文章列表，新文章在前
- `/about/` 关于
- `/categories/` 三个栏目
- `/feed.xml` Atom 订阅（RSS 阅读器可直接使用）

页脚 `_includes/footer.html` 里有一段注释掉的 GitHub Sponsors 按钮，目前不显示。不要删掉注释两边的 `<!-- -->`，除非打算正式启用。
