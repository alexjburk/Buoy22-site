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
    },
    {
        "slug": "hubspot-crm-data-quality-playbook",
        "title": "The HubSpot CRM Data Quality Playbook",
        "description": "A RevOps playbook for HubSpot CRM data quality: required fields, property sprawl, stage integrity, freeform criteria, and when native tools stop.",
        "date": "2026-09-18",
        "date_display": "September 18, 2026",
        "excerpt": "If the portal looks complete but forecasts still miss and next steps say “will follow up,” you have a process problem dressed up as hygiene."
    },
    {
        "slug": "what-happens-in-a-crm-audit",
        "title": "What Actually Happens in a CRM Audit? A Property-by-Property Walkthrough",
        "description": "A CRM audit isn't a health score or a report — it's a structured, property-by-property review of what your CRM actually does, compared with what your process says it should. Here's the real method.",
        "date": "2026-09-21",
        "date_display": "September 21, 2026",
        "excerpt": "A CRM audit isn't a report you read once. It's a field-by-field decision process — and the decisions it produces are more specific than \"keep\" or \"delete.\""
    },
    {
        "slug": "signs-your-crm-data-has-drifted",
        "title": "10 Signs Your CRM Data Has Drifted (Before It Shows Up in Your Forecast)",
        "description": "Blank fields are easy to spot. Drift isn't — it's a field that looks completely normal and just isn't telling the truth anymore. Here are 10 concrete signs to check for.",
        "date": "2026-09-22",
        "date_display": "September 22, 2026",
        "excerpt": "Blank fields are easy to catch. Drift is harder — it's a field that looks completely normal and just isn't telling the truth anymore. Here's what to actually look for."
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
# Post 2
# ---------------------------------------------------------------------------
post = POSTS[1]

post2_article_html = """
<p>HubSpot data quality means required fields, clean picklists, stage gates, and ongoing audits of unused properties—not just duplicate cleanup. If the portal looks complete but forecasts still miss and next steps say “will follow up,” you have a process problem dressed up as hygiene.</p>
<hr />
<h2>What HubSpot CRM data quality actually means</h2>
<p>Most teams treat “data quality” as a cleanup project: merge duplicates, fix email formats, archive zombie deals. That work matters. It is also incomplete.</p>
<p>For RevOps, Sales Ops, and HubSpot admins, <strong>HubSpot CRM data quality</strong> is the degree to which records are:</p>
<ol>
<li><strong>Present</strong> — required fields are filled when the process says they must be.</li>
<li><strong>Consistent</strong> — picklists, lifecycle stages, and pipeline stages use shared definitions.</li>
<li><strong>Current</strong> — close dates, next steps, and ownership stay fresh enough to coach and forecast.</li>
<li><strong>Process-true</strong> — freeform fields and stage moves reflect real buyer progress, not theater.</li>
<li><strong>Governed</strong> — someone owns the data model, the SLAs, and the cleanup cadence.</li>
</ol>
<p>Duplicates and format errors sit in layers 1–2. Forecast trust and coaching quality live in layers 3–5. Native HubSpot is strong on presence and format. It is weaker on process-true freeform text and continuous enforcement while reps work a record.</p>
<h3>Scope: deals and every object that runs a process</h3>
<p>Deal pipeline hygiene gets the headlines because CROs feel forecast pain first. A durable HubSpot data quality program also covers:</p>
<div class="table-wrap"><table>
<thead>
<tr>
<th>Object</th>
<th>Why data quality matters</th>
<th>Typical failure mode</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Deals</strong></td>
<td>Forecast, stage conversion, coaching</td>
<td>Blank amount/close date; fake next steps; stage parking</td>
</tr>
<tr>
<td><strong>Contacts</strong></td>
<td>Routing, lifecycle, attribution</td>
<td>Lifecycle drift; duplicate personas; empty ICP fields</td>
</tr>
<tr>
<td><strong>Companies</strong></td>
<td>Account scoring, territory, ABM</td>
<td>Conflicting firmographics; missing parent/child links</td>
</tr>
<tr>
<td><strong>Tickets</strong></td>
<td>Support SLAs, CS handoffs</td>
<td>Skipped stages; freeform “resolution” with no taxonomy</td>
</tr>
<tr>
<td><strong>Custom objects</strong></td>
<td>Onboarding, renewals, implementations</td>
<td>Process documented in Notion, not enforced in CRM</td>
</tr>
</tbody>
</table></div>
<p>If you only clean deals, marketing and CS will keep writing into a different reality. Multi-object scope is not a nice-to-have; it is how GTM systems stay comparable quarter to quarter.</p>
<hr />
<h2>Why HubSpot data quality breaks</h2>
<h3>Property sprawl without retirement</h3>
<p>Every new campaign, integration, and “quick ask from sales” adds properties. Few get deleted. Over time, forms and workflows write into fields nobody reports on, while the fields leadership cares about stay optional. Sprawl is the silent tax on every new required-field project: reps do not know which fields matter, so they fill the ones that unblock a stage move and ignore the rest.</p>
<h3>Process theater</h3>
<p>A portal can show high completion rates and still be useless for coaching. Classic patterns:</p>
<ul>
<li>Next step = “Follow up next week” with no date, owner, or buyer action.</li>
<li>Closed-lost reason = “Other” or a free-text novel that cannot be rolled up.</li>
<li>Amount and close date filled once at creation, never revisited.</li>
<li>Stage moved forward because a gate asked for a field—and the field got a placeholder.</li>
</ul>
<p>Hygiene dashboards celebrate filled. Forecast meetings discover false.</p>
<h3>Forecast and leadership impact</h3>
<p>When stage definitions drift and freeform updates look complete but are not, leadership does not get a “slightly noisy” forecast. They get a confident wrong number. Ops then spends the quarter explaining variance instead of fixing the record-level behavior that created it. Industry commentary often cites large revenue and productivity costs from bad CRM data; whatever the external number, the internal cost is measurable: forecast miss size, time spent scrubbing pipeline before board packs, and coaching sessions that re-litigate what the CRM should already show.</p>
<h3>Ownership gaps</h3>
<p>If Marketing owns lifecycle, Sales owns pipeline stages, CS owns tickets, and “the HubSpot admin” owns properties without a RACI, quality becomes everyone’s problem and nobody’s job. Tools do not fix missing owners. Cadence without owners becomes another ignored Slack reminder.</p>
<hr />
<h2>Native HubSpot toolkit map: what each tool fixes (and what it doesn’t)</h2>
<p>Earn trust with the native stack first. HubSpot already ships useful data quality and enforcement features. Use them hard. Then be honest about the edges.</p>
<div class="table-wrap"><table>
<thead>
<tr>
<th>HubSpot capability</th>
<th>What it fixes well</th>
<th>What it does not fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Data Quality Command Center / Data Quality tools</strong></td>
<td>Surfaces formatting issues, incomplete records, and hygiene opportunities at portal scale; pairs with digests and remediation workflows</td>
<td>Does not define your sales process; does not judge whether a filled next step is useful; not a substitute for stage exit criteria</td>
</tr>
<tr>
<td><strong>Data Model Health Check</strong></td>
<td>Helps spot unused or underused properties and model complexity</td>
<td>Will not tell you which rare fields are still strategically required; cleanup still needs a decision matrix and stakeholder review</td>
</tr>
<tr>
<td><strong>Property validation rules</strong></td>
<td>Constrains formats, ranges, and some input patterns on properties</td>
<td>Blank ≠ quality for free text; complex process criteria (commitment + date + owner) usually exceed validation rules</td>
</tr>
<tr>
<td><strong>Required properties &amp; conditional stage properties</strong></td>
<td>Stops many blank fields at stage transition; excellent for minimum viable deal records</td>
<td>Gates fire mainly when someone tries to move stage; Super Admins, workflows, and API updates can bypass many UI rules; placeholders still pass</td>
</tr>
<tr>
<td><strong>Pipeline rules</strong> (skip stages, move backwards, approvals)</td>
<td>Protects stage integrity and reduces gaming of the board</td>
<td>Does not evaluate freeform quality; does not continuously flag drift while a deal sits in-stage</td>
</tr>
<tr>
<td><strong>Deduplication &amp; enrichment / Breeze-style data actions</strong></td>
<td>Reduces contact/company mess and fills firmographic gaps</td>
<td>Enrichment ≠ process adherence; a perfect company domain can still sit on a deal with a fake close date</td>
</tr>
<tr>
<td><strong>Workflows &amp; custom coded actions</strong></td>
<td>Can nag, route, or soft-block based on property logic</td>
<td>Fragile to maintain; easy to bypass; rarely evaluate semantic quality of freeform fields at scale</td>
</tr>
<tr>
<td><strong>Reports &amp; dashboards</strong></td>
<td>Discover completion %, stale close dates, stage conversion anomalies</td>
<td>Discover drift late—after the week’s forecast call, not while the rep is on the record</td>
</tr>
</tbody>
</table></div>
<p><strong>Takeaway:</strong> Native HubSpot is excellent at <strong>presence, format, and stage-transition control</strong>. Native HubSpot is limited at <strong>semantic freeform quality</strong> and <strong>continuous, in-record process enforcement</strong>. Audit products and hygiene platforms (including tools like PortalPilot and similar portal health scorers) help you <em>find</em> sprawl and broken configuration. They are complementary to—not the same as—live process markers on the record.</p>
<p>When you are ready to compare blank checks with deeper enforcement, see <a href="/blog/enforce-sales-process-hubspot">enforce sales process in HubSpot</a>.</p>
<hr />
<h2>The playbook scorecard: 6–8 metrics that matter</h2>
<p>Do not start with a 40-metric dashboard. Start with a scorecard your VP Sales will actually open. The table below is a <strong>playbook framework</strong> (illustrative thresholds you can tune)—not a published Buoy customer benchmark.</p>
<div class="table-wrap"><table>
<thead>
<tr>
<th>#</th>
<th>Metric</th>
<th>How to measure in HubSpot</th>
<th>Suggested starting target</th>
<th>What “bad” looks like</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><strong>Critical field completion %</strong></td>
<td>Report: open deals with Amount, Close Date, Deal Owner, Pipeline Stage known</td>
<td>≥95% on open pipeline</td>
<td>Below 90% → forecast is theater</td>
</tr>
<tr>
<td>2</td>
<td><strong>Stage-required compliance %</strong></td>
<td>Sample deals that entered a stage in the last 30 days; check conditional required properties</td>
<td>≥90% without Super Admin overrides</td>
<td>High override rate = gates are theater</td>
</tr>
<tr>
<td>3</td>
<td><strong>Unused / rare property share</strong></td>
<td>Property usage export or Data Model Health signals; % of custom properties filled on &lt;5% of relevant records</td>
<td>Trend down quarter over quarter; document before delete</td>
<td>Growing rare-property % = sprawl tax</td>
</tr>
<tr>
<td>4</td>
<td><strong>Close date staleness</strong></td>
<td>Open deals where Close Date is in the past, or unchanged for N days while stage unchanged</td>
<td>&lt;10% of open deals</td>
<td>Past close dates = sandbagging or neglect</td>
</tr>
<tr>
<td>5</td>
<td><strong>Next-step quality pass rate</strong></td>
<td>Manual or assisted review of a sample (e.g. 20–50 open deals): requires buyer-tied action + date + owner</td>
<td>≥80% of sample passes criteria</td>
<td>“Will follow up” dominates → coaching blind</td>
</tr>
<tr>
<td>6</td>
<td><strong>Closed-lost taxonomy health</strong></td>
<td>% closed-lost with a primary reason from an approved picklist (not Other/blank/free-text only)</td>
<td>≥90% mapped reasons</td>
<td>Other &gt;15% → taxonomy failure</td>
</tr>
<tr>
<td>7</td>
<td><strong>Duplicate / identity conflict rate</strong></td>
<td>Contacts/companies flagged by HubSpot DQ tools or merge queues</td>
<td>Trend down; clear SLA to clear queue</td>
<td>Growing queue = trust erosion at handoff</td>
</tr>
<tr>
<td>8</td>
<td><strong>Forecast variance vs. CRM snapshot</strong></td>
<td>Compare committed forecast to CRM weighted/pipeline snapshot at lock; track miss attribution to data vs. judgment</td>
<td>Data-attributed miss share trending down</td>
<td>Every miss blamed on “judgment” when records were incomplete</td>
</tr>
</tbody>
</table></div>
<h3>How to run the scorecard without buying anything new</h3>
<ol>
<li>Pick one pipeline and one quarter of history.</li>
<li>Build four lists/reports for metrics 1, 2, 4, and 7.</li>
<li>Spend 45 minutes on a next-step sample (metric 5) with a sales manager.</li>
<li>Export closed-lost for metric 6.</li>
<li>Review rare properties monthly (metric 3)—do not delete on day one.</li>
<li>Bring metric 8 to the forecast meeting as a standing slide.</li>
</ol>
<p>If metrics 1–2 look fine but 5–6 look terrible, you have already found Buoy’s wedge: <strong>filled ≠ true</strong>. Hygiene tools will congratulate you. Process quality will not.</p>
<hr />
<h2>A 10-day DIY HubSpot CRM data quality audit</h2>
<p>This outline is designed so a sharp RevOps pair can learn the truth of the portal. It also maps cleanly to when a productized <a href="https://buildwithbuoy.com/">Buoy Audit</a> (~$20k) is the better use of calendar time: multi-pipeline complexity, PE-style standardization pressure, or when freeform fail rates need quantification across objects.</p>
<h3>Day 1–2: Inventory and owners</h3>
<ul>
<li>Export custom properties for Deals, Contacts, Companies, Tickets (and any critical custom objects).</li>
<li>Note create date, group, form/workflow usage if available, and last known reporting use.</li>
<li>Name a temporary owner per object (even if “interim”).</li>
<li>Pull HubSpot Data Quality / Data Model Health views and screenshot the top issues.</li>
</ul>
<h3>Day 3: Critical path fields</h3>
<ul>
<li>With Sales leadership, lock the <strong>minimum viable deal record</strong>: typically Amount, Close Date, Owner, Stage, Next Step, and 1–2 ICP or MEDDICC-style fields you will actually coach on.</li>
<li>Document which fields are required at create vs. at specific stages.</li>
<li>Resist adding new properties during the audit.</li>
</ul>
<h3>Day 4–5: Property sprawl pass</h3>
<ul>
<li>Flag properties filled on &lt;5% of records in the last 12 months as <strong>rare</strong> (tune the threshold to your volume).</li>
<li>Separate HubSpot defaults from custom noise.</li>
<li>Build a keep / deprecate / delete shortlist (matrix in the next section)—do not delete yet.</li>
</ul>
<h3>Day 6: Stage integrity spot-check</h3>
<ul>
<li>For each open stage, pull 10 recent deals.</li>
<li>Ask: What buyer evidence should exist before this stage? What does the CRM actually show?</li>
<li>Note Super Admin overrides and workflow/API stage changes if you can see them in history.</li>
<li>Capture gaps for a future <a href="/blog/hubspot-deal-stage-exit-criteria">HubSpot deal stage exit criteria guide</a>.</li>
</ul>
<h3>Day 7: Freeform quality sample</h3>
<ul>
<li>Sample next steps and closed-lost notes.</li>
<li>Score pass/fail against written criteria (examples below).</li>
<li>Record fail themes: no date, no owner, internal task instead of buyer action, unusable Other.</li>
</ul>
<h3>Day 8: Multi-object skim</h3>
<ul>
<li>Repeat a lighter version of Days 3–7 for tickets or onboarding records if CS is in HubSpot.</li>
<li>Confirm lifecycle stage definitions still match Marketing’s current funnel language.</li>
</ul>
<h3>Day 9: Scorecard baseline</h3>
<ul>
<li>Fill the eight metrics for one pipeline.</li>
<li>Write a one-page “CRM risk” brief: what leadership believes vs. what records show.</li>
</ul>
<h3>Day 10: Decision meeting</h3>
<ul>
<li>Approve deprecations, stage-required changes, and taxonomy edits.</li>
<li>Decide DIY remediation vs. hiring help.</li>
<li>If the work expands into process redesign + enforcement design across objects, that is the natural handoff to a structured Audit engagement rather than another month of heroics.</li>
</ul>
<p><strong>When DIY is enough:</strong> one primary pipeline, engaged sales leadership, and willingness to delete/deprecate ruthlessly.</p>
<p><strong>When to book an Audit:</strong> sprawl across years of admins, PE portfolio comparison needs, or when you already know blank checks are not catching the forecast miss.</p>
<hr />
<h2>Property sprawl and unused properties: keep / deprecate / delete</h2>
<p>Unused properties are not just clutter. They confuse forms, slow onboarding of new reps, and make every “required field” conversation political. Use a decision matrix—not vibes.</p>
<h3>Decision matrix (printable)</h3>
<div class="table-wrap"><table>
<thead>
<tr>
<th>Signal</th>
<th>Keep</th>
<th>Deprecate (hide / stop writing)</th>
<th>Delete (after archive period)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Filled on ≥20% of relevant records in 12 months</td>
<td>Default keep</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>Filled on 5–20%, still in active reports or forecasts</td>
<td>Keep; document owner</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>Filled on &lt;5%, no report, no workflow, no form</td>
<td>—</td>
<td>First choice</td>
<td>After 60–90 days unused</td>
</tr>
<tr>
<td>Legal / finance / contractual retention</td>
<td>Keep or archive object</td>
<td>Never silent-delete</td>
<td>Only with counsel</td>
</tr>
<tr>
<td>Integration-owned (Salesforce sync, ERP, product DB)</td>
<td>Keep if integration live</td>
<td>Pause writes first</td>
<td>Only after integration owner signs off</td>
</tr>
<tr>
<td>Duplicate meaning (two “Industry” fields)</td>
<td>Keep the canonical one</td>
<td>Deprecate the alias</td>
<td>Delete alias after migration</td>
</tr>
<tr>
<td>One exec asked for it once, never used</td>
<td>—</td>
<td>Deprecate immediately</td>
<td>Delete after quiet period</td>
</tr>
<tr>
<td>Required by a stage gate but never coached</td>
<td>Revisit process first</td>
<td>Do not delete until gate redesign</td>
<td>—</td>
</tr>
</tbody>
</table></div>
<h3>Operating rules</h3>
<ol>
<li><strong>Document before you delete.</strong> Export definitions and sample values.</li>
<li><strong>Deprecate before delete.</strong> Remove from forms, workflows, and layouts; rename with a <code>z_deprecated_</code> prefix if your team needs a visual cue.</li>
<li><strong>Never enforce a field you plan to kill.</strong> Enforcement amplifies sprawl if the property is noise.</li>
<li><strong>Batch communications.</strong> Tell Sales and Marketing which fields disappeared and which remain canonical.</li>
</ol>
<p>A deeper property-only deep dive belongs in the follow-on pillar on <a href="/blog/hubspot-property-audit">HubSpot unused properties and property audits</a>. For this playbook, the point is simpler: <strong>you cannot have HubSpot CRM data quality on top of an infinite data model.</strong></p>
<hr />
<h2>Stage integrity and exit criteria (brief)</h2>
<p>Data quality and stage design are the same system. If anyone can skip from Discovery to Negotiation without evidence, your completion metrics will look fine while conversion math lies.</p>
<p>Exit criteria should be <strong>verifiable conditions</strong>—ideally buyer actions with CRM evidence—not rep opinions. Examples of the difference:</p>
<div class="table-wrap"><table>
<thead>
<tr>
<th>Weak (opinion)</th>
<th>Stronger (evidence-oriented)</th>
</tr>
</thead>
<tbody>
<tr>
<td>“Champion is engaged”</td>
<td>Champion identified + last activity logged within N days + next meeting booked</td>
</tr>
<tr>
<td>“Budget confirmed”</td>
<td>Amount updated + budget source field from approved picklist</td>
</tr>
<tr>
<td>“Demo completed”</td>
<td>Meeting outcome property + associated call/meeting on the timeline</td>
</tr>
</tbody>
</table></div>
<p>Native HubSpot supports much of this with conditional stage properties and pipeline rules. Those tools still primarily check <strong>presence at stage move</strong>. They do not continuously argue with a stale deal sitting in Commit with a close date that slipped three times.</p>
<p>Treat this section as the bridge to process enforcement content: <a href="/blog/hubspot-deal-stage-exit-criteria">HubSpot deal stage exit criteria guide</a> and <a href="/blog/enforce-sales-process-hubspot">enforce sales process in HubSpot</a>. Get the definitions right before you buy more automation.</p>
<hr />
<h2>Freeform field quality: where “filled in” still fails</h2>
<p>This is the educational heart of Buoy’s product wedge—stated plainly, without theater.</p>
<p>HubSpot can require that <strong>Next step</strong>, <strong>Closed-lost details</strong>, or <strong>Discovery notes</strong> are not blank. It cannot, natively and at scale, require that those strings meet your real process criteria.</p>
<h3>What good freeform looks like</h3>
<p><strong>Next step (pass examples)</strong></p>
<ul>
<li>“Buyer security review scheduled with Ana (CISO) for Oct 14; waiting on questionnaire return.”</li>
<li>“Send revised commercial proposal to Sam by Friday; decision meeting booked for Oct 21.”</li>
</ul>
<p><strong>Next step (fail examples)</strong></p>
<ul>
<li>“Follow up”</li>
<li>“Circling back next week”</li>
<li>“Working it”</li>
<li>A pasted email thread with no commitment</li>
</ul>
<p><strong>Closed-lost detail (pass examples)</strong></p>
<ul>
<li>Primary reason: Lost to competitor → Competitor: Acme → Detail: “Chose Acme for existing SSO; price within 8%.”</li>
<li>Primary reason: No decision / timing → Detail: “Budget pushed to FY27; champion left; no reopen date.”</li>
</ul>
<p><strong>Closed-lost detail (fail examples)</strong></p>
<ul>
<li>“Other”</li>
<li>“Not a fit”</li>
<li>A paragraph that cannot map to coaching or product feedback</li>
</ul>
<h3>A simple scoring rubric (use in the Day 7 sample)</h3>
<p>Give one point each:</p>
<ol>
<li>Names a <strong>buyer-tied action</strong> (not only an internal task).</li>
<li>Includes a <strong>date</strong> or clear timebox.</li>
<li>Names an <strong>owner</strong> (rep or buyer contact).</li>
<li>Would make sense to a manager who did not attend the last call.</li>
</ol>
<p>Three or four points = pass. Zero to two = fail. Track pass rate on the scorecard.</p>
<h3>Where Buoy for HubSpot fits (softly)</h3>
<p><strong>Buoy (buildwithbuoy.com)</strong> documents how your GTM/CRM process should run, then helps enforce it with a <strong>record-level overlay</strong> inside HubSpot. Native HubSpot can insist a field is filled; Buoy for HubSpot evaluates whether freeform fields meet your criteria and flags drift live on the record—not only when someone tries to change stage. Diagnostic and hygiene platforms remain useful for portal health scores and configuration sprawl; Buoy’s focus is process truth while the rep is still looking at the deal, ticket, or onboarding record.</p>
<p>If your scorecard shows strong completion and weak freeform pass rates, you are past “buy another cleanup tool.” You are in process documentation + enforcement territory—typically <strong>Audit → Validation</strong> (~$20k one-time, then ~$24k/yr ongoing).</p>
<hr />
<h2>Governance: owners, cadence, and SLAs</h2>
<p>Tools without governance recreate the same mess in six months. Keep governance lightweight enough that people follow it.</p>
<h3>RACI sketch (adapt, do not copy blindly)</h3>
<div class="table-wrap"><table>
<thead>
<tr>
<th>Decision</th>
<th>RevOps / Sales Ops</th>
<th>HubSpot Admin</th>
<th>VP Sales / CRO</th>
<th>Marketing Ops</th>
<th>CS Ops</th>
</tr>
</thead>
<tbody>
<tr>
<td>Canonical deal properties</td>
<td>A</td>
<td>R</td>
<td>C</td>
<td>I</td>
<td>I</td>
</tr>
<tr>
<td>Pipeline stages &amp; exit criteria</td>
<td>R</td>
<td>C</td>
<td>A</td>
<td>I</td>
<td>I</td>
</tr>
<tr>
<td>Lifecycle definitions</td>
<td>C</td>
<td>C</td>
<td>I</td>
<td>A/R</td>
<td>C</td>
</tr>
<tr>
<td>Ticket stages</td>
<td>C</td>
<td>C</td>
<td>I</td>
<td>I</td>
<td>A/R</td>
</tr>
<tr>
<td>Property create / deprecate</td>
<td>A</td>
<td>R</td>
<td>C</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>DQ scorecard review</td>
<td>R</td>
<td>C</td>
<td>A (quarterly)</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>Enforcement exceptions (Super Admin bypass policy)</td>
<td>A</td>
<td>R</td>
<td>C</td>
<td>I</td>
<td>I</td>
</tr>
</tbody>
</table></div>
<p>R = Responsible, A = Accountable, C = Consulted, I = Informed.</p>
<h3>Cadence that survives busy seasons</h3>
<div class="table-wrap"><table>
<thead>
<tr>
<th>Cadence</th>
<th>Ritual</th>
<th>Owner</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Weekly</strong></td>
<td>Clear DQ merge/format queues; spot-check 10 open deals for next-step quality</td>
<td>Admin + Sales manager rotate</td>
</tr>
<tr>
<td><strong>Monthly</strong></td>
<td>Scorecard update; rare-property watchlist; override audit</td>
<td>RevOps</td>
</tr>
<tr>
<td><strong>Quarterly</strong></td>
<td>Stage definition review; closed-lost taxonomy prune; deprecate batch</td>
<td>RevOps + CRO</td>
</tr>
<tr>
<td><strong>Annually</strong></td>
<td>Full property &amp; workflow sprawl review; integration owner re-attestation</td>
<td>RevOps + Admin</td>
</tr>
</tbody>
</table></div>
<h3>Example SLA language (tune thresholds)</h3>
<ul>
<li>Critical deal fields (Amount, Close Date, Owner): <strong>95% complete</strong> on open pipeline, measured weekly.</li>
<li>Past-due close dates on open deals: <strong>cleared or re-dated within 5 business days</strong>.</li>
<li>Duplicate contact merge queue: <strong>no item older than 10 business days</strong>.</li>
<li>New custom property requests: <strong>require owner, report/use case, and retirement criteria</strong> before create.</li>
<li>Stage gate overrides by Super Admin: <strong>logged and reviewed monthly</strong>; pattern = process redesign, not more exceptions.</li>
</ul>
<p>Governance is how HubSpot data hygiene becomes HubSpot data <strong>governance</strong>—the secondary query buyers actually mean when they search for lasting fixes.</p>
<hr />
<h2>Printable checklist: HubSpot CRM data quality (one page)</h2>
<p>Use this as the downloadable checklist companion to the playbook.</p>
<h3>Portal readiness</h3>
<ul>
<li>☐ Named owner per object (Deals, Contacts, Companies, Tickets)</li>
<li>☐ Minimum viable deal record documented (≤8 coached fields)</li>
<li>☐ Lifecycle and pipeline definitions written in one shared doc</li>
<li>☐ Super Admin override policy written (even if one paragraph)</li>
</ul>
<h3>Native HubSpot configured</h3>
<ul>
<li>☐ Data Quality tools / Command Center reviewed in last 30 days</li>
<li>☐ Data Model Health Check reviewed; rare properties listed</li>
<li>☐ Conditional stage properties set for critical blanks</li>
<li>☐ Pipeline rules reviewed (skip / backwards / approvals)</li>
<li>☐ Property validation rules on formats that break routing or billing</li>
</ul>
<h3>Measurement live</h3>
<ul>
<li>☐ Scorecard metrics 1–8 baselined for one pipeline</li>
<li>☐ Next-step sample scored with written pass/fail criteria</li>
<li>☐ Closed-lost picklist pruned; Other usage measured</li>
<li>☐ Forecast variance slide includes a data-quality attribution line</li>
</ul>
<h3>Sprawl control</h3>
<ul>
<li>☐ Keep / deprecate / delete matrix applied to top 50 custom properties</li>
<li>☐ No new properties without owner + use case + retirement rule</li>
<li>☐ Deprecated fields removed from forms and layouts</li>
</ul>
<h3>Process truth</h3>
<ul>
<li>☐ Exit criteria drafted per stage (buyer evidence, not opinion)</li>
<li>☐ Freeform fail themes shared with managers (not only admins)</li>
<li>☐ Decision made: DIY remediation vs. <a href="https://buildwithbuoy.com/">Book a Buoy Audit</a></li>
</ul>
<hr />
<h2>FAQ: HubSpot CRM data quality</h2>
<h3>What is HubSpot CRM data quality?</h3>
<p>HubSpot CRM data quality is how well records are complete, consistent, current, process-true, and governed—across deals and other objects—not merely how few duplicates you have. Required fields, clean picklists, stage gates, and unused-property audits are part of it; freeform field quality is the part most portals skip.</p>
<h3>How is data hygiene different from data governance in HubSpot?</h3>
<p>Hygiene is the ongoing cleanup (formats, duplicates, stale dates). Governance is the operating system: owners, definitions, create/deprecate rules, SLAs, and review cadence. Hygiene without governance is a recurring project. Governance makes hygiene cheaper.</p>
<h3>What does HubSpot’s Data Quality Command Center not do?</h3>
<p>It helps you find and remediate many formatting and completeness issues at portal scale. It does not define your sales process, judge whether a filled next step is useful, or continuously enforce exit criteria while a rep works a record. Treat it as necessary infrastructure—not as process enforcement.</p>
<h3>How do I audit unused HubSpot properties?</h3>
<p>Export or review property usage (and Data Model Health signals), flag fields filled on a small share of records (many teams start at &lt;5%), map each to keep / deprecate / delete, document before you remove anything, and get sign-off from integration and report owners. Do not delete on sight.</p>
<h3>Can HubSpot require high-quality freeform fields like “Next step”?</h3>
<p>HubSpot can require the field to be non-blank and can apply some validation patterns. It cannot natively and reliably enforce semantic criteria (buyer action + date + owner) the way a process-aware layer can. That gap is why filled portals still produce weak forecasts and weak coaching.</p>
<h3>How often should we run a HubSpot CRM data quality audit?</h3>
<p>Run a lightweight scorecard monthly and a deeper property/process audit at least annually—or after major org changes, CRM migrations, PE carve-outs/add-ons, or a painful forecast miss. Teams with heavy sprawl often need a structured reset (DIY 10-day audit or a productized Audit) before ongoing enforcement will stick.</p>
<h3>When are native HubSpot tools not enough?</h3>
<p>When completion rates look healthy but freeform fields fail process criteria; when gates are bypassed by workflows, API, or Super Admins; when drift happens between stage moves; or when you need the same process truth across deals, tickets, and onboarding—not just blank checks on one pipeline.</p>
<hr />
<h2>Soft CTA: checklist + Book Audit</h2>
<p>If you only do one thing after reading this playbook, baseline the scorecard on a single pipeline and score twenty next steps with a manager. That afternoon of honesty beats another quarter of dashboard theater.</p>
<p>When you want a structured reset—property sprawl decisions, multi-object process documentation, and a clear line between what native HubSpot should enforce and what needs live, in-record criteria—<a href="https://buildwithbuoy.com/">book a Buoy Audit</a> (productized HubSpot GTM/CRM process audit, typically ~$20k). Teams that need ongoing enforcement after the reset usually move into <strong>Buoy Validation</strong> (~$24k/yr). Enterprise and PE portfolio standardization builds on the same foundation: shared definitions first, then enforcement that makes them stick.</p>
<p>Buoy is <strong>Buoy for HubSpot</strong> at <a href="https://buildwithbuoy.com/">buildwithbuoy.com</a>—process documentation plus live enforcement inside HubSpot. It is not an unrelated “Buoy CRM” product elsewhere on the web.</p>
<p><strong>Download the checklist</strong> (use the printable section above) · <strong><a href="https://buildwithbuoy.com/">Book an Audit</a></strong> · Continue with <a href="/blog/enforce-sales-process-hubspot">enforce sales process in HubSpot</a></p>"""

post_body = f"""
<p class="eyebrow">Published {post['date_display']}</p>
<h1 class="post-title">{post['title']}</h1>
<p class="post-meta">By the Buoy team &middot; 25 min read</p>

<article class="post-body">
{post2_article_html}

<div class="post-cta">
  <h3>Start with the scorecard, not another dashboard</h3>
  <p>Buoy documents how your process is actually supposed to run, then flags freeform and stage drift live on the record &mdash; the part native HubSpot data-quality tools don't reach.</p>
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
# Post 3
# ---------------------------------------------------------------------------
post = POSTS[2]

post_body = f"""
<p class="eyebrow">Published {post['date_display']}</p>
<h1 class="post-title">{post['title']}</h1>
<p class="post-meta">By the Buoy team &middot; 5 min read</p>

<article class="post-body">
<p>A CRM audit is a structured, property-by-property review of what your CRM actually does — every field, every workflow, every stage — compared against what your business is actually supposed to be doing. It isn't a generic health score or a one-time report you read and file away. It's a series of specific, explicit decisions, made one property at a time, about what stays, what goes, and what nobody's agreed on yet.</p>

<h2>The actual method: check usage, trace the logic, decide</h2>

<p>For every property on an object, the same three-step pattern repeats. First, check where it's actually used — most CRMs can show you whether a field appears in any workflow, form, report, or view. Second, if it is used somewhere, open that workflow and trace what it's actually doing, not what its name implies it does. Third, make an explicit call. That third step is where most audits are vague and where a real one has to be specific — "review the data" isn't a decision, and neither is "clean it up."</p>

<p>In practice, every property lands in one of five buckets:</p>
<ul>
<li><strong>Keep</strong> — it works as intended, no changes needed.</li>
<li><strong>Delete</strong> — no longer serves a purpose, safe to remove.</li>
<li><strong>Turn into a rule</strong> — the field itself is fine, but what counts as a <em>correct</em> value needs to be written down as an explicit, checkable condition instead of left to interpretation.</li>
<li><strong>Pending on a person</strong> — genuinely undecidable in this session; a specific stakeholder needs to weigh in before it can close.</li>
<li><strong>Blocked on a process decision</strong> — the field isn't the problem. The process it's supposed to reflect hasn't been agreed on yet, so there's nothing to decide until that happens separately.</li>
</ul>

<p>That last bucket matters more than it sounds like it should. A field can be perfectly well-built and still be un-auditable, because the real issue is one level up — the business hasn't actually settled on what the process should be. Forcing a data decision onto an unresolved process question just produces a field that's "fixed" until the process changes again next quarter.</p>

<h2>What audits actually find (three patterns worth knowing before you start)</h2>

<h3>Shadow duplicates of native platform fields</h3>
<p>Most CRMs calculate certain things automatically — days since last contact, weighted pipeline value, that kind of thing. It's extremely common to find a custom-built field quietly recreating one of these, usually because whoever built it didn't know the native version existed, or built it before the platform added one. Neither field is wrong exactly, but now there are two sources of truth for the same number, and nothing forces them to agree.</p>

<h3>Fields that are populated and still wrong</h3>
<p>The most common surprise in any real audit isn't a blank field — it's a filled-in one that's quietly inaccurate. A date field everyone assumes is reliable turns out to be off by a meaningful margin on a real share of records, and often nobody can say exactly why. This is the sharpest version of the problem an audit exists to catch: the field isn't broken in any way a formatting check would notice. It's just not telling the truth, and it's been that way long enough that it's shaped decisions before anyone caught it.</p>

<h3>Dependencies that live outside the CRM entirely</h3>
<p>Before removing or hiding anything, a real audit has to check more than internal usage. A property can show zero workflows, zero forms, and zero reports referencing it inside the CRM, and still break something the moment it's deleted — because a finance spreadsheet or a reporting export pulls that column every month, completely invisible from inside the CRM itself. Checking internal usage alone isn't enough; the audit has to account for what consumes the data downstream, outside the platform.</p>

<h2>How long does a CRM audit actually take?</h2>
<p>Longer than a checklist. For a CRM with a meaningful amount of custom-built complexity — hundreds of properties spread across Deals, Companies, and Contacts — a proper audit moves object by object, and each major object takes real, focused working time to get through carefully. This isn't something to compress into an afternoon; treating it that way is usually how audits end up being cleanup theater instead of an actual fix.</p>

<h2>What you actually get at the end</h2>
<p>Two things, not one. A clear, current picture of how the business actually runs today — not the onboarding-deck version — and a set of best-practice recommendations for what should change, grounded in real GTM and CRM architecture judgment rather than a generic template. The second part is what separates an audit from a cleanup: a cleanup tidies up what's already there, an audit tells you what should be different.</p>

<h2>Common questions</h2>
<h3>What's the difference between a CRM audit and a data cleanup?</h3>
<p>A data cleanup fixes formatting, duplicates, and blanks. A CRM audit goes further: it checks whether each property, workflow, and stage still reflects the process your business actually runs today, not just whether the data looks tidy. A field can pass every cleanup check and still be drifted.</p>
<h3>Do I need to fix my sales process before auditing my CRM?</h3>
<p>No — for many teams, the audit is what surfaces that the process needs to be redefined in the first place. Some properties end up flagged as blocked on a process decision rather than fixed immediately, which is a normal and expected outcome, not a failed audit.</p>
<h3>How long does a CRM audit actually take?</h3>
<p>It depends on how much custom complexity has accumulated, but for a CRM with hundreds of properties across Deals, Companies, and Contacts, expect real, focused work — not a single afternoon. A thorough audit typically moves object by object, with each major object taking substantial dedicated time to get through properly.</p>
<h3>What happens to a field nobody's sure about?</h3>
<p>It gets marked pending rather than forced into a decision on the spot. A good audit process explicitly tracks which fields are waiting on a specific person's input, so nothing gets deleted or kept just to close out the list.</p>

<div class="post-cta">
  <h3>See what a real audit finds in your CRM</h3>
  <p>Buoy runs this exact process — property by property, workflow by workflow — then builds the enforcement layer that keeps it from drifting back.</p>
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
# Post 4 — 10 Signs Your CRM Data Has Drifted
# Article body is kept in _signs_body.html (not inlined here).
# ---------------------------------------------------------------------------
post = next(p for p in POSTS if p["slug"] == "signs-your-crm-data-has-drifted")
signs_body_path = "_signs_body.html"
try:
    with open(signs_body_path) as f:
        post_body = f.read()
except FileNotFoundError:
    print(f"kept existing blog/{post['slug']}.html (no {signs_body_path})")
else:
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

