# areas_data.py - Area/city page data and generator function
# This file is exec'd by generate.py

AREAS = [
    {
        "slug": "irvine-graduation-photographer",
        "name": "Irvine",
        "title": "Irvine Graduation Photographer | UCI Grad Photos",
        "meta_desc": "Looking for a graduation photographer in Irvine, CA? Professional grad photos at UCI and around Irvine with 24-hour delivery and expert lighting.",
        "h1": "Irvine Graduation<br>Photographer",
        "hero_label": "Irvine, CA",
        "lat": 33.6846, "lng": -117.8265,
        "content": """<p>Irvine is home to the University of California, Irvine, one of the most beautiful campuses in Southern California. As an Irvine-based graduation photographer, I know this city inside and out. From the eucalyptus-lined paths of Aldrich Park to the modern architecture of the Great Park, Irvine offers a range of graduation photo backdrops that go far beyond the typical campus shots.</p>

      <p>UCI is my home campus. I graduated from UC Irvine and have been photographing Anteater graduates for nearly seven years. That deep familiarity means your session runs smoothly. I know which spots have the best light at which times, where the crowds thin out, and how to build a route that maximizes variety without wasting your afternoon walking.</p>

      <p>Beyond the UCI campus, Irvine offers additional options for graduates who want something different. The Irvine Spectrum area, Jeffrey Open Space Trail, and various neighborhood parks provide natural and urban backdrops for a more personalized session. I am happy to incorporate off-campus locations into your shoot if you want a mix.</p>

      <p>Every session includes professional off-camera lighting, 24-hour raw photo delivery, and fully edited images in 7 to 10 days. Whether you are graduating from UCI, a local high school, or any other program, I bring the same level of care and professionalism to every Irvine graduation session.</p>""",
        "campuses": [
            {"name": "UC Irvine", "page": "uci-graduation-photos.html", "desc": "My home campus. 11 iconic photo spots, from Aldrich Park to the Peter the Anteater statue."},
        ],
        "featured_spots": ["uci-aldrich-park-graduation-photos", "uci-langson-library-graduation-photos", "uci-peter-anteater-statue-graduation-photos", "uci-infinity-fountain-graduation-photos"],
        "faqs": [
            ("How much does a graduation photographer in Irvine cost?", "UCI graduation sessions start at $300 for a solo session. Duo sessions are $250 per person. All packages include professional off-camera lighting, all raw photos delivered within 24 hours, and edited selections in 7 to 10 days."),
            ("Where are the best places for graduation photos in Irvine?", "The UCI campus is the top choice, with Aldrich Park, Langson Library, and the Peter the Anteater statue being the most popular spots. Off-campus options include the Irvine Spectrum area and local parks."),
            ("Do you only photograph UCI students in Irvine?", "No. I photograph graduates from any school or program in the Irvine area. Whether you are graduating from UCI, a local high school, or a graduate program, I am available to capture your milestone."),
            ("When is the best time for graduation photos in Irvine?", "The best time is between 3pm and 5pm. The afternoon light in Irvine is consistently soft and warm, especially on the UCI campus where tree cover and building shade create flattering conditions."),
        ],
    },
    {
        "slug": "orange-county-graduation-photographer",
        "name": "Orange County",
        "title": "Orange County Graduation Photographer | UCI Grad Photos",
        "meta_desc": "Professional graduation photographer serving all of Orange County, CA. Campus sessions at UCI and beyond with 24-hour delivery.",
        "h1": "Orange County<br>Graduation Photographer",
        "hero_label": "Orange County, CA",
        "lat": 33.7175, "lng": -117.8311,
        "content": """<p>Orange County is home to some of the most beautiful college campuses in California. As an OC-based graduation photographer, I serve students across the county, from UC Irvine in the heart of Irvine to campuses throughout the region. My professional off-camera lighting and relaxed shooting style produce portraits that stand out from the typical graduation snapshot.</p>

      <p>I have been photographing graduation sessions in Orange County for nearly seven years. That experience means I know the best spots, the best light, and the best times at campuses across the area. Every session is planned in advance so we make the most of your time without feeling rushed.</p>

      <p>Orange County's mild weather and abundant sunshine make it one of the best places in the country for outdoor graduation portraits. The consistent golden afternoon light, combined with the diverse architecture and landscaping across OC campuses, gives your photos a warm, polished look that is hard to replicate indoors.</p>

      <p>Whether you are graduating from UCI, a community college, a high school, or a graduate program anywhere in Orange County, I bring the same professional equipment and attention to detail to every session. Every package includes 24-hour raw photo delivery and fully edited selections in 7 to 10 days.</p>""",
        "campuses": [
            {"name": "UC Irvine", "page": "uci-graduation-photos.html", "desc": "My home campus with 11 iconic photo locations across the beautiful UCI grounds."},
        ],
        "featured_spots": ["uci-aldrich-park-graduation-photos", "uci-peter-anteater-statue-graduation-photos", "uci-langson-library-graduation-photos"],
        "faqs": [
            ("Do you travel throughout Orange County for graduation sessions?", "Yes. I am based in Irvine and travel throughout Orange County for graduation sessions. Travel within OC is included in my pricing with no additional fees."),
            ("What campuses do you photograph at in Orange County?", "I primarily photograph at UC Irvine, where I have nearly seven years of experience. I also photograph graduates at locations throughout Orange County."),
            ("How much does a graduation photographer in Orange County cost?", "Sessions start at $300 for solo UCI sessions. Pricing varies by campus and group size. All packages include professional off-camera lighting, 24-hour raw delivery, and edited photos in 7 to 10 days."),
            ("What is the best season for graduation photos in Orange County?", "Orange County has great light year-round, but peak graduation season is April through June. Booking early ensures you get your preferred date and time slot."),
        ],
    },
    {
        "slug": "los-angeles-graduation-photographer",
        "name": "Los Angeles",
        "title": "Los Angeles Graduation Photographer | UCI Grad Photos",
        "meta_desc": "Professional graduation photographer in Los Angeles. USC campus sessions and more with expert off-camera lighting and 24-hour delivery.",
        "h1": "Los Angeles<br>Graduation Photographer",
        "hero_label": "Los Angeles, CA",
        "lat": 34.0522, "lng": -118.2437,
        "content": """<p>Los Angeles is home to the University of Southern California and dozens of other colleges and universities. As a graduation photographer who regularly shoots at USC, I bring professional off-camera lighting and years of campus experience to every LA session.</p>

      <p>USC is my primary Los Angeles campus. The Romanesque architecture, iconic landmarks like Tommy Trojan and Doheny Library, and the sprawling tree-lined walkways make it one of the most photogenic campuses in the country. I have photographed dozens of Trojan graduates and know every corner of the campus.</p>

      <p>Beyond USC, Los Angeles offers a wealth of graduation photo opportunities. From the grand architecture of other LA campuses to the city's parks, murals, and urban backdrops, I can tailor your session to fit your personality and style. If you want something beyond the traditional campus shots, LA delivers.</p>

      <p>I am based in Orange County and travel to Los Angeles regularly for USC graduation sessions. Travel is built into my LA pricing, so there are no surprise fees. Every session includes professional off-camera lighting, all raw photos delivered within 24 hours, and fully edited selections in 7 to 10 days.</p>""",
        "campuses": [
            {"name": "USC", "page": "usc-graduation-photos.html", "desc": "Iconic Trojan campus with Tommy Trojan, Doheny Library, and 5 more stunning photo spots."},
        ],
        "featured_spots": ["usc-tommy-trojan-graduation-photos", "usc-doheny-library-graduation-photos", "usc-bovard-auditorium-graduation-photos", "usc-steps-of-troy-graduation-photos"],
        "faqs": [
            ("Do you travel to Los Angeles for graduation sessions?", "Yes. I travel to Los Angeles regularly for USC graduation sessions. Travel from Orange County is built into my LA pricing with no additional fees."),
            ("How much do graduation photos cost in Los Angeles?", "USC solo sessions are $350. Duo sessions are $300 per person. All packages include professional off-camera lighting, 24-hour raw photo delivery, and edited selections in 7 to 10 days."),
            ("What is the best time for graduation photos in Los Angeles?", "Between 3pm and 6pm. The afternoon light at USC is consistently beautiful, and the campus architecture creates natural shade that keeps conditions flattering."),
            ("Do you only shoot at USC in Los Angeles?", "USC is my primary LA campus, but I am open to other locations in the city. If you have a specific spot in mind, let me know and I can plan a session around it."),
        ],
    },
    {
        "slug": "anaheim-graduation-photographer",
        "name": "Anaheim",
        "title": "Anaheim Graduation Photographer | UCI Grad Photos",
        "meta_desc": "Professional graduation photographer serving Anaheim, CA. Expert off-camera lighting, 24-hour delivery, and campus sessions at UCI and USC.",
        "h1": "Anaheim<br>Graduation Photographer",
        "hero_label": "Anaheim, CA",
        "lat": 33.8366, "lng": -117.9143,
        "content": """<p>Anaheim graduates looking for professional graduation photos have easy access to some of the best campus photo locations in Southern California. Located in the heart of Orange County, Anaheim is a short drive from UC Irvine and within reach of USC in Los Angeles. I serve Anaheim students with the same professional equipment and experienced eye that I bring to every session.</p>

      <p>Most Anaheim graduates choose to shoot at the UCI campus, which is about 15 minutes south. UCI offers 11 incredible photo spots, from the shaded paths of Aldrich Park to the iconic Peter the Anteater statue. My familiarity with the campus means your session will be efficient, well-lit, and full of variety.</p>

      <p>For Anaheim graduates who attend USC, I also travel to Los Angeles regularly for campus sessions. The travel is built into my pricing, so there are no hidden fees or surprise charges.</p>

      <p>Whether you are graduating from a local Anaheim high school, a nearby community college, or a four-year university, I bring professional off-camera lighting and a relaxed shooting style to every session. All packages include 24-hour raw photo delivery and edited selections in 7 to 10 days.</p>""",
        "campuses": [
            {"name": "UC Irvine", "page": "uci-graduation-photos.html", "desc": "Just 15 minutes from Anaheim. 11 stunning photo spots across the UCI campus."},
            {"name": "USC", "page": "usc-graduation-photos.html", "desc": "Tommy Trojan, Doheny Library, and more. Travel from OC included in pricing."},
        ],
        "featured_spots": ["uci-aldrich-park-graduation-photos", "uci-peter-anteater-statue-graduation-photos", "uci-langson-library-graduation-photos"],
        "faqs": [
            ("Do you serve Anaheim for graduation photos?", "Yes. I am based in Irvine, about 15 minutes from Anaheim. I serve Anaheim graduates for sessions at UCI, USC, and other locations throughout the area."),
            ("Where do Anaheim graduates usually take grad photos?", "Most Anaheim graduates shoot at the UCI campus, which is the closest major university. UCI offers 11 photo spots including Aldrich Park, Langson Library, and the Peter the Anteater statue."),
            ("How much do graduation photos cost for Anaheim students?", "UCI sessions start at $300 for solo. Duo sessions are $250 per person. All packages include professional lighting, 24-hour raw delivery, and edited photos in 7 to 10 days."),
        ],
    },
    {
        "slug": "newport-beach-graduation-photographer",
        "name": "Newport Beach",
        "title": "Newport Beach Graduation Photographer | UCI Grad Photos",
        "meta_desc": "Professional graduation photographer in Newport Beach, CA. Campus sessions at UCI and coastal backdrops with expert lighting and 24-hour delivery.",
        "h1": "Newport Beach<br>Graduation Photographer",
        "hero_label": "Newport Beach, CA",
        "lat": 33.6189, "lng": -117.9289,
        "content": """<p>Newport Beach graduates are just minutes from the UC Irvine campus, one of the most beautiful graduation photo locations in Southern California. As a photographer based in the Irvine and Newport Beach area, I offer convenient, professional graduation sessions with expert off-camera lighting and fast turnaround.</p>

      <p>UCI is the most popular campus for Newport Beach graduates, and for good reason. The 11 photo spots across campus offer everything from lush park settings to modern architecture to iconic mascot statues. My seven years of experience shooting at UCI means I know exactly where to take you and when to be there for the best light.</p>

      <p>Newport Beach itself offers unique coastal backdrop options for graduates who want something different. The harbor, pier, and beach settings can complement a campus session beautifully, giving your gallery a mix of academic and lifestyle shots. I am happy to incorporate Newport Beach locations into a multi-stop session.</p>

      <p>Every session includes professional off-camera lighting, all raw photos delivered within 24 hours, and fully edited selections in 7 to 10 days. Whether you are graduating from UCI, a local school, or any program in the area, I bring the same quality and care to your portraits.</p>""",
        "campuses": [
            {"name": "UC Irvine", "page": "uci-graduation-photos.html", "desc": "Minutes from Newport Beach. 11 gorgeous photo spots across the UCI campus."},
        ],
        "featured_spots": ["uci-aldrich-park-graduation-photos", "uci-infinity-fountain-graduation-photos", "uci-peter-anteater-statue-graduation-photos"],
        "faqs": [
            ("Do you offer graduation photos in Newport Beach?", "Yes. I am based in the Irvine and Newport Beach area and offer sessions at UCI, as well as Newport Beach coastal locations for a unique look."),
            ("Can I combine campus and beach photos?", "Absolutely. I can plan a session that starts at UCI and finishes at a Newport Beach location for a mix of academic and lifestyle portraits in your gallery."),
            ("How far is UCI from Newport Beach?", "UCI is about 10 minutes from most Newport Beach neighborhoods. The drive is quick and easy, making it convenient to shoot on campus even for a weekday evening session."),
            ("What is the best time for graduation photos in Newport Beach?", "For campus sessions at UCI, 3pm to 5pm is ideal. For coastal Newport Beach shots, golden hour between 5pm and 6:30pm gives you warm, dramatic light on the water."),
        ],
    },
]

def generate_area_page(area, idx):
    a = area
    url = f"https://www.ucigradphotos.com/areas/{a['slug']}.html"

    # Campus cards
    campus_html = ""
    for c in a["campuses"]:
        campus_html += f'''        <a href="../{c["page"]}" class="spot-card" style="text-decoration:none;color:inherit;">
          <div style="padding:2rem;text-align:center;">
            <h3>{c["name"]}</h3>
            <p>{c["desc"]}</p>
          </div>
        </a>\n'''

    # Featured spots
    spots_html = ""
    for slug in a.get("featured_spots", []):
        spot = next((x for x in ALL_SPOTS if x["slug"] == slug), None)
        if spot:
            spots_html += f'''        <a href="../spots/{slug}.html" class="spot-card" style="text-decoration:none;color:inherit;">
          <img src="../{spot["image"]}" alt="{spot["name"]} graduation photo" loading="lazy">
          <h3>{spot["name"]}</h3>
        </a>\n'''

    gallery = GALLERY_SETS[idx % len(GALLERY_SETS)]
    gallery_html = "\n          ".join(f'<img src="../{img}" alt="Graduation portrait in {a["name"]}" loading="lazy">' for img in gallery)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{GA}
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{a["title"]}</title>
  <meta name="description" content="{a["meta_desc"]}">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="{a["title"]}">
  <meta property="og:description" content="{a["meta_desc"]}">
  <meta property="og:url" content="{url}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://www.ucigradphotos.com/images/portfolio/img-030.jpg">
  <meta property="og:site_name" content="UCI Grad Photos">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{a["title"]}">
  <meta name="twitter:description" content="{a["meta_desc"]}">
  <meta name="twitter:image" content="https://www.ucigradphotos.com/images/portfolio/img-030.jpg">
{favicons()}
  <link rel="stylesheet" href="../css/style.css">
  <script type="application/ld+json">
  {local_business_jsonld(a["meta_desc"], url, a["lat"], a["lng"], a["name"])}
  </script>
  <script type="application/ld+json">
  {breadcrumb_jsonld([("Home", "https://www.ucigradphotos.com/"), (f"{a['name']} Graduation Photographer", url)])}
  </script>
  <script type="application/ld+json">
  {faq_jsonld(a["faqs"])}
  </script>
</head>
<body>
{navbar()}

{hero_section(a["hero_label"], a["h1"], f"Professional graduation photography in {a['name']}. Expert lighting, relaxed vibes, 24-hour delivery.", idx + 10)}

  <!-- Area Overview -->
  <section class="section section-padding fade-in">
    <div class="container container--narrow">
      <p class="section-label">{a["name"]}</p>
      <h2>Graduation Photography in {a["name"]}</h2>
      {a["content"]}
    </div>
  </section>

  <!-- Campuses Served -->
  <section class="section-padding bg-light fade-in">
    <div class="container">
      <div class="text-center">
        <p class="section-label">Campuses</p>
        <h2>Campuses Near {a["name"]}</h2>
      </div>
      <div class="spots-grid" style="margin-top:2rem;max-width:700px;margin-left:auto;margin-right:auto;">
{campus_html}      </div>
    </div>
  </section>

  <!-- Featured Spots -->
  <section class="section section-padding fade-in">
    <div class="container">
      <div class="text-center">
        <p class="section-label">Popular Spots</p>
        <h2>Featured Photo Locations</h2>
      </div>
      <div class="spots-grid" style="margin-top:2rem;">
{spots_html}      </div>
    </div>
  </section>

  <!-- Sample Gallery -->
  <section class="section section-padding bg-light fade-in">
    <div class="container">
      <div class="text-center">
        <p class="section-label">Portfolio</p>
        <h2>Recent Graduation Portraits</h2>
      </div>
      <div class="img-slider" style="margin-top:2rem;">
        <div class="img-slider-track">
          {gallery_html}
        </div>
      </div>
      <div class="text-center" style="margin-top:2rem;">
        <a href="../portfolio.html" class="btn btn--secondary">View Full Portfolio</a>
      </div>
    </div>
  </section>

{pricing_section("uci")}

  <!-- FAQ -->
  <section class="section section-padding bg-light fade-in" id="faq">
    <div class="container">
      <div class="text-center">
        <p class="section-label">FAQ</p>
        <h2>{a["name"]} Graduation Photo Questions</h2>
      </div>
      <div class="faq-list" style="margin-top: var(--space-2xl);">
{faq_html(a["faqs"])}      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section section-padding fade-in">
    <div class="container text-center">
      <h2>Book Your {a["name"]} Graduation Session</h2>
      <p class="mx-auto" style="max-width:640px;margin:1.5rem auto 3rem;">Ready for professional graduation photos in {a["name"]}? Book your session and get your raw photos within 24 hours.</p>
      <a href="../contact.html" class="btn btn--primary btn--large">Book Your Session</a>
    </div>
  </section>

{footer()}
  <script src="../js/main.js"></script>
</body>
</html>'''
    write_page("areas", f"{a['slug']}.html", html)

# Generate all area pages
print("Generating area pages...")
for i, area in enumerate(AREAS):
    generate_area_page(area, i)
print(f"  Done: {len(AREAS)} area pages generated.")
