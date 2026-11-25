# Olson & Tenglund — Official Facebook link update

Official page: https://www.facebook.com/olson.tenglund

This is a full replacement for the Phase 2 informational website. Copy the ZIP contents into the root of your existing `olson-info-site` Git working folder, replacing matching files. Do not replace or delete `.git`.

## Changes
- A small Facebook icon/link was added to the footer of all nine pages.
- The About page now links to the official Facebook page for news and announcements.
- `sameAs` now identifies the official Facebook page in the organization JSON-LD on all nine pages.
- `data/business.json` and the JSON-LD generator were updated so the URL is retained in future generation.
- Existing header, hero, popup, local store content, sitemap, and styles are retained.

## Deploy
```powershell
git status
git add .
git commit -m "Connect official Facebook profile across website and schema"
git push origin main
```

## Verification
Open the homepage, About page, and a store page and check the footer link. Verify the page opens the official Olson & Tenglund profile. To inspect structured data, view source and search for `sameAs`.

On Facebook, also add https://olsontenglund.com as the official website URL.
