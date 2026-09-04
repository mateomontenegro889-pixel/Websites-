# What's left for the client — Calais Alteration & Dry Cleaning

Research here came from a Google search results page and Google Business
Profile reviews (screenshots), not a phone call or site visit. Everything
below marked "resolved" is corroborated by that research; everything
marked "needs the studio" could not be verified and is flagged
`CLIENT INPUT` directly in `index.html`.

## Photos (not addressed — none exist yet)

The site uses labeled placeholder images (placehold.co) everywhere a real
photo belongs. Each is described in a comment so anyone shooting them knows
what's needed:

1. **Hero background** — wide photo or short muted video of the studio:
   Rosie at the machine, a garment on the dress form, pins and chalk on
   the cutting table. 1920x1280 or larger, landscape.
2. **Before/after alteration photo** — for the "Our Work" section, ideally
   matching the dress-cleaning story from the Anastasiya Badan review.
3. **At the machine** and **on the form** photos — also for "Our Work".
4. **Studio photo** — Rosie and her husband in the shop, for "The Studio"
   section.
5. **Logo** — none was supplied; the site currently uses a text wordmark
   ("Calais"). Swap in a real logo file if one exists.

## Resolved from public research (please spot-check)

- **Address** — 10325 Bonaventure Dr SE #106, Willow Park Centre, Calgary,
  AB, consistent across the Google Business Profile, MapQuest and
  YellowPages.ca.
- **Postal code discrepancy** — one source lists T2J 0P8, another T2J 7E4,
  for the same address. Used T2J 0P8 in the schema and left the footer
  vague — please confirm the correct one.
- **Phone** — (403) 254-5258, matching the Google Business Profile.
- **Rating** — 4.6 stars, 19 Google reviews, per the Business Profile panel.
- **Owner** — Rosie, described in multiple reviews as a trained fashion
  designer from Taiwan who runs the studio with her husband.
- **Reviews used as testimonials** — three real 5-star reviews (Joni
  Mallabone, Anastasiya Badan, "Where It's Art") are quoted verbatim.
  Two of them were truncated by Google's "…More" cutoff in the screenshot —
  marked with `CLIENT INPUT` in `index.html` in case you want to pull the
  full text from the Business Profile.
- **Social media** — no public Facebook/Instagram/website turned up in
  research. Footer just links to Google instead.

## Still open — needs the studio, not research

- **Hours** — could not be reliably sourced. The search snippets for this
  listing were contradictory and garbled ("Closed 09:00 A.M – 05:00 P.M",
  "Open until 4:00 am") and not trustworthy enough to publish. The footer
  and JSON-LD both currently omit hours — please supply real ones for
  every day of the week.
- **Years in business** — reviews mention being a customer "for 8 years"
  and "over 10 years," so the trust strip uses "10+" as a conservative,
  corroborated floor. Confirm the studio's actual opening year if you want
  a more precise (and likely higher) number.
- **Exact service scope** — alterations/repairs and dry cleaning are
  confirmed by the business name and category. Bridal/formal wear and
  custom dressmaking are inferred from Rosie's design background and the
  reviews mentioning dresses — confirm the real scope (e.g. does bridal
  work include bustles, boning, beading repair?).
- **Pricing** — no price range is published anywhere in the FAQ; a rough
  range could be added if the studio wants to set expectations up front.
- **Walk-in vs. appointment policy** — assumed "call ahead," not confirmed.
- **Form endpoint** — the contact form shows a success state client-side
  but isn't wired to anywhere yet. Needs a real email address or CRM/
  form-service endpoint before launch (see the `CLIENT INPUT` comment in
  `js/main.js`).
- **Geo coordinates** for the `LocalBusiness`/`DryCleaningOrLaundry`
  JSON-LD — omitted rather than guessed.
