#!/usr/bin/env python3
"""Generate programmatic SEO pages for ucigradphotos.com"""
import os, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# === SHARED HTML SNIPPETS ===

GA = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-G6BXCEZ36W"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-G6BXCEZ36W');
</script>'''

def favicons():
    return '''  <link rel="icon" type="image/png" sizes="32x32" href="../favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="../favicon-192x192.png">
  <link rel="apple-touch-icon" href="../apple-touch-icon.png">'''

def navbar():
    return '''  <nav class="navbar scrolled">
    <div class="container">
      <a href="../index.html" class="navbar-logo">UCI Grad Photos</a>
      <div class="navbar-links">
        <a href="../index.html">Home</a>
        <a href="../portfolio.html">Portfolio</a>
        <a href="../pricing.html">Pricing</a>
        <a href="../faq.html">FAQ</a>
        <a href="../blog.html">Blog</a>
        <a href="../contact.html" class="btn btn--primary btn--small navbar-cta">Book Now</a>
      </div>
      <button class="hamburger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </nav>
  <div class="mobile-nav">
    <a href="../index.html">Home</a>
    <a href="../portfolio.html">Portfolio</a>
    <a href="../pricing.html">Pricing</a>
    <a href="../faq.html">FAQ</a>
    <a href="../blog.html">Blog</a>
    <a href="../contact.html">Book Now</a>
  </div>'''

def footer():
    return '''  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand"><div class="logo">UCI Grad Photos</div><p>Professional graduation photography in Orange County, CA.</p></div>
        <div><h4 class="footer-heading">Pages</h4><ul class="footer-links"><li><a href="../index.html">Home</a></li><li><a href="../portfolio.html">Portfolio</a></li><li><a href="../pricing.html">Pricing</a></li><li><a href="../faq.html">FAQ</a></li><li><a href="../blog.html">Blog</a></li></ul></div>
        <div><h4 class="footer-heading">Campuses</h4><ul class="footer-links"><li><a href="../uci-graduation-photos.html">UC Irvine</a></li><li><a href="../usc-graduation-photos.html">USC</a></li></ul></div>
        <div><h4 class="footer-heading">Contact</h4><ul class="footer-links"><li><a href="tel:9493128300">(949) 312-8300</a></li><li><a href="mailto:guramrit.art@gmail.com">guramrit.art@gmail.com</a></li><li><a href="https://www.instagram.com/ucigradpics/" target="_blank" rel="noopener">@ucigradpics</a></li></ul></div>
      </div>
      <div class="footer-bottom"><span>&copy; 2026 UCI Grad Photos. All rights reserved.</span></div>
    </div>
  </footer>'''

# 5 image sets to rotate across pages
HERO_SETS = [
    [
        ["images/more/0S9A8228.jpg","images/more/0S9A2717.jpg","images/more/3E8A8301.jpg","images/more/0S9A3775.jpg","images/more/IMG_1744.jpg","images/more/0S9A9300.jpg"],
        ["images/more/0S9A3121.jpg","images/more/3E8A5961.jpg","images/more/IMG_6533.jpg","images/more/0S9A6427.jpg","images/more/0S9A2878.jpg","images/more/IMG_0676.jpg"],
        ["images/more/0S9A0425.jpg","images/more/IMG_4633.jpg","images/more/0S9A6734.jpg","images/more/0S9A3981.jpg","images/more/IMG_1462.jpg","images/more/3E8A8269.jpg"],
    ],
    [
        ["images/more/0S9A9538.jpg","images/more/0S9A0280.jpg","images/more/IMG_7388.jpg","images/more/0S9A3342.jpg","images/more/3E8A5961.jpg","images/more/IMG_9417.jpg"],
        ["images/more/0S9A8228.jpg","images/more/IMG_4633.jpg","images/more/0S9A6427.jpg","images/more/0S9A2717.jpg","images/more/IMG_1744.jpg","images/more/3E8A8301.jpg"],
        ["images/more/0S9A3121.jpg","images/more/0S9A2878.jpg","images/more/IMG_6533.jpg","images/more/0S9A3775.jpg","images/more/0S9A9300.jpg","images/more/0S9A0425.jpg"],
    ],
    [
        ["images/more/3E8A5961.jpg","images/more/0S9A3981.jpg","images/more/IMG_1462.jpg","images/more/0S9A8228.jpg","images/more/IMG_7388.jpg","images/more/0S9A0280.jpg"],
        ["images/more/0S9A9538.jpg","images/more/0S9A3342.jpg","images/more/3E8A5961.jpg","images/more/IMG_9417.jpg","images/more/0S9A6734.jpg","images/more/0S9A2717.jpg"],
        ["images/more/IMG_4633.jpg","images/more/0S9A3775.jpg","images/more/IMG_1744.jpg","images/more/0S9A6427.jpg","images/more/3E8A8301.jpg","images/more/0S9A3121.jpg"],
    ],
    [
        ["images/more/0S9A2878.jpg","images/more/IMG_6533.jpg","images/more/0S9A9300.jpg","images/more/0S9A0425.jpg","images/more/3E8A5961.jpg","images/more/0S9A3981.jpg"],
        ["images/more/IMG_1462.jpg","images/more/0S9A8228.jpg","images/more/IMG_7388.jpg","images/more/0S9A0280.jpg","images/more/0S9A9538.jpg","images/more/0S9A3342.jpg"],
        ["images/more/3E8A5961.jpg","images/more/IMG_9417.jpg","images/more/0S9A6734.jpg","images/more/IMG_4633.jpg","images/more/0S9A2717.jpg","images/more/IMG_1744.jpg"],
    ],
    [
        ["images/more/0S9A6427.jpg","images/more/3E8A8301.jpg","images/more/0S9A3121.jpg","images/more/0S9A2878.jpg","images/more/IMG_6533.jpg","images/more/0S9A9300.jpg"],
        ["images/more/0S9A0425.jpg","images/more/3E8A5961.jpg","images/more/0S9A3981.jpg","images/more/IMG_1462.jpg","images/more/0S9A8228.jpg","images/more/IMG_7388.jpg"],
        ["images/more/0S9A0280.jpg","images/more/0S9A9538.jpg","images/more/0S9A3342.jpg","images/more/3E8A5961.jpg","images/more/IMG_9417.jpg","images/more/0S9A6734.jpg"],
    ],
]

def hero_section(label, h1, tagline, hero_set_idx=0):
    s = hero_set_idx % len(HERO_SETS)
    rows = HERO_SETS[s]
    dirs = ["left", "right", "left-slow"]
    row_html = ""
    for i, (d, imgs) in enumerate(zip(dirs, rows)):
        img_tags = "\n          ".join(f'<img src="../{p}" alt="Graduation portrait">' for p in imgs)
        dup = "\n          ".join(f'<img src="../{p}" alt="Graduation portrait">' for p in imgs)
        row_html += f'''      <div class="scroll-row" data-direction="{d}">
        <div class="scroll-track">
          {img_tags}
          {dup}
        </div>
      </div>\n'''
    return f'''  <section class="hero-scroll">
    <div class="hero-scroll-bg">
{row_html}    </div>
    <div class="hero-scroll-overlay"></div>
    <div class="hero-scroll-content">
      <span class="section-label">{label}</span>
      <h1>{h1}</h1>
      <p class="hero-tagline">{tagline}</p>
      <div class="hero-buttons">
        <a href="../contact.html" class="btn btn--primary btn--large">Book Now</a>
        <a href="../portfolio.html" class="btn btn--secondary btn--large">View Portfolio</a>
      </div>
    </div>
  </section>'''

def faq_html(faqs):
    items = ""
    for q, a in faqs:
        items += f'''        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            {q}
            <span class="icon">+</span>
          </button>
          <div class="faq-answer">
            <p>{a}</p>
          </div>
        </div>\n'''
    return items

def faq_jsonld(faqs):
    entities = []
    for q, a in faqs:
        entities.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities})

def breadcrumb_jsonld(crumbs):
    items = []
    for i, (name, url) in enumerate(crumbs, 1):
        items.append({"@type": "ListItem", "position": i, "name": name, "item": url})
    return json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})

def local_business_jsonld(desc, url, lat, lng, city):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "UCI Grad Photos",
        "description": desc,
        "url": url,
        "telephone": "(949) 312-8300",
        "email": "guramrit.art@gmail.com",
        "address": {"@type": "PostalAddress", "addressLocality": city, "addressRegion": "CA", "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": lat, "longitude": lng},
        "image": "https://www.ucigradphotos.com/images/portfolio/img-030.jpg",
        "priceRange": "$$"
    })

def pricing_section(campus="uci"):
    if campus == "uci":
        return '''  <section class="section section-padding fade-in">
    <div class="container">
      <div class="text-center">
        <p class="section-label">Pricing</p>
        <h2>Graduation Photo Packages</h2>
      </div>
      <div class="pricing-grid" style="margin-top: 3rem; max-width: 700px; margin-left: auto; margin-right: auto;">
        <div class="pricing-card">
          <div class="pricing-tier">Solo</div>
          <div class="pricing-amount"><span class="currency">$</span>300</div>
          <p class="pricing-description">Per person</p>
          <ul class="pricing-features">
            <li>1.5 - 2 hour session</li>
            <li>Multiple campus locations</li>
            <li>Professional lighting</li>
            <li>All raw photos in 24 hours</li>
            <li>Edited selections in 7-10 days</li>
          </ul>
          <a href="../contact.html" class="btn btn--primary" style="width:100%;">Book Solo</a>
        </div>
        <div class="pricing-card popular">
          <div class="pricing-badge">Most Popular</div>
          <div class="pricing-tier">Duo</div>
          <div class="pricing-amount"><span class="currency">$</span>250</div>
          <p class="pricing-description">Per person</p>
          <ul class="pricing-features">
            <li>2 hour session</li>
            <li>Individual and paired shots</li>
            <li>Professional lighting</li>
            <li>All raw photos in 24 hours</li>
            <li>Edited selections in 7-10 days</li>
          </ul>
          <a href="../contact.html" class="btn btn--primary" style="width:100%;">Book Duo</a>
        </div>
      </div>
      <div class="text-center" style="margin-top: 2rem;">
        <a href="../pricing.html" class="btn btn--secondary">View Full Pricing</a>
      </div>
    </div>
  </section>'''
    else:
        return '''  <section class="section section-padding fade-in">
    <div class="container">
      <div class="text-center">
        <p class="section-label">Pricing</p>
        <h2>Graduation Photo Packages</h2>
      </div>
      <div class="pricing-grid" style="margin-top: 3rem; max-width: 700px; margin-left: auto; margin-right: auto;">
        <div class="pricing-card">
          <div class="pricing-tier">Solo</div>
          <div class="pricing-amount"><span class="currency">$</span>350</div>
          <p class="pricing-description">Per person</p>
          <ul class="pricing-features">
            <li>1.5 - 2 hour session</li>
            <li>Multiple campus locations</li>
            <li>Professional lighting</li>
            <li>All raw photos in 24 hours</li>
            <li>Edited selections in 7-10 days</li>
          </ul>
          <a href="../contact.html" class="btn btn--primary" style="width:100%;">Book Solo</a>
        </div>
        <div class="pricing-card popular">
          <div class="pricing-badge">Most Popular</div>
          <div class="pricing-tier">Duo</div>
          <div class="pricing-amount"><span class="currency">$</span>300</div>
          <p class="pricing-description">Per person</p>
          <ul class="pricing-features">
            <li>2 hour session</li>
            <li>Individual and paired shots</li>
            <li>Professional lighting</li>
            <li>All raw photos in 24 hours</li>
            <li>Edited selections in 7-10 days</li>
          </ul>
          <a href="../contact.html" class="btn btn--primary" style="width:100%;">Book Duo</a>
        </div>
      </div>
      <div class="text-center" style="margin-top: 2rem;">
        <a href="../pricing.html" class="btn btn--secondary">View Full Pricing</a>
      </div>
    </div>
  </section>'''

def write_page(subdir, filename, html):
    path = os.path.join(BASE, subdir, filename)
    with open(path, 'w') as f:
        f.write(html)
    print(f"  Created {subdir}/{filename}")

# === DATA will be loaded from separate files ===
# We import from data modules
exec(open(os.path.join(os.path.dirname(__file__), 'spots_data.py')).read())
exec(open(os.path.join(os.path.dirname(__file__), 'areas_data.py')).read())
exec(open(os.path.join(os.path.dirname(__file__), 'programs_data.py')).read())
