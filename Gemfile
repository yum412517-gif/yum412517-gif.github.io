source "https://rubygems.org"

# Same gem GitHub Pages uses to build the site.
# https://pages.github.com/versions.json
gem "github-pages", "~> 232", group: :jekyll_plugins

# Minimal Mistakes calls include_cached. github-pages 232 already depends on
# jekyll-include-cache 0.2.1, and that plugin is on the Pages whitelist, so
# Deploy from a branch can load it. No extra Pages Actions workflow.
gem "jekyll-include-cache", group: :jekyll_plugins

# Ruby 3 no longer ships webrick, which `jekyll serve` needs.
gem "webrick", "~> 1.8"
