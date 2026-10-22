# Chem Kings Pool Service

Public website: https://chem-kings-pool-service.roundprawn256.chatgpt.site

29 server-rendered public pages for Sacramento pool and spa service. Built with a dependency-free Cloudflare Worker; no framework maintenance or client-side routing required.

## Included

- Home, services overview, five service pages, about, reviews, FAQs, contact and privacy.
- Service-area overview plus 16 community pages.
- Unique titles/descriptions, canonical URLs, LocalBusiness JSON-LD, XML sitemap, robots.txt, accessible navigation and responsive layouts.
- Locally served 1200×630 JPEG social card, Open Graph and Twitter metadata.
- Call/email actions, verified Instagram/Facebook/X/Yelp links and Google Maps business link.
- Validated live quote endpoint with consent, honeypot, origin validation and basic per-hour submission limits.
- Durable R2 inquiry storage and a server-key-protected inbox at `/admin/`.

## Develop / verify

Requires Node 22+ and bash. No dependency installation.

```sh
npm run dev
npm test
npm run build
npm run validate
```

`npm run dev` uses an **in-memory, local-only** inquiry store. Restarting preview clears it. Production uses the Sites-provisioned `BUCKET` R2 binding. Never treat local preview submissions as real leads.

Edit `worker/site.js` for page content/design and `worker/handler.js` for routes and APIs. `assets-data.json` contains optimized photo/card image bytes. `scripts/assemble.mjs` produces the self-contained `worker/index.js`. Build packages `dist/server/index.js` and the hosting manifest.

## Lead operations

Visit `/admin/` and enter the `INBOX_KEY` configured as a Sites secret. The key is intentionally excluded from GitHub. Requests are saved before success is returned; the form does not send email notifications or automatically schedule appointments. Check the inbox regularly. Phone and email links remain available directly to visitors.

The inbox shows the latest 200 requests, newest first. All inquiry data remains in R2. Operators should remove old inquiries through hosting storage administration when no longer needed. Rate-limit objects contain only a hashed identifier and counter. Basic R2 counters are best-effort under simultaneous submissions; add Turnstile or an atomic limiter if traffic warrants it.

## Publication and handoff

The authoritative Sites project ID is in `.openai/hosting.json`. Preserve it for updates. Use Sites source workflow helpers to push and package, then save the matching commit/archive and deploy. The GitHub repository is a source mirror, not an automatic deployment trigger. Add your own deployment automation only after choosing the target account.

1. Transfer/collaborate on source repository as agreed with the buyer.
2. Add the buyer to hosting management or redeploy the Worker in their Cloudflare account with R2 and a new `INBOX_KEY`.
3. Connect their domain and update `origin` in `worker/site.js`, then rebuild/publish.
4. Validate live form capture and inbox access; add an email provider for alerts if desired.
5. Confirm business owner approval of claims, hours, scope and review summaries. No invented pricing, licenses, guarantees or customer counts are published.

## Sources and asset attribution

See `SOURCES.md`. Hero photo is illustrative stock imagery, not a claimed Chem Kings project. Logo is an original text/crown concept. Review cards are explicitly labeled summaries of published customer reviews, not fabricated quotations.

The public footer identifies this as a website concept prepared for Chem Kings. Remove that note upon business approval and handoff.
