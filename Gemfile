# frozen_string_literal: true

source "https://rubygems.org"

# Chirpy is not part of the github-pages gem, so Pages must build
# this site with GitHub Actions. See .github/workflows/pages-deploy.yml.
gem "jekyll-theme-chirpy", "~> 7.6"

# Ruby 3 does not ship webrick, which `jekyll serve` needs.
gem "webrick", "~> 1.8"

gem "html-proofer", "~> 5.0", group: :test

platforms :windows, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.2.0", :platforms => [:windows]
