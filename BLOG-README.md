# Buoy blog — how it works

Every page here is a self-contained HTML file (same pattern as the main
site) — no build step required to deploy, just drop the files in your
GitHub Pages repo root exactly as they're arranged in this folder.

## Adding a new post

**Easiest path — ask Claude Code to do it.** Open this project in Claude
Code and say something like: "Add a new blog post titled '[your title]'
about [topic] — follow the same pattern as what-is-crm-data-drift.html."
It can read `build_blog.py` to see the pattern, write the new post content,
add it to the `POSTS` list, and regenerate the index for you.

**Doing it yourself:**
1. Open `build_blog.py`. Copy the `post = POSTS[0]` block's structure — add
   a new entry to the `POSTS` list at the top with your new post's slug,
   title, description, date, and excerpt.
2. Write the actual post content as a new Python string (copy the `post_body`
   variable as a starting structure), or just hand-edit a copy of
   `blog/_post-template.html` directly if you'd rather skip the script
   entirely for a one-off post.
3. If using the script: run `python3 build_blog.py` — this regenerates the
   post file, rebuilds `blog/index.html` to include it, and updates
   `sitemap.xml` automatically.
4. Commit and push the new/changed files.

## Why it's built this way

- **SEO/AEO basics are already wired in per page**: a real `<title>` and
  meta description, Open Graph tags, a canonical URL, and JSON-LD structured
  data (`BlogPosting` schema) on every post — this last one is specifically
  what helps AI answer engines (not just traditional search) understand and
  cite the content correctly.
- **`sitemap.xml` and `robots.txt`** at the site root tell crawlers every
  page exists and explicitly invite indexing — without these, a search
  engine has to stumble onto pages via links alone.
- **Every page shares the same nav, footer, audit-call modal, and HubSpot
  tracking script** as the main site, so a blog reader gets the exact same
  brand experience and can book a call without leaving the post.

## What's NOT done here, worth knowing

- No RSS feed yet — easy to add later if you want one, just not wired up now.
- No tagging/categories — fine for a handful of posts, worth adding once
  there are enough posts that a flat list stops being browsable.
- No image support built into the template beyond what plain HTML/CSS
  gives you — a post with a screenshot would need the image base64-encoded
  and inlined the same way the logo is, or hosted somewhere and linked to.
