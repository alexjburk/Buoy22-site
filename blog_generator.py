# Shared CSS for every blog page. White base, paper footer, Newsreader, Inter,
# JetBrains Mono. Duplicated into each page so a file still renders alone.
SHARED_CSS = """
:root{
  --ink:#161513; --navy:#0F1F33; --paper:#F4F0E6; --slate:#4A5768; --oxblood:#8C3B32;
  --line:rgba(22,21,19,0.18); --max:760px;
}
*{ box-sizing:border-box; }
html{ scroll-behavior:smooth; }
body{
  margin:0; background:#fff; color:var(--ink);
  font-family:Inter, sans-serif; font-size:17px; line-height:1.65;
  -webkit-font-smoothing:antialiased;
}
h1,h2,h3,.serif{
  font-family:Newsreader, serif; font-optical-sizing:auto; font-weight:500;
  letter-spacing:-0.02em; margin:0; color:var(--ink);
}
a{ color:inherit; }
.wrap{ max-width:var(--max); margin:0 auto; padding:0 32px; }
img{ max-width:100%; display:block; }
:focus-visible{ outline:2px solid var(--navy); outline-offset:3px; }

header{
  position:sticky; top:0; z-index:20;
  background:#fff;
  border-bottom:1px solid #E4DED0;
}
nav.wrap{ display:flex; align-items:center; justify-content:space-between; height:72px; max-width:1120px; }
.brand{ display:flex; align-items:center; gap:10px; text-decoration:none; color:var(--ink); }
.brand img{ height:32px; width:32px; flex:none; display:block; }
.word{ font-family:Newsreader, serif; font-weight:500; font-size:26px; letter-spacing:-0.03em; line-height:1; text-transform:lowercase; }
.dot{ display:inline-block; width:5px; height:5px; margin:0 0 11px 3px; border-radius:50%; background:var(--oxblood); vertical-align:middle; }
.navlinks{ display:flex; align-items:center; gap:28px; }
.navlinks a{ text-decoration:none; color:var(--ink); font-size:14px; }
.navlinks a:hover{ color:var(--navy); }
.nav-menu{
  display:none; width:44px; height:44px; flex:none; padding:0;
  border:1px solid var(--ink); background:transparent; color:var(--ink); cursor:pointer;
  align-items:center; justify-content:center;
}
.nav-menu-bars, .nav-menu-bars::before, .nav-menu-bars::after{
  display:block; width:16px; height:1.5px; background:currentColor; position:relative;
}
.nav-menu-bars::before, .nav-menu-bars::after{ content:""; position:absolute; left:0; }
.nav-menu-bars::before{ top:-5px; }
.nav-menu-bars::after{ top:5px; }
.nav-menu[aria-expanded="true"] .nav-menu-bars{ background:transparent; }
.nav-menu[aria-expanded="true"] .nav-menu-bars::before{ top:0; transform:rotate(45deg); }
.nav-menu[aria-expanded="true"] .nav-menu-bars::after{ top:0; transform:rotate(-45deg); }
.btn{
  display:inline-flex; align-items:center; justify-content:center;
  min-height:44px; padding:12px 18px; border-radius:0;
  font-family:Inter, sans-serif; font-size:14px; font-weight:500;
  white-space:nowrap; text-decoration:none; border:1px solid transparent; cursor:pointer;
}
.btn-primary{ background:var(--navy); color:var(--paper); }
.btn-primary:hover{ background:#183049; }
.navcta{ display:flex; gap:14px; align-items:center; }

main{ padding:96px 0 96px; }
.eyebrow{
  font-family:"JetBrains Mono", ui-monospace, monospace;
  font-size:12px; letter-spacing:0.14em; text-transform:uppercase;
  color:var(--slate); margin:0 0 12px;
}
.post-title{ font-size:48px; line-height:1.08; margin-bottom:14px; }
.post-meta{
  font-family:"JetBrains Mono", ui-monospace, monospace;
  font-size:12px; letter-spacing:0.04em; color:var(--slate); margin-bottom:40px;
}
article.post-body{ max-width:620px; }
article.post-body h2{ font-size:28px; margin:48px 0 14px; line-height:1.2; }
article.post-body h3{ font-size:22px; margin:32px 0 10px; line-height:1.25; }
article.post-body p{ margin:0 0 18px; }
article.post-body a{ text-underline-offset:3px; }
article.post-body ul, article.post-body ol{ margin:0 0 18px; padding-left:22px; }
article.post-body li{ margin-bottom:8px; }
article.post-body strong{ font-weight:600; }
article.post-body blockquote{ margin:28px 0; padding:0 0 0 18px; border-left:2px solid var(--ink); color:var(--ink); font-family:Newsreader, serif; font-size:22px; line-height:1.35; font-weight:500; }
article.post-body table{ width:100%; border-collapse:collapse; margin:0 0 22px; font-size:15px; }
article.post-body th, article.post-body td{ border-bottom:1px solid var(--line); padding:10px 12px; text-align:left; vertical-align:top; }
article.post-body th{ font-family:"JetBrains Mono", ui-monospace, monospace; font-size:12px; letter-spacing:0.06em; text-transform:uppercase; font-weight:500; color:var(--slate); }
article.post-body td{ font-variant-numeric:tabular-nums; }
article.post-body code{ font-family:"JetBrains Mono", ui-monospace, monospace; font-size:0.9em; background:#EBE6DA; padding:1px 5px; }
article.post-body hr{ border:none; border-top:1px solid var(--line); margin:40px 0; }
.table-wrap{ overflow-x:auto; margin:0 0 22px; }
.table-wrap table{ width:100%; border-collapse:collapse; font-size:15px; }
.table-wrap th, .table-wrap td{ text-align:left; padding:10px 14px; border-bottom:1px solid var(--line); vertical-align:top; }
.table-wrap th{ font-family:"JetBrains Mono", ui-monospace, monospace; font-size:12px; letter-spacing:0.06em; text-transform:uppercase; font-weight:500; color:var(--slate); }
.table-wrap td{ font-variant-numeric:tabular-nums; }
.post-cta{ background:var(--navy); color:var(--paper); padding:36px 32px; margin:56px 0 48px; }
.post-cta h3,
article.post-body .post-cta h3{ font-size:32px; line-height:1.15; color:var(--paper); margin:0 0 10px; max-width:22ch; font-weight:500; }
.post-cta p{ color:var(--paper); margin:0 0 18px; }
.post-cta .btn-primary{ background:var(--paper); color:var(--navy); }
.post-cta .btn-primary:hover{ background:#fff; }
.post-cta :focus-visible{ outline-color:var(--paper); }

.post-list-item{ padding:28px 0; border-top:1px solid var(--line); }
.post-list-item:first-of-type{ border-top:1px solid var(--line); }
.post-list-item h2{ font-size:28px; line-height:1.2; margin-bottom:8px; }
.post-list-item h2 a{ text-decoration:none; }
.post-list-item h2 a:hover{ text-decoration:underline; text-underline-offset:3px; }
.post-list-item p{ color:var(--slate); margin:0; }

footer{ background:var(--paper); border-top:1px solid var(--line); padding:48px 0 28px; }
footer .wrap{ display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:28px; max-width:1120px; }
footer .word{ font-size:22px; }
footer .fnote{ font-size:14px; color:var(--slate); margin-top:12px; max-width:46ch; line-height:1.5; }
footer .fnav{ display:flex; gap:22px; flex-wrap:wrap; }
footer .fnav a{ text-decoration:none; font-size:14px; color:var(--slate); }
footer .fnav a:hover{ color:var(--ink); }
.copyright{ font-size:12px; letter-spacing:0.04em; color:var(--slate); margin-top:28px; max-width:1120px; margin-left:auto; margin-right:auto; padding:0 32px; font-family:"JetBrains Mono", ui-monospace, monospace; }

.hs-modal-overlay{ display:none; position:fixed; inset:0; z-index:1000; background:rgba(15,31,51,0.72); align-items:center; justify-content:center; padding:24px; }
.hs-modal-overlay.open{ display:flex; }
.hs-modal{ background:var(--paper); border-radius:0; width:100%; max-width:500px; max-height:88vh; overflow-y:auto; padding:36px 28px 28px; position:relative; border:1px solid var(--line); }
.hs-modal-close{ position:absolute; top:8px; right:8px; width:44px; height:44px; background:none; border:none; font-size:26px; line-height:1; cursor:pointer; color:var(--ink); }
.hs-modal h3{ font-size:28px; margin:0 0 8px; }
.hs-modal p.sub{ color:var(--slate); font-size:15px; margin:0 0 20px; }

@media (max-width: 720px){
  nav.wrap{ flex-wrap:wrap; height:auto; padding-top:8px; padding-bottom:8px; row-gap:0; }
  .nav-menu{ display:inline-flex; }
  .navlinks{ display:none; order:3; width:100%; flex-direction:column; align-items:stretch; gap:0; padding:4px 0 8px; }
  .navlinks.is-open{ display:flex; }
  .navlinks a{ white-space:nowrap; min-height:44px; display:flex; align-items:center; padding:0 4px; }
  footer .fnav{ width:100%; flex-wrap:wrap; overflow:visible; }
  footer .fnav a{ white-space:nowrap; min-height:44px; display:inline-flex; align-items:center; padding:0 10px; }
  .post-title{ font-size:36px; }
  .wrap{ padding:0 20px; }
}
"""

HEAD = """<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{description}" />
<link rel="canonical" href="{canonical}" />
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="/favicon-64.png">
<link rel="icon" type="image/png" sizes="128x128" href="/favicon-128.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">

<meta property="og:type" content="{og_type}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="https://buildwithbuoy.com/assets/og-image.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="Buoy — Stop debating the numbers. Start deciding." />
<meta property="og:site_name" content="Buoy" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{description}" />
<meta name="twitter:image" content="https://buildwithbuoy.com/assets/og-image.png" />

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style>
{json_ld}"""

NAV = """<header>
  <nav class="wrap">
    <a class="brand" href="/">
      <img src="/assets/buoy-mark.svg" alt="Buoy">
      <span class="word">buoy<span class="dot" aria-hidden="true"></span></span>
    </a>
    <div class="navlinks" id="site-nav">
      <a href="/#how-it-works">How it works</a>
      <a href="/#product">Product</a>
      <a href="/#story">Why Buoy</a>
      <a href="/#pricing">Pricing</a>
      <a href="/blog/">Blog</a>
    </div>
    <div class="navcta">
      <button class="nav-menu" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Menu"><span class="nav-menu-bars" aria-hidden="true"></span></button>
      <button class="btn btn-primary" onclick="openAuditModal(event)">Book an audit call</button>
    </div>
  </nav>
</header>"""

FOOTER_AND_MODAL = """<footer>
  <div class="wrap">
    <div>
      <a class="brand" href="/">
        <img src="/assets/buoy-mark.svg" alt="Buoy">
        <span class="word">buoy<span class="dot" aria-hidden="true"></span></span>
      </a>
      <p class="fnote">Done with you, a small number of clients at a time: the Audit, with Included Access to the workspace; Validation and AI fields; and Sonar and Ask Buoy for your leadership team.</p>
    </div>
    <div class="fnav">
      <a href="/#how-it-works">How it works</a>
      <a href="/#product">Product</a>
      <a href="/#story">Why Buoy</a>
      <a href="/#pricing">Pricing</a>
      <a href="/blog/">Blog</a>
      <a href="mailto:alex@buildwithbuoy.com">alex@buildwithbuoy.com</a>
    </div>
  </div>
  <p class="copyright">&copy; 2026 Buoy.</p>
</footer>

<div class="hs-modal-overlay" id="hs-modal-overlay">
  <div class="hs-modal" role="dialog" aria-modal="true" aria-labelledby="hs-modal-title">
    <button class="hs-modal-close" onclick="closeAuditModal()" aria-label="Close">&times;</button>
    <h3 id="hs-modal-title">Book an audit call</h3>
    <p class="sub">Tell us a bit about your business and we'll follow up to schedule a time.</p>
    <div class="hs-form-frame" data-region="na2" data-form-id="8dd9daaf-2e19-460c-90ba-590573d0a90c" data-portal-id="247350596"></div>
  </div>
</div>
<script src="https://js-na2.hsforms.net/forms/embed/247350596.js" defer></script>
<script>
  function openAuditModal(e){{
    if (e) e.preventDefault();
    document.getElementById('hs-modal-overlay').classList.add('open');
    document.body.style.overflow = 'hidden';
  }}
  function closeAuditModal(){{
    document.getElementById('hs-modal-overlay').classList.remove('open');
    document.body.style.overflow = '';
  }}
  document.getElementById('hs-modal-overlay').addEventListener('click', function(e){{
    if (e.target === this) closeAuditModal();
  }});
  document.addEventListener('keydown', function(e){{
    if (e.key !== 'Escape') return;
    var menu = document.querySelector('.nav-menu');
    if (menu && menu.getAttribute('aria-expanded') === 'true'){{
      setNavOpen(false);
      menu.focus();
      return;
    }}
    closeAuditModal();
  }});
  function setNavOpen(open){{
    var menu = document.querySelector('.nav-menu');
    var nav = document.getElementById('site-nav');
    if (!menu || !nav) return;
    menu.setAttribute('aria-expanded', open ? 'true' : 'false');
    menu.setAttribute('aria-label', open ? 'Close menu' : 'Menu');
    nav.classList.toggle('is-open', open);
  }}
  var navMenu = document.querySelector('.nav-menu');
  if (navMenu){{
    navMenu.addEventListener('click', function(){{
      var open = navMenu.getAttribute('aria-expanded') !== 'true';
      setNavOpen(open);
      if (open){{
        var first = document.querySelector('#site-nav a');
        if (first) first.focus();
      }}
    }});
  }}
</script>

<!-- HubSpot tracking code -->
<script type="text/javascript" id="hs-script-loader" async defer src="//js.hs-scripts.com/247350596.js"></script>"""


def build_page(title, description, canonical, body_html, og_type="website", json_ld=""):
    head = HEAD.format(
        title=title, description=description, canonical=canonical,
        og_type=og_type, css=SHARED_CSS, json_ld=json_ld
    )
    nav = NAV
    footer = FOOTER_AND_MODAL.format()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head}
</head>
<body>
{nav}
<main>
<div class="wrap">
{body_html}
</div>
</main>
{footer}
</body>
</html>
"""

print("generator ready")
