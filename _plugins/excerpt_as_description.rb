# frozen_string_literal: true

# Chirpy's post cards and Atom feed read `description`.
# Existing posts store that one-line summary in `excerpt`, which the README
# archive script also reads. Copy it when `description` was left blank.
#
# `:post_init` runs before front matter is read, so this waits until the
# site has loaded every document.

Jekyll::Hooks.register :site, :post_read do |site|
  site.posts.docs.each do |post|
    description = post.data["description"]
    excerpt = post.data["excerpt"]
    next unless description.nil? || description.to_s.strip.empty?
    next if excerpt.nil? || excerpt.to_s.strip.empty?
    next unless excerpt.is_a?(String)

    post.data["description"] = excerpt
  end
end
