# Promotions correction — November 25, 2026

## Fixed
- Every wiper SKU in all seven families now has a conspicuous length badge in inches.
- Several previously unverified photo URLs replaced with product-source URLs identified via web research.
- Remote image failures no longer show broken-image icons: instead a labeled fallback appears with product data still intact.
- IMPORTANT: External retailer images may still fail due to hotlink blocking. Obtain licensed product photography from your Auto Value supplier for dependable publication.
- ZIP is deliberately packaged with index.html, promotions.html, CSS etc. AT THE ZIP ROOT so overwriting your existing `olson-info-site` directory actually updates the site. Do not overwrite your `.git` folder.

## Publishing
Extract all ZIP contents into the root of your `olson-info-site` repository, verify that promotions.html and promotions-photo-fallback.js sit alongside index.html, then `git add .`, `git commit -m "Fix wiper blade sizes and promotion image handling"`, and `git push origin main`.
