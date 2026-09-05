# Chinook Auto Repair — what's left for the client

This is a separate, standalone site (`Chinook Auto Repair.html`, one
self-contained file — same pattern as `Just Barbs Hair.html`) — it does not
share `index.html`, `css/style.css` or `js/main.js`, which belong to the
unrelated Fifty Fourth & Fourth Auto Repair site already in this repo.

Search `Chinook Auto Repair.html` for `CLIENT INPUT` comments for exact
locations of everything below.

## Photos (none exist yet)

The site uses a self-contained SVG placeholder (no external service) for
any image that fails to load. Drop real photos in next to the HTML file
with the exact filenames listed in the `PHOTO BRIEF` comment near the top
of `Chinook Auto Repair.html` and the placeholders disappear automatically:

1. **hero-bay.jpg** — wide shop bay shot for the hero.
2. **service-diagnostics.jpg, service-brakes.jpg, service-tires.jpg,
   service-oil.jpg, service-battery.jpg** — one per row in "What we fix";
   swaps into the sticky frame on hover/tap.
3. **people-shop.jpg** — John and Waheed in the bay, for the "Who you'll
   actually talk to" section.
4. **og-image.jpg** — social share preview, once real photos exist.
5. **Logo** — none supplied; site uses a text wordmark ("Chinook Auto
   Repair"). Swap in a real logo file if one exists.

## Resolved from public research (please spot-check)

- **Address / phone** — 312 55 Ave SW, Calgary, AB T2H 2Z6 /
  (403) 252-5290, matching the Google Business Profile screenshot
  provided and cross-checked against Yelp, Yellow Pages and Canpages.
- **Rating** — 4.3★ / 50 Google reviews, from the provided screenshot.
  (One older third-party directory shows 3.5★/11 reviews — likely a
  stale or partial index; the live Google listing screenshot was
  trusted as the source of truth.)
- **Hours** — Monday–Saturday 9:00 AM–5:30 PM, Sunday closed. Cross-checked
  between a directory listing and the "closes 5:30 p.m." live status on
  the Google listing screenshot (today's status matched: closed by
  evening, 5:30 close). One other directory instead lists Mon–Fri 8–5 —
  flagged in the HTML in case that's more current. Please confirm,
  especially Saturday and any holiday hours.
- **Services** — narrowed to what's corroborated across directories and
  the supplied reviews: diagnostics/check-engine lights, brakes/suspension,
  tires (new/used/seasonal swaps), oil/fluid service, batteries/no-start
  calls. Did **not** invent anything beyond this list.
- **Staff names** — "John and his mechanic Waheed" are named directly in a
  provided review (Moe Amiri) and used throughout as the people customers
  actually deal with. One older third-party review elsewhere names an
  "Eddy" as owner instead — worth confirming who's currently running the
  shop day to day, and correcting the site if needed.
- **Reviews quoted** — Moe Amiri, Akinwale Fadamiro and Perkins Imadojemu
  are quoted verbatim (trimmed only where the original screenshot itself
  was truncated with "…", cutting at the last complete sentence rather
  than guessing the missing words).
- **Upholstery arm** — a provided review (Marlene) mentions "CR Techniques"
  as an upholstery arm of Chinook Auto; public records show a related,
  separately BBB-listed "Chinook Auto Upholstery Inc." Included in the FAQ
  as a soft mention ("ask at the counter") rather than a confident claim,
  since the exact current name/relationship isn't fully clear — please
  confirm and correct.

## Still open — needs the shop, not research

- **A closure-adjacent search snippet** — one screenshot fragment read
  "…TRIEVE YOUR STORED TIRES – PLEASE EMAIL… will arrange to return them
  to you," which can read like a wind-down notice. The client confirmed
  the shop is still open and asked to proceed regardless, so the site
  was built as a normal active-business site — flagging here only so
  it's on record.
- **Warranty terms** — not referenced anywhere in research; not included
  on the site rather than guessed.
- **Appointment policy** (walk-in vs. call-ahead) — FAQ answer is a
  reasonable default, not confirmed.
- **Form endpoint** — the contact form shows a success state client-side
  but isn't wired to anywhere yet. Needs a real email address or CRM/
  form-service endpoint before launch (see the `CLIENT INPUT` comment in
  the page's inline script).
- **Geo coordinates** for the `AutoRepair` JSON-LD — omitted rather than
  guessed.
- **Social media** — no public Facebook/Instagram turned up in research;
  footer links to Google instead.
