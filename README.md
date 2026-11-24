# Olson & Tenglund, Inc. — Informational Website MVP

An independent, fast-launch informational website for the three Olson & Tenglund auto parts stores. Built as **plain HTML/CSS/JavaScript** with no backend, database, npm dependencies, or third-party website builder.

**This is a separate project from the existing Olson & Tenglund ecommerce/catalog prototype.** It is intended to be launched independently so the existing repository is not overwritten.

## Pages

| Page | File | Production path |
| --- | --- | --- |
| Home | `index.html` | `/` |
| Locations | `locations.html` | `/locations` |
| About | `about.html` | `/about` |
| Contact | `contact.html` | `/contact` |

Vercel's `cleanUrls` setting maps `/locations` to `locations.html` and similarly for the other pages.

## Store information used

- **Port Allegany:** 303 N Main St, Port Allegany, PA 16743 — 814-642-2517
- **Coudersport:** 112 N Main St, Coudersport, PA 16915 — 814-274-8881
- **Smethport:** 400 W Main St, Smethport, PA 16749 — 814-887-7777

Hours were **not provided** and are intentionally absent. Website instructs visitors to call for current hours.

## Design assets

The source artwork supplied by the owner/developer was optimized and included in `assets/`:

- `olson-horizontal.webp` — header/footer wordmark
- `olson-stacked.webp` — interior contact section
- `olson-badge.webp` — hero and about section
- `olson-banner.webp` — promotional banner
- `favicon.png` — browser icon

The promotional copy is generic, not a representation of an approved Auto Value advertisement or current sale. Confirm use of any additional Auto Value branding/promotions with the distributor and the business owner.

## Local preview

Open `index.html` in a modern browser. For accurate clean URLs, use a basic local server:

```powershell
python -m http.server 3000
```

Then open `http://localhost:3000/`. Local Python HTTP serving does not apply Vercel clean URL rewriting: use `/locations.html`, `/about.html`, and `/contact.html` when previewing directly from Python.

## Put this into a NEW GitHub repository (recommended)

1. Download and extract the complete ZIP, for example to `C:\Users\Kasey Pelchy\Downloads\olson-tenglund-info`.
2. Create a new **empty** GitHub repo named `olson-tenglund-info` (do **not** initialize a README or .gitignore in GitHub; the project includes these).
3. In PowerShell inside the extracted project directory, run:

```powershell
git init
git add .
git commit -m "Launch Olson & Tenglund informational site"
git branch -M main
git remote add origin https://github.com/kaseypelchy-ops/olson-tenglund-info.git
git push -u origin main
```

If the GitHub account or repo name is different, replace the remote URL.

## Deploy to Vercel

1. Vercel dashboard → **Add New → Project**.
2. Import the new GitHub repository `olson-tenglund-info`.
3. Select **Framework Preset: Other**.
4. Set **Root Directory** to the repository root; leave build command empty and output directory at the root/default for a static site (depending on Vercel UI, choose **Other** and use `.` as output directory if required).
5. Deploy. Test the assigned `*.vercel.app` URL on desktop and mobile.
6. Vercel → project **Settings → Domains** to add the domain after purchasing it. Follow Vercel's exact recommended DNS records for your registrar. Then test the domain and SSL.

This site requires **no Turso, Better Auth, API keys, environment variables, package.json, or installation of dependencies**.

**Important:** The older `olson-tenglund.vercel.app` site is a separate deployment. It will **not change** unless you explicitly change its Vercel project/domain routing or replace its code. Keep it unchanged until the owner approves the informational replacement.

## Launch checklist

- [ ] Confirm the owner approves the wording “We're here” and all three locations remain operational.
- [ ] Confirm all three address and phone numbers (click-to-call and directions links).
- [ ] Confirm and add accurate **business hours** for all three stores, if the owner wants hours online; otherwise keep the current call-to-confirm message.
- [ ] Confirm permission to use supplied artwork and any Auto Value brand material.
- [ ] Confirm current logo uses correct legal spelling and visible mark.
- [ ] Preview and test the four pages on desktop and mobile.
- [ ] Test phone links on a mobile device and Google Maps directions links.
- [ ] Add the purchased domain in Vercel, then update site canonical tags, Open Graph image URL, and a sitemap if SEO becomes a focus.
- [ ] Update/claim Google Business Profiles and Facebook with the new domain, store numbers, hours, and open status.
- [ ] If changing the live site, first agree which Vercel project and custom domain should serve the informational site.

## Not included in this MVP

Ecommerce checkout, real-time inventory, vehicle fitment, My Garage, accounts, newsletter forms, email sending, admin dashboard, promotions pulled from Auto Value, and online order intake. These belong to a future phase and are not necessary for confirming that the local stores are open.
