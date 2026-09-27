# Sourcing the parts (everything except the case and the PCBs)

Goal: buy everything from sellers inside the EU, so there is **no customs duty and no customs handling fee** on delivery to Spain. The budget is **$150 (about €128)**, and the switches take about $50 of it.

> **About the prices:** these are estimates made in September 2026 from search results. The shop pages could not be opened directly, so check each price in the cart. I used €1 ≈ $1.17.

## Why EU sellers matter now

- Since **1 July 2026**, the EU charges a **€3 customs duty on every parcel from outside the EU worth under €150**. The €3 is charged once for each *type* of product (tariff heading), not once per parcel. An AliExpress order with sockets, keycaps, stabilizers and encoders pays about **€12 in duty**, and Correos can add a handling fee on top.
- **21% Spanish VAT is paid on everything**, including Amazon.es. That part cannot be avoided. The extra you can avoid is the duty and the handling fee.
- **Amazon tip:** filter for **"Enviado por Amazon"** (shipped by Amazon). Some marketplace sellers ship from China, and those parcels still go through customs.
- **AliExpress tip:** only items marked as shipped from an EU/Spanish warehouse avoid the €3 duty, and very few keyboard parts are sold that way.

## Where to buy each part

| Part | Qty needed | Buy | Where | Est. USD |
|---|---|---|---|---|
| Switches | 113 | **120** (a 110 pack is not enough) | Amazon.es, e.g. [Glorious Gateron 120](https://www.amazon.es/Glorious-switches-teclado-mec%C3%A1nico-Gateron/dp/B07CVQ7ZRL) | 50.00 |
| Hot-swap sockets CPG151101S11 | 113 | **120+** | [Amazon.es 100 pcs](https://www.amazon.es/Intercambiable-Caliente-CPG151101S11-Teclado-Mec%C3%A1nico/dp/B096WZ6TJ5) + a top-up, or 12 × 10-packs from [KEYGEM](https://keygem.com/products/switches-kailh-pcb-socket-10pcs) / [Keycapsss](https://keycapsss.com/Kailh-Hotswap-PCB-Sockets-10-pcs/KC10019-MX) (Germany) | 21.00 |
| Keycaps | 110 × 1u + 3 × 2u | Blank **XDA/DSA** (same height on every row) | Amazon.es | 33.00 |
| MCP23017-E/SO | 4 | 4 | [TME](https://www.tme.eu/es/details/mcp23017-e_so/interfaces-otros-circuitos-integrados/microchip-technology/) (Poland; invoices with Spanish VAT) | 6.80 |
| 1N4148 DO-35 | 113 | 150 | TME (or 2 × 100 on [Amazon.es](https://www.amazon.es/100pcs-1N4148-Diodo-DO-35-conmutaci%C3%B3n/dp/B07C1YYSDX)) | 4.40 |
| 0603 2.2k / 100R, 0603 100nF, 0805 10uF | 2 / 8 / 4 / 4 | 10 of each | TME | 2.50 |
| USB-C receptacle (16-pin, TYPE-C-31-M-12 size) | 2 | 15-pack | [Amazon.es](https://www.amazon.es/Conector-Pines-Hembra-r%C3%A1pida-Unidades/dp/B0848KV868) | 8.20 |
| Magnetic pogo 4P, curved, with ears | 3 pairs | 2 × "2 pairs" | [Amazon.de](https://www.amazon.de/Pogo-Pin-Anschluss-Magnetstecker-Durchgangsl%C3%B6cher-federbelastete-Steckverbinder-Schwarz/dp/B0CSX6GKCY) (EU, no customs) | 18.70 |
| Raspberry Pi Pico, USB-C | 1 | 1 | Amazon.es: search "USB-C Pico RP2040" | 9.40 |
| EC11 encoder + knobs | 4 | 5-set | [WayinTop on Amazon.es](https://www.amazon.es/WayinTop-Encoder-Codificador-Rotatorio-Interruptor/dp/B08728PS6N) (knobs included) | 10.50 |
| OLED 0.91" SSD1306 | 3 | 5-pack (3-pack ~$13) | [AZDelivery on Amazon.es](https://www.amazon.es/AZDelivery-Pantalla-Display-Pixeles-Parent/dp/B082MC4QJ4) | 16.40 |
| Stabilizers 2u, PCB-mount | 3 | "60 set" (4 × 2u) | [YMDK on Amazon.es](https://www.amazon.es/Cherry-Style-OEM-Estabilizadores-interruptores/dp/B07CHLNKV8) | 9.40 |
| M2×6 button head (ISO 7380) | 35 | 50 | Amazon.es | 5.85 |
| M2×10 button head (ISO 7380, 1.1 mm head) | 35 | 50 | Amazon.es | 5.85 |
| M2×3 spacer, OD ≤ 3.5 mm | 35 | — | Amazon.es: 2 × 3 mm PTFE tube, cut into 3 mm pieces | 5.85 |
| USB-C ↔ USB-C short cable | 1 | 1 | Amazon.es (skip if you own one) | 7.00 |
| USB-C cable to PC | 1 | 1 | Amazon.es (skip if you own one) | 7.00 |
| Shipping | | | TME Standard Economy €4.90 + VAT; Amazon.es free over €35 | 6.95 |
| **Total (everything)** | | | | **≈ 229** |

## Budget: the full list does not fit in $150

Buying everything above costs about **$229**, which is about **$79 over**. Here are the cuts, from easiest to hardest:

| Cut | Saves |
|---|---|
| Reuse USB-C cables you already own | ~$14 |
| Cheaper 120-pack of switches (Outemu / Gateron from Amazon.es, ~€28) instead of $50 | ~$17 |
| Cheapest ABS blank keycaps instead of PBT | ~$12 |
| OLED 3-pack instead of 5-pack | ~$3.50 |
| **Total with these cuts** | **≈ $182** |

That is still about **$32 over**. There are two ways to close the gap:

1. **Raise the budget to about $185** and keep every order inside the EU. (Recommended.)
2. **Buy only the bulk, low-risk parts on AliExpress** (sockets, keycaps, diodes; about €9 in duty for 3 product types), and keep everything else EU. This is roughly break-even with option 1 once the duty is added, so it is only worth it if AliExpress has a sale.

## Things to check before you order

- **Pogo connectors:** your footprint is based on a 19.9 × 4.2 mm body with magnets 13.54 mm apart. Compare this with the drawing in the listing before you buy. This part must match the holes in your case.
- **Pico:** buy the **full-size** USB-C Pico clone (51 × 21 mm, 40 pins). An RP2040-Zero will **not** fit. The official Pico ([Tiendatec](https://www.tiendatec.es/raspberry-pi-pico/1371-raspberry-pi-pico-5056561801445.html), ~€4.84) is pin-compatible, but it has micro-USB, so it only works if the case opening fits it.
- **Spacers:** most M2 nylon spacers in the EU are 4–5 mm wide. If 3.5 mm is a hard limit, use the PTFE tube trick.
- **Switches and sockets:** 113 are needed, so a 110 pack is **not** enough.
- **Keycaps:** a normal 104–135 key set has only about 85–90 1u keys. You need 110, so buy blank 1u packs.
