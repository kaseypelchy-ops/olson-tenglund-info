# Promotions page — launch and pricing review

Built from six uploaded photographed pages: 248.jpg, 249.jpg, 250.jpg, 251.jpg, 252.jpg, 253.jpg.

The page contains **84 product family/cards**, grouped into 6 categories, with search and quick filters. Each card includes a product/line name, manufacturer, flyer SKU(s), and a cropped product illustration from the original user-supplied flyer. These are documentary flyer illustrations; some illustrate a product *family*, not the exact size/variant.

**IMPORTANT — PRICE APPROVAL REQUIRED**

The first and fourth pages are marked **JOBBER SPECIALS**. Jobber prices are typically trade/dealer pricing, not guaranteed consumer retail pricing. Pages also say prices, availability and brands vary by location. Therefore the public website intentionally says **Ask for current pricing** instead of displaying unapproved dollar amounts. Do not advertise the flyer wholesale prices publicly without explicit confirmation from the business owner / distributor.

The source flyer says **valid through February 28, 2027**; confirm this applies to all uploaded pages. Keep current campaign dates up-to-date, and remove the page from promotional navigation when offers expire.

**Before publishing publicly**:
1. Owner confirms the flyer items/brands are available at Olson & Tenglund rather than only through the upstream wholesaler.
2. Owner approves retail vs trade offer prices and whether they should be displayed.
3. Owner confirms any exclusions, fees, and hours.
4. Confirm flyers can be used for retailer advertising.
5. Review product images: cropped from flyers, not official manufacturer product photos; replace with licensed manufacturer product images where available.

### Deploy
Extract the contents directly into `olson-info-site`, keeping `.git`. Push to main; Vercel deploys. `promotions.html`, `promotions.js`, `data/promotions.json`, and `assets/promotions/` are new; global nav and footer links are updated. The sitemap gains one URL.

No online shopping or payment workflow is added. Cards call for confirmation in-store.
