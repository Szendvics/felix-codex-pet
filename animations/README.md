# Felix — GIF-választó

Mind a **29 archivált képsor** külön GIF-ben, lent. A képkockaszámra kattintva
megnyílik a számozott képsor, ha csak egy részletet szeretnél használni.

A GIF-ek a forráslapok teljes képsorát mutatják, balról jobbra, fentről lefelé.
Csak a lapok végi üres kitöltőcellák maradtak ki. A nagyítás 2×, a szürke háttér
az átláthatóságot segíti. A tempó egységesen **120 ms/képkocka**; ez előnézeti
tempó, nem a régi programból visszanyert időzítés. Az átmenetek a GIF végén
visszaugranak az elejére, ezért nem mind alkalmas változtatás nélkül nyugalmi huroknak.

## Ezekhez kell választani

| Codex állapot | Mit fejezzen ki? | Végleges képkockák száma | Codex időzítés |
| --- | --- | ---: | --- |
| `idle` | Nyugodt alapállapot; finom, kevéssé zavaró mozgás | 6 | 280, 110, 110, 140, 140, 320 ms |
| `running-right` | Mozgás jobbra, jobbra néző macskával | 8 | 7 × 120 + 220 ms |
| `running-left` | Mozgás balra, balra néző macskával | 8 | 7 × 120 + 220 ms |
| `waving` | Köszönés vagy figyelemfelhívás | 4 | 3 × 140 + 280 ms |
| `jumping` | Ugrás: készülődés, emelkedés, leérkezés | 5 | 4 × 140 + 280 ms |
| `failed` | Hiba, sikertelenség, csalódottság | 8 | 7 × 140 + 240 ms |
| `waiting` | A Codex a válaszodra, jóváhagyásodra vár | 6 | 5 × 150 + 260 ms |
| `running` | A Codex éppen dolgozik; gondolkodás vagy elfoglaltság | 6 | 5 × 120 + 220 ms |
| `review` | Koncentrált nézelődés, vizsgálódás | 6 | 5 × 150 + 280 ms |

A `running` **munkaállapot**, a két irányhoz a `running-left/right` tartozik.
A táblázat az animációk célját írja le; a konkrét kiváltást a Codex app kezeli.
Nem kell pontosan ennyi képkockás GIF-et keresned: a választott képsort a végleges
atlaszhoz igazítjuk. Ugyanaz a forrás több állapothoz is használható.

Elég az azonosítókat megadnod, például `idle=325`, vagy egy részletet:
`idle=325:2–6` (nullától számozva, mindkét végponttal). Ez csak formátumpélda,
nem előre kiválasztott bekötés. Másolható választólista:

```text
idle =
running-right =
running-left =
waving =
jumping =
failed =
waiting =
running =
review =
```

A 312–314 külön halas kellékek, a 317 csak fejrészlet. A 326–328 az archívumban
apró mozgó pontokat tartalmaz, teljes macskát nem; önálló pet-animációnak így
nem használhatók. Az 1200 egyetlen állókép. A forrásoldal több neve és száma
pontatlan, ezért itt a látható képek alapján szerepelnek a leírások és a darabszámok.

Az export nem módosítja a telepített petet. Újragenerálás a repó gyökeréből:
`.venv/bin/python export_gifs.py`.

[Források és eredet](../NOTICE.md) ·
[Codex állapotok és időzítés](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/hatch-pet/references/animation-rows.md)

## Az összes GIF

<!-- generated gallery -->

| ID · képsor | Képkockák | GIF |
| --- | --- | --- |
| **301** · Talajra érkezés, felállás | [4 db, 0–3](fig_301.frames.png) | ![301 — Talajra érkezés, felállás](fig_301.gif) |
| **302** · Séta balra | [12 db, 0–11](fig_302.frames.png) | ![302 — Séta balra](fig_302.gif) |
| **303** · Séta jobbra | [12 db, 0–11](fig_303.frames.png) | ![303 — Séta jobbra](fig_303.gif) |
| **304** · Fordulás szemből jobbra | [2 db, 0–1](fig_304.frames.png) | ![304 — Fordulás szemből jobbra](fig_304.gif) |
| **305** · Fordulás szemből balra | [2 db, 0–1](fig_305.frames.png) | ![305 — Fordulás szemből balra](fig_305.gif) |
| **306** · Leülés, nézelődés, felállás | [12 db, 0–11](fig_306.frames.png) | ![306 — Leülés, nézelődés, felállás](fig_306.gif) |
| **307** · Oldalra néző ülő pózok | [4 db, 0–3](fig_307.frames.png) | ![307 — Oldalra néző ülő pózok](fig_307.gif) |
| **308** · Kikukucskálás alulról | [8 db, 0–7](fig_308.frames.png) | ![308 — Kikukucskálás alulról](fig_308.gif) |
| **309** · Kikukucskálás oldalról | [8 db, 0–7](fig_309.frames.png) | ![309 — Kikukucskálás oldalról](fig_309.gif) |
| **310** · Eltűnés az alsó szélen | [5 db, 0–4](fig_310.frames.png) | ![310 — Eltűnés az alsó szélen](fig_310.gif) |
| **311** · Evés a tálból | [24 db, 0–23](fig_311.frames.png) | ![311 — Evés a tálból](fig_311.gif) |
| **312** · Hal, A változat — külön kellék | [34 db, 0–33](fig_312.frames.png) | ![312 — Hal, A változat — külön kellék](fig_312.gif) |
| **313** · Hal, B változat — külön kellék | [22 db, 0–21](fig_313.frames.png) | ![313 — Hal, B változat — külön kellék](fig_313.gif) |
| **314** · Hal, C változat — külön kellék | [8 db, 0–7](fig_314.frames.png) | ![314 — Hal, C változat — külön kellék](fig_314.gif) |
| **315** · Macska az akváriummal | [24 db, 0–23](fig_315.frames.png) | ![315 — Macska az akváriummal](fig_315.gif) |
| **316** · Bebújás a macskaajtón | [26 db, 0–25](fig_316.frames.png) | ![316 — Bebújás a macskaajtón](fig_316.gif) |
| **317** · Apró fej / szemek a peremnél — részlet | [4 db, 0–3](fig_317.frames.png) | ![317 — Apró fej / szemek a peremnél — részlet](fig_317.gif) |
| **318** · Kibújás a macskaajtón | [23 db, 0–22](fig_318.frames.png) | ![318 — Kibújás a macskaajtón](fig_318.gif) |
| **319** · Felugrás, mancsnyomok az üvegen | [9 db, 0–8](fig_319.frames.png) | ![319 — Felugrás, mancsnyomok az üvegen](fig_319.gif) |
| **320** · Leülés, fejfordítás | [12 db, 0–11](fig_320.frames.png) | ![320 — Leülés, fejfordítás](fig_320.gif) |
| **321** · Lelapulás, fülek hátra, farokmozgás | [32 db, 0–31](fig_321.frames.png) | ![321 — Lelapulás, fülek hátra, farokmozgás](fig_321.gif) |
| **322** · Hátat fordít, leül, mozgatja a farkát | [12 db, 0–11](fig_322.frames.png) | ![322 — Hátat fordít, leül, mozgatja a farkát](fig_322.gif) |
| **323** · Tévénézés | [12 db, 0–11](fig_323.frames.png) | ![323 — Tévénézés](fig_323.gif) |
| **324** · Mosakodás, mancsnyalogatás | [20 db, 0–19](fig_324.frames.png) | ![324 — Mosakodás, mancsnyalogatás](fig_324.gif) |
| **325** · Szemből ülés, mancs felemelése | [18 db, 0–17](fig_325.frames.png) | ![325 — Szemből ülés, mancs felemelése](fig_325.gif) |
| **326** · Mozgó pontok — az archívumban nincs teljes macska | [32 db, 0–31](fig_326.frames.png) | ![326 — Mozgó pontok — az archívumban nincs teljes macska](fig_326.gif) |
| **327** · Mozgó pontok — az archívumban nincs teljes macska | [13 db, 0–12](fig_327.frames.png) | ![327 — Mozgó pontok — az archívumban nincs teljes macska](fig_327.gif) |
| **328** · Mozgó pontok — az archívumban nincs teljes macska | [14 db, 0–13](fig_328.frames.png) | ![328 — Mozgó pontok — az archívumban nincs teljes macska](fig_328.gif) |
| **1200** · Nyitókép / logó — állókép | [1 db, 0–0](fig_1200.frames.png) | ![1200 — Nyitókép / logó — állókép](fig_1200.gif) |
