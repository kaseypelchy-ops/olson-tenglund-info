# Jobber Specials — Call for Price Update

- Jobber Special products display **Call for Price** rather than distributor/wholesale amounts.
- Part numbers, wiper blade measurements, manufacturer and photos remain visible.
- All non-jobber promotional flyer prices are preserved.
- Numeric jobber prices were removed from the public `data/promotions.json` as well as from `promotions.html` to avoid leaking them in page source.
- Jobber cards link customers to the store contact details.
- All three locations continue to appear through the existing Locations page.

## Deployment

Extract the ZIP **contents** into the existing website root folder (`olson-info-site`) to overwrite matching files, leaving `.git` intact. Then run `git add .`, `git commit -m "Hide jobber wholesale pricing on promotions"`, `git push origin main`.

## Note

Any old git history or previously deployed content may still contain the earlier values. If the figures are sensitive, consider removing them from prior public commits and deployments as well.
