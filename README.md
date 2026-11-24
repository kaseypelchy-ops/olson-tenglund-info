# Olson & Tenglund, Inc. — Informational Website

A static four-page website for the Olson & Tenglund auto parts stores in Port Allegany, Coudersport and Smethport, Pennsylvania. This design follows the approved dark-navy parts-counter homepage reference, with real HTML content and responsive layouts.

## Pages
- `/` — Homepage: parts-counter hero, Auto Value partnership, hours, all three locations, parts/supplies, and a local-service message.
- `/locations` — Addresses, telephone links and maps directions.
- `/about` — Company overview.
- `/contact` — Contact information.

## Business details
Store hours: Monday–Friday, 8:00 AM–5:00 PM at all locations.
- Port Allegany: 303 N Main St, Port Allegany, PA 16743 · 814-642-2517
- Coudersport: 112 N Main St, Coudersport, PA 16915 · 814-274-8881
- Smethport: 400 W Main St, Smethport, PA 16749 · 814-887-7777

## Deploy
Extract the ZIP contents into the **existing** `olson-info-site` Git working directory (do not delete `.git`), replacing existing files. Then:

```powershell
git add .
git commit -m "Match informational homepage to preferred design"
git push origin main
```

Vercel automatically redeploys if the connected repository has auto deployment enabled. No npm install, database or build step is required.

## Notes
- Homepage photography is illustrative AI-generated artwork, not a photograph of an Olson & Tenglund store or employee.
- The Auto Value partner mention reflects the business information provided by the owner. The stylized text mark on the page is not an official supplied Auto Value logo file. Replace with an officially licensed vector/brand asset when available.
- This site does not offer ecommerce or claim real-time product availability.
- When the business purchases a domain, assign it under Vercel project settings.
