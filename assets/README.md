# Assets needed from the client

The site currently uses labeled placeholder images (placehold.co) everywhere a
real photo belongs. Search `index.html` for `CLIENT INPUT` comments — each one
names exactly what to shoot or supply. Summary:

1. **Hero background** — wide shot or short muted video of the shop bay (a car
   on the hoist, tools in motion). 1920x1080 or larger, landscape.
2. **Wheel bearing job photo** — matches the Chris Rozenberg review story, for
   the "Recent Work" section.
3. **Honda/Acura service bay photo** and **diagnostics/tools close-up photo**
   — also for "Recent Work".
4. **Team photo** — Dale, Marilyn and Dylan in the shop, for "The Shop"
   section.
5. **Logo** — none was supplied; the site currently uses a text wordmark
   ("54&4"). Swap in a real logo file if one exists.
6. **Full weekly hours** — only "opens 8:00 AM Friday" was visible in the
   Google listing screenshot. Need the complete week to fill in the footer
   and the `LocalBusiness` JSON-LD.
7. **Exact years in business** — a review mentions "twenty years"; confirm
   the real number for the trust-strip stat.
8. **Warranty terms** — referenced in the FAQ but not specified.
9. **Confirmed service area / radius** and **full service list** beyond what
   the reviews confirm (Honda/Acura, wheel bearings/suspension).
10. **Real Google Maps place link** for the "Read all 40 reviews" link in the
    footer/reviews section.
11. **Social media links**, if any, for the footer.
12. **Form endpoint** — the contact form currently only shows a success state
    client-side; it needs to be wired to a real email/CRM endpoint before
    launch (see the `CLIENT INPUT` comment in `js/main.js`).
