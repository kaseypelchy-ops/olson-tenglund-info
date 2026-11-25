# Customer-facing copy update

- Replaced the internal explanation of jobber pricing with customer-friendly seasonal offer information.
- Jobber Special labels are no longer shown; relevant products still display **Call for Price**.
- Removed back-office image sourcing notes and flyer-production references from product cards.
- Retained all product numbers, blade sizes, images, and the three-column layout.
- Kept special prices visible where they are designated as public/retail promotions.
- Did not reintroduce wholesale prices into site HTML or the public JSON data file.

## Deployment

Extract the ZIP directly into the root of the existing `olson-info-site` repository (do not delete `.git`). Overwrite matching files, then run:

```powershell
git add .
git commit -m "Polish customer-facing promotions copy"
git push origin main
```
