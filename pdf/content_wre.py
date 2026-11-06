# -*- coding: utf-8 -*-
"""Content: Water Resource Engineering (2415305) — Term Work file (no laboratory)."""

META = {
    "title": "Water Resource Engineering — Term Work File",
    "subject": "Water Resource Engineering",
    "code": "2415305 (S2415305)",
    "item_label": "TERM WORK  NO.",
    "footer": "Water Resource Engineering (2415305)  •  Diploma in Civil Engineering, Semester III  •  SBTE Bihar",
    "index_note": "Is subject ka koi laboratory/practical nahi hai — sirf term work (assignment, micro project, "
                  "seminar aur visit report) 50 marks ka jama hota hai. Page number index mein bharein.",
    "references": [
        'S.K. Garg, <i>Irrigation Engineering and Hydraulic Structures</i>, Khanna Publishers.',
        'P.N. Modi, <i>Irrigation, Water Resources and Water Power Engineering</i>, Standard Book House.',
        'IS: 6512 — gravity dams; IS: 8826 — spillways; IS: 7114 — canal linings.',
        'IS: 10824 — sprinkler irrigation; IS: 10799 — drip irrigation; IS: 15797 — rainwater harvesting.',
        'SBTE Bihar curriculum for Water Resource Engineering (2415305 / S2415305).',
    ],

}

ITEMS = [
    {
        "num": 1,
        "title": "Assignment 1 — Hydrology: average rainfall and runoff",
        "blocks": [
            {"h": "Q1. Define hydrology and explain the hydrological cycle with a neat sketch."},
            {"p": [
                "Hydrology is the science that deals with the occurrence, movement, distribution and circulation "
                "of water on the earth, including precipitation, evaporation, infiltration, runoff and storage. "
                "The hydrological cycle is the continuous circulation of water from the ocean to the atmosphere "
                "as vapour, from the atmosphere to the land as precipitation, and back to the ocean as surface "
                "runoff and groundwater flow.",
                "The main components of the cycle are: precipitation (rainfall, snow), interception, evaporation "
                "and transpiration, infiltration, detention storage, surface runoff and groundwater flow. The "
                "water balance equation for a catchment is: P = R + E + ΔS, where P is precipitation, R is runoff, "
                "E is evapotranspiration and ΔS is the change in storage.",
            ]},
            {"h": "Q2. The rainfall recorded at four rain gauge stations in a catchment is 12, 18, 22 and 28 mm. "
                  "Calculate the average rainfall by the arithmetic mean method."},
            {"p": [
                "Arithmetic mean method: P<sub>avg</sub> = (P₁ + P₂ + P₃ + P₄)/n = (12 + 18 + 22 + 28)/4 = "
                "<b>20 mm</b>.",
                "This method is used only when the gauges are evenly distributed and the terrain is plain.",
            ]},
            {"h": "Q3. The rainfall at three stations with Thiessen weights 0.25, 0.35 and 0.40 is 20 mm, 26 mm and "
                  "32 mm. Find the average rainfall by the Thiessen polygon method."},
            {"p": [
                "P<sub>avg</sub> = Σ (P<sub>i</sub> × A<sub>i</sub>)/ΣA<sub>i</sub> = (20 × 0.25) + (26 × 0.35) + "
                "(32 × 0.40) = 5.00 + 9.10 + 12.80 = <b>26.90 mm</b>.",
                "The Thiessen polygon method gives better results than the arithmetic mean when the gauges are "
                "unevenly distributed, because each gauge is weighted according to its area of influence.",
            ]},
            {"h": "Q4. A catchment of 150 km² receives 900 mm of rainfall in a year. If the annual runoff is "
                  "0.42 Mm³, calculate the runoff coefficient."},
            {"p": [
                "Runoff coefficient, C = Runoff / Rainfall = (0.42 × 10⁶ m³) / (900 × 10⁻³ m × 150 × 10⁶ m²) = "
                "0.42 × 10⁶ / 135 × 10⁶ = <b>0.31</b>.",
                "The coefficient is about 0.31 (31%), which is typical of a catchment with moderate vegetation "
                "and soil permeability.",
            ]},
            {"h": "Q5. Name the factors affecting runoff and state two methods of computing flood discharge."},
            {"p": [
                "Runoff depends on rainfall intensity and duration, catchment area, shape and slope, soil type, "
                "land use and vegetation, antecedent moisture condition and evaporation. Flood discharge is "
                "estimated by the rational method (Q = C·i·A) and by empirical formulae such as Ryve's, "
                "Inglis' or Dickens' formula.",
            ]},
        ],
        "code": "Curriculum — TSO 1.1–1.5 (T2415305); S.K. Garg, Irrigation Engineering and Hydraulic Structures.",
    },
    {
        "num": 2,
        "title": "Assignment 2 — Crop water requirement: duty, delta and consumptive use",
        "blocks": [
            {"h": "Q1. Define duty and delta and derive the relation between them."},
            {"p": [
                "Duty (D) is the area of land in hectares irrigated by a continuous flow of 1 m³/s (1 cumec) for "
                "the whole base period, expressed in ha/cumec. Delta (Δ) is the total depth of water required by "
                "a crop during its base period, expressed in metres.",
                "For a base period B days, the volume of water supplied = 1 × B × 86400 m³, and this water covers "
                "D hectares to a depth Δ, so D × Δ × 10⁴ = 86400 B. Hence Δ = 8.64 B / D (m), or "
                "D = 8.64 B / Δ (ha/cumec).",
            ]},
            {"h": "Q2. A crop has a base period of 120 days and a delta of 0.60 m. Find its duty."},
            {"p": ["D = 8.64 B / Δ = (8.64 × 120) / 0.60 = 1036.8/0.60 = <b>1728 ha/cumec</b>."]},
            {"h": "Q3. Water is supplied at 2 cumecs to a field of 400 hectares for 100 days. Calculate the delta."},
            {"p": [
                "Volume supplied = 2 × 100 × 86400 = 17.28 × 10⁶ m³.",
                "Δ = Volume / Area = 17.28 × 10⁶ / (400 × 10⁴) = <b>4.32 m</b>.",
                "Duty, D = 8.64 × 100 / 4.32 = <b>200 ha/cumec</b>.",
            ]},
            {"h": "Q4. Explain consumptive use and the factors affecting it."},
            {"p": [
                "Consumptive use (evapotranspiration) is the total water used by a crop for its growth, "
                "including transpiration and evaporation from the soil and plant surfaces. It depends on climate "
                "(temperature, humidity, wind, sunshine), crop type and stage of growth, soil moisture and "
                "irrigation practices. It is estimated by the Blaney–Criddle method, Penman method or by "
                "lysimeter measurements.",
            ]},
        ],
        "code": "Curriculum — TSO 2.1–2.5 (T2415305); S.K. Garg, Irrigation Engineering.",
    },
    {
        "num": 3,
        "title": "Assignment 3 — Dams and spillways",
        "blocks": [
            {"h": "Q1. Classify dams and state the factors governing the choice of a dam site."},
            {"p": [
                "Dams are classified as: (i) by material — earthen, rockfill, masonry, concrete and composite "
                "dams; (ii) by purpose — storage, detention, diversion and check dams; (iii) by structural "
                "behaviour — gravity, arch, buttress and embankment dams.",
                "A dam site is selected on the basis of a narrow valley with a wide reservoir basin, sound rock "
                "or impervious foundation, availability of construction material, favourable geology, low "
                "seismic risk, minimum submergence of land, and accessibility.",
            ]},
            {"h": "Q2. Draw a labelled sketch of a gravity dam section and show the forces acting on it."},
            {"p": [
                "The forces acting on a gravity dam are: (i) the weight of the dam, (ii) water pressure on the "
                "upstream face, (iii) uplift pressure at the base, (iv) silt pressure, (v) wave pressure, "
                "(vi) earthquake forces, and (vii) ice pressure (in cold regions).",
                "A gravity dam resists these forces by its own weight and must satisfy the requirements of "
                "stability against overturning, sliding, crushing and tension at the heel.",
            ]},
            {"h": "Q3. Why is a spillway necessary? Name the common types."},
            {"p": [
                "A spillway is a safety structure which passes the surplus flood water from the reservoir to the "
                "downstream side without damaging the dam. Without a spillway, the water level would rise above "
                "the dam crest and endanger the structure. Common types are the ogee (overflow) spillway, chute "
                "spillway, side channel spillway, shaft spillway, siphon spillway and emergency spillway.",
            ]},
            {"h": "Q4. Write short notes on the causes and control of seepage through an earthen dam."},
            {"p": [
                "Seepage through an earthen dam occurs through the body of the dam, the foundation and the "
                "abutments. It may cause erosion (piping), sloughing and reduction of stability. Seepage is "
                "controlled by a central clay core, upstream impervious blanket, cut-off trench, toe drain, "
                "horizontal drainage blanket, rock toe and grouting of the foundation.",
            ]},
        ],
        "code": "Curriculum — TSO 3.1–3.5 (T2415305); IS: 6512 (gravity dams), IS: 8826 (spillways).",
    },
    {
        "num": 4,
        "title": "Assignment 4 — Minor and micro irrigation",
        "blocks": [
            {"h": "Q1. Differentiate between flow irrigation and lift irrigation."},
            {"p": [
                "In flow irrigation, water is supplied to the fields by gravity from a canal or a river at a "
                "higher level, and no pumping is required. In lift irrigation, water is lifted from a river, well "
                "or canal by pumps and then distributed to the fields; it is used where the source is lower than "
                "the commanded area.",
            ]},
            {"h": "Q2. Explain drip and sprinkler irrigation with their advantages."},
            {"p": [
                "Drip (trickle) irrigation applies water drop by drop near the root zone of the plant through "
                "emitters and lateral pipes. Sprinkler irrigation sprays water over the crop like rain through "
                "nozzles mounted on pipes.",
                "Advantages: water saving of 30–60%, uniform application, reduced weed growth, no land levelling, "
                "suitable for undulating land, fertigation possible, and higher crop yield.",
            ]},
            {"h": "Q3. A drip irrigation system is to be designed for 1 hectare with 4000 plants spaced 2.5 m × 1 m. "
                  "If each plant needs 8 litres per day through 4 emitters of 4 l/h, find the daily operating time."},
            {"p": [
                "Discharge per plant = 4 emitters × 4 l/h = 16 l/h.",
                "Time required per plant = 8 l / 16 l/h = 0.5 h = <b>30 minutes</b> per day.",
                "Total water requirement = 4000 × 8 = 32,000 l/day = <b>32 m³/day</b>.",
                "If the system is operated in two shifts, the capacity of the pump = 32/2 = <b>16 m³/h</b>.",
            ]},
            {"h": "Q4. Write a short note on rainwater harvesting."},
            {"p": [
                "Rainwater harvesting is the collection and storage of rainwater from roofs and other surfaces for "
                "reuse, or its artificial recharge into the ground. For a roof area of 100 m² with 800 mm annual "
                "rainfall and a runoff coefficient of 0.85, the harvestable water = 100 × 0.8 × 0.85 = "
                "<b>68 m³ per year</b>. A first-flush arrangement, filter and storage tank or recharge pit are the "
                "main components of the system.",
            ]},
        ],
        "code": "Curriculum — TSO 4.1–4.5 (T2415305); IS: 10824 (sprinkler), IS: 10799 (drip irrigation).",
    },
    {
        "num": 5,
        "title": "Assignment 5 — Diversion headworks and cross drainage works",
        "blocks": [
            {"h": "Q1. What is a diversion headwork? Draw a labelled sketch and name its components."},
            {"p": [
                "A diversion headwork is constructed across a river to raise its water level and to divert the "
                "required quantity of water into an off-taking canal. Its main components are the weir or barrage "
                "(crest, body wall, downstream floor, cut-off walls), under-sluices, canal head regulator, river "
                "training works (guide banks, spurs) and fish ladder.",
            ]},
            {"h": "Q2. Differentiate between a weir and a barrage."},
            {"p": [
                "A weir is a solid masonry/concrete wall over which water flows, and its crest level is fixed. A "
                "barrage has a series of gates between piers, so that the water level and discharge can be "
                "regulated; it provides better control of silt and floods and is preferred on alluvial rivers.",
            ]},
            {"h": "Q3. What are cross drainage works? Name the four main types with their suitability."},
            {"p": [
                "Cross drainage works are structures constructed where a canal crosses a natural drainage or "
                "river. The four main types are: (i) aqueduct — canal over the drainage; (ii) super-passage — "
                "drainage over the canal; (iii) level crossing — both at the same level, with a regulator on each; "
                "and (iv) inlet and outlet — the drainage water is admitted into the canal and taken out again "
                "downstream.",
            ]},
            {"h": "Q4. Sketch a typical cross section of a canal showing bed width, side slopes, berms, banks and "
                  "the freeboard."},
            {"p": [
                "A canal section consists of the bed, side slopes (usually 1:1 to 1.5:1 in cutting and 1.5:1 in "
                "filling), berms, service roads on the banks, and a freeboard (about 0.5–0.75 m) above the full "
                "supply level to prevent overtopping.",
            ]},
        ],
        "code": "Curriculum — TSO 5.1–5.5 (T2415305); IS: 7114 (canal linings), S.K. Garg.",
    },
    {
        "num": 6,
        "title": "Micro project — design of a rainwater harvesting system for a college building",
        "blocks": [
            {"h": "1. Objective"},
            {"p": [
                "To design a rainwater harvesting and artificial recharge system for the roof of the civil "
                "engineering block of the institute, so that a part of the water demand is met and the "
                "groundwater table is recharged.",
            ]},
            {"h": "2. Data collected"},
            {"table": {
                "header": ["Particular", "Value"],
                "rows": [
                    ["Roof area (RCC slab)", "620 m²"],
                    ["Average annual rainfall of the district", "1050 mm"],
                    ["Runoff coefficient for RCC roof", "0.85"],
                    ["Number of rainy days", "45"],
                    ["Water demand of the building", "8,000 litres/day"],
                ],
                "widths": [2.4, 1.2],
                "note": "Rainfall data collected from the district agriculture office / IMD website.",
            }},
            {"h": "3. Design calculations"},
            {"p": [
                "Annual harvestable volume = roof area × rainfall × runoff coefficient = 620 × 1.05 × 0.85 = "
                "<b>553.35 m³/year ≈ 5.5 lakh litres/year</b>.",
                "Average daily availability over the year = 553,350/365 = <b>1516 litres/day</b>. If water is "
                "stored only for the rainy season, the storage tank may be designed for 20,000 litres, and the "
                "excess water is taken to a recharge pit.",
                "Size of the first-flush tank = 1 mm of rainfall over the roof = 620 × 0.001 = <b>0.62 m³</b>.",
                "Recharge pit: for a percolation rate of 0.15 m/h and a peak rainfall intensity of 50 mm/h, the "
                "peak flow = 620 × 0.050 × 0.85/3600 = 0.0073 m³/s = 7.3 l/s; a pit of 2 m × 2 m × 3 m filled "
                "with pebbles and sand is adequate.",
            ]},
            {"h": "4. Components of the system"},
            {"ul": [
                "Roof gutters and down-take pipes of 110 mm PVC.",
                "First-flush valve and wire-mesh filter.",
                "Storage tank of 20,000 litres capacity with a settling chamber.",
                "Desilting chamber and recharge pit with a bore for excess water.",
                "Overflow pipe connected to the campus storm-water drain.",
            ]},
            {"h": "5. Conclusion"},
            {"p": [
                "The proposed system can harvest about 5.5 lakh litres of water per year, which is sufficient to "
                "meet roughly 19% of the annual water demand of the building, and it will also recharge the "
                "groundwater. The payback period is about 4 to 5 years considering the prevailing water charges.",
            ]},
        ],
        "code": "Curriculum — Micro project (S2415305); IS: 15797 (rainwater harvesting).",
    },
    {
        "num": 7,
        "title": "Seminar — Applications of remote sensing and GIS in water resource engineering",
        "blocks": [
            {"h": "1. Introduction"},
            {"p": [
                "Remote sensing is the technique of collecting information about the earth's surface from "
                "satellites or aircraft without physical contact, while a Geographic Information System (GIS) is "
                "a computer-based tool for storing, analysing and displaying spatial data. Together they provide "
                "fast, accurate and repeatable information for planning and managing water resources.",
            ]},
            {"h": "2. Applications"},
            {"ul": [
                "Mapping of catchment areas, drainage networks and watershed boundaries.",
                "Estimation of rainfall, snow cover, evaporation and soil moisture from satellite data.",
                "Identification of suitable sites for dams, reservoirs and recharge structures.",
                "Flood mapping and flood damage assessment using multi-date satellite images.",
                "Monitoring of reservoir water spread area and sedimentation.",
                "Groundwater potential mapping and selection of well sites.",
                "Canal alignment, command area mapping and irrigation scheduling.",
                "Land use / land cover change detection for hydrological modelling.",
            ]},
            {"h": "3. Merits and limitations"},
            {"p": [
                "Merits: large area coverage, repeatability, less field work, digital data suitable for GIS "
                "analysis, and quick updating. Limitations: high initial cost, need for trained manpower, "
                "cloud cover affecting optical data, and the need for ground-truth verification.",
            ]},
            {"h": "4. Conclusion"},
            {"p": [
                "Remote sensing and GIS have become essential tools for water resource planning, from watershed "
                "development to flood management, and their use should be included in the planning of every "
                "irrigation and water supply project.",
            ]},
        ],
        "code": "Curriculum — Seminar topic (S2415305); NRSC / ISRO technical reports.",
    },
    {
        "num": 8,
        "title": "Visit report — irrigation project / dam site visit",
        "blocks": [
            {"h": "1. Particulars of the visit"},
            {"table": {
                "header": ["Item", "Details"],
                "rows": [
                    ["Name of the project", "______________________________________"],
                    ["Location / district", "______________________________________"],
                    ["Date of visit", "______________________________________"],
                    ["Type of structure", "Dam / weir / barrage / canal head regulator"],
                    ["Officer who explained", "______________________________________"],
                    ["Number of students", "______________________________________"],
                ],
                "widths": [1.4, 2.6],
                "note": "Visit report ko apne actual visit ke anusaar bharein; yahan diya format reference ke liye hai.",
            }},
            {"h": "2. Technical details observed"},
            {"ul": [
                "Catchment area, reservoir capacity and water spread area.",
                "Type and height of the dam, length of the spillway and number of gates.",
                "Full reservoir level, maximum water level and dead storage level.",
                "Canals off-taking from the headworks, their discharge and command area.",
                "Instruments installed for measurement of water level and discharge.",
            ]},
            {"h": "3. Observations and comments"},
            {"p": [
                "The condition of the concrete surfaces, gates, hoists and spillway was observed. Seepage "
                "markings, vegetation on the earthen portion and the condition of the approach roads were noted. "
                "The maintenance work being carried out at the site was also observed.",
            ]},
            {"h": "4. Learning outcome"},
            {"p": [
                "The visit gave a practical understanding of the working of a diversion headwork and the "
                "importance of regular inspection and maintenance of hydraulic structures. Photographs and "
                "sketches may be attached with this report.",
            ]},
        ],
        "code": "Curriculum — Visit / other activity (S2415305).",
    },
]
