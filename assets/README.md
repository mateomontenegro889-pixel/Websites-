# What's left for the client

Everything that could be filled in from public research (business hours,
service list, Google Maps links) has been. What's left genuinely needs to
come from the shop directly — search `index.html` and `js/main.js` for
`CLIENT INPUT` comments for exact locations.

## Photos (not addressed — none exist yet, per the client)

The site uses labeled placeholder images (placehold.co) everywhere a real
photo belongs. Each is described in a comment so anyone shooting them knows
what's needed:

1. **Hero background** — wide shot or short muted video of the shop bay (a
   car on the hoist, tools in motion). 1920x1080 or larger, landscape.
2. **Wheel bearing job photo** — matches the Chris Rozenberg review story,
   for the "Recent Work" section.
3. **Honda/Acura service bay photo** and **diagnostics/tools close-up
   photo** — also for "Recent Work".
4. **Team photo** — Dale, Marilyn and Dylan in the shop, for "The Shop"
   section.
5. **Logo** — none was supplied; the site currently uses a text wordmark
   ("54&4"). Swap in a real logo file if one exists.

## Resolved from public research (please spot-check)

- **Hours** — Monday–Friday 8:00 AM–6:00 PM, sourced from a Yellow Pages
  listing at this exact address and cross-checked against the "Opens 8 a.m.
  Fri" status in the Google listing screenshot. Saturday/Sunday shown as
  closed since no weekend hours are listed anywhere found. Not confirmed
  directly by the shop — worth a quick check, especially holiday hours.
- **Google Maps links** (footer directions, "read all 40 reviews") — built
  from the business name + address, so they resolve to the real listing.
  If you have the exact Google Business Profile "Place" link, swap it in
  for a more direct jump.
- **Service list** — narrowed to what's corroborated by reviews (Honda/
  Acura specialty, wheel bearings/suspension) plus what showed up
  consistently across independent directory listings (brakes, tires,
  diagnostics, general maintenance). Did **not** add less-corroborated
  items (transmission work, muffler service, motorcycle inspections) that
  turned up in only one noisy source — worth confirming if those are real.
- **Social media** — no public Facebook/Instagram/website turned up in
  research (a domain, fiftyfourthandfourthauto.com, is referenced by
  directories but doesn't currently resolve). Footer just links to Google
  instead. Add real profiles if/when they exist.
- **Phone number** — kept as (403) 252-5987 throughout, matching the Google
  Business Profile screenshot. A couple of third-party directories list a
  different, likely outdated number (403-252-5905) — flagging in case
  that's actually a second line, but the live Google listing was trusted
  as the source of truth.

## Still open — needs the shop, not research

- **Exact years in business** — only evidence found is a review mentioning
  "twenty years." Used as "20+" on the trust strip; confirm the real number.
- **Warranty terms** — referenced in the FAQ only as "ask us when you
  call," since no specific policy could be found or should be guessed.
- **Form endpoint** — the contact form shows a success state client-side
  but isn't wired to anywhere yet. Needs a real email address or CRM/
  form-service endpoint before launch (see the `CLIENT INPUT` comment in
  `js/main.js`).
- **Geo coordinates** for the `LocalBusiness` JSON-LD — omitted rather than
  guessed; not required for the schema to be valid, just a nice-to-have.
