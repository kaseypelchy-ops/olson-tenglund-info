# Olson & Tenglund — SEO / AEO / GEO Update

## What this ZIP contains

This is a **complete replacement of the informational website files** (not the separate ecommerce project). The current navy/red design, images, logos, navigation, and existing page URLs are preserved.

### Implemented
- One factual record of the business and the three store addresses/phone numbers in `data/business.json`.
- Connected `Organization`, `WebSite`, `WebPage`, `BreadcrumbList`, and each `AutoPartsStore` schema with stable `@id` values. Store schema only includes confirmed weekday hours.
- Answer-first, visible HTML content on the homepage and each city page: open status, change from NAPA to Auto Value, weekday hours, call to check parts.
- Expanded customer FAQ covering the transition, repair shops, parts availability, official website and ordering inquiries.
- Breadcrumbs and associated schema on inner pages.
- 8-URL sitemap matching the existing site; no indexing resubmission required just because HTML changed.
- Responsive minimal CSS additions for the Q&A sections.
- Removed *unconfirmed* claims that Saturdays and Sundays are closed.
- A repeatable local `build_site.py` generator for structured data/answer panels, designed to be run only when business information changes.

### Deploy without touching Git history

1. Download and extract this archive.
2. Open your local repo folder `olson-info-site` (the repo with `origin https://github.com/kaseypelchy-ops/olson-tenglund-info.git`).
3. Copy **the extracted file contents** into that repo folder, replacing matching files. Keep your existing `.git` folder; do not replace it or copy into a new nested folder.
4. Commit/push:
   ```powershell
   git status
   git add .
   git commit -m "Improve location schema and AI-search answer content"
   git push origin main
   ```
5. Vercel deploys the commit. Verify `https://olsontenglund.com/faq`, the three city pages, `sitemap.xml`, and `robots.txt`.
6. In Google Search Console and Bing Webmaster Tools, verify that the URLs are discoverable. You **do not need to re-verify the domains, change DNS or resubmit a working sitemap**.

### After deployment

- Verify the structured data with https://validator.schema.org/ and https://search.google.com/test/rich-results . Not every valid type generates a special Google search feature.
- Replace generic image assets with genuine exterior images, ideally each showing updated store signage.
- Confirm weekend/holiday hours with the owner and only then publish them in page copy, `data/business.json`, and store schema.
- Add actual official Auto Value store directory URLs and official verified GBP/Apple/Bing listing URLs *only once those specific pages are known*. Do not add invented social profiles or fake `sameAs` links.
- Claim/correct old NAPA-branded listings separately. Website schema cannot change third-party profile statuses.
- Never publish tax EIN or verification tokens in HTML or this JSON file.

### Updating business data later

Edit `data/business.json` and run:

```bash
python -m pip install beautifulsoup4
python build_site.py
```

This will regenerate JSON-LD and answer-first panels from the configured locations. **Important:** If you change addresses, phone numbers, or store hours, also review the original static content in `index.html`, `locations.html`, `about.html`, `contact.html` and `faq.html` for corresponding visible copy; the script currently regenerates only the schemas and panels, not every existing paragraph/footer. Do not assume all legacy copy updates itself.

### Optional future IndexNow

IndexNow is intentionally **not enabled** here: it requires a domain verification key and a notification made after successful production deployment. Do not commit a fake key or call the service before pages are live. It can be set up later with a Vercel deployment hook or GitHub Action, after validating the domain key and published page URLs.

### Important limitations

Structured data and FAQs improve machine-readable clarity; no code can guarantee inclusion, citations, rankings, or answers in ChatGPT, Google AI Overviews, or Copilot. This package does not create Google/Apple/Bing business listings, claim them, prove store status to those services, or include store-specific original photos not supplied by the owner.
