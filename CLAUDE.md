# CLAUDE.md

## Project Overview

Static multi-page graduation photography site for UCI Grad Photos (Orange County, CA). No framework or build system. Pure HTML/CSS/JavaScript.

## Development

No build step. To preview locally:

```bash
python -m http.server
```

No test suite or linting is configured.

## Architecture

- `index.html` - Homepage
- `portfolio.html` - Photo gallery with filtering
- `pricing.html` - Package pricing for all campuses
- `contact.html` - Booking page with Calendly embed
- `faq.html` - Expanded FAQ
- `blog.html` - Blog listing page
- `uci-graduation-photos.html` - UCI campus landing page
- `usc-graduation-photos.html` - USC campus landing page
- `csuf-graduation-photos.html` - CSUF campus landing page
- `chapman-graduation-photos.html` - Chapman campus landing page
- `css/style.css` - All styles, CSS custom properties for theming
- `js/main.js` - Navbar, mobile menu, animations, FAQ accordion, lightbox, Calendly helper
- `blog/` - Individual blog post HTML files
- `images/` - All images organized by subfolder

## CSS Theming

Colors and fonts controlled via CSS custom properties in `css/style.css`:
- Accent: `--color-accent: #6c5ce7` (vibrant purple)
- Fonts: Sora (display) + Inter (body) via Google Fonts
- Responsive breakpoints: 768px (mobile), 1024px (tablet)

## Blog

Static blog. Each post is a standalone HTML file in `blog/`. No markdown or fetch calls.

- Listing page: `blog.html` - manually add a card for each new post (newest first)
- Post files: `blog/[slug].html`
- Images: `images/blog-{slug}/`
- All links use relative paths

## Booking Integration

Calendly embed: `https://calendly.com/guramrit-art/2026-graduation-season`
- Inline widget on contact.html
- CTA buttons on other pages link to contact.html

## Key Contact Info

- Phone: (949) 312-8300
- Email: guramrit.art@gmail.com
- Instagram: @ucigradpics, @guramrit.art

## Git Policy

Never push to git without explicit user approval.

## SEO

Every page includes JSON-LD structured data (LocalBusiness, FAQPage, Service, BreadcrumbList as appropriate). After creating any new page, review SEO before considering the task complete.

## Writing Style

Never use em dashes. Use commas, periods, semicolons, or rewrite the sentence instead.

## Image Optimization

Resize to max 1600px width, compress to JPG. Use `sips` on macOS. Never serve unoptimized files.
