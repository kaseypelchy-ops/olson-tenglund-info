# Olson & Tenglund informational website — redesigned

A lightweight, responsive, static four-page site for the three Olson & Tenglund auto parts locations. The design uses the user-supplied company logos and automotive parts Facebook banner. No database, catalog, or checkout is required.

## Pages
- `/` Home
- `/locations` Stores, addresses, click-to-call, directions
- `/about` Local-business overview
- `/contact` Contact details

## Deploy
Upload the contents of this folder into the existing `olson-tenglund-info` GitHub repository, then push to `main`. Vercel should redeploy the existing `olson-tenglund-info` project automatically. This is **not** the original inventory/catalog repository.

From Windows PowerShell inside this site directory: `git add .; git commit -m "Redesign informational site"; git push origin main`.

## Before owner approval
Confirm the owner approves all copy and Auto Value mentions, and confirm the listed phone/address information. Store hours are intentionally omitted; the site advises customers to call. The parts banner is owner-provided design artwork; this release does not add unauthorised Auto Value offers or prices.

## Technical
Four static HTML pages, one CSS file, one small JS file, and `/assets`. Routes are configured in `vercel.json`. Google Fonts are loaded online, with system fallbacks. Phone links use `tel:`; directions use Google Maps search URLs.


## November image refresh
- `assets/parts-counter-scene.webp`: new homepage hero background — photographed-style service at a parts counter.
- `assets/mechanic-at-work.webp`: new, distinct photo for the lower promotional section.
- The original `assets/olson-banner.webp` stays in the archive but is not referenced on the homepage.
- The pictures are illustrative AI-generated scenes, not photographs of actual Olson & Tenglund personnel or premises.
- Publicly displayed store hours: Monday–Friday, 8:00 AM–5:00 PM.
