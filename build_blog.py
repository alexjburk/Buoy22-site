import sys
sys.path.insert(0, '.')
import json
from blog_generator import build_page

SITE_URL = "https://buildwithbuoy.com"

# ---------------------------------------------------------------------------
# Post registry — adding a future post means adding one entry here (plus the
# actual post HTML file). This dict is also what builds the blog index page,
# so the two never drift out of sync.
# ---------------------------------------------------------------------------
POSTS = [
    {
        "slug": "what-is-crm-data-drift",
        "title": "What Is CRM Data Drift? Why Your Sales Team Can't See It",
        "description": "CRM data drift is the gap between what your team is supposed to do and what your CRM actually shows. Here's what causes it, and why nobody notices until forecasting breaks.",
        "date": "2026-09-15",
        "date_display": "September 15, 2026",
        "excerpt": "Nobody deletes their sales process on purpose. It erodes one skipped field at a time — and by the time it shows up in a missed forecast, it's already been happening for months."
    }
]


def json_ld_for_post(post):
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": {json.dumps(post['title'])},
  "description": {json.dumps(post['description'])},
  "datePublished": "{post['date']}",
  "dateModified": "{post['date']}",
  "author": {{"@type": "Organization", "name": "Buoy"}},
  "publisher": {{
    "@type": "Organization",
    "name": "Buoy",
    "logo": {{"@type": "ImageObject", "url": "{SITE_URL}/favicon.png"}}
  }},
  "mainEntityOfPage": {{"@type": "WebPage", "@id": "{SITE_URL}/blog/{post['slug']}.html"}}
}}
</script>"""


# ---------------------------------------------------------------------------
# Post 1
# ---------------------------------------------------------------------------
post = POSTS[0]

post_body = f"""
<p class="eyebrow">Published {post['date_display']}</p>
<h1 class="post-title">{post['title']}</h1>
<p class="post-meta">By the Buoy team · 6 min read</p>

<article class="post-body">
<p>Nobody deletes their sales process on purpose. A rep skips a required field once because they're in a hurry. Nobody notices, so nothing corrects it. Three months later, half the team has quietly adopted the same shortcut — not out of rebellion, just drift. That's CRM data drift: the slow, invisible gap between the process your business is supposed to run on and what your CRM actually shows.</p>

<p>It's different from a data-quality problem in the way people usually mean it. A typo in a phone number is an error. Drift is subtler — the data isn't necessarily wrong, it's just no longer telling the truth about your process. A deal can have a perfectly valid-looking close date, a real dollar amount, and a normal-sounding next step, and still be completely disconnected from what your actual sales methodology says should be true at that stage.</p>

<h2>Why nobody notices until it's expensive</h2>

<p>Drift is asymptomatic by design. Every individual skipped field, every vague "will follow up" logged as a next step, looks harmless in isolation — it's one deal, one rep, one bad day. Nothing breaks. No error message fires. The CRM keeps working exactly as before, which is precisely the problem: a system that keeps functioning gives you no signal that what it's telling you has quietly stopped being true.</p>

<p>The cost shows up downstream, disconnected from the cause. Research on data quality broadly estimates organizations lose <a href="/#problem">15–25% of annual revenue</a> to exactly this kind of erosion — not from one catastrophic failure, but from thousands of small ones compounding. By the time it's visible, it usually looks like a forecasting problem, not a data problem: Xactly's 2024 benchmark found only one in five B2B sales orgs hit their forecast within 5% of target. Nobody traces a missed forecast back to a next-step field that quietly stopped meaning anything six months earlier — but that's usually exactly where it started.</p>

<h2>What drift actually looks like inside a real CRM</h2>

<p>We reviewed a real HubSpot Deal-object export while scoping a client audit: 391 properties, 230 of them custom-built for that specific business. 37% of those properties were filled in on fewer than 5% of records. Only 10% were filled in reliably, on more than 80% of records.</p>

<p>That's not a data-entry problem you fix with a training session. It's what drift looks like at scale: a CRM built with real intention, accumulating fields nobody enforces anymore, until the useful signal is buried under properties that technically exist but functionally don't.</p>

<h2>Why generic data-quality tools don't catch it</h2>

<p>Most CRM data-quality tools check whether a field is populated, correctly formatted, or duplicated. That catches typos and blanks — genuinely useful, but beside the point for drift. A field can be perfectly filled in and still be drifted: "Next step: followed up, will call again" isn't blank, isn't malformed, and would pass every formatting check that exists. It's also not a real commitment, has no date attached, and tells a manager nothing about whether this deal is actually progressing. Catching that requires knowing what your own sales process says a real next step looks like at this specific stage — which means the check has to be grounded in your process documentation, not a generic rule that ships the same for every company.</p>

<h2>The fix starts with writing the process down, honestly</h2>

<p>Drift can't be enforced against a process that only exists as institutional memory. The first real step is external and slightly uncomfortable: an honest audit of what your CRM's properties, workflows, and stages currently do, compared with what your sales process actually says should happen — not the version in the onboarding deck, the version reps are actually running today.</p>

<p>From there, enforcement is what keeps drift from creeping back in the moment the audit is over. That means catching it live, inside the CRM, the moment a record starts to disconnect from the process — not three months later in a quarterly review, once it's already shaped a dozen decisions.</p>

<blockquote>Drift isn't a data problem you fix once. It's a gap you have to keep watching, because it never stops trying to reopen.</blockquote>

<div class="post-cta">
  <h3>See what drift looks like in your own CRM</h3>
  <p>Buoy audits how your process is actually supposed to run, then flags the moment your CRM drifts from it — live, before it becomes a forecasting problem.</p>
  <button class="btn btn-primary" onclick="openAuditModal(event)">Book an audit call</button>
</div>
</article>
"""

html = build_page(
    title=post["title"] + " | Buoy",
    description=post["description"],
    canonical=f"{SITE_URL}/blog/{post['slug']}.html",
    body_html=post_body,
    og_type="article",
    json_ld=json_ld_for_post(post)
)

with open(f"blog/{post['slug']}.html", "w") as f:
    f.write(html)

print(f"wrote blog/{post['slug']}.html")

# ---------------------------------------------------------------------------
# Blog index — lists every post in POSTS, newest first
# ---------------------------------------------------------------------------
list_items = ""
for p in sorted(POSTS, key=lambda x: x["date"], reverse=True):
    list_items += f"""<div class="post-list-item">
  <p class="eyebrow">{p['date_display']}</p>
  <h2><a href="/blog/{p['slug']}.html">{p['title']}</a></h2>
  <p>{p['excerpt']}</p>
</div>
"""

index_body = f"""
<p class="eyebrow">Buoy</p>
<h1 class="post-title" style="font-size:32px;">Notes on CRM data, sales process, and what actually holds up at scale</h1>
{list_items}
"""

index_html = build_page(
    title="Blog | Buoy",
    description="Notes on CRM data quality, sales process adherence, and what it actually takes to scale a revenue team without the data falling apart.",
    canonical=f"{SITE_URL}/blog/",
    body_html=index_body
)

with open("blog/index.html", "w") as f:
    f.write(index_html)
print("wrote blog/index.html")

# ---------------------------------------------------------------------------
# Reusable template for future posts — copy this file, fill in the marked
# spots, add an entry to POSTS in this script (or just hand-edit both files
# if that's easier), rebuild the index.
# ---------------------------------------------------------------------------
template_body = """
<p class="eyebrow">Published [MONTH DAY, YEAR]</p>
<h1 class="post-title">[POST TITLE]</h1>
<p class="post-meta">By the Buoy team &middot; [X] min read</p>

<article class="post-body">
<p>[Opening paragraph. Lead with the actual point, not a windup.]</p>

<h2>[First section heading]</h2>
<p>[Section content.]</p>

<h2>[Second section heading]</h2>
<p>[Section content.]</p>

<blockquote>[Optional pull quote — one sharp sentence, not a summary.]</blockquote>

<div class="post-cta">
  <h3>See what drift looks like in your own CRM</h3>
  <p>Buoy audits how your process is actually supposed to run, then flags the moment your CRM drifts from it &mdash; live, before it becomes a forecasting problem.</p>
  <button class="btn btn-primary" onclick="openAuditModal(event)">Book an audit call</button>
</div>
</article>
"""

template_html = build_page(
    title="[POST TITLE] | Buoy",
    description="[One or two sentences — this is what shows in search results and gets cited by AI answer engines, so make it a real, specific summary, not a teaser.]",
    canonical=f"{SITE_URL}/blog/[slug].html",
    body_html=template_body,
    og_type="article"
)

with open("blog/_post-template.html", "w") as f:
    f.write(template_html)
print("wrote blog/_post-template.html")

# ---------------------------------------------------------------------------
# sitemap.xml — every real page, so search engines and AI crawlers can find
# all of it without depending on internal links alone
# ---------------------------------------------------------------------------
urls = [
    (f"{SITE_URL}/", "1.0"),
    (f"{SITE_URL}/blog/", "0.8"),
] + [(f"{SITE_URL}/blog/{p['slug']}.html", "0.7") for p in POSTS]

sitemap_entries = "\n".join(
    f"""  <url>
    <loc>{url}</loc>
    <priority>{priority}</priority>
  </url>""" for url, priority in urls
)

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_entries}
</urlset>
"""

with open("sitemap.xml", "w") as f:
    f.write(sitemap)
print("wrote sitemap.xml")

# ---------------------------------------------------------------------------
# robots.txt
# ---------------------------------------------------------------------------
robots = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""

with open("robots.txt", "w") as f:
    f.write(robots)
print("wrote robots.txt")

