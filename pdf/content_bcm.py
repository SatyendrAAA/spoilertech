# -*- coding: utf-8 -*-
"""Content: Building Construction & Material (2415304) — 12 practicals."""

META = {
    "title": "Building Construction & Material — Laboratory Practical File",
    "subject": "Building Construction & Material",
    "code": "2415304 (P2415304)",
    "footer": "Building Construction & Material (2415304)  •  Diploma in Civil Engineering, Semester III  •  SBTE Bihar",
    "index_note": "Ye file SBTE Bihar curriculum P2415304 ke practicals par aadharit hai (approx. 12 practicals). "
                  "Apne college ke lab manual se practical ki sankhya confirm karein aur index mein page number bharein.",
    "references": [
        'Sushil Kumar, <i>Building Construction</i>, Standard Publishers Distributors.',
        'B.C. Punmia, <i>Building Construction</i>, Laxmi Publications.',
        'M.S. Shetty, <i>Concrete Technology</i> (for cement and mortar tests), S. Chand.',
        'IS: 1077, IS: 3495 (Parts 1–3) — bricks and their tests.',
        'IS: 4031 (Parts 1–6) — tests on cement; IS: 2250 and IS: 5512 — masonry mortar and flow table.',
        'IS: 2185, IS: 12894, IS: 15622 — concrete blocks, fly ash bricks and AAC blocks.',
        'IS: 287 and IS: 399 — timber; SP: 7 National Building Code; IS: 962 — staircases.',
        'SBTE Bihar curriculum for Building Construction &amp; Material (2415304 / P2415304).',
    ],

}

PRACTICALS = [
    {
        "num": 1,
        "title": "Identification and classification of building stones by field tests",
        "aim": "To identify the given samples of building stones and to classify them on the basis of their "
               "physical properties and field tests.",
        "apparatus": [
            "Stone samples (granite, sandstone, limestone, marble, laterite, slate)",
            "Geologist's hammer, magnifying glass, pen knife, weighing balance, measuring cylinder, dilute HCl",
        ],
        "theory": [
            "Stone is one of the oldest building materials and is used for masonry, flooring, cladding and "
            "foundations. Stones are classified geologically into igneous (granite, basalt), sedimentary "
            "(sandstone, limestone) and metamorphic (marble, slate) rocks.",
            "A good building stone should be hard, durable, compact, free from cracks and harmful salts, and "
            "should have sufficient strength and low water absorption. Field tests such as appearance, hardness, "
            "acid test and water absorption give a quick indication of its quality.",
        ],
        "procedure": [
            "The colour, texture and structure of each stone sample were observed with the naked eye and a "
            "magnifying glass.",
            "The hardness of each sample was tested by scratching with a pen knife and observing the mark left.",
            "A few drops of dilute hydrochloric acid were placed on each sample and the reaction was noted "
            "(effervescence indicates lime content).",
            "The specific gravity and water absorption of each sample were determined by weighing the dry and "
            "saturated samples.",
            "The samples were classified as igneous, sedimentary or metamorphic, and their suitability for "
            "different construction uses was noted.",
        ],
        "observation": {
            "header": ["Stone", "Colour / texture", "Hardness (knife)", "Acid test", "Class"],
            "rows": [
                ["Granite", "Grey, crystalline, granular", "No scratch", "No reaction", "Igneous"],
                ["Sandstone", "Reddish, granular", "Slight scratch", "No reaction", "Sedimentary"],
                ["Limestone", "Cream, fine grained", "Scratches easily", "Effervescence", "Sedimentary"],
                ["Marble", "White, crystalline", "Scratches", "Effervescence", "Metamorphic"],
                ["Laterite", "Brown, porous", "Scratches easily", "Slight reaction", "Sedimentary"],
            ],
            "widths": [1.0, 1.8, 1.2, 1.3, 1.1],
            "note": "Acid used: dilute HCl (1:10). Observations are sample values.",
        },
        "calculation": [
            "Water absorption of granite = [(W<sub>sat</sub> − W<sub>dry</sub>)/W<sub>dry</sub>] × 100 "
            "= [(1030 − 1000)/1000] × 100 = <b>3.0 %</b>",
            "Water absorption of sandstone = [(1120 − 1000)/1000] × 100 = <b>12.0 %</b>",
            "Lower water absorption indicates a more compact and durable stone; granite and marble are therefore "
            "more suitable for flooring and facing work, while sandstone and limestone are used for masonry.",
        ],
        "result": "The given stone samples were identified as granite (igneous), sandstone and limestone "
                  "(sedimentary), marble (metamorphic) and laterite. Granite was found to be the hardest and least "
                  "porous, and is suitable for flooring and heavy masonry, whereas limestone and sandstone are "
                  "suitable for general masonry work.",
        "precautions": [
            "Handle the acid carefully and keep it away from the eyes and skin.",
            "Test hardness on a fresh, clean surface of the stone.",
            "Use a representative sample and avoid broken or weathered pieces.",
            "Record the observations immediately to avoid mixing up the samples.",
        ],
        "code": "Curriculum — TSO 1.1 (T2415304); IS: 1124 (sandstone), IS: 1121 (granite).",
    },
    {
        "num": 2,
        "title": "Field tests on bricks — shape, size, soundness, hardness and structure",
        "aim": "To carry out the field tests on the given samples of bricks to judge their quality.",
        "apparatus": [
            "Brick samples (10 nos.), steel scale, measuring tape, pen knife, weighing balance, two bricks",
        ],
        "theory": [
            "Bricks are the most commonly used masonry units. A first class brick should have a uniform shape and "
            "standard size, sharp edges, a smooth surface, a clear metallic ringing sound when struck, and should "
            "not break when dropped from a height of about 1 m.",
            "Field tests are quick tests carried out at the site to check the quality of bricks before they are "
            "used. Laboratory tests such as water absorption and compressive strength are carried out for "
            "confirming the quality.",
        ],
        "procedure": [
            "Ten bricks were taken at random from the stack and their dimensions were measured with a steel scale.",
            "Each brick was examined for shape, edges, cracks, warping and uniformity of colour.",
            "Two bricks were struck against each other and the ringing sound was noted.",
            "A scratch was made on the surface of each brick with a pen knife to check its hardness.",
            "One brick was dropped flat on hard ground from a height of about 1 m and the result was noted.",
            "A broken brick was examined for a uniform, compact and free-from-lumps structure.",
        ],
        "observation": {
            "header": ["Test", "Observation", "Inference"],
            "rows": [
                ["Dimensions", "230 × 110 × 70 mm (mean)", "Standard modular size"],
                ["Shape and edges", "Sharp, square edges, uniform", "Good"],
                ["Colour", "Uniform deep red", "Well burnt"],
                ["Sound test", "Clear ringing sound", "Good"],
                ["Hardness test", "No impression by finger nail; slight knife scratch", "Good"],
                ["Structure", "Compact, no lumps or stones", "Good"],
                ["Drop test (1 m)", "Did not break", "Good"],
            ],
            "widths": [1.5, 2.4, 1.7],
            "note": "Bricks: conventional burnt clay bricks from a local kiln. Observations are sample values.",
        },
        "calculation": [
            "Standard modular brick size = 190 × 90 × 90 mm (with mortar) and conventional size = 230 × 110 × 70 mm.",
            "Percentage variation in length = (232 − 230)/230 × 100 = <b>0.87 %</b>, which is within the "
            "permissible tolerance of ±3%.",
            "All the field tests indicate that the bricks are well burnt and of good quality (first class).",
        ],
        "result": "The given bricks satisfy all the field tests — standard size, uniform colour, clear ringing "
                  "sound, good hardness, compact structure and no breakage on dropping. Hence the bricks are of "
                  "<b>first class quality</b> and suitable for masonry work.",
        "precautions": [
            "Take samples at random from different parts of the stack.",
            "Measure the dimensions of at least ten bricks and use the mean value.",
            "Do not use broken or over-burnt bricks for the tests.",
            "Carry out the drop test on a hard, level surface.",
        ],
        "code": "IS: 1077 — 1992, Common burnt clay bricks; curriculum TSO 1.2–1.4 (T2415304).",
    },
    {
        "num": 3,
        "title": "Determination of water absorption of bricks (IS: 3495 Part 2)",
        "aim": "To determine the water absorption of the given bricks after 24 hours of immersion in cold water.",
        "apparatus": [
            "Brick samples (3 nos.), weighing balance (accuracy 1 g), water tank, oven, absorbent cloth",
        ],
        "theory": [
            "Water absorption of a brick indicates its porosity and, indirectly, its durability. A highly porous "
            "brick absorbs more water, which may cause efflorescence, dampness and disintegration on freezing.",
            "As per IS: 1077, the water absorption of first class bricks shall not exceed 20% by mass, and for "
            "second class bricks it shall not exceed 22%.",
        ],
        "formula": [
            "Water absorption (%) = [ (W₂ − W₁) / W₁ ] × 100",
            "where W₁ = mass of the oven-dry brick and W₂ = mass of the brick after 24 hours of immersion",
        ],
        "procedure": [
            "The bricks were dried in an oven at 105–115 °C until constant mass and then cooled.",
            "The dry mass W₁ of each brick was recorded.",
            "The bricks were immersed in clean water at 27 ± 2 °C for 24 hours, being kept fully covered.",
            "The bricks were taken out, the surface water was wiped off with a damp cloth and the mass W₂ was recorded.",
            "The water absorption of each brick was calculated and the mean value reported.",
        ],
        "observation": {
            "header": ["Brick", "Dry mass W₁ (g)", "Wet mass W₂ (g)", "Absorption (%)"],
            "rows": [
                ["1", "3000", "3360", "12.0"],
                ["2", "2980", "3338", "12.0"],
                ["3", "3020", "3382", "12.0"],
                ["Mean", "3000", "3360", "12.0"],
            ],
            "widths": [0.9, 1.5, 1.5, 1.3],
            "note": "Bricks: first class burnt clay bricks. Readings are sample values.",
        },
        "calculation": [
            "Absorption of brick 1 = (3360 − 3000)/3000 × 100 = <b>12.0 %</b>",
            "Absorption of brick 2 = (3338 − 2980)/2980 × 100 = <b>12.0 %</b>",
            "Absorption of brick 3 = (3382 − 3020)/3020 × 100 = <b>12.0 %</b>",
            "The mean absorption of 12% is less than the 20% limit specified for first class bricks.",
        ],
        "result": "The water absorption of the given bricks is <b>12.0 %</b>, which is less than the permissible "
                  "limit of 20% for first class bricks. Hence the bricks are sufficiently dense and durable for "
                  "masonry work.",
        "precautions": [
            "Dry the bricks to constant mass before the test.",
            "Keep the bricks fully immersed and separate from each other during soaking.",
            "Wipe off only the surface water before weighing — do not press the brick.",
            "Weigh the bricks immediately after wiping to avoid evaporation loss.",
        ],
        "code": "IS: 3495 (Part 2) — 1992, Determination of water absorption of bricks.",
    },
    {
        "num": 4,
        "title": "Determination of compressive strength of bricks / blocks (IS: 3495 Part 1)",
        "aim": "To determine the compressive strength of the given bricks (or blocks) by testing them in a "
               "compression testing machine.",
        "apparatus": [
            "Compression testing machine (2000 kN), brick samples (5 nos.)",
            "Cement mortar (1:3) for capping, glass plate, steel scale, water bath, oven",
        ],
        "theory": [
            "The compressive strength of a brick is the most important criterion of its quality, because masonry "
            "is mainly subjected to compressive loads. The test is carried out on bricks whose frog and bed faces "
            "are made plane and parallel by cement mortar capping.",
            "As per IS: 1077, the minimum average compressive strength of common burnt clay bricks is 3.5 N/mm² "
            "for class 3.5, and a first class brick should have a strength of not less than 10 N/mm².",
        ],
        "formula": [
            "Compressive strength = maximum load at failure / area of the brick (N/mm²)",
            "Area = length × width of the brick",
        ],
        "procedure": [
            "Five bricks were taken and their dimensions were measured; the frog and bed faces were made plane.",
            "The bricks were soaked in water for 24 hours before testing.",
            "The bricks were removed from water and the surface water was wiped off.",
            "Cement mortar (1:3) was applied on the bed faces to make them parallel and the bricks were kept "
            "under a moist cloth for 24 hours.",
            "Each brick was placed centrally in the compression testing machine with the mortar-capped faces in "
            "contact with the platens.",
            "The load was applied uniformly at the rate of 14 N/mm² per minute until failure, and the maximum load "
            "was recorded.",
        ],
        "observation": {
            "header": ["Brick", "Length × width (mm)", "Area (mm²)", "Failure load (kN)", "Strength (N/mm²)"],
            "rows": [
                ["1", "230 × 110", "25300", "205", "8.10"],
                ["2", "230 × 110", "25300", "215", "8.50"],
                ["3", "230 × 110", "25300", "210", "8.30"],
                ["4", "230 × 110", "25300", "220", "8.70"],
                ["5", "230 × 110", "25300", "212", "8.38"],
            ],
            "widths": [0.8, 1.4, 1.1, 1.3, 1.3],
            "note": "Bricks: burnt clay bricks; rate of loading 14 N/mm² per minute. Readings are sample values.",
        },
        "calculation": [
            "Area = 230 × 110 = <b>25300 mm²</b>",
            "Strength of brick 1 = 205 × 10³ / 25300 = <b>8.10 N/mm²</b>",
            "Mean strength = (8.10 + 8.50 + 8.30 + 8.70 + 8.38)/5 = <b>8.40 N/mm²</b>",
            "As the mean strength is between 7.5 and 10 N/mm², the bricks conform to <b>class 7.5</b> of IS: 1077 "
            "(second class bricks), not to first class.",
        ],
        "result": "The average compressive strength of the given bricks is <b>8.40 N/mm²</b>, hence they conform "
                  "to <b>class 7.5</b> of IS: 1077 and can be used for load-bearing masonry with a suitable factor "
                  "of safety.",
        "precautions": [
            "The bed faces must be plane and parallel; capping with cement mortar is essential.",
            "Soak the bricks before testing to avoid absorption of water from the mortar.",
            "Place the brick centrally in the machine so that the load is axial.",
            "Apply the load at a uniform rate without shock.",
        ],
        "code": "IS: 3495 (Part 1) — 1992, Compressive strength of bricks; IS: 1077 — 1992.",
    },
    {
        "num": 5,
        "title": "Efflorescence test on bricks",
        "aim": "To find out the presence of soluble salts in the given bricks by the efflorescence test.",
        "apparatus": [
            "Brick samples (5 nos.), shallow dish, distilled water, oven, drying rack",
        ],
        "theory": [
            "Efflorescence is the deposition of white, soluble salts on the surface of bricks and masonry when "
            "water evaporates. The salts are usually sulphates of sodium, potassium and magnesium present in the "
            "brick earth or in the mortar, and their presence indicates poor durability.",
            "In the test, bricks are partially immersed in distilled water and dried alternately for seven days; "
            "the deposit is graded as nil, slight, moderate, heavy or serious as per IS: 3495 (Part 3).",
        ],
        "procedure": [
            "Five bricks were dried in an oven and placed vertically in a shallow dish.",
            "Distilled water was poured into the dish up to a depth of about 25 mm.",
            "The dish was kept in a well-ventilated room at 20–30 °C for seven days, the water being replenished "
            "whenever it evaporated.",
            "After seven days the bricks were taken out and dried in an oven at 110 °C.",
            "The surface of each brick was examined for white deposits and the efflorescence was graded.",
        ],
        "observation": {
            "header": ["Brick", "Observation after 7 days", "Grade of efflorescence"],
            "rows": [
                ["1", "No perceptible deposit", "Nil"],
                ["2", "Very small deposit (less than 10% area)", "Slight"],
                ["3", "No perceptible deposit", "Nil"],
                ["4", "Small deposit covering about 10% area", "Slight"],
                ["5", "No perceptible deposit", "Nil"],
            ],
            "widths": [0.9, 3.2, 1.9],
            "note": "Water used: distilled water. Grading as per IS: 3495 (Part 3).",
        },
        "calculation": [
            "Nil — no perceptible deposit.",
            "Slight — deposit covers not more than 10% of the surface.",
            "Moderate — deposit covers about 50% of the surface.",
            "Heavy — deposit covers more than 50% of the surface, with powdering and flaking.",
            "Serious — heavy deposit with powdering and flaking of the surface.",
        ],
        "result": "Out of the five bricks tested, three showed <b>nil</b> efflorescence and two showed <b>slight</b> "
                  "efflorescence. Since the deposit is only slight, the bricks are <b>acceptable</b> for masonry "
                  "work; bricks showing moderate or heavy efflorescence should be rejected.",
        "precautions": [
            "Use distilled water, not tap water, to avoid adding salts.",
            "Maintain the water level throughout the seven-day period.",
            "Dry the bricks in the shade before the final oven drying.",
            "Examine the bricks in good light and compare with the standard plate.",
        ],
        "code": "IS: 3495 (Part 3) — 1992, Efflorescence of bricks.",
    },
    {
        "num": 6,
        "title": "Field tests and fineness of cement",
        "aim": "To carry out the field tests on a cement sample and to determine its fineness by sieving.",
        "apparatus": [
            "Cement sample, 90 µm IS sieve, weighing balance (0.1 g), airtight container",
            "Glass of water, trowel, non-porous plate",
        ],
        "theory": [
            "Cement is a finely ground binding material which, when mixed with water, sets and hardens. Field "
            "tests such as feel, colour, presence of lumps and the float test give a quick idea of the quality of "
            "cement at the site, while the fineness test gives an indication of the rate of strength gain.",
            "Fresher and finer cement gives better strength, but cement that has absorbed moisture from the air "
            "forms lumps and loses strength; such cement should not be used for important work.",
        ],
        "formula": [
            "Percentage residue = (mass of residue / mass of sample) × 100",
        ],
        "procedure": [
            "The colour, feel and presence of lumps in the cement sample were observed.",
            "A small quantity of cement was thrown into a glass of water and its floating behaviour was noted.",
            "A handful of cement was rubbed between the palms to check for grittiness.",
            "A 100 g sample was sieved on a 90 µm IS sieve for 15 minutes and the residue was weighed.",
            "The percentage residue was calculated and the quality of the cement was judged.",
        ],
        "observation": {
            "header": ["Test", "Observation", "Inference"],
            "rows": [
                ["Colour", "Uniform grey with greenish tinge", "Fresh OPC"],
                ["Feel", "Smooth, not gritty", "Fineness satisfactory"],
                ["Lumps", "No hard lumps", "No moisture absorption"],
                ["Float test", "Floats for a short time before sinking", "Good quality cement"],
                ["Mass of sample / residue", "100 g / 8.4 g", "Residue 8.4%"],
            ],
            "widths": [1.5, 2.6, 1.7],
            "note": "Cement: OPC 43 grade, fresh stock. Observations are sample values.",
        },
        "calculation": [
            "Percentage residue = (8.4 / 100) × 100 = <b>8.4 %</b>",
            "A residue of less than 10% on the 90 µm sieve indicates cement of satisfactory fineness.",
        ],
        "result": "The cement sample passes all the field tests — uniform colour, smooth feel, no lumps and the "
                  "float test — and its residue on the 90 µm sieve is <b>8.4%</b>, which is within the permissible "
                  "limit. Hence the cement is of <b>good quality and satisfactory fineness</b>.",
        "precautions": [
            "Collect the cement sample from a freshly opened bag.",
            "Store the sample in an airtight container to prevent moisture absorption.",
            "Clean the sieve before and after sieving.",
            "Do not judge the fineness by touch alone; confirm it by sieving.",
        ],
        "code": "IS: 4031 (Part 1) — 1996; IS: 269 — 2015 (OPC specification).",
    },
    {
        "num": 7,
        "title": "Determination of initial and final setting time of cement",
        "aim": "To determine the initial and final setting time of the given cement sample using the Vicat apparatus.",
        "apparatus": [
            "Vicat apparatus with plunger and needle, balance, measuring cylinder, mixing tray, trowel",
            "Stopwatch, glass plate, cement sample (400 g)",
        ],
        "theory": [
            "Setting is the stiffening of the cement paste after mixing with water. The initial setting time is "
            "the period up to which the paste remains workable, and the final setting time is the period after "
            "which the paste has completely hardened.",
            "As per IS: 4031 (Part 5), the initial setting time of ordinary Portland cement shall not be less "
            "than 30 minutes and the final setting time shall not exceed 600 minutes. These times govern the "
            "placing and finishing of concrete and mortar.",
        ],
        "formula": [
            "Initial setting time = time of 5 ± 0.5 mm penetration − time of adding water",
            "Final setting time = time at which the ring fails to make an impression − time of adding water",
        ],
        "procedure": [
            "A cement paste of standard consistency was prepared (400 g cement with 30% water).",
            "The paste was filled in the Vicat mould and placed on the base plate.",
            "The needle was lowered at intervals of 5 minutes and the penetration was observed.",
            "The time when the needle penetrated only 5 mm from the bottom was recorded as the initial setting time.",
            "Testing was continued with the annular ring needle until it failed to make an impression on the "
            "surface of the paste.",
            "The elapsed times were calculated and compared with the IS limits.",
        ],
        "observation": {
            "header": ["Time after adding water", "Penetration / impression", "Inference"],
            "rows": [
                ["15 min", "Full penetration", "Paste plastic"],
                ["35 min", "Penetration 12 mm", "Setting started"],
                ["50 min", "Penetration 5 mm", "Initial setting time"],
                ["5 h 30 min", "Ring makes impression", "—"],
                ["7 h 00 min", "Ring fails to impress", "Final setting time"],
            ],
            "widths": [1.5, 2.1, 1.7],
            "note": "Water added = 30% of mass of cement (standard consistency). Readings are sample values.",
        },
        "calculation": [
            "Initial setting time = <b>50 minutes</b> (greater than the minimum of 30 minutes ✓)",
            "Final setting time = <b>7 hours = 420 minutes</b> (less than the maximum of 600 minutes ✓)",
            "Both values satisfy the requirements of IS: 4031 (Part 5).",
        ],
        "result": "The initial setting time of the given cement is <b>50 minutes</b> and the final setting time is "
                  "<b>420 minutes</b>. Both are within the limits specified by IS, hence the cement is suitable for "
                  "mortar and concrete work.",
        "precautions": [
            "Start the stopwatch exactly at the moment water is added.",
            "Use the correct needle (1 mm square) for setting time and the annular ring for final setting.",
            "Keep the mould in a place free from vibration and draught.",
            "Maintain a room temperature of 27 ± 2 °C.",
        ],
        "code": "IS: 4031 (Part 5) — 1988; IS: 269 — 2015.",
    },
    {
        "num": 8,
        "title": "Determination of compressive strength of cement mortar cubes",
        "aim": "To determine the compressive strength of the given cement by testing 70.6 mm cement mortar cubes "
               "prepared with standard sand.",
        "apparatus": [
            "70.6 mm cube moulds, vibrating machine, standard sand, mixing tray, trowel",
            "Compression testing machine, curing tank, weighing balance",
        ],
        "theory": [
            "The compressive strength of cement is determined on mortar cubes of 1 part cement and 3 parts of "
            "standard sand, with water equal to (P/4 + 3)% of the total mass, where P is the standard consistency. "
            "The test gives an indication of the grade of the cement.",
            "The cubes are cured in water at 27 ± 2 °C and tested at 7 and 28 days. The 28-day strength of OPC 43 "
            "grade cement shall not be less than 43 N/mm².",
        ],
        "formula": [
            "Water to be added = (P/4 + 3)% of (cement + sand) mass",
            "Compressive strength = failure load / area of cube (70.6 × 70.6 = 4984 mm²)",
        ],
        "procedure": [
            "200 g cement and 600 g standard sand were mixed dry and water was added as per the formula.",
            "The mortar was mixed for 3 minutes and filled in the cube moulds in three layers.",
            "The moulds were vibrated for 2 minutes and kept covered for 24 hours.",
            "The cubes were demoulded and cured in water until the date of testing.",
            "Three cubes were tested at 7 days and three at 28 days in the compression testing machine.",
            "The compressive strength of each cube and the mean strength were calculated.",
        ],
        "observation": {
            "header": ["Age", "Cube No.", "Failure load (kN)", "Area (mm²)", "Strength (N/mm²)"],
            "rows": [
                ["7 days", "1", "196", "4984", "39.3"],
                ["7 days", "2", "201", "4984", "40.3"],
                ["7 days", "3", "198", "4984", "39.7"],
                ["28 days", "1", "258", "4984", "51.8"],
                ["28 days", "2", "264", "4984", "53.0"],
                ["28 days", "3", "261", "4984", "52.4"],
            ],
            "widths": [0.9, 0.8, 1.2, 1.1, 1.3],
            "note": "Cement OPC 43 grade; P = 30%, so water = (30/4 + 3) = 10.5% of 800 g = 84 ml. "
                    "Readings are sample values.",
         },
        "calculation": [
            "Water required = (30/4 + 3)% of 800 g = 10.5% of 800 = <b>84 ml</b>",
            "Mean 7-day strength = (39.3 + 40.3 + 39.7)/3 = <b>39.8 N/mm²</b>",
            "Mean 28-day strength = (51.8 + 53.0 + 52.4)/3 = <b>52.4 N/mm²</b>",
            "As 52.4 N/mm² &gt; 43 N/mm², the cement satisfies the requirement of OPC 43 grade.",
        ],
        "result": "The compressive strength of the given cement is <b>39.8 N/mm² at 7 days</b> and "
                  "<b>52.4 N/mm² at 28 days</b>. The 28-day strength is more than the specified 43 N/mm², hence the "
                  "cement conforms to <b>OPC 43 grade</b>.",
        "precautions": [
            "Use standard sand and weigh all materials accurately.",
            "Vibrate the moulds for exactly 2 minutes for all cubes.",
            "Cure the cubes in water at 27 ± 2 °C and test them on the due date.",
            "Keep the loading faces of the cube parallel while testing.",
        ],
        "code": "IS: 4031 (Part 6) — 1988; IS: 650 — standard sand.",
    },
    {
        "num": 9,
        "title": "Determination of flow (workability) of cement mortar by flow table",
        "aim": "To determine the flow value of a cement mortar mix of given proportion using the flow table.",
        "apparatus": [
            "Flow table with brass cone and 25 mm drop arrangement",
            "Mixing tray, trowel, weighing balance, tamping rod, measuring cylinder, cement and sand",
        ],
        "theory": [
            "Flow of mortar is a measure of its consistency and workability. In the flow table test the mortar is "
            "placed in a standard cone, the table is dropped 25 times through a height of 25 mm, and the increase "
            "in the average diameter of the mortar is expressed as the flow value.",
            "The flow value depends on the water-cement ratio and the proportion of sand. A mortar for masonry "
            "work generally has a flow of about 105–115%, while plaster requires a slightly higher flow.",
        ],
        "formula": [
            "Flow (%) = [ (average diameter after drops − base diameter) / base diameter ] × 100",
            "Average diameter = (d₁ + d₂ + d₃ + d₄) / 4",
        ],
        "procedure": [
            "Cement and sand in the proportion 1:4 by mass were mixed dry, and water was added gradually to get a "
            "workable mix.",
            "The flow table was cleaned and the brass cone was placed at its centre.",
            "The mortar was filled in the cone in two layers, each tamped 20 times, and the top was struck off level.",
            "The cone was lifted vertically and the table was dropped 25 times in about 15 seconds.",
            "Four diameters of the spread mortar were measured and their average was calculated.",
            "The flow value was computed as a percentage of the base diameter (250 mm).",
        ],
        "observation": {
            "header": ["Trial", "d₁ (mm)", "d₂ (mm)", "d₃ (mm)", "d₄ (mm)", "Mean dia. (mm)", "Flow (%)"],
            "rows": [
                ["1", "272", "276", "274", "270", "273", "109.2"],
                ["2", "270", "274", "272", "268", "271", "108.4"],
                ["3", "274", "278", "276", "272", "275", "110.0"],
                ["Mean", "—", "—", "—", "—", "273", "109.2"],
            ],
            "widths": [0.7, 0.8, 0.8, 0.8, 0.8, 1.2, 1.0],
            "note": "Mortar 1:4 by mass, water-cement ratio 0.55. Base diameter of table top = 250 mm. "
                    "Readings are sample values.",
        },
        "calculation": [
            "Mean diameter = 273 mm",
            "Flow = (273 − 250)/250 × 100 = <b>9.2 %</b> (i.e. flow value = 109.2%)",
            "Flow value = 100 + 9.2 = <b>109.2 %</b>, which is within the usual range of 105–115% for masonry mortar.",
        ],
        "result": "The flow value of the given 1:4 cement mortar at a water-cement ratio of 0.55 is "
                  "<b>109.2 %</b>. The mortar has satisfactory workability for masonry and plastering work.",
        "precautions": [
            "The flow table must be level and firmly fixed.",
            "Lift the cone vertically without twisting or shaking.",
            "Give exactly 25 drops at a uniform rate of about one drop per 0.6 second.",
            "Measure the diameters along four equally spaced directions.",
        ],
        "code": "IS: 5512 — 1983; IS: 2250 — 1981 (masonry mortar).",
    },
    {
        "num": 10,
        "title": "Study of timber as a building material — identification, seasoning and defects",
        "aim": "To study the properties of timber used in construction and to identify its common defects, "
               "seasoning methods and uses.",
        "apparatus": [
            "Timber samples (teak, sal, deodar, pine, shisham), magnifying glass, pen knife",
            "Moisture meter, weighing balance, steel scale",
        ],
        "theory": [
            "Timber is obtained from trees and is used for doors, windows, roofs, floors, shuttering and furniture "
            "because of its light weight, strength and good thermal insulation. Its properties depend on the "
            "species, age of the tree, rate of growth and moisture content.",
            "Green timber contains a large amount of sap which causes shrinkage, warping and decay; it is "
            "therefore seasoned by air drying, kiln drying or chemical treatment before use. Defects such as "
            "knots, shakes, twists and decay reduce its strength and durability.",
        ],
        "procedure": [
            "The colour, grain, texture and smell of each timber sample were observed.",
            "The hardness was tested with a pen knife and the weight was compared by lifting the samples.",
            "The moisture content of each sample was measured with a moisture meter.",
            "The samples were examined with a magnifying glass for knots, shakes, cracks and other defects.",
            "The species were identified and their common uses in building construction were recorded.",
        ],
        "observation": {
            "header": ["Timber", "Colour / grain", "Hardness", "Moisture (%)", "Common use"],
            "rows": [
                ["Teak", "Golden brown, straight grain", "Hard", "10.5", "Doors, windows, furniture"],
                ["Sal", "Dark brown, coarse grain", "Very hard", "11.0", "Beams, sleepers, flooring"],
                ["Deodar", "Light brown, fine grain", "Soft", "9.8", "Roof trusses, shuttering"],
                ["Shisham", "Brown, interlocked grain", "Hard", "10.2", "Furniture, doors"],
                ["Pine", "Light yellow, straight grain", "Soft", "12.0", "Ceiling, panelling"],
            ],
            "widths": [0.9, 2.0, 1.0, 1.0, 2.0],
            "note": "Moisture content measured with an electrical moisture meter; readings are sample values.",
        },
        "calculation": [
            "Seasoning reduces the moisture content from about 60–70% in green timber to 10–12% for use.",
            "Percentage shrinkage in volume = (volume green − volume dry)/volume green × 100. For the test sample: "
            "(100 − 92)/100 × 100 = <b>8 %</b>.",
            "Timber with moisture content above 15% should not be used for joinery work.",
        ],
        "result": "Five species of timber were studied. Teak and sal are hard, durable and suitable for doors, "
                  "windows and structural members; deodar and pine are soft and light and are used for trusses, "
                  "shuttering and panelling. The moisture content of the seasoned samples is 9.8–12%, which is "
                  "within the acceptable range.",
        "precautions": [
            "Store timber on a level surface with spacers so that air circulates freely.",
            "Protect timber from rain and direct sun during storage.",
            "Reject samples showing knots, shakes or fungal growth for structural use.",
            "Measure moisture content at several places on the sample and take the average.",
        ],
        "code": "IS: 287 — 1993 (timber for structural use); IS: 399 — 1963 (classification of timber).",
    },
    {
        "num": 11,
        "title": "Comparative study of modern building materials — fly ash bricks, AAC blocks and ceramic tiles",
        "aim": "To compare the properties of modern building materials such as fly ash bricks, autoclaved "
               "aerated concrete (AAC) blocks and ceramic tiles with conventional burnt clay bricks.",
        "apparatus": [
            "Samples of fly ash brick, AAC block, burnt clay brick and ceramic tile",
            "Weighing balance, steel scale, water tank, compression testing machine (if available)",
        ],
        "theory": [
            "Modern building materials are being adopted to reduce the dead load of structures, to use industrial "
            "waste and to improve thermal insulation. Fly ash bricks are made from fly ash, lime, gypsum and sand; "
            "AAC blocks are lightweight, aerated, autoclaved cement products; ceramic tiles are used for flooring "
            "and wall finishes.",
            "The selection of a material depends on its density, compressive strength, water absorption, thermal "
            "conductivity, fire resistance and cost.",
        ],
        "procedure": [
            "The dimensions and mass of each sample were measured and the density was calculated.",
            "Each sample was immersed in water for 24 hours and the water absorption was determined.",
            "The compressive strength of the samples was found from the values supplied by the manufacturer, or "
            "by testing in the compression testing machine.",
            "The surface finish, edges, thermal insulation and fire resistance were observed and compared.",
            "The observations were tabulated and the suitability of each material for different uses was noted.",
        ],
        "observation": {
            "header": ["Property", "Fly ash brick", "AAC block", "Clay brick", "Ceramic tile"],
            "rows": [
                ["Size (mm)", "230×110×75", "600×200×100", "230×110×70", "300×300×8"],
                ["Density (kg/m³)", "1700", "650", "1800", "2300"],
                ["Compressive strength (N/mm²)", "10.0", "4.0", "8.4", "—"],
                ["Water absorption (%)", "12", "20", "12", "3"],
                ["Thermal conductivity (W/mK)", "0.55", "0.16", "0.60", "1.10"],
                ["Main use", "Masonry", "Partition walls", "Masonry", "Flooring / wall finish"],
            ],
            "widths": [1.8, 1.2, 1.2, 1.1, 1.3],
            "note": "Values are typical manufacturer/standard data; actual laboratory values may vary.",
        },
        "calculation": [
            "Density = mass / volume. For the AAC block: 0.6 × 0.2 × 0.1 = 0.012 m³; mass 7.8 kg → "
            "7.8/0.012 = <b>650 kg/m³</b>.",
            "For the clay brick: volume = 0.23 × 0.11 × 0.07 = 0.001771 m³; mass 3.19 kg → "
            "3.19/0.001771 = <b>1800 kg/m³</b>.",
            "Saving in dead load with AAC blocks = (1800 − 650)/1800 × 100 = <b>64 %</b>, which reduces the "
            "structural cost of the building.",
        ],
        "result": "Fly ash bricks have good strength (10 N/mm²) and use an industrial waste; AAC blocks are much "
                  "lighter (650 kg/m³) and give better thermal insulation but lower strength; ceramic tiles have "
                  "very low water absorption and are best suited for flooring and wall finishes.",
        "precautions": [
            "Handle AAC blocks carefully as they are brittle and easily damaged at the edges.",
            "Soak fly ash bricks before use only if specified by the manufacturer.",
            "Use tiles of the specified grade for flooring and skirting.",
            "Check the manufacturer's test certificate for strength and density values.",
        ],
        "code": "IS: 12894 (fly ash bricks), IS: 2185 (concrete masonry blocks), IS: 15622 (AAC blocks).",
    },
    {
        "num": 12,
        "title": "Preparation of labelled sketches of building components — doors, windows, stairs and roofs",
        "aim": "To prepare labelled sketches of the common building components — doors, windows, staircases and "
               "roofs — and to study their parts and functions.",
        "apparatus": [
            "Drawing sheet (A3), drawing board, T-square, set squares, scale, pencil, eraser, compass",
        ],
        "theory": [
            "Doors and windows are openings in walls provided for access, light and ventilation. A door consists "
            "of a frame, shutters, panels, and fittings such as hinges, handles and locks; windows may be fixed, "
            "sliding or pivoted.",
            "Stairs provide vertical circulation within a building and consist of steps (riser and tread), "
            "landing, stringer and handrail. Roofs are classified as pitched or flat and consist of the "
            "covering, purlins, rafters and trusses.",
        ],
        "procedure": [
            "The drawing sheet was fixed on the board and a border and title block were drawn.",
            "A plan and elevation of a panelled door (1.0 m × 2.1 m) were drawn to a scale of 1:20.",
            "A plan and elevation of a sliding window (1.2 m × 1.2 m) were drawn next to the door.",
            "A section of a dog-legged staircase was drawn showing riser, tread, landing and handrail.",
            "Sketches of a pitched roof (king post truss) and a flat roof were drawn with labels.",
            "All parts were labelled neatly and the sheet was completed with a title block.",
        ],
        "observation": {
            "header": ["Component", "Parts", "Standard dimensions / proportion"],
            "rows": [
                ["Door", "Frame, shutter, panel, hinges, handle, lock", "Width 0.9–1.2 m, height 2.0–2.1 m"],
                ["Window", "Frame, shutter, glass pane, sill, lintel", "Sill height 0.9 m, area 1/8 of floor area"],
                ["Staircase", "Riser, tread, landing, stringer, handrail", "Riser 150–175 mm, tread 250–300 mm"],
                ["Pitched roof", "Ridge, eaves, purlin, rafter, truss, covering", "Slope 1:3 to 1:5"],
                ["Flat roof", "Slab, waterproofing, parapet, drain", "Slope 1:50 for drainage"],
            ],
            "widths": [1.1, 2.4, 2.2],
            "note": "Sketches drawn to scale 1:20 for doors/windows and 1:50 for stair and roof.",
        },
        "calculation": [
            "Stair calculation: for a floor height of 3.0 m and riser 165 mm, number of risers = 3000/165 = "
            "<b>18.2 ≈ 18</b>, hence 17 treads (number of treads = risers − 1).",
            "Width of staircase = 1.0 m per flight for a residential building.",
            "Ventilation check: window area required = 1/8 of floor area = 12/8 = <b>1.5 m²</b> for a room of "
            "12 m²; the window of 1.2 m × 1.2 m provides 1.44 m², which is slightly less and should be increased.",
        ],
        "result": "Labelled sketches of doors, windows, a dog-legged staircase and pitched and flat roofs were "
                  "prepared to a suitable scale. The standard dimensions and proportions of each component were "
                  "studied; for a floor height of 3.0 m, 18 risers of 165 mm and 17 treads of 280 mm are required.",
        "precautions": [
            "Draw all lines with a sharp pencil and to the stated scale.",
            "Keep the proportions correct — a wrong proportion makes the drawing misleading.",
            "Label each part clearly with leader lines.",
            "Do not fold the drawing sheet; submit it flat or rolled.",
        ],
        "code": "Curriculum — Unit 4 &amp; 5 (T2415304); SP: 7 (national building code), IS: 962 (staircases).",
    },
]
