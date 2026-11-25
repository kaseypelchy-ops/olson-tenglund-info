# Olson & Tenglund — Search Visibility & Listing Recovery

## Deployment
- Merge these files into the EXISTING `olson-tenglund-info` project, not the separate ecommerce app. Preserve `.git`.
- Ensure `olsontenglund.com` resolves to this deployment and redirects consistently from alternate hostnames. Set domain primary in Vercel.
- Open all eight canonical URLs and confirm they return HTTP 200 without auth, and that `robots.txt`/`sitemap.xml` are available.
- Validate the JSON-LD with https://validator.schema.org/ and Google's Rich Results Test (rich result eligibility is not guaranteed).
- Inspect canonical tags and ensure there is no noindex.

## Search Console
1. Verify `olsontenglund.com` as a Domain property using the DNS TXT verification provided by Search Console: https://search.google.com/search-console/
2. Submit `https://olsontenglund.com/sitemap.xml`.
3. Inspect and request indexing for `/`, `/locations`, the three city pages, and `/faq`.
4. Check indexing status and search queries weekly. Crawling/indexing is not instantaneous or guaranteed.

## Google Business Profile — MOST IMPORTANT
- Identify the three existing profiles by EXACT physical address, not name alone. Determine who controls each (the previous owner/supplier may still manage it).
- If the business is the same continuing store and its closed status is incorrect, request ownership/access and mark it OPEN. Do not create duplicate profiles unless Google requires a new business identity profile.
- Display the real-world sign name (avoid keyword-stuffing): Olson & Tenglund, Inc. or exact sign name. Remove NAPA as a current affiliation; describe Auto Value partnership accurately.
- Set addresses, three unique phone numbers, all weekday hours, website or individual location URL, and primary category Auto parts store. Add current storefront and signage photos, business description, and holiday hours.
- If access is with another account, use https://business.google.com/add to request ownership. Google provides a 3-day response window to current managers.
- If unclaimed, claim and verify. If marked incorrectly closed, see Google support article https://support.google.com/business/answer/15300571
- Save screenshots/evidence of actual business operations and signage for possible verification or appeal.

## Outdated supplier listings
- Notify the former supplier/NAPA that its live store pages still list Olson & Tenglund at the same addresses and request correction/removal of the outdated association. Do NOT ask that the actual business be marked closed in Google.
- Correct high-value citations: Apple Business Connect, Bing Places, Facebook page, Yelp and major directories. Preserve a consistent business name, address, phone, hours and domain for each store.
- Avoid buying low-quality link packages, fabricated reviews, or duplicate listings.

## AEO/GEO
- The `/faq` page answers directly: still open, changed affiliation, precise hours, addresses, phone numbers, and online ordering expectations. Keep all answers accurate and updated.
- Maintain one canonical location page per storefront and LocalBusiness structured data; publish genuine photos if available.
- Align organization and three store entities across the website and business profiles. Do not claim that schema guarantees an AI citation or ranking.

## Not done by this ZIP
- Claim or edit Google profiles; request removals from NAPA; verify Search Console; obtain indexing; link external social accounts. Each needs authorized human account action.
- Site live content/domain was not crawled successfully by the research tool at packaging time; verify in the browser.
