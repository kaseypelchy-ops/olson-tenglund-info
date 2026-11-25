# Phase 3 — Parts Help resources and technical audit

This package builds on the Facebook integration update and preserves the approved homepage hero, status popup, navigation, and logos.

## New pages
- `/guides` — resources index
- `/guides/car-battery-replacement` — battery group size, CCA, chemistry, fitment and safety
- `/guides/oem-vs-aftermarket-parts` — definitions, selection criteria and fitment

The new material is general educational content, not a claim about store inventory, battery services, warranty, installation or commercial services.

## Updated
- Homepage: low-profile three-card Parts Help section below the main content
- Existing parts guide: related reading links
- Site footer: Parts Help internal link on all pages
- Sitemap: 12 URLs total
- New pages: canonical URLs, title and descriptions, Open Graph, JSON-LD (WebPage, Article where applicable, BreadcrumbList and Organization with official Facebook sameAs)

## Deployment
Copy ZIP contents into your existing `olson-info-site` repo, overwriting matching files without deleting `.git`, then commit/push. Verify `/guides` and the two new articles. Request indexing of the three new URLs using Google Search Console after deployment.

## Later work
Add actual store-specific photography and owner-verified services. Continue Google/Apple listing corrections after organization verification.
