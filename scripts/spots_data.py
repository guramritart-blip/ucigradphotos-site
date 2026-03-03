# spots_data.py - Spot page data and generator function
# This file is exec'd by generate.py, so all functions from generate.py are available.

UCI_SPOTS = [
    {
        "slug": "uci-aldrich-park-graduation-photos",
        "name": "Aldrich Park",
        "campus": "uci",
        "campus_name": "UCI",
        "campus_page": "uci-graduation-photos.html",
        "image": "images/location/aldrich-park.jpg",
        "title": "Aldrich Park Graduation Photos at UCI | UCI Grad Photos",
        "meta_desc": "Aldrich Park is the most iconic graduation photo spot at UCI. Tips on best time, lighting, and how to get stunning portraits in the heart of campus.",
        "h1": "Aldrich Park<br>Graduation Photos",
        "hero_label": "UCI Photo Spot",
        "best_time": "3pm to 5pm",
        "crowd_level": "Moderate",
        "pairs_with": "Langson Library, Peter Anteater Statue",
        "content": """<p>Aldrich Park is the centerpiece of the UC Irvine campus. This 36-acre circular park sits at the heart of Ring Road, surrounded by every major academic building on campus. Towering eucalyptus trees, Aleppo pines, and lush greenery create a canopy that filters sunlight into soft, flattering rays. For graduation photos, there is no better starting point.</p>

      <p>What makes Aldrich Park stand out is the variety within a single location. The winding paths offer natural leading lines that draw the eye to you. The dense tree cover provides shade on bright days, eliminating harsh shadows and squinting. And the park's depth means you can shoot in multiple spots without walking more than a few minutes between setups.</p>

      <p>I have shot hundreds of UCI graduation sessions in Aldrich Park, and the location never gets old. Every angle produces a different look. The trick is knowing which paths photograph best at which times. In the early afternoon, the south-facing paths get beautiful backlight filtering through the canopy. By 4pm, the central meadow opens up with soft, even light that flatters every skin tone.</p>

      <p>One of my favorite techniques here is using the layered foliage as a natural frame. By positioning you between foreground branches and a blurred background of green, I create depth that makes your portrait pop off the screen. With professional off-camera lighting, the result is a photo that looks like it belongs in a magazine, not a campus snapshot.</p>

      <p>If you are doing a multi-location session, I recommend starting in Aldrich Park. The relaxed setting helps you warm up in front of the camera before moving to busier spots like the Peter the Anteater statue or Langson Library. Most of my best-selling UCI portraits come from the first 20 minutes in Aldrich Park, when my clients are relaxed and the light is cooperating.</p>""",
        "faqs": [
            ("What is the best time to shoot at Aldrich Park?", "The best time for Aldrich Park graduation photos is between 3pm and 5pm. The afternoon sun filters through the tree canopy, creating soft, dappled light that looks beautiful in portraits without harsh shadows or squinting."),
            ("Is Aldrich Park crowded during graduation season?", "Aldrich Park can get busy on weekends during May and June, but the park is large enough that you can usually find quiet pockets. Weekday sessions are the best way to avoid crowds entirely."),
            ("Can I do multiple outfit changes in Aldrich Park?", "Yes. Aldrich Park has restroom facilities nearby at the Student Center. Most of my clients do at least one outfit change, going from cap and gown to a casual or dressy look."),
            ("Do I need a permit for graduation photos at Aldrich Park?", "For small portrait sessions at UCI, a permit is generally not required. I have been shooting at Aldrich Park for nearly 7 years and know the campus policies well."),
        ],
        "related": ["uci-langson-library-graduation-photos", "uci-peter-anteater-statue-graduation-photos", "uci-infinity-fountain-graduation-photos"],
    },
    {
        "slug": "uci-langson-library-graduation-photos",
        "name": "Langson Library",
        "campus": "uci",
        "campus_name": "UCI",
        "campus_page": "uci-graduation-photos.html",
        "image": "images/location/langson-library.jpg",
        "title": "Langson Library Graduation Photos at UCI | UCI Grad Photos",
        "meta_desc": "Langson Library at UCI offers grand columns and classic architecture for timeless graduation portraits. Best times, poses, and tips for your session.",
        "h1": "Langson Library<br>Graduation Photos",
        "hero_label": "UCI Photo Spot",
        "best_time": "3pm to 5pm",
        "crowd_level": "Low to Moderate",
        "pairs_with": "Aldrich Park, Science Library",
        "content": """<p>Langson Library is one of the most architecturally striking buildings on the UCI campus. The grand columns flanking the entrance, the wide staircase, and the clean symmetrical facade give your graduation photos a timeless, classic quality. If you want portraits that feel polished and elegant, this is the spot.</p>

      <p>The front steps are the signature shot. The natural leading lines of the staircase draw the eye upward to you standing at the top in your cap and gown. From below, the columns frame you against the sky, creating a dramatic composition that works every time. From above, I can shoot down the stairs for a unique perspective that uses the geometric patterns of the steps as a design element.</p>

      <p>What I love about Langson Library is how the building handles light. The front faces south, which means the facade gets direct sun in the morning and transitions to soft, even shade by mid-afternoon. That shaded window between 3pm and 5pm is when the library photographs best. You get beautiful, diffused light across your face without any squinting, and the building's light stone picks up warm reflected tones that complement your gown.</p>

      <p>The side of the building is worth exploring too. The walkway along the east side has a covered corridor with repeating columns that create a stunning rhythm in your photos. I use this area for more intimate, portrait-style shots where the architectural details frame you tightly. It is a great counterpoint to the wide, open shots on the front steps.</p>

      <p>Langson Library pairs naturally with Aldrich Park, which sits directly behind it. I typically start in the park for relaxed, nature-heavy portraits, then walk two minutes to the library for the architectural contrast. The combination gives your gallery a balanced mix of soft and structured compositions.</p>""",
        "faqs": [
            ("When is the best time to photograph at Langson Library?", "The best time is between 3pm and 5pm when the front facade is evenly shaded. This eliminates harsh shadows from the columns and creates soft, flattering light for portraits."),
            ("Is Langson Library a popular graduation photo spot?", "It is popular but less crowded than Aldrich Park or the Peter statue. The wide staircase means there is room for multiple groups without interfering with each other."),
            ("What should I wear for Langson Library photos?", "The light stone and clean architecture pair well with almost any color. Cap and gown always looks great here, and a dressy outfit works well for the elegant backdrop."),
        ],
        "related": ["uci-aldrich-park-graduation-photos", "uci-science-library-graduation-photos", "uci-mstb-graduation-photos"],
    },
    {
        "slug": "uci-infinity-fountain-graduation-photos",
        "name": "Infinity Fountain",
        "campus": "uci",
        "campus_name": "UCI",
        "campus_page": "uci-graduation-photos.html",
        "image": "images/location/infinity-fountain.jpg",
        "title": "Infinity Fountain Graduation Photos at UCI | UCI Grad Photos",
        "meta_desc": "The Infinity Fountain at UCI is a sleek, modern water feature perfect for contemporary graduation portraits. Timing tips and lighting advice.",
        "h1": "Infinity Fountain<br>Graduation Photos",
        "hero_label": "UCI Photo Spot",
        "best_time": "4pm to 5:30pm",
        "crowd_level": "Low",
        "pairs_with": "Peter Anteater Statue, Business School",
        "content": """<p>The Infinity Fountain near the UCI Student Center is one of the most visually striking water features on any college campus. The sleek, modern design with water cascading over a flat surface creates a mirror-like effect that adds a polished, contemporary feel to your graduation portraits.</p>

      <p>What sets this location apart is the way it interacts with light. In the late afternoon, the water catches golden hour rays and creates shimmering reflections behind you. I use professional off-camera lighting to balance you against the bright water, producing a look where you glow against a sparkling, blurred backdrop. The effect is cinematic and eye-catching.</p>

      <p>The fountain sits in an open area near Gateway Plaza, which gives me flexibility with composition. I can shoot tight portraits with the water immediately behind you, or pull back for wider shots that capture the fountain's full scale with the campus architecture in the frame. The open surroundings also mean you rarely have to wait for other groups to clear out.</p>

      <p>One of my favorite approaches here is positioning you at the edge of the fountain so the water line creates a horizontal element across the frame. This grounds the composition and adds a sense of place that feels intentional and designed. It works especially well for duo shots where two graduates can face each other with the fountain stretching between them.</p>

      <p>The Infinity Fountain is a two-minute walk from the Peter the Anteater statue, making it easy to combine both in a single session. I typically hit the fountain during golden hour for the best light on the water, then move to Peter for the iconic mascot shot before sunset.</p>""",
        "faqs": [
            ("Is the Infinity Fountain always running?", "The fountain typically runs during normal campus hours, but it may be turned off occasionally for maintenance. I check conditions before every session and have backup plans if needed."),
            ("What is the best time to shoot at the Infinity Fountain?", "Golden hour, between 4pm and 5:30pm, is ideal. The low sun creates beautiful reflections and sparkle on the water surface that add energy to your portraits."),
            ("Can I get close to the water for photos?", "Yes. The fountain is designed with accessible edges. I position graduates right at the edge for the best reflection effects. Just be careful not to step into the water."),
        ],
        "related": ["uci-peter-anteater-statue-graduation-photos", "uci-business-school-graduation-photos", "uci-aldrich-park-graduation-photos"],
    },
    {
        "slug": "uci-peter-anteater-statue-graduation-photos",
        "name": "Peter the Anteater Statue",
        "campus": "uci",
        "campus_name": "UCI",
        "campus_page": "uci-graduation-photos.html",
        "image": "images/location/peter-statue.jpg",
        "title": "Peter the Anteater Statue Graduation Photos | UCI Grad Photos",
        "meta_desc": "The Peter the Anteater statue is the most iconic UCI graduation photo spot. Tips for getting the best shot at this beloved campus landmark.",
        "h1": "Peter the Anteater<br>Graduation Photos",
        "hero_label": "UCI Photo Spot",
        "best_time": "3pm to 5pm",
        "crowd_level": "High",
        "pairs_with": "Infinity Fountain, UCI Sign off Bison",
        "content": """<p>If there is one photo every UCI graduate needs, it is a shot with Peter the Anteater. The bronze mascot statue near the Student Center is the most beloved landmark on campus and the single most recognizable symbol of UC Irvine. It instantly tells the world where you earned your degree, and it is the photo your family will frame on the mantle.</p>

      <p>The statue sits on a raised platform in an open area, which gives me room to shoot from multiple angles. The classic shot is standing next to Peter with your hand on the statue, but I also love shooting from a low angle to make both you and the statue look larger than life. For couples or friend groups, I position people on either side of Peter for a balanced composition that includes everyone.</p>

      <p>The biggest challenge at Peter is the crowds. During graduation season, especially on weekends, there can be a steady stream of graduates waiting for their turn. I manage this by timing our arrival carefully. Early in the session (before 3:30pm) or later in the evening (after 5:30pm), the area is noticeably quieter. Weekday sessions nearly eliminate the wait entirely.</p>

      <p>Another advantage of shooting with a professional here is lighting. The statue sits in an open area that gets direct sun, which can create harsh shadows on your face. I bring off-camera lighting to fill those shadows and balance the exposure between you and the bright sky. The result is a clean, evenly lit portrait where both you and Peter look great, rather than a silhouette or a squinting snapshot.</p>

      <p>I recommend pairing the Peter statue with the nearby Infinity Fountain and the UCI Sign off Bison. All three are within a short walk and give you a well-rounded set of iconic UCI photos for your gallery.</p>""",
        "faqs": [
            ("How crowded is the Peter statue during graduation season?", "The Peter the Anteater statue is the most popular photo spot at UCI, so expect crowds on weekends in May and June. Weekday sessions and early/late timing help avoid long waits."),
            ("What poses work best at the Peter statue?", "The classic is standing next to Peter with your hand on the statue. I also shoot low-angle shots for a dramatic look, and wider shots that capture the full statue with the campus behind you."),
            ("Is there parking near the Peter statue?", "The closest parking is at the Student Center parking structure, a short walk from the statue. I can help you plan logistics before your session."),
            ("Can I bring props to the Peter statue?", "Absolutely. Sashes, custom caps, balloons, and signs all look great here. The open area gives plenty of room for creative setups."),
        ],
        "related": ["uci-infinity-fountain-graduation-photos", "uci-uci-sign-bison-graduation-photos", "uci-aldrich-park-graduation-photos"],
    },
    {
        "slug": "uci-peter-water-tower-graduation-photos",
        "name": "Peter the Anteater Water Tower",
        "campus": "uci",
        "campus_name": "UCI",
        "campus_page": "uci-graduation-photos.html",
        "image": "images/location/peter-water-tower.jpg",
        "title": "Peter Water Tower Graduation Photos at UCI | UCI Grad Photos",
        "meta_desc": "The iconic Anteater water tower mural near the ARC makes for a bold, uniquely UCI graduation photo backdrop. Tips and best times.",
        "h1": "Peter Water Tower<br>Graduation Photos",
        "hero_label": "UCI Photo Spot",
        "best_time": "3pm to 5pm",
        "crowd_level": "Low",
        "pairs_with": "Bren Events Center, UCI Sign off Bison",
        "content": """<p>The Anteater water tower near the ARC (Anteater Recreation Center) is one of the most recognizable landmarks at UC Irvine. The massive mural of Peter the Anteater painted across the tower makes for a bold, colorful backdrop that is uniquely UCI. No other campus has anything quite like it.</p>

      <p>What makes this location special for graduation photos is the scale. The tower looms large behind you, creating a composition where the viewer's eye moves from you in the foreground to the vibrant mural above. I shoot from various distances to get both tight portraits with the mural peeking in behind you and wider shots that capture the full tower and surrounding landscape.</p>

      <p>The area around the water tower is relatively open, with grass and walkways providing clean foregrounds. Because this is on the east side of campus near the athletic facilities, foot traffic is lighter than central campus spots like Aldrich Park or the Peter statue. You will rarely have to wait for other groups to move out of the frame.</p>

      <p>Lighting here depends on the time of day. The mural faces southwest, so it catches direct afternoon sun that brings out the colors. I typically shoot this location between 3pm and 5pm when the mural is well-lit and the surrounding area gets warm, golden tones. My off-camera lighting fills any shadows on your face so you match the brightness of the vibrant backdrop.</p>

      <p>The water tower is a quick drive or short walk from the Bren Events Center and the UCI Sign off Bison, making it easy to combine all three in a single session route on the east side of campus.</p>""",
        "faqs": [
            ("Where exactly is the water tower at UCI?", "The Anteater water tower is located near the ARC (Anteater Recreation Center) on the east side of campus, close to the athletic fields."),
            ("Is the water tower area accessible for photos?", "Yes. The area around the base of the water tower is open and accessible with grass and paved paths. There are no restricted zones for portrait sessions."),
            ("What time is best for water tower photos?", "Between 3pm and 5pm is ideal. The mural faces southwest and catches direct afternoon light that brings out the colors beautifully."),
        ],
        "related": ["uci-bren-events-center-graduation-photos", "uci-uci-sign-bison-graduation-photos", "uci-peter-anteater-statue-graduation-photos"],
    },
    {
        "slug": "uci-uci-sign-bison-graduation-photos",
        "name": "UCI Sign off Bison",
        "campus": "uci",
        "campus_name": "UCI",
        "campus_page": "uci-graduation-photos.html",
        "image": "images/location/uci-sign-bison.jpg",
        "title": "UCI Sign off Bison Graduation Photos | UCI Grad Photos",
        "meta_desc": "The large UCI entrance sign off Bison Avenue is a classic graduation photo spot. Tips for timing, posing, and getting the best shot.",
        "h1": "UCI Sign off Bison<br>Graduation Photos",
        "hero_label": "UCI Photo Spot",
        "best_time": "4pm to 6pm",
        "crowd_level": "Moderate",
        "pairs_with": "Peter Water Tower, Bren Events Center",
        "content": """<p>The large UCI entrance sign off Bison Avenue is one of the first things you see when you drive onto campus, and it is one of the last shots you want before you leave as a graduate. The bold block letters spelling out "University of California, Irvine" make a statement that needs no explanation. This is the definitive "I went to UCI" photo.</p>

      <p>The sign sits in a landscaped area along Bison Avenue with low hedges and open sky behind it. The composition is straightforward but effective: you stand in front of or next to the sign, and the university name tells the story. What separates a professional shot here from a phone snapshot is lighting and angle. I use off-camera flash to make you pop against the sign, and I shoot from positions that avoid the parking lot and road in the background.</p>

      <p>Timing matters at this spot. The sign faces roughly west, so it catches beautiful warm light during golden hour between 4pm and 6pm. The low sun creates a glow on the letters and wraps around you for a flattering, warm portrait. Earlier in the day, the sign can be in shadow or backlit in a way that is harder to work with.</p>

      <p>This location does get busy during graduation season since it is easy to access and does not require walking deep into campus. Weekday sessions are noticeably less crowded. I also know a few angles that work even when other groups are nearby, using tighter framing to isolate you and the sign from the surroundings.</p>

      <p>The UCI Sign is on the east side of campus, close to the Anteater water tower and Bren Events Center. I often combine all three in an efficient route that covers the major east-side landmarks in about 30 minutes.</p>""",
        "faqs": [
            ("Where is the UCI sign located?", "The main UCI entrance sign is along Bison Avenue on the east side of campus. There is street parking and nearby lot parking available."),
            ("What is the best time to shoot at the UCI sign?", "Golden hour between 4pm and 6pm is best. The sign faces west and catches warm light during this window, creating a beautiful glow on both you and the letters."),
            ("Is the UCI sign area crowded?", "It can get busy on weekends during graduation season since it is easy to access from the road. Weekday sessions offer a much more relaxed experience."),
        ],
        "related": ["uci-peter-water-tower-graduation-photos", "uci-bren-events-center-graduation-photos", "uci-peter-anteater-statue-graduation-photos"],
    },
    {
        "slug": "uci-business-school-graduation-photos",
        "name": "Business School",
        "campus": "uci",
        "campus_name": "UCI",
        "campus_page": "uci-graduation-photos.html",
        "image": "images/location/business-school.jpg",
        "title": "UCI Business School Graduation Photos | UCI Grad Photos",
        "meta_desc": "The Paul Merage School of Business at UCI features modern glass architecture perfect for professional graduation portraits. Tips and best times.",
        "h1": "Business School<br>Graduation Photos",
        "hero_label": "UCI Photo Spot",
        "best_time": "3pm to 5pm",
        "crowd_level": "Low",
        "pairs_with": "Infinity Fountain, Aldrich Park",
        "content": """<p>The Paul Merage School of Business at UCI is a standout for graduation photos. The modern glass-and-steel architecture gives your portraits a sharp, professional edge that you will not find at the older, tree-heavy spots on campus. If you are graduating from the business school, this is your building. And even if you are not, the sleek design makes an impressive backdrop for any graduate.</p>

      <p>The building's courtyard is the star of the show. Clean lines, open space, and a mix of glass walls and concrete create a contemporary aesthetic that photographs beautifully. I use the reflective glass surfaces to add depth to compositions, sometimes catching your reflection alongside your actual portrait for a creative double-image effect.</p>

      <p>The exterior walkways along the building feature covered areas with geometric ceiling patterns that create interesting shadow play on sunny days. These covered sections also provide reliable shade, which means consistent, flattering light regardless of cloud cover or sun position. It is one of the most forgiving locations on campus in terms of lighting flexibility.</p>

      <p>Because the business school is on the south side of campus, it gets less foot traffic from general visitors than Aldrich Park or the Student Center area. You will often have the courtyard to yourselves, which makes for a more relaxed shooting experience and cleaner backgrounds.</p>

      <p>I recommend pairing the business school with the Infinity Fountain, which is a short walk north. The contrast between the fountain's water and the school's glass-and-steel creates variety in your gallery, and both locations photograph well in the same afternoon time window.</p>""",
        "faqs": [
            ("Do I have to be a business student to take photos at the business school?", "Not at all. The exterior and courtyard areas are accessible to everyone. Many non-business graduates choose this spot for its modern, professional look."),
            ("What time is best for business school photos?", "Between 3pm and 5pm. The covered walkways provide shade throughout the afternoon, and the courtyard gets soft, even light during this window."),
            ("What should I wear for business school photos?", "The modern architecture pairs well with both cap and gown and business-formal attire. A sharp suit or professional outfit looks especially fitting against the sleek backdrop."),
        ],
        "related": ["uci-infinity-fountain-graduation-photos", "uci-aldrich-park-graduation-photos", "uci-science-library-graduation-photos"],
    },
    {
        "slug": "uci-science-library-graduation-photos",
        "name": "Science Library",
        "campus": "uci",
        "campus_name": "UCI",
        "campus_page": "uci-graduation-photos.html",
        "image": "images/location/science-library.jpg",
        "title": "Science Library Graduation Photos at UCI | UCI Grad Photos",
        "meta_desc": "UCI Science Library offers a quiet, intimate setting with lush greenery for beautiful graduation portraits. Best times and photography tips.",
        "h1": "Science Library<br>Graduation Photos",
        "hero_label": "UCI Photo Spot",
        "best_time": "3pm to 5pm",
        "crowd_level": "Low",
        "pairs_with": "Langson Library, MSTB",
        "content": """<p>The Science Library at UCI offers something different from the busier central campus spots. Tucked away on the north side of Ring Road, it provides a quieter, more intimate setting surrounded by lush gardens and mature trees. If you want graduation photos with a natural, peaceful feel without sacrificing architectural interest, this is an excellent choice.</p>

      <p>The building itself has a distinctive design with concrete and glass elements that photograph well from multiple angles. But the real draw is the surrounding landscape. The gardens near the Science Library include flowering plants, shaded walkways, and secluded benches that create intimate compositions you cannot get in the more open central campus areas.</p>

      <p>I particularly love the north side of the building where a covered walkway provides consistent shade and clean geometric lines. This area is ideal for portrait-style shots where the background is simplified and the focus is entirely on you. The combination of natural greenery visible through the walkway openings and the building's angular forms creates a layered, visually interesting backdrop.</p>

      <p>Because this location is off the main graduation photo circuit, you will almost never encounter other groups here. That privacy means a more relaxed pace, more creative freedom, and no waiting. It is one of my go-to spots for clients who feel more comfortable without an audience.</p>

      <p>The Science Library is a five-minute walk from both Langson Library and MSTB, making it easy to include in a multi-location session that covers the northern arc of campus. I often recommend this three-stop route for clients who want variety without spending their whole session walking.</p>""",
        "faqs": [
            ("Is the Science Library a good spot for quiet, private photos?", "Yes. It is one of the least crowded graduation photo locations at UCI. The surrounding gardens provide seclusion and a peaceful atmosphere for your session."),
            ("What is the best time for Science Library photos?", "Between 3pm and 5pm. The north-facing walkways stay evenly lit throughout the afternoon, and the gardens catch soft light through the trees."),
            ("Can I combine the Science Library with other spots?", "Absolutely. It is close to Langson Library and MSTB, making it easy to hit all three in a single session for a variety of looks."),
        ],
        "related": ["uci-langson-library-graduation-photos", "uci-mstb-graduation-photos", "uci-aldrich-park-graduation-photos"],
    },
    {
        "slug": "uci-bren-events-center-graduation-photos",
        "name": "Bren Events Center",
        "campus": "uci",
        "campus_name": "UCI",
        "campus_page": "uci-graduation-photos.html",
        "image": "images/location/bren-events-center.jpg",
        "title": "Bren Events Center Graduation Photos at UCI | UCI Grad Photos",
        "meta_desc": "Bren Events Center is where UCI commencement happens. Capture graduation photos at the building where you walked the stage.",
        "h1": "Bren Events Center<br>Graduation Photos",
        "hero_label": "UCI Photo Spot",
        "best_time": "3pm to 5:30pm",
        "crowd_level": "Low",
        "pairs_with": "Peter Water Tower, UCI Sign off Bison",
        "content": """<p>The Bren Events Center holds a special place for every UCI graduate. This is the building where commencement ceremonies take place, where you walk across the stage and officially become a UCI alum. Taking graduation photos here bookends the experience in a meaningful way.</p>

      <p>The front of the building features the Bren Events Center signage and a distinctive anteater statue that provides a secondary mascot photo opportunity beyond the main Peter statue near the Student Center. The open plaza in front of the building gives me room for wider compositions that capture both you and the building in context.</p>

      <p>Architecturally, the Bren Center has a modern, arena-style design with sweeping curved lines and a large entrance canopy. The canopy area provides reliable shade for portrait-style shots, and the wide steps leading up to the entrance create natural leading lines similar to Langson Library but with a more contemporary feel.</p>

      <p>This is one of the quieter locations on campus for graduation photos. Since the Bren Center is on the east side near the athletic complex, it does not see the same foot traffic as central campus spots. You will often have the entire front plaza to yourselves, which means more time for creative shots and less time waiting.</p>

      <p>I recommend combining the Bren Center with the nearby Anteater water tower and UCI Sign off Bison for an east-side campus route. All three are within a short walk or quick drive of each other, and together they cover the major landmarks on this side of campus efficiently.</p>""",
        "faqs": [
            ("Why take graduation photos at the Bren Events Center?", "The Bren Center is where UCI commencement ceremonies are held. Photographing here connects your portraits to the place where you officially graduated, adding sentimental value to your gallery."),
            ("Is the Bren Center area open for photos?", "Yes. The exterior plaza, steps, and surrounding areas are accessible for portrait sessions. The anteater statue in front is also available for photos."),
            ("What time is best for Bren Center photos?", "Between 3pm and 5:30pm. The front entrance faces south and gets even afternoon light, while the canopy provides shade options for different looks."),
        ],
        "related": ["uci-peter-water-tower-graduation-photos", "uci-uci-sign-bison-graduation-photos", "uci-peter-anteater-statue-graduation-photos"],
    },
    {
        "slug": "uci-social-science-gateway-graduation-photos",
        "name": "Social Science Gateway",
        "campus": "uci",
        "campus_name": "UCI",
        "campus_page": "uci-graduation-photos.html",
        "image": "images/location/social-science-gateway.jpg",
        "title": "Social Science Gateway Graduation Photos at UCI | UCI Grad Photos",
        "meta_desc": "The Social Science Gateway at UCI features a colorful stained glass tower and bold architecture for eye-catching graduation portraits.",
        "h1": "Social Science Gateway<br>Graduation Photos",
        "hero_label": "UCI Photo Spot",
        "best_time": "2pm to 4pm",
        "crowd_level": "Low",
        "pairs_with": "Aldrich Park, Langson Library",
        "content": """<p>The Social Science Gateway is one of UCI's most visually distinctive buildings. The colorful stained glass tower is visible from across Ring Road, and its bold geometric design makes it an eye-catching backdrop for graduation portraits. If you want photos that stand out from the typical park-and-library shots, this is the spot to include.</p>

      <p>The stained glass panels create splashes of color that add vibrancy to your photos without competing with your outfit or regalia. I position graduates to catch the colored light falling through the glass, which can create beautiful tinted highlights on your skin and gown. The effect is subtle but distinctive, and it gives your photos from this location a signature look.</p>

      <p>The building's brutalist architecture, with its strong concrete forms and geometric angles, provides a bold structural backdrop. The interplay between the heavy concrete and the delicate stained glass creates visual tension that makes compositions more interesting. I use the angular walls and walkways to frame you in tight shots where the architecture leads the eye directly to you.</p>

      <p>This is a lesser-known graduation photo spot, which works in your favor. Even during peak graduation season, the Social Science Gateway rarely has groups waiting. You can take your time exploring different angles and compositions without feeling rushed.</p>

      <p>The gateway connects naturally to Aldrich Park and Langson Library, both of which are a short walk away on Ring Road. I recommend hitting Social Science Gateway first in a session, when the light on the stained glass is most vivid (before 4pm), then moving to Aldrich Park as the afternoon softens.</p>""",
        "faqs": [
            ("What makes Social Science Gateway unique for photos?", "The colorful stained glass tower is unlike anything else on campus. It adds vibrant color and artistic flair to your graduation portraits in a way that trees and libraries cannot."),
            ("When should I shoot at Social Science Gateway?", "Between 2pm and 4pm is ideal. The stained glass catches the most light during this window, and the colors come through most vividly in your photos."),
            ("Is Social Science Gateway crowded?", "No. It is one of the least crowded graduation photo spots at UCI. You will usually have the area to yourselves even during graduation season."),
        ],
        "related": ["uci-aldrich-park-graduation-photos", "uci-langson-library-graduation-photos", "uci-mstb-graduation-photos"],
    },
    {
        "slug": "uci-mstb-graduation-photos",
        "name": "MSTB",
        "campus": "uci",
        "campus_name": "UCI",
        "campus_page": "uci-graduation-photos.html",
        "image": "images/location/mstb.jpg",
        "title": "MSTB Graduation Photos at UCI | UCI Grad Photos",
        "meta_desc": "The MSTB arched walkways at UCI create stunning, symmetrical graduation portraits. Tips on timing, angles, and making the most of this photogenic spot.",
        "h1": "MSTB Arches<br>Graduation Photos",
        "hero_label": "UCI Photo Spot",
        "best_time": "3pm to 5pm",
        "crowd_level": "Low",
        "pairs_with": "Science Library, Langson Library",
        "content": """<p>The Mathematical Sciences and Teaching Building, known as MSTB, is one of the most photogenic spots on the UCI campus. The repeating arched walkways create a stunning sense of depth and symmetry that makes every portrait feel architectural and intentional. If you have ever seen a UCI graduation photo with beautiful arches receding into the background, it was probably taken here.</p>

      <p>The arches work because they create natural framing. I position you within one of the archways so the repeating forms behind you draw the eye deep into the frame while you remain the clear focal point. The curved lines soften the composition compared to the straight edges of most campus buildings, giving your photos an almost European feel.</p>

      <p>The walkway is covered, which means consistent shade regardless of the time of day. This is one of the most lighting-friendly spots at UCI. Even on a bright afternoon, the covered arches block direct sun and create soft, even illumination that flatters your features. Add professional off-camera lighting, and the result is a portrait with gallery-quality light and a stunning architectural backdrop.</p>

      <p>MSTB is on the north side of campus and sees very little foot traffic for graduation photos. Most graduates head straight to Aldrich Park and the Peter statue, which means the arched walkways are often completely empty. That privacy gives us time to experiment with different angles, focal lengths, and compositions without rushing.</p>

      <p>I recommend pairing MSTB with the Science Library and Langson Library, both of which are nearby on the northern Ring Road. This three-stop route gives you nature (Science Library gardens), architecture (MSTB arches), and classic academia (Langson columns) in a compact loop.</p>""",
        "faqs": [
            ("What are the MSTB arches at UCI?", "MSTB stands for Mathematical Sciences and Teaching Building. It features a covered walkway with repeating arches that create one of the most photogenic backdrops on campus."),
            ("When is the best time for MSTB photos?", "The covered arches provide shade all day, so you have flexibility. Between 3pm and 5pm, the surrounding light is warmest, which enhances the look of the archway shots."),
            ("Is MSTB crowded for graduation photos?", "Rarely. MSTB is one of the quieter graduation photo spots at UCI, located on the north side of campus away from the busier central areas."),
        ],
        "related": ["uci-science-library-graduation-photos", "uci-langson-library-graduation-photos", "uci-social-science-gateway-graduation-photos"],
    },
]

USC_SPOTS = [
    {
        "slug": "usc-mudd-hall-graduation-photos",
        "name": "Mudd Hall of Philosophy",
        "campus": "usc",
        "campus_name": "USC",
        "campus_page": "usc-graduation-photos.html",
        "image": "images/portfolio/img-025.jpg",
        "title": "Mudd Hall Graduation Photos at USC | UCI Grad Photos",
        "meta_desc": "Mudd Hall of Philosophy at USC offers Romanesque architecture and lush gardens for dramatic, old-world graduation portraits.",
        "h1": "Mudd Hall<br>Graduation Photos",
        "hero_label": "USC Photo Spot",
        "best_time": "2pm to 5pm",
        "crowd_level": "Low",
        "pairs_with": "Doheny Library, Bovard Auditorium",
        "content": """<p>Mudd Hall of Philosophy is one of USC's hidden gems for graduation photos. The Romanesque architecture, with its arched doorways, stone columns, and warm brick tones, creates a dramatic, old-world backdrop that you will not find anywhere else on campus. While most graduates flock to Tommy Trojan and Doheny Library, Mudd Hall offers equally stunning photos with significantly less competition for space.</p>

      <p>The building's exterior walkways are the standout feature. The arched openings create natural frames for portrait shots, and the repeating columns add rhythm and depth to wider compositions. I love positioning graduates within one of the arches so the stone forms a clean border around the portrait, drawing the viewer's eye directly to you.</p>

      <p>The courtyard garden adjacent to Mudd Hall provides a completely different aesthetic. Lush greenery, flowering plants, and mature trees create a softer, more romantic backdrop that contrasts beautifully with the building's heavy stone architecture. I typically shoot both the architectural and garden sides to give your gallery variety without walking more than a few steps between setups.</p>

      <p>Lighting at Mudd Hall is forgiving. The covered walkways block direct sun throughout the afternoon, giving you even, soft light that flatters every skin tone. The warm stone surfaces also bounce golden tones back into your photos, adding a richness that cold concrete buildings cannot match.</p>

      <p>Mudd Hall is a short walk from both Doheny Library and Bovard Auditorium, making it easy to combine in a multi-location USC session. I recommend starting here while the garden light is soft, then moving to the more iconic spots as the afternoon progresses.</p>""",
        "faqs": [
            ("Where is Mudd Hall at USC?", "Mudd Hall of Philosophy is located on the west side of the USC campus, near the Hoose Library of Philosophy. It is a short walk from Doheny Library and Bovard Auditorium."),
            ("Is Mudd Hall crowded during graduation season?", "No. Mudd Hall is one of the least crowded graduation photo spots at USC. Most graduates head to Tommy Trojan and Doheny, leaving Mudd Hall quiet and private."),
            ("What makes Mudd Hall special for photos?", "The Romanesque arched walkways and lush courtyard garden create a dramatic, European-inspired backdrop. The warm stone tones and natural shade make it one of the most photogenic buildings on campus."),
        ],
        "related": ["usc-doheny-library-graduation-photos", "usc-bovard-auditorium-graduation-photos", "usc-tommy-trojan-graduation-photos"],
    },
    {
        "slug": "usc-tommy-trojan-graduation-photos",
        "name": "Tommy Trojan",
        "campus": "usc",
        "campus_name": "USC",
        "campus_page": "usc-graduation-photos.html",
        "image": "images/location/tommy-trojan.jpg",
        "title": "Tommy Trojan Graduation Photos at USC | UCI Grad Photos",
        "meta_desc": "Tommy Trojan is the most iconic USC graduation photo spot. Tips on timing, avoiding crowds, and getting the perfect shot at the Trojan Shrine.",
        "h1": "Tommy Trojan<br>Graduation Photos",
        "hero_label": "USC Photo Spot",
        "best_time": "Before 3pm or after 6pm",
        "crowd_level": "Very High",
        "pairs_with": "Bovard Auditorium, Steps of Troy",
        "content": """<p>Tommy Trojan is the graduation photo that every USC student needs. The iconic bronze warrior statue at the center of Trousdale Parkway, surrounded by the Trojan Shrine, is the single most recognizable symbol of the university. It is the shot your family will frame, the one you will post on every social media platform, and the image that defines your USC experience in a single frame.</p>

      <p>The statue faces west on a raised circular platform, with the Trojan Shrine columns creating a semicircular backdrop behind it. This arrangement gives me several composition options: the classic standing-next-to-Tommy shot, a wider frame that includes the shrine columns, and creative angles that use the columns as leading lines pointing toward you and the statue.</p>

      <p>The biggest challenge here is crowds. During graduation season, especially on weekends, there can be a line of 30 to 45 minutes for a clean shot. I manage this with strategic timing. Early sessions (before 3pm) catch the area before the afternoon rush. Evening sessions (after 6pm) benefit from thinning crowds and beautiful warm light. Weekday sessions nearly eliminate the wait entirely.</p>

      <p>Lighting at Tommy Trojan requires thought. The statue faces west, so late afternoon sun hits it from behind, creating a warm backlit glow. I bring professional off-camera lighting to fill the shadows on your face, balancing you against the golden backlight for a polished, editorial look. Without that fill light, you would be a silhouette against the bright sky.</p>

      <p>I recommend pairing Tommy Trojan with Bovard Auditorium and the Steps of Troy, both of which are on Trousdale Parkway within a two-minute walk. This central campus loop covers the three most iconic USC locations efficiently.</p>""",
        "faqs": [
            ("How long is the wait at Tommy Trojan during graduation season?", "On weekends in May, waits can reach 30 to 45 minutes. Weekday sessions and early/late timing (before 3pm or after 6pm) significantly reduce wait times."),
            ("What is the best time to photograph Tommy Trojan?", "Before 3pm or after 6pm on weekdays. The statue faces west, so late afternoon creates warm backlight. My off-camera lighting fills the shadows for a balanced exposure."),
            ("Can I get solo shots at Tommy Trojan?", "Yes. Even during busy times, I work quickly to capture clean solo portraits. Having professional lighting means I can get the shot in less time than casual phone photographers."),
            ("What poses work best at Tommy Trojan?", "Classic poses include standing next to the statue with your hand on the shield, sitting on the base, and wider shots with the Trojan Shrine columns. The Fight On hand sign is also popular."),
        ],
        "related": ["usc-bovard-auditorium-graduation-photos", "usc-steps-of-troy-graduation-photos", "usc-doheny-library-graduation-photos"],
    },
    {
        "slug": "usc-traveler-horse-graduation-photos",
        "name": "Traveler Horse Statue",
        "campus": "usc",
        "campus_name": "USC",
        "campus_page": "usc-graduation-photos.html",
        "image": "images/location/traveler-horse.jpg",
        "title": "Traveler Horse Statue Graduation Photos at USC | UCI Grad Photos",
        "meta_desc": "The Traveler horse statue near the Coliseum captures USC athletic tradition. Tips for getting bold, energetic graduation portraits here.",
        "h1": "Traveler Horse Statue<br>Graduation Photos",
        "hero_label": "USC Photo Spot",
        "best_time": "4pm to 5:30pm",
        "crowd_level": "Low to Moderate",
        "pairs_with": "Tommy Trojan, Steps of Troy",
        "content": """<p>The Traveler statue near the Los Angeles Memorial Coliseum embodies the spirit of USC athletics and tradition. The dynamic bronze horse and rider captured mid-charge create an energetic, powerful backdrop that makes your graduation portraits feel bold and celebratory. It is a departure from the typical columns-and-libraries graduation photo, and that is exactly the point.</p>

      <p>The statue sits in an open area on the south side of campus, slightly removed from the main pedestrian pathways. This works in your favor. While Tommy Trojan draws the biggest crowds, Traveler is often nearly empty, giving you time to explore different angles and compositions without waiting. The open surroundings also mean cleaner backgrounds and more room for group shots.</p>

      <p>The horse and rider are positioned dynamically, which lends energy to your photos even in static poses. I shoot from low angles to emphasize the statue's drama, placing you alongside it so the composition feels balanced between the charging horse and your confident, celebratory stance. Wider shots that capture the full statue with the Coliseum visible in the background tell the complete USC athletic story.</p>

      <p>Late afternoon is the sweet spot for this location. Between 4pm and 5:30pm, the open area catches golden hour light that wraps around both you and the statue. The warm tones enhance the bronze surface of Traveler and give your skin a healthy, sun-kissed glow. My off-camera lighting adds fill to keep the details sharp even as the natural light gets dramatic.</p>

      <p>I typically pair Traveler with Tommy Trojan and the Steps of Troy for clients who want a mix of USC's most recognizable landmarks. The three are connected by a short walk along Trousdale Parkway and Exposition Boulevard.</p>""",
        "faqs": [
            ("Where is the Traveler horse statue?", "The Traveler statue is located near the Los Angeles Memorial Coliseum on the south side of the USC campus, close to Exposition Boulevard."),
            ("Is the Traveler statue crowded during graduation season?", "Much less than Tommy Trojan or Doheny Library. The slightly off-campus location means fewer groups, giving you a more private, relaxed session."),
            ("What time is best for Traveler statue photos?", "Between 4pm and 5:30pm. The open area gets beautiful golden hour light that enhances the bronze statue and creates warm, flattering portraits."),
        ],
        "related": ["usc-tommy-trojan-graduation-photos", "usc-steps-of-troy-graduation-photos", "usc-bovard-auditorium-graduation-photos"],
    },
    {
        "slug": "usc-doheny-library-graduation-photos",
        "name": "Doheny Library",
        "campus": "usc",
        "campus_name": "USC",
        "campus_page": "usc-graduation-photos.html",
        "image": "images/location/doheny-library.jpg",
        "title": "Doheny Library Graduation Photos at USC | UCI Grad Photos",
        "meta_desc": "Doheny Memorial Library at USC is the architectural crown jewel of campus. Tips for getting stunning graduation portraits on the grand staircase.",
        "h1": "Doheny Library<br>Graduation Photos",
        "hero_label": "USC Photo Spot",
        "best_time": "3pm to 5pm",
        "crowd_level": "Moderate",
        "pairs_with": "Mudd Hall, Tommy Trojan",
        "content": """<p>Doheny Memorial Library is the architectural crown jewel of USC. The Romanesque facade, the arched entrance, the grand staircase, and the towering columns create a backdrop that looks like it belongs in a film. It is one of the most versatile photo locations on campus because you can shoot from so many different angles, each producing a distinct composition.</p>

      <p>The front steps are the signature shot. The wide staircase gives you elevation options: standing at the top with the building framing you, walking up the steps for a candid feel, or sitting on the lower stairs for a relaxed pose. I also use the side pillars to frame tighter portraits where the stone columns create a natural border around you.</p>

      <p>What makes Doheny special from a photography standpoint is the light. The building faces east, which means the front facade transitions into shade during the afternoon. This shaded condition is ideal for portraits because it eliminates squinting, removes harsh shadows from the columns, and creates soft, even illumination across your face. The window between 3pm and 5pm is when Doheny photographs best.</p>

      <p>The arched entrance is another highlight. Standing centered in the doorway with the dark interior behind you creates a dramatic, high-contrast composition. I use off-camera flash to light you against the shadow, producing a portrait that has real depth and visual impact. It is one of the most requested shots from my USC portfolio.</p>

      <p>Doheny pairs naturally with Mudd Hall (a short walk west) and Tommy Trojan (a few minutes east on Trousdale). This central campus route gives your gallery a mix of grand architecture, Romanesque details, and the iconic statue.</p>""",
        "faqs": [
            ("When is the best time to photograph at Doheny Library?", "Between 3pm and 5pm. The east-facing building is shaded during the afternoon, which creates soft, even light that is perfect for portraits without squinting or harsh shadows."),
            ("Is Doheny Library crowded for graduation photos?", "Moderately. It is popular but the wide staircase accommodates multiple groups. Weekday sessions are less crowded than weekends during graduation season."),
            ("What are the best shots at Doheny Library?", "The front staircase, the side pillars, and the arched entrance doorway. Each offers a different composition, from wide architectural shots to tight framed portraits."),
        ],
        "related": ["usc-mudd-hall-graduation-photos", "usc-tommy-trojan-graduation-photos", "usc-bovard-auditorium-graduation-photos"],
    },
    {
        "slug": "usc-bovard-auditorium-graduation-photos",
        "name": "Bovard Auditorium",
        "campus": "usc",
        "campus_name": "USC",
        "campus_page": "usc-graduation-photos.html",
        "image": "images/location/bovard-auditorium.jpg",
        "title": "Bovard Auditorium Graduation Photos at USC | UCI Grad Photos",
        "meta_desc": "Bovard Auditorium on Trousdale Parkway features red brick, white columns, and a dramatic walkway for beautiful USC graduation portraits.",
        "h1": "Bovard Auditorium<br>Graduation Photos",
        "hero_label": "USC Photo Spot",
        "best_time": "3pm to 5pm",
        "crowd_level": "Low to Moderate",
        "pairs_with": "Tommy Trojan, Doheny Library",
        "content": """<p>Bovard Auditorium sits prominently on Trousdale Parkway with its red brick exterior, white columns, and classic collegiate design. The long walkway leading up to the building creates one of the most dramatic approach compositions on campus. It is an underrated location that delivers stunning results.</p>

      <p>What makes Bovard special is depth. The long walkway provides leading lines that draw the viewer's eye straight to you standing in front of the building. This depth creates a sense of grandeur that flatter compositions cannot achieve. I shoot from the far end of the walkway with a telephoto lens to compress the perspective, making the columns and building loom impressively behind you.</p>

      <p>The columns along the front of the building are ideal for portrait-style shots. I position graduates between columns for a clean, framed composition where the white pillars create strong vertical lines on either side of you. The red brick background provides a warm, rich tone that complements both cardinal-and-gold USC regalia and casual outfits.</p>

      <p>The building faces south, so afternoon light hits the front evenly without harsh shadows from the columns. Between 3pm and 5pm, the lighting is consistently flattering. The covered colonnade also provides shade for alternative compositions if the sun is too direct.</p>

      <p>Bovard connects directly to Tommy Trojan and Doheny Library via Trousdale Parkway, making it the natural middle stop in a three-location central campus route. I typically shoot Bovard between the other two, capturing the walkway approach while we are already moving between the marquee spots.</p>""",
        "faqs": [
            ("Is Bovard Auditorium a popular graduation photo spot?", "It is less crowded than Tommy Trojan or Doheny Library but equally photogenic. The walkway and columns produce beautiful compositions with shorter wait times."),
            ("What is the best time for Bovard photos?", "Between 3pm and 5pm. The south-facing building gets even afternoon light, and the covered colonnade provides shade options for variety."),
            ("What makes the Bovard walkway special for photos?", "The long, tree-lined walkway creates dramatic leading lines and depth. Shot with a telephoto lens, the compressed perspective makes the building look grand and imposing behind you."),
        ],
        "related": ["usc-tommy-trojan-graduation-photos", "usc-doheny-library-graduation-photos", "usc-steps-of-troy-graduation-photos"],
    },
    {
        "slug": "usc-steps-of-troy-graduation-photos",
        "name": "Steps of Troy",
        "campus": "usc",
        "campus_name": "USC",
        "campus_page": "usc-graduation-photos.html",
        "image": "images/location/steps-of-troy.jpg",
        "title": "Steps of Troy Graduation Photos at USC | UCI Grad Photos",
        "meta_desc": "The Steps of Troy at USC is a grand staircase perfect for cinematic graduation photos. Tips on angles, group shots, and the best times to shoot.",
        "h1": "Steps of Troy<br>Graduation Photos",
        "hero_label": "USC Photo Spot",
        "best_time": "3pm to 4:30pm",
        "crowd_level": "Moderate",
        "pairs_with": "Tommy Trojan, Bovard Auditorium",
        "content": """<p>The Steps of Troy is the wide, sweeping staircase at the heart of the USC campus. Its symmetrical design and surrounding architecture create a grand, cinematic composition that captures the scale and prestige of the university. If you want a graduation photo that screams "I graduated from USC," the Steps of Troy delivers.</p>

      <p>The staircase offers natural elevation changes, which gives me incredible variety within a single location. From below, I shoot upward with you standing at the top, arms wide, celebrating. This angle makes you look powerful and triumphant against the sky. From above, I capture you walking down the steps with the campus stretching out behind you. From the side, the repeating horizontal lines of the steps create a graphic, architectural composition.</p>

      <p>This is also one of the best spots on campus for group photos. The width of the staircase comfortably accommodates a dozen or more people without anyone feeling cramped. I line groups across a single step for a clean horizontal composition, or stagger people across multiple steps for a more dynamic arrangement.</p>

      <p>The steps face north, which means they stay evenly lit throughout the afternoon without harsh directional shadows. Between 3pm and 4:30pm, the light is warm but diffused, creating flattering conditions for both solo and group portraits. The building facades on either side of the steps also act as natural reflectors, bouncing soft light back into the scene.</p>

      <p>The Steps of Troy connects directly to Tommy Trojan and Bovard Auditorium, making it a natural stop in the central Trousdale Parkway route. I recommend including it in any USC session that covers the campus core.</p>""",
        "faqs": [
            ("What makes the Steps of Troy good for graduation photos?", "The grand staircase creates a cinematic backdrop with natural elevation changes. You can shoot from above, below, or from the side for completely different looks within one location."),
            ("Is the Steps of Troy good for group photos?", "Excellent. The wide staircase is one of the best spots on campus for large groups. A dozen people can pose comfortably across the steps without feeling cramped."),
            ("When should I shoot at the Steps of Troy?", "Between 3pm and 4:30pm. The north-facing steps stay evenly lit without harsh shadows throughout the afternoon, and the surrounding buildings provide soft, reflected light."),
        ],
        "related": ["usc-tommy-trojan-graduation-photos", "usc-bovard-auditorium-graduation-photos", "usc-doheny-library-graduation-photos"],
    },
    {
        "slug": "usc-shumway-fountain-graduation-photos",
        "name": "Shumway Fountain",
        "campus": "usc",
        "campus_name": "USC",
        "campus_page": "usc-graduation-photos.html",
        "image": "images/location/shumway-fountain.jpg",
        "title": "Shumway Fountain Graduation Photos at USC | UCI Grad Photos",
        "meta_desc": "Shumway Fountain at USC adds water, movement, and golden hour sparkle to your graduation portraits. Tips on timing and the best compositions.",
        "h1": "Shumway Fountain<br>Graduation Photos",
        "hero_label": "USC Photo Spot",
        "best_time": "4pm to 5:30pm",
        "crowd_level": "Low",
        "pairs_with": "Doheny Library, Mudd Hall",
        "content": """<p>The Patsy and Forrest Shumway Fountain near Alumni Park is a stunning water feature surrounded by lush landscaping. The cascading water adds movement and energy to your graduation portraits in a way that static architectural backdrops simply cannot match. It is a refreshing change of pace that brings variety to any USC session.</p>

      <p>What makes Shumway Fountain stand out for photography is how it interacts with light. In the late afternoon, the sun catches the water surface and creates shimmering reflections and sparkle behind you. I position graduates in front of the fountain and use a wide aperture to blur the water into a soft, dreamy backdrop filled with golden bokeh dots. Combined with off-camera lighting on your face, the effect is cinematic.</p>

      <p>The surrounding landscaping adds to the location's appeal. Mature trees and manicured gardens provide additional backdrop options within steps of the fountain itself. I often start with the fountain for the dramatic water shots, then pivot to the nearby greenery for softer, nature-focused portraits. This gives your gallery two distinct looks from one location.</p>

      <p>Shumway Fountain is one of the quieter spots on campus for graduation photos. Located near Alumni Park on the north side, it does not see the heavy foot traffic of Trousdale Parkway. You will usually have the fountain to yourselves, which means more time for creative experimentation and less time waiting for other groups to clear out.</p>

      <p>I recommend shooting here between 4pm and 5:30pm for the best water sparkle and golden hour warmth. Pair it with Doheny Library or Mudd Hall for a session route that covers the north and west sides of campus.</p>""",
        "faqs": [
            ("Is the Shumway Fountain always running?", "The fountain typically operates during normal campus hours. Occasionally it may be off for maintenance. I check conditions before every session and have alternative plans if needed."),
            ("What time is best for fountain photos?", "Between 4pm and 5:30pm. The backlit water creates beautiful bokeh and golden sparkle during the late afternoon golden hour."),
            ("What style of photos work best at the fountain?", "Portraits with the water blurred in the background, candid walking shots along the surrounding paths, and couples photos with the fountain as a romantic backdrop all work beautifully here."),
        ],
        "related": ["usc-doheny-library-graduation-photos", "usc-mudd-hall-graduation-photos", "usc-tommy-trojan-graduation-photos"],
    },
]

ALL_SPOTS = UCI_SPOTS + USC_SPOTS

# Gallery images for spot pages (cycle through these)
GALLERY_SETS = [
    ["images/portfolio/img-009.jpg", "images/portfolio/img-020.jpg", "images/portfolio/img-030.jpg", "images/portfolio/img-040.jpg", "images/portfolio/img-050.jpg"],
    ["images/portfolio/img-011.jpg", "images/portfolio/img-025.jpg", "images/portfolio/img-033.jpg", "images/portfolio/img-041.jpg", "images/portfolio/img-051.jpg"],
    ["images/portfolio/img-008.jpg", "images/portfolio/img-021.jpg", "images/portfolio/img-028.jpg", "images/portfolio/img-035.jpg", "images/portfolio/img-044.jpg"],
    ["images/portfolio/img-007.jpg", "images/portfolio/img-024.jpg", "images/portfolio/img-031.jpg", "images/portfolio/img-039.jpg", "images/portfolio/img-047.jpg"],
    ["images/portfolio/img-010.jpg", "images/portfolio/img-027.jpg", "images/portfolio/img-034.jpg", "images/portfolio/img-045.jpg", "images/portfolio/img-053.jpg"],
]

def get_spot_name(slug):
    for s in ALL_SPOTS:
        if s["slug"] == slug:
            return s["name"]
    return slug

def generate_spot_page(spot, idx):
    s = spot
    campus = s["campus"]
    lat = 33.6405 if campus == "uci" else 34.0224
    lng = -117.8443 if campus == "uci" else -118.2851
    city = "Irvine" if campus == "uci" else "Los Angeles"
    url = f"https://www.ucigradphotos.com/spots/{s['slug']}.html"

    # Related spots
    related_html = ""
    for rs in s.get("related", []):
        rspot = next((x for x in ALL_SPOTS if x["slug"] == rs), None)
        if rspot:
            related_html += f'''        <a href="{rs}.html" class="spot-card" style="text-decoration:none;color:inherit;">
          <img src="../{rspot['image']}" alt="{rspot['name']} graduation photo" loading="lazy">
          <h3>{rspot['name']}</h3>
        </a>\n'''

    gallery = GALLERY_SETS[idx % len(GALLERY_SETS)]
    gallery_html = "\n          ".join(f'<img src="../{img}" alt="{s["campus_name"]} graduation portrait" loading="lazy">' for img in gallery)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{GA}
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{s["title"]}</title>
  <meta name="description" content="{s["meta_desc"]}">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="{s["title"]}">
  <meta property="og:description" content="{s["meta_desc"]}">
  <meta property="og:url" content="{url}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://www.ucigradphotos.com/{s["image"]}">
  <meta property="og:site_name" content="UCI Grad Photos">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{s["title"]}">
  <meta name="twitter:description" content="{s["meta_desc"]}">
  <meta name="twitter:image" content="https://www.ucigradphotos.com/{s["image"]}">
{favicons()}
  <link rel="stylesheet" href="../css/style.css">
  <script type="application/ld+json">
  {local_business_jsonld(s["meta_desc"], url, lat, lng, city)}
  </script>
  <script type="application/ld+json">
  {breadcrumb_jsonld([("Home", "https://www.ucigradphotos.com/"), (f"{s['campus_name']} Graduation Photos", f"https://www.ucigradphotos.com/{s['campus_page']}"), (f"{s['name']} Graduation Photos", url)])}
  </script>
  <script type="application/ld+json">
  {faq_jsonld(s["faqs"])}
  </script>
</head>
<body>
{navbar()}

{hero_section(s["hero_label"], s["h1"], f"Professional graduation photos at {s['name']}. Expert lighting, relaxed vibes, 24-hour delivery.", idx)}

  <!-- Spot Deep Dive -->
  <section class="section section-padding fade-in">
    <div class="container container--narrow">
      <p class="section-label">{s["campus_name"]} Photo Spot</p>
      <h2>Why {s["name"]} is Perfect for Graduation Photos</h2>
      <img src="../{s["image"]}" alt="{s["name"]} graduation photo at {s['campus_name']}" style="width:100%;border-radius:var(--r-lg);margin:2rem 0;">
      {s["content"]}
    </div>
  </section>

  <!-- Quick Facts -->
  <section class="section-padding bg-light fade-in">
    <div class="container" style="max-width:600px;">
      <div class="quick-facts-card">
        <h3>Quick Facts</h3>
        <div class="quick-facts-grid">
          <div><strong>Best Time</strong><p>{s["best_time"]}</p></div>
          <div><strong>Crowd Level</strong><p>{s["crowd_level"]}</p></div>
          <div><strong>Pairs Well With</strong><p>{s["pairs_with"]}</p></div>
          <div><strong>Campus</strong><p><a href="../{s["campus_page"]}" style="color:var(--accent);">{s["campus_name"]}</a></p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Sample Gallery -->
  <section class="section section-padding fade-in">
    <div class="container">
      <div class="text-center">
        <p class="section-label">Portfolio</p>
        <h2>Sample Graduation Portraits</h2>
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

{pricing_section(campus)}

  <!-- FAQ -->
  <section class="section section-padding bg-light fade-in" id="faq">
    <div class="container">
      <div class="text-center">
        <p class="section-label">FAQ</p>
        <h2>{s["name"]} Photo Questions</h2>
      </div>
      <div class="faq-list" style="margin-top: var(--space-2xl);">
{faq_html(s["faqs"])}      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section section-padding fade-in">
    <div class="container text-center">
      <h2>Book Your {s["name"]} Session</h2>
      <p class="mx-auto" style="max-width:640px;margin:1.5rem auto 3rem;">Ready for stunning graduation photos at {s["name"]}? Book your session and get your raw photos within 24 hours.</p>
      <a href="../contact.html" class="btn btn--primary btn--large">Book Your Session</a>
    </div>
  </section>

  <!-- Related Spots -->
  <section class="section section-padding bg-light fade-in">
    <div class="container">
      <div class="text-center">
        <p class="section-label">Explore More</p>
        <h2>Other {s["campus_name"]} Photo Spots</h2>
      </div>
      <div class="spots-grid" style="margin-top:2rem;">
{related_html}      </div>
    </div>
  </section>

{footer()}
  <script src="../js/main.js"></script>
</body>
</html>'''
    write_page("spots", f"{s['slug']}.html", html)

# Generate all spot pages
print("Generating spot pages...")
for i, spot in enumerate(ALL_SPOTS):
    generate_spot_page(spot, i)
print(f"  Done: {len(ALL_SPOTS)} spot pages generated.")
