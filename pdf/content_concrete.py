# -*- coding: utf-8 -*-
"""Content: Concrete Technology (2415302) — 18 practicals."""

META = {
    "title": "Concrete Technology — Laboratory Practical File",
    "subject": "Concrete Technology",
    "code": "2415302 (P2415302)",
    "footer": "Concrete Technology (2415302)  •  Diploma in Civil Engineering, Semester III  •  SBTE Bihar",
    "index_note": "Ye file SBTE Bihar curriculum ke P2415302 ke 18 practicals par aadharit hai. Page number "
                  "index mein bharein aur har practical par date aur signature lein.",
    "references": [
        'M.S. Shetty, <i>Concrete Technology</i>, S. Chand &amp; Co., New Delhi.',
        'M.L. Gambhir, <i>Concrete Technology</i>, McGraw Hill Education.',
        'A.M. Neville, <i>Properties of Concrete</i>, Pearson Education.',
        'IS: 4031 (Parts 1–6) — Methods of physical tests for hydraulic cement.',
        'IS: 2386 (Parts 1–4) — Methods of test for aggregates for concrete.',
        'IS: 1199, IS: 516, IS: 10262, IS: 456 — workability, strength, mix design and concrete code.',
        'IS: 13311 (Parts 1 &amp; 2), IS: 3085 and ASTM C 1202 — non-destructive and permeability tests.',
        'SBTE Bihar curriculum for Concrete Technology (2415302 / P2415302).',
    ],

}

PRACTICALS = [
    {
        "num": 1,
        "title": "Determination of fineness of cement by sieving (IS: 4031 Part 1)",
        "aim": "To determine the fineness of the given sample of cement by sieving on a 90 µm IS sieve.",
        "apparatus": [
            "90 µm IS sieve with pan and lid",
            "Weighing balance (accuracy 0.1 g)",
            "Sieve shaker / brush, airtight container, sample of cement",
        ],
        "theory": [
            "Fineness of cement is a measure of the size of its particles and affects the rate of hydration, "
            "workability, rate of strength gain, shrinkage and heat of hydration. Finer cement hydrates faster and "
            "gives higher early strength, but needs more water and increases shrinkage.",
            "In the sieving method a known mass of cement is sieved continuously on a 90 µm IS sieve and the mass "
            "of the residue is expressed as a percentage of the original mass. A residue of about 5–10% indicates "
            "cement of normal fineness.",
        ],
        "formula": [
            "Percentage residue = (mass of residue / mass of sample) × 100",
            "Fineness is reported as the percentage of cement retained on the 90 µm sieve.",
        ],
        "procedure": [
            "The 90 µm sieve was cleaned, dried and weighed along with the pan.",
            "A cement sample of 100 g was taken and placed on the sieve; the lid was fixed.",
            "The sieve was shaken continuously by hand for 15 minutes, or in a sieve shaker for 10 minutes, with "
            "occasional tapping of the sides.",
            "The residue left on the sieve was weighed accurately on a balance of 0.1 g accuracy.",
            "The operation was repeated for a second sample and the mean percentage residue was calculated.",
        ],
        "observation": {
            "header": ["Trial", "Mass of sample (g)", "Mass of residue (g)", "Residue (%)"],
            "rows": [
                ["1", "100.0", "8.4", "8.4"],
                ["2", "100.0", "8.7", "8.7"],
                ["3", "100.0", "8.5", "8.5"],
                ["Mean", "100.0", "8.53", "8.53"],
            ],
            "widths": [0.9, 1.4, 1.4, 1.2],
            "note": "Cement used: OPC 43 grade. Readings are sample values.",
        },
        "calculation": [
            "Percentage residue = (8.53 / 100.0) × 100 = <b>8.53 %</b>",
            "Fineness of the cement in terms of specific surface (Blaine's apparatus) is normally 280–350 m²/kg "
            "for OPC 43 grade; the sieving method gives the residue on the 90 µm sieve only.",
        ],
        "result": "The fineness of the given cement sample is <b>8.53 % residue on the 90 µm IS sieve</b>, which is "
                  "less than 10% and hence the cement is of satisfactory fineness as per IS: 4031 (Part 1).",
        "precautions": [
            "The sieve should be perfectly clean and dry before sieving.",
            "Continuous shaking is necessary; the cement should not be pressed or rubbed by hand.",
            "Weighing must be done immediately to avoid absorption of moisture from the air.",
            "Take two samples and report the mean value.",
        ],
        "code": "IS: 4031 (Part 1) — 1996, Methods of physical tests for hydraulic cement.",
    },
    {
        "num": 2,
        "title": "Determination of standard consistency of cement using Vicat apparatus (IS: 4031 Part 4)",
        "aim": "To determine the standard consistency of the given cement paste, i.e. the quantity of water "
               "required to produce a paste that allows the Vicat plunger to penetrate 5–7 mm from the bottom.",
        "apparatus": [
            "Vicat apparatus with plunger (10 mm diameter, 50 mm long)",
            "Balance (0.1 g), measuring cylinder (100 ml), non-porous mixing tray, trowel",
            "Stopwatch, 400 g cement sample",
        ],
        "theory": [
            "Standard consistency is the water content of a cement paste, expressed as a percentage of the mass of "
            "cement, which will permit the Vicat plunger to penetrate to a point 5–7 mm above the bottom of the "
            "mould. It is used to fix the water content for the setting-time and soundness tests.",
            "The water requirement for standard consistency of ordinary Portland cement is usually between 25% and "
            "35% of the mass of cement.",
        ],
        "formula": [
            "Standard consistency, P = (mass of water added / mass of cement) × 100",
        ],
        "procedure": [
            "400 g of cement was weighed and placed in the mixing tray.",
            "Water was added in stages (starting with 25%) and the paste was mixed thoroughly for 3–5 minutes.",
            "The paste was filled in the Vicat mould, levelled and placed on the base plate of the apparatus.",
            "The plunger was lowered gently and allowed to penetrate the paste for 30 seconds; the depth of "
            "penetration from the bottom was noted with the scale.",
            "The trial was repeated with different water contents (28%, 30%, 32%) until the penetration was 5–7 mm.",
            "The percentage of water giving the required penetration was recorded as the standard consistency.",
        ],
        "observation": {
            "header": ["Trial", "Mass of cement (g)", "Water added (ml)", "Penetration from bottom (mm)", "P (%)"],
            "rows": [
                ["1", "400", "100 (25%)", "16", "25.0"],
                ["2", "400", "112 (28%)", "11", "28.0"],
                ["3", "400", "120 (30%)", "6", "30.0"],
                ["4", "400", "128 (32%)", "2", "32.0"],
            ],
            "widths": [0.7, 1.2, 1.2, 1.6, 1.0],
            "note": "The required penetration of 5–7 mm was obtained at 30% water content.",
        },
        "calculation": [
            "P = (120 / 400) × 100 = <b>30.0 %</b>",
            "Since the penetration at this water content was 6 mm (within 5–7 mm), the standard consistency is 30%.",
        ],
        "result": "The standard consistency of the given cement is <b>30 %</b>, i.e. 30 parts of water are required "
                  "for every 100 parts of cement (120 ml for 400 g of cement).",
        "precautions": [
            "The mixing must be done quickly and uniformly; mixing time should be 3–5 minutes.",
            "The plunger must be cleaned after every trial and the paste must be freshly made for each trial.",
            "The plunger should be released gently, without any jerk, and readings taken exactly after 30 seconds.",
            "Use potable water at room temperature (27 ± 2 °C).",
        ],
        "code": "IS: 4031 (Part 4) — 1988, Determination of standard consistency of cement.",
    },
    {
        "num": 3,
        "title": "Determination of initial and final setting time of cement using Vicat apparatus (IS: 4031 Part 5)",
        "aim": "To determine the initial and final setting time of the given cement sample by the Vicat apparatus.",
        "apparatus": [
            "Vicat apparatus with plunger (10 mm) and needle (1 mm square with 1 mm projecting core)",
            "Balance, measuring cylinder, mixing tray, trowel, stopwatch, glass plate",
        ],
        "theory": [
            "Setting is the process of stiffening of cement paste after mixing with water. Initial setting time is "
            "the interval between the time of mixing water and the time when the Vicat needle fails to penetrate "
            "the paste more than 5 ± 0.5 mm from the bottom of the mould. Final setting time is the interval until "
            "the needle makes an impression on the surface but the annular ring fails to cut it.",
            "As per IS: 4031, the initial setting time of OPC shall not be less than 30 minutes and the final "
            "setting time shall not exceed 600 minutes.",
        ],
        "formula": [
            "Initial setting time = (time at which penetration is 5 ± 0.5 mm) − (time of adding water)",
            "Final setting time = (time at which the annular ring fails to make an impression) − (time of adding water)",
        ],
        "procedure": [
            "A cement paste of standard consistency (30% water) was prepared and filled in the Vicat mould.",
            "The mould was placed on the base plate and the 1 mm square needle was lowered gently on the surface.",
            "The penetration was observed at regular intervals of 5 minutes until the needle failed to penetrate "
            "5 ± 0.5 mm from the bottom; the time was recorded as the initial setting time.",
            "The same specimen was then tested with the annular ring needle until the ring failed to make an "
            "impression on the surface; this time was noted.",
            "The elapsed time for both observations was calculated and compared with IS limits.",
        ],
        "observation": {
            "header": ["Time from adding water", "Observation with needle", "Remark"],
            "rows": [
                ["10 min", "Full penetration up to bottom", "Paste still plastic"],
                ["30 min", "Penetration 12 mm from bottom", "Setting started"],
                ["40 min", "Penetration 7 mm from bottom", "—"],
                ["45 min", "Penetration 5 mm from bottom", "Initial setting time = 45 min"],
                ["6 h 00 min", "Ring makes impression", "—"],
                ["5 h 50 min", "Ring fails to make impression", "Final setting time = 350 min"],
            ],
            "widths": [1.3, 2.0, 1.6],
            "note": "Water used = 30% of mass of cement (standard consistency). Readings are sample values.",
        },
        "calculation": [
            "Initial setting time = <b>45 minutes</b>",
            "Final setting time = <b>5 hours 50 minutes = 350 minutes</b>",
            "Check: initial setting time 45 min &gt; 30 min (minimum limit) ✓",
            "Final setting time 350 min &lt; 600 min (maximum limit) ✓",
        ],
        "result": "The initial setting time of the given cement is <b>45 minutes</b> and the final setting time is "
                  "<b>350 minutes</b>. Both values are within the limits specified by IS: 4031 (Part 5), hence the "
                  "cement is suitable for construction work.",
        "precautions": [
            "The stopwatch should be started at the instant of adding water to the cement.",
            "The needle must be cleaned and lowered gently at every observation, and should be kept 10 mm inside "
            "the edge of the mould.",
            "The mould must not be disturbed or tapped during the test.",
            "Maintain room temperature of 27 ± 2 °C and relative humidity of at least 50%.",
        ],
        "code": "IS: 4031 (Part 5) — 1988, Determination of setting time of cement.",
    },
    {
        "num": 4,
        "title": "Determination of compressive strength of cement (IS: 4031 Part 6)",
        "aim": "To determine the compressive strength of the given cement by testing 70.6 mm cement mortar cubes "
               "at 7 days and 28 days.",
        "apparatus": [
            "70.6 mm cube moulds (steel, ISI marked), vibrating machine",
            "Standard sand (Grade I–III as per IS 650), mixing tray, trowel, 1 kg balance with 1 g accuracy",
            "Compression testing machine (2000 kN), curing tank, stopwatch",
        ],
        "theory": [
            "The compressive strength of cement is determined on mortar cubes made of 1 part cement and 3 parts of "
            "standard sand by mass, with water equal to (P/4 + 3) percent of the combined mass of cement and sand, "
            "where P is the standard consistency.",
            "The cubes are cured under water at 27 ± 2 °C and tested in a compression testing machine. The "
            "compressive strength gives an indication of the class (grade) of the cement.",
        ],
        "formula": [
            "Water content = (P/4 + 3) % of (cement + sand) mass",
            "Compressive strength = load at failure / area of cube (mm²) = P/A",
        ],
        "procedure": [
            "200 g cement and 600 g standard sand were mixed dry on a non-porous mixing surface.",
            "Water equal to (P/4 + 3)% of 800 g, i.e. about 96 ml, was added and a uniform mortar was prepared.",
            "The mortar was filled in 70.6 mm cube moulds in three layers, compacted and vibrated for 2 minutes.",
            "The cubes were kept for 24 hours in a moist room and then demoulded and cured in water.",
            "Three cubes were taken out after 7 days and three after 28 days and tested in the compression "
            "testing machine at a uniform rate of loading.",
            "The compressive strength of each cube and the mean strength were calculated.",
        ],
        "observation": {
            "header": ["Age of curing", "Cube No.", "Failure load (kN)", "Area (mm²)", "Strength (N/mm²)"],
            "rows": [
                ["7 days", "1", "212", "4984", "42.5"],
                ["7 days", "2", "218", "4984", "43.7"],
                ["7 days", "3", "216", "4984", "43.3"],
                ["28 days", "1", "262", "4984", "52.6"],
                ["28 days", "2", "268", "4984", "53.8"],
                ["28 days", "3", "265", "4984", "53.2"],
            ],
            "widths": [1.0, 0.8, 1.2, 1.1, 1.2],
            "note": "Cement: OPC 43 grade; mortar 1:3 by mass; water content 12% (P = 36%). Area of 70.6 mm cube = "
                    "4984 mm². Readings are sample values.",
        },
        "calculation": [
            "Mean 7-day strength = (42.5 + 43.7 + 43.3)/3 = <b>43.2 N/mm²</b>",
            "Mean 28-day strength = (52.6 + 53.8 + 53.2)/3 = <b>53.2 N/mm²</b>",
            "Sample calculation: 212 kN / 4984 mm² = 212000/4984 = 42.54 N/mm²",
            "As per IS: 4031 (Part 6), 28-day strength of OPC 43 grade shall not be less than 43 N/mm² — "
            "the result satisfies this requirement.",
        ],
        "result": "The compressive strength of the given cement is <b>43.2 N/mm² at 7 days</b> and <b>53.2 N/mm² at "
                  "28 days</b>. The cement satisfies the 43 grade requirement of IS: 4031 (Part 6).",
        "precautions": [
            "Use standard sand and accurate proportions; even small errors change the result considerably.",
            "Compact the mortar uniformly and at the same time for all cubes.",
            "Keep the cubes covered with wet cloth before demoulding and cure them in water at 27 ± 2 °C.",
            "The rate of loading must be uniform and the cube must be tested at right angles to the compacting face.",
        ],
        "code": "IS: 4031 (Part 6) — 1988; IS: 650 — standard sand for testing cement.",
    },
    {
        "num": 5,
        "title": "Determination of soundness of cement by Le-Chatelier method (IS: 4031 Part 3)",
        "aim": "To determine the soundness of the given cement by measuring the expansion of the set cement paste "
               "in the Le-Chatelier apparatus.",
        "apparatus": [
            "Le-Chatelier apparatus (set of 6 moulds with weights and glass plates)",
            "Water bath, balance, measuring cylinder, mixing tray, trowel, Vicat apparatus",
        ],
        "theory": [
            "A cement is said to be sound if it does not undergo excessive expansion after setting. Unsoundness is "
            "caused by uncombined lime and magnesia, and by excessive gypsum, which expand on hydration and cause "
            "cracking of concrete.",
            "In the Le-Chatelier test, a cement paste of standard consistency is placed in the split mould and the "
            "distance between the two pointers is measured before and after boiling. The difference gives the "
            "expansion, which shall not exceed 10 mm for ordinary cement.",
        ],
        "formula": [
            "Expansion = (distance between pointers after boiling) − (distance before boiling)",
            "Soundness is satisfactory if expansion ≤ 10 mm.",
        ],
        "procedure": [
            "The Le-Chatelier mould was assembled, lightly oiled and opened out on a glass plate.",
            "A cement paste of standard consistency (30% water) was prepared and filled in the mould.",
            "The mould was covered with a glass plate, kept for 24 hours in moist air and then the distance "
            "between the pointers was measured.",
            "The mould was then immersed in water and heated to boiling in 27 ± 3 minutes and kept boiling for 3 hours.",
            "The mould was cooled and the distance between the pointers was measured again.",
            "The expansion was calculated and compared with the permissible limit.",
        ],
        "observation": {
            "header": ["Sample", "Pointer distance before (mm)", "Pointer distance after (mm)", "Expansion (mm)"],
            "rows": [
                ["1", "12.5", "14.0", "1.5"],
                ["2", "12.6", "14.1", "1.5"],
                ["Mean", "12.55", "14.05", "1.5"],
            ],
            "widths": [0.9, 1.6, 1.6, 1.2],
            "note": "Cement: OPC 43 grade. The initial 24-hour curing was done at 27 ± 2 °C in a moist chamber.",
        },
        "calculation": [
            "Expansion = 14.0 − 12.5 = <b>1.5 mm</b> (sample 1); 14.1 − 12.6 = 1.5 mm (sample 2)",
            "Mean expansion = <b>1.5 mm</b>",
            "Permissible limit = 10 mm; 1.5 mm &lt; 10 mm, hence the cement is sound.",
        ],
        "result": "The expansion of the given cement is <b>1.5 mm</b>, which is much less than the permissible limit "
                  "of 10 mm. Hence the cement is <b>sound</b> and does not contain free lime in harmful quantity.",
        "precautions": [
            "Fill the mould carefully so that the split is not distorted.",
            "The paste must be at standard consistency, otherwise the expansion value changes.",
            "Heat the water bath gradually so that boiling is reached in 27 ± 3 minutes.",
            "Measure the pointer distance with a vernier caliper or scale held exactly at the same position.",
        ],
        "code": "IS: 4031 (Part 3) — 1988, Determination of soundness of cement.",
    },
    {
        "num": 6,
        "title": "Sieve analysis of fine and coarse aggregates — grading and fineness modulus (IS: 2386 Part 1)",
        "aim": "To determine the size, grading and fineness modulus of the given fine and coarse aggregates by "
               "sieve analysis.",
        "apparatus": [
            "Set of IS sieves (4.75 mm to 150 µm for fine and 80 mm to 2.36 mm for coarse aggregate)",
            "Sieve shaker, weighing balance (0.1 g), tray, brush, oven",
        ],
        "theory": [
            "Sieve analysis shows the distribution of aggregate particles by size and governs the grading of the "
            "aggregate; a well-graded aggregate gives a dense and workable concrete. The fineness modulus (FM) is "
            "the sum of the cumulative percentages retained on a standard series of sieves divided by 100, and is "
            "an index of fineness — fine sand has FM about 2.0–2.6, medium sand 2.6–2.9 and coarse sand above 2.9.",
        ],
        "formula": [
            "Percentage retained = (mass retained on a sieve / total mass) × 100",
            "Cumulative percentage retained = sum of the percentages retained on that sieve and all coarser sieves",
            "Fineness modulus = (Σ cumulative % retained) / 100",
        ],
        "procedure": [
            "The sample was dried in an oven at 100–110 °C and exactly 1000 g of fine aggregate was weighed.",
            "The sieves were placed in a nest in descending order (4.75 mm at top) and the sample was sieved for "
            "10 minutes in a sieve shaker.",
            "The mass retained on each sieve was weighed and recorded.",
            "The operation was repeated for 5 kg of coarse aggregate with the coarse sieve set.",
            "The percentage retained, cumulative percentage retained and fineness modulus were calculated, and "
            "the grading was plotted on a semi-log graph.",
        ],
        "observation": {
            "header": ["IS sieve", "Fine agg. retained (g)", "Cum. % retained", "Coarse agg. retained (g)", "Cum. % retained"],
            "rows": [
                ["20 mm", "—", "—", "400", "8"],
                ["12.5 mm", "—", "—", "2350", "55"],
                ["10 mm", "—", "—", "1150", "78"],
                ["4.75 mm", "20", "2", "750", "93"],
                ["2.36 mm", "80", "10", "250", "98"],
                ["1.18 mm", "180", "28", "100", "100"],
                ["600 µm", "260", "54", "—", "100"],
                ["300 µm", "250", "79", "—", "100"],
                ["150 µm", "170", "96", "—", "100"],
            ],
            "widths": [1.0, 1.4, 1.2, 1.5, 1.2],
            "note": "Sample masses: fine aggregate 1000 g, coarse aggregate 5000 g. Sieves coarser than 20 mm "
                    "retained nothing. Readings are sample values.",
        },
        "calculation": [
            "<b>Fine aggregate:</b> Σ cumulative % retained = 2 + 10 + 28 + 54 + 79 + 96 = 269, hence "
            "FM = 269/100 = <b>2.69</b>; the grading satisfies the Zone II limits of IS 383, so the sand is "
            "<b>Zone II (medium sand)</b>.",
            "<b>Coarse aggregate:</b> Σ cumulative % retained = 0 + 0 + 8 + 55 + 78 + 93 + 98 + 100 + 100 + 100 + 100 = 732",
            "FM of coarse aggregate = 732/100 = <b>7.32</b>; nominal size = 20 mm.",
        ],
        "result": "The fineness modulus of the given fine aggregate is <b>2.69</b> (Zone II, medium sand) and that of "
                  "the coarse aggregate is <b>7.32</b> for a nominal size of 20 mm. Both aggregates are well graded "
                  "and suitable for concrete.",
        "precautions": [
            "The sample must be oven-dried before sieving; wet aggregate gives wrong results.",
            "Do not overload the sieves — the mass retained should not exceed the recommended limit.",
            "Shake the sieves for the specified time and brush the underside of each sieve.",
            "Avoid loss of material during handling; check that the sum of masses equals the sample mass.",
        ],
        "code": "IS: 2386 (Part 1) — 1963; IS: 383 — 2016 (aggregate grading and zones).",
    },
    {
        "num": 7,
        "title": "Determination of flakiness index and elongation index of coarse aggregate (IS: 2386 Part 1)",
        "aim": "To determine the flakiness index and elongation index of the given coarse aggregate sample.",
        "apparatus": [
            "Thickness (flakiness) gauge and length (elongation) gauge",
            "Weighing balance (0.1% accuracy), IS sieves 63, 50, 40, 31.5, 25, 20, 16, 12.5, 10 mm and 6.3 mm",
            "Tray, brush, sample of coarse aggregate",
        ],
        "theory": [
            "Flaky particles have a thickness less than 0.6 times their mean dimension, while elongated particles "
            "have a length greater than 1.8 times their mean dimension. Such particles reduce workability, strength "
            "and durability of concrete because they pack badly and break easily.",
            "The flakiness index is the percentage by mass of particles passing the thickness gauge; the "
            "elongation index is the percentage by mass of particles retained on the length gauge.",
        ],
        "formula": [
            "Flakiness index = (mass passing thickness gauge / total mass of sample) × 100",
            "Elongation index = (mass retained on length gauge / total mass of sample) × 100",
        ],
        "procedure": [
            "The sample was sieved and the material passing the 6.3 mm sieve and retained on the 63 mm sieve was discarded.",
            "About 2000 g of the sized aggregate was taken and weighed.",
            "Each particle was tested on the thickness gauge; particles passing through the gauge were separated and weighed.",
            "The remaining particles were tested on the length gauge, and particles retained on the gauge were weighed.",
            "The flakiness index and elongation index were calculated as percentages of the sample mass.",
        ],
        "observation": {
            "header": ["Test", "Mass of sample (g)", "Mass of flaky/elongated particles (g)", "Index (%)"],
            "rows": [
                ["Flakiness", "2000", "360", "18.0"],
                ["Elongation", "2000", "250", "12.5"],
            ],
            "widths": [1.2, 1.5, 2.2, 1.0],
            "note": "Aggregate size 20 mm nominal. Readings are sample values.",
        },
        "calculation": [
            "Flakiness index = (360 / 2000) × 100 = <b>18.0 %</b>",
            "Elongation index = (250 / 2000) × 100 = <b>12.5 %</b>",
            "Combined flakiness and elongation index = 18.0 + 12.5 = <b>30.5 %</b>, which is within the limit of "
            "40% generally specified for concrete aggregates.",
        ],
        "result": "The flakiness index of the given coarse aggregate is <b>18.0 %</b> and the elongation index is "
                  "<b>12.5 %</b>. The combined index (30.5%) is within permissible limits, hence the aggregate is "
                  "suitable for concrete work.",
        "precautions": [
            "Test each particle singly and pass it through the gauge without forcing.",
            "Use the correct gauge for the size group being tested.",
            "Weigh the separated particles accurately and keep the sample free from dust.",
            "Take a representative sample by quartering.",
        ],
        "code": "IS: 2386 (Part 1) — 1963, Particle size and shape.",
    },
    {
        "num": 8,
        "title": "Determination of silt content in sand (IS: 2386 Part 2)",
        "aim": "To determine the percentage of silt and clay present in the given sample of sand.",
        "apparatus": [
            "250 ml measuring cylinder, 1000 ml jar, weighing balance",
            "Common salt solution (1%), glass rod, oven, tray",
        ],
        "theory": [
            "Sand may contain silt and clay which coat the particles and increase the water demand, thereby "
            "reducing the strength and durability of concrete. As per IS: 2386 (Part 2), the silt content should "
            "not exceed 3% by mass for concrete work (up to 5% may be allowed where the concrete is not "
            "subjected to abrasion).",
            "When sand is stirred in salt water, the silt remains in suspension while the sand settles quickly, "
            "and the volume of silt can be read from the graduated cylinder.",
        ],
        "formula": [
            "Silt content by volume = (volume of silt layer / volume of sand layer) × 100",
        ],
        "procedure": [
            "A 250 ml measuring cylinder was filled up to 100 ml with the sand sample.",
            "Salt solution was added up to 150 ml and the contents were stirred thoroughly with a glass rod.",
            "The cylinder was kept undisturbed for 3 hours so that the silt settled above the sand.",
            "The volume of the silt layer and that of the sand layer were read from the graduations.",
            "The test was repeated and the mean silt content was calculated.",
        ],
        "observation": {
            "header": ["Trial", "Volume of sand (ml)", "Volume of silt (ml)", "Silt content (%)"],
            "rows": [
                ["1", "100", "4.0", "4.0"],
                ["2", "100", "3.8", "3.8"],
                ["3", "100", "4.2", "4.2"],
                ["Mean", "100", "4.0", "4.0"],
            ],
            "widths": [0.9, 1.4, 1.4, 1.2],
            "note": "Salt solution (1%) is used instead of plain water so that clay particles do not flocculate.",
        },
        "calculation": [
            "Silt content = (4.0 / 100) × 100 = <b>4.0 % by volume</b>",
            "Since 4.0% is more than the 3% limit for concrete work, the sand should be washed before use.",
        ],
        "result": "The silt content of the given sand sample is <b>4.0 %</b> by volume. This is slightly above the "
                  "permissible limit of 3% for concrete work, hence the sand requires washing before use.",
        "precautions": [
            "Stir the sample thoroughly so that all silt goes into suspension.",
            "Do not disturb the cylinder while the silt is settling.",
            "Read the levels with the eye at the same height as the meniscus.",
            "Take a representative sample of sand and remove pebbles before testing.",
        ],
        "code": "IS: 2386 (Part 2) — 1963, Estimation of deleterious materials and organic impurities.",
    },
    {
        "num": 9,
        "title": "Determination of bulking of sand (IS: 2386 Part 3)",
        "aim": "To determine the percentage of bulking of the given sand at different moisture contents.",
        "apparatus": [
            "250 ml measuring cylinder, weighing balance, oven, tray",
            "Measuring jar, glass rod, sample of air-dry sand",
        ],
        "theory": [
            "Bulking of sand is the increase in the volume of sand due to the film of water surrounding its "
            "particles when it becomes moist. Bulking makes the measuring of sand by volume unreliable and can "
            "lead to deficiency of sand in the mix; hence the volume must be corrected.",
            "Bulking is maximum at a moisture content of about 4–6% (up to 20–30% for fine sand) and disappears "
            "when the sand is fully saturated or completely dry.",
        ],
        "formula": [
            "Bulking (%) = [ (h₂ − h₁) / h₁ ] × 100",
            "where h₁ = height of sand in the cylinder when dry and h₂ = height when moist",
        ],
        "procedure": [
            "The sand was dried in an oven and 200 ml of it was filled in a measuring cylinder without tamping; "
            "the height was recorded.",
            "Water was added in increments of 1%, 2%, 4% and 6% by mass and the sand was mixed thoroughly each time.",
            "After each addition the sand was poured into the cylinder and the height was measured.",
            "The bulking percentage was calculated for each moisture content.",
            "A graph of bulking percentage against moisture content was plotted.",
        ],
        "observation": {
            "header": ["Moisture content (%)", "Height dry h₁ (ml)", "Height moist h₂ (ml)", "Bulking (%)"],
            "rows": [
                ["0", "200", "200", "0.0"],
                ["1", "200", "212", "6.0"],
                ["2", "200", "228", "14.0"],
                ["4", "200", "244", "22.0"],
                ["6", "200", "248", "24.0"],
                ["Saturated", "200", "204", "2.0"],
            ],
            "widths": [1.3, 1.3, 1.3, 1.2],
            "note": "Bulking is maximum (24%) at about 6% moisture content and reduces when the sand is saturated.",
        },
        "calculation": [
            "At 4% moisture: bulking = (244 − 200)/200 × 100 = <b>22.0 %</b>",
            "At 6% moisture: bulking = (248 − 200)/200 × 100 = <b>24.0 %</b>",
            "Correction for volume batching: if 1 m³ of dry sand is required, the volume of moist sand to be "
            "measured = 1 × (1 + 0.24) = <b>1.24 m³</b> at 6% moisture.",
        ],
        "result": "The bulking of the given sand is maximum, <b>24 %</b>, at a moisture content of about 6%. For "
                  "volume batching, the measured volume of moist sand must be increased by 24% to get the same "
                  "quantity of dry sand.",
        "precautions": [
            "Fill the cylinder loosely and do not tamp the sand, otherwise bulking is underestimated.",
            "Mix the water uniformly through the sample and allow it to stand for a few minutes before measuring.",
            "Use the same cylinder and the same method of filling throughout the test.",
            "Take readings at the same eye level to avoid parallax error.",
        ],
        "code": "IS: 2386 (Part 3) — 1963, Specific gravity, density, voids and bulking.",
    },
    {
        "num": 10,
        "title": "Determination of bulk density and voids of fine and coarse aggregates (IS: 2386 Part 3)",
        "aim": "To determine the bulk density (loose and compacted) and percentage of voids of the given fine and "
               "coarse aggregates.",
        "apparatus": [
            "Cylindrical metal measure of 3 litre / 15 litre capacity",
            "Weighing balance (accuracy 0.1%), tamping rod (16 mm diameter, 600 mm long), oven, tray",
        ],
        "theory": [
            "Bulk density is the mass of aggregate required to fill a unit volume, including the voids between "
            "particles. It is needed for converting mass proportions into volume proportions and for checking the "
            "yield of concrete.",
            "The percentage of voids is the ratio of the volume of voids to the total volume of the aggregate and "
            "is calculated from the bulk density and the specific gravity of the aggregate.",
        ],
        "formula": [
            "Bulk density = mass of aggregate filling the measure / volume of measure  (kg/m³ or kg/litre)",
            "Voids (%) = [ (specific gravity × 1000 − bulk density) / (specific gravity × 1000) ] × 100",
        ],
        "procedure": [
            "The empty measure was weighed and its volume was determined (3 litres for fine aggregate).",
            "The aggregate was filled in the measure up to the top and struck off level with a straight edge; "
            "the measure was weighed to obtain the loose bulk density.",
            "For compacted bulk density, the aggregate was filled in three layers, each layer being tamped 25 times.",
            "The measure was weighed again and the compacted bulk density was calculated.",
            "The percentage of voids was computed using the specific gravity of the aggregate.",
        ],
        "observation": {
            "header": ["Aggregate", "Mass of aggregate (kg)", "Volume of measure (l)", "Bulk density (kg/m³)"],
            "rows": [
                ["Fine — loose", "4.62", "3", "1540"],
                ["Fine — compacted", "4.92", "3", "1640"],
                ["Coarse — loose", "23.10", "15", "1540"],
                ["Coarse — compacted", "24.60", "15", "1640"],
            ],
            "widths": [1.5, 1.4, 1.4, 1.3],
            "note": "Specific gravity: fine aggregate 2.65, coarse aggregate 2.70. Readings are sample values.",
        },
        "calculation": [
            "Fine aggregate (loose): 4.62/3 = 1.54 kg/l = <b>1540 kg/m³</b>",
            "Fine aggregate (compacted): 4.92/3 = 1.64 kg/l = <b>1640 kg/m³</b>",
            "Coarse aggregate (loose): 23.10/15 = 1.54 kg/l = <b>1540 kg/m³</b>",
            "Voids in fine aggregate (loose) = [(2.65 × 1000 − 1540)/(2.65 × 1000)] × 100 = <b>41.9 %</b>",
            "Voids in coarse aggregate (compact) = [(2.70 × 1000 − 1640)/(2.70 × 1000)] × 100 = <b>39.3 %</b>",
        ],
        "result": "The bulk density of the fine aggregate is <b>1540 kg/m³ (loose)</b> and <b>1640 kg/m³ (compacted)</b>; "
                  "for the coarse aggregate it is <b>1540 kg/m³ (loose)</b> and <b>1640 kg/m³ (compacted)</b>. The "
                  "voids are about 42% in fine and 39% in coarse aggregate.",
        "precautions": [
            "Fill the measure from a height of about 50 mm without compacting for the loose bulk density test.",
            "Strike off the top surface carefully so that no aggregate is lost or pressed down.",
            "Tamp each layer uniformly (25 strokes) and distribute the strokes over the whole surface.",
            "Determine the volume of the measure accurately by filling it with water.",
        ],
        "code": "IS: 2386 (Part 3) — 1963, Bulk density and voids.",
    },
    {
        "num": 11,
        "title": "Determination of water absorption of fine and coarse aggregates (IS: 2386 Part 3)",
        "aim": "To determine the water absorption of the given fine and coarse aggregates after 24 hours of "
               "immersion in water.",
        "apparatus": [
            "Weighing balance (0.1 g), oven, vessel for immersion, wire basket",
            "Absorbent cloth, tray, sample of aggregate",
        ],
        "theory": [
            "Water absorption is the percentage of water absorbed by an aggregate when soaked in water for 24 "
            "hours. Porous aggregates absorb more water, which reduces the effective water available for "
            "hydration and affects the water-cement ratio.",
            "As per IS: 2386 (Part 3), the water absorption of aggregate suitable for concrete should normally be "
            "limited to about 2% for coarse aggregate and 1–2% for fine aggregate.",
        ],
        "formula": [
            "Water absorption = [ (W₂ − W₁) / W₁ ] × 100",
            "where W₁ = mass of oven-dry sample and W₂ = mass of saturated surface-dry sample",
        ],
        "procedure": [
            "The aggregate sample was washed and dried in an oven at 100–110 °C to constant mass.",
            "The oven-dry mass W₁ was recorded.",
            "The sample was immersed in clean water for 24 hours at room temperature.",
            "The sample was taken out, the surface water removed with an absorbent cloth, and the saturated "
            "surface-dry mass W₂ was recorded.",
            "The water absorption was calculated and the mean of three samples taken.",
        ],
        "observation": {
            "header": ["Sample", "Dry mass W₁ (g)", "SSD mass W₂ (g)", "Absorption (%)"],
            "rows": [
                ["Fine agg. — 1", "1000", "1012", "1.20"],
                ["Fine agg. — 2", "1000", "1010", "1.00"],
                ["Coarse agg. — 1", "2000", "2012", "0.60"],
                ["Coarse agg. — 2", "2000", "2016", "0.80"],
            ],
            "widths": [1.5, 1.4, 1.4, 1.2],
            "note": "Aggregate: 20 mm crushed stone and river sand. Readings are sample values.",
        },
        "calculation": [
            "Fine aggregate: (1012 − 1000)/1000 × 100 = <b>1.20 %</b>",
            "Coarse aggregate: (2012 − 2000)/2000 × 100 = <b>0.60 %</b>",
            "Both values are less than the permissible limit of 2%, hence the aggregates are suitable for concrete.",
        ],
        "result": "The water absorption of the given fine aggregate is <b>1.10 %</b> (mean) and that of the coarse "
                  "aggregate is <b>0.70 %</b> (mean). Both are within the permissible limit, hence the aggregates "
                  "are suitable for concrete.",
        "precautions": [
            "Dry the sample to constant mass, otherwise absorption will be underestimated.",
            "Remove only the surface moisture with a cloth; do not dry the pores.",
            "Use clean water and keep the sample fully immersed during the 24 hours.",
            "Weigh the samples quickly to prevent evaporation.",
        ],
        "code": "IS: 2386 (Part 3) — 1963, Water absorption of aggregates.",
    },
    {
        "num": 12,
        "title": "Determination of impact value of coarse aggregate (IS: 2386 Part 4)",
        "aim": "To determine the aggregate impact value of the given coarse aggregate, which indicates its "
               "resistance to sudden shock or impact.",
        "apparatus": [
            "Aggregate impact testing machine (with 13.5 kg hammer falling through 380 mm)",
            "IS sieves 12.5 mm and 2.36 mm, cylindrical measure, tamping rod, weighing balance, oven",
        ],
        "theory": [
            "The impact value is a measure of the toughness of an aggregate and is used to judge its suitability "
            "for road and concrete work. The test consists of subjecting the aggregate to 15 blows of a standard "
            "hammer and measuring the percentage of material crushed to finer than 2.36 mm.",
            "As per IS: 2386 (Part 4), an impact value up to 30% is satisfactory for concrete and wearing surfaces; "
            "for road surfaces the value should preferably be below 20–30%.",
        ],
        "formula": [
            "Impact value = (W₂ / W₁) × 100",
            "where W₁ = mass of oven-dry sample and W₂ = mass of material passing the 2.36 mm sieve after test",
        ],
        "procedure": [
            "The aggregate was sieved and material passing 12.5 mm and retained on 10 mm was taken and dried.",
            "The measure was filled in three layers, each tamped 25 times, and the mass W₁ was recorded.",
            "The sample was placed in the cup of the impact machine and the hammer was released 15 times.",
            "The crushed material was sieved on the 2.36 mm sieve and the passing mass W₂ was weighed.",
            "The impact value was calculated as a percentage of the total mass.",
        ],
        "observation": {
            "header": ["Trial", "Mass of sample W₁ (g)", "Mass passing 2.36 mm W₂ (g)", "Impact value (%)"],
            "rows": [
                ["1", "500", "72", "14.4"],
                ["2", "500", "70", "14.0"],
                ["3", "500", "71", "14.2"],
                ["Mean", "500", "71.0", "14.2"],
            ],
            "widths": [0.9, 1.5, 1.7, 1.2],
            "note": "Aggregate: 20 mm crushed stone, 12.5 mm to 10 mm size fraction. Readings are sample values.",
        },
        "calculation": [
            "Impact value = (72 / 500) × 100 = <b>14.4 %</b>",
            "Mean impact value = (14.4 + 14.0 + 14.2)/3 = <b>14.2 %</b>",
            "As 14.2% &lt; 20%, the aggregate is classified as <b>strong / excellent</b> for wearing surfaces.",
        ],
        "result": "The aggregate impact value of the given coarse aggregate is <b>14.2 %</b>, which is well within "
                  "the permissible limit of 30% and indicates strong, tough aggregate suitable for concrete and "
                  "road work.",
        "precautions": [
            "The hammer must fall freely through exactly 380 mm and the machine must be on a level base.",
            "Apply exactly 15 blows at intervals of at least one second.",
            "Sieve the crushed sample thoroughly before weighing the passing material.",
            "Use a representative, oven-dry sample of the specified size fraction.",
        ],
        "code": "IS: 2386 (Part 4) — 1963, Mechanical properties — impact value.",
    },
    {
        "num": 13,
        "title": "Determination of crushing value of coarse aggregate (IS: 2386 Part 4)",
        "aim": "To determine the crushing value of the given coarse aggregate, which indicates its resistance to "
               "crushing under a gradually applied compressive load.",
        "apparatus": [
            "Aggregate crushing test apparatus (cylinder, plunger and base plate)",
            "Compression testing machine (2000 kN), IS sieves 12.5 mm and 2.36 mm, tamping rod, balance, oven",
        ],
        "theory": [
            "The crushing value gives a relative measure of the resistance of an aggregate to crushing under a "
            "gradually applied compressive load. It is used for judging the suitability of aggregate for road "
            "surfaces and concrete.",
            "As per IS: 2386 (Part 4), a crushing value of up to 30% is acceptable for concrete; for road wearing "
            "courses it should not exceed 30% and preferably 20%.",
        ],
        "formula": [
            "Crushing value = (W₂ / W₁) × 100",
            "where W₁ = mass of the sample and W₂ = mass passing the 2.36 mm sieve after crushing",
        ],
        "procedure": [
            "The aggregate passing 12.5 mm and retained on 10 mm was dried and filled in the cylinder in three "
            "layers, each tamped 25 times.",
            "The mass of the sample W₁ was recorded and the plunger was placed on the surface.",
            "The assembly was placed in the compression testing machine and the load was applied uniformly to reach "
            "40 tonnes in about 10 minutes.",
            "The load was released and the crushed material was sieved on the 2.36 mm sieve.",
            "The mass passing W₂ was weighed and the crushing value calculated.",
        ],
        "observation": {
            "header": ["Trial", "Mass of sample W₁ (g)", "Mass passing 2.36 mm W₂ (g)", "Crushing value (%)"],
            "rows": [
                ["1", "3000", "540", "18.0"],
                ["2", "3000", "552", "18.4"],
                ["3", "3000", "546", "18.2"],
                ["Mean", "3000", "546", "18.2"],
            ],
            "widths": [0.9, 1.5, 1.7, 1.3],
            "note": "Load applied: 40 tonnes in 10 minutes. Readings are sample values.",
        },
        "calculation": [
            "Crushing value = (540 / 3000) × 100 = <b>18.0 %</b>",
            "Mean crushing value = (18.0 + 18.4 + 18.2)/3 = <b>18.2 %</b>",
            "As 18.2% &lt; 30%, the aggregate is suitable for concrete and for road wearing courses.",
        ],
        "result": "The crushing value of the given coarse aggregate is <b>18.2 %</b>, which is less than the "
                  "permissible limit of 30%. Hence the aggregate has good crushing strength and is suitable for "
                  "concrete work.",
        "precautions": [
            "Apply the load uniformly and reach 40 tonnes in about 10 minutes.",
            "Tamp each layer 25 times uniformly over the surface.",
            "Use oven-dry aggregate of the specified size fraction only.",
            "Clean the apparatus and sieves before and after the test.",
        ],
        "code": "IS: 2386 (Part 4) — 1963, Mechanical properties — crushing value.",
    },
    {
        "num": 14,
        "title": "Determination of abrasion value of coarse aggregate by Los Angeles machine (IS: 2386 Part 4)",
        "aim": "To determine the Los Angeles abrasion value of the given coarse aggregate.",
        "apparatus": [
            "Los Angeles abrasion testing machine (with steel balls, 500–700 revolutions)",
            "IS sieves 1.70 mm, 20 mm, 12.5 mm, 10 mm, weighing balance, oven",
        ],
        "theory": [
            "The Los Angeles abrasion test measures the resistance of an aggregate to wear by abrasion, which is "
            "important for aggregates used in road surfaces and floors. The aggregate is rotated in a drum with "
            "steel balls and the loss in mass indicates its toughness and abrasion resistance.",
            "As per IS: 2386 (Part 4), an abrasion value up to 30% is satisfactory for concrete and up to 40% for "
            "road surfaces.",
        ],
        "formula": [
            "Abrasion value = (loss in mass / initial mass) × 100",
        ],
        "procedure": [
            "A sample of 5000 g of the specified grading was prepared, washed and oven-dried.",
            "The sample and the required number of steel balls (12 for grading A) were placed in the drum.",
            "The machine was run at 30–33 revolutions per minute for 500 revolutions.",
            "The material was taken out and sieved on the 1.70 mm sieve; the retained material was weighed.",
            "The loss in mass was calculated and expressed as a percentage of the initial mass.",
        ],
        "observation": {
            "header": ["Trial", "Initial mass (g)", "Mass retained on 1.70 mm (g)", "Loss in mass (g)", "Abrasion value (%)"],
            "rows": [
                ["1", "5000", "3900", "1100", "22.0"],
                ["2", "5000", "3925", "1075", "21.5"],
                ["Mean", "5000", "3912.5", "1087.5", "21.8"],
            ],
            "widths": [0.9, 1.2, 1.7, 1.3, 1.4],
            "note": "Grading A, 12 steel balls, 500 revolutions at 30–33 rpm. Readings are sample values.",
        },
        "calculation": [
            "Loss in mass = 5000 − 3900 = 1100 g",
            "Abrasion value = (1100 / 5000) × 100 = <b>22.0 %</b>",
            "Mean abrasion value = <b>21.8 %</b>, which is less than the 30% limit for concrete work.",
        ],
        "result": "The Los Angeles abrasion value of the given coarse aggregate is <b>21.8 %</b>. Since it is below "
                  "30%, the aggregate has good abrasion resistance and is suitable for concrete and road work.",
        "precautions": [
            "Use the correct grading and number of steel balls as per IS: 2386 (Part 4).",
            "Maintain the specified speed of 30–33 rpm and the exact number of revolutions.",
            "Wash and dry the sample before weighing to remove dust and fines.",
            "Ensure that the machine door is tightly closed during the test.",
        ],
        "code": "IS: 2386 (Part 4) — 1963, Los Angeles abrasion test.",
    },
    {
        "num": 15,
        "title": "Determination of workability of concrete by slump / compaction factor test (IS: 1199)",
        "aim": "To determine the workability of the given concrete mix by the slump test (and to compare it with "
               "the compaction factor test).",
        "apparatus": [
            "Slump cone (bottom 200 mm, top 100 mm, height 300 mm) with base plate and tamping rod (16 mm)",
            "Compaction factor apparatus, trowel, scoop, weighing balance, slump scale",
        ],
        "theory": [
            "Workability describes the ease with which concrete can be mixed, transported, placed and compacted "
            "without segregation. It is commonly measured by the slump test, which indicates the consistency of "
            "the mix; the compaction factor test is used for mixes of low workability.",
            "As per IS: 1199, a slump of 25–75 mm represents medium workability, suitable for normal RCC work; a "
            "slump of 75–125 mm is high workability and 125–200 mm is very high.",
        ],
        "formula": [
            "Slump = height of cone − height of the concrete after removing the cone (mm)",
            "Compaction factor = mass of partially compacted concrete / mass of fully compacted concrete",
        ],
        "procedure": [
            "The internal surface of the slump cone and base plate was cleaned and oiled.",
            "Concrete was filled in the cone in four layers, each layer being tamped 25 times with the tamping rod.",
            "The top surface was levelled and the cone was lifted vertically slowly.",
            "The slump, i.e. the subsidence of the concrete, was measured with the scale.",
            "For the compaction factor test, concrete was placed in the upper hopper and allowed to fall into the "
            "lower hopper and then into the cylinder, and the masses were recorded.",
        ],
        "observation": {
            "header": ["Test", "Observation", "Value"],
            "rows": [
                ["Slump — mix M25 (w/c 0.50)", "Height of cone", "300 mm"],
                ["", "Height after slump", "255 mm"],
                ["", "Slump", "45 mm"],
                ["Compaction factor — partially compacted mass", "—", "12.30 kg"],
                ["Compaction factor — fully compacted mass", "—", "14.60 kg"],
                ["Compaction factor", "12.30 / 14.60", "0.84"],
            ],
            "widths": [2.4, 1.3, 1.0],
            "note": "Mix M25, cement 380 kg/m³, w/c ratio 0.50, coarse aggregate 20 mm. Readings are sample values.",
        },
        "calculation": [
            "Slump = 300 − 255 = <b>45 mm</b>",
            "Compaction factor = 12.30 / 14.60 = <b>0.84</b>",
            "As per IS: 1199, a slump of 45 mm corresponds to medium workability, and a compaction factor of 0.84 "
            "corresponds to a mix of low–medium workability; both values agree.",
        ],
        "result": "The slump of the given concrete mix is <b>45 mm</b> and its compaction factor is <b>0.84</b>. The "
                  "mix has <b>medium workability</b>, which is suitable for reinforced concrete work.",
        "precautions": [
            "Fill the cone in four equal layers and tamp each layer 25 times uniformly.",
            "Lift the cone vertically without any twisting or vibration.",
            "Measure the slump immediately after lifting the cone.",
            "Clean and oil the apparatus before every test to avoid friction.",
        ],
        "code": "IS: 1199 — 1959, Methods of sampling and analysis of concrete (workability tests).",
    },
    {
        "num": 16,
        "title": "Determination of compressive strength of concrete cubes at 7 and 28 days (IS: 516)",
        "aim": "To determine the compressive strength of the given concrete mix by testing 150 mm cubes at 7 days "
               "and 28 days of curing.",
        "apparatus": [
            "150 mm cube moulds with base plates, tamping rod, vibrating table",
            "Compression testing machine (2000 kN), curing tank, weighing balance, slump cone, trowel",
        ],
        "theory": [
            "Compressive strength is the most important property of concrete and is used as a measure of its "
            "quality. Concrete cubes of 150 mm are cast, cured under water at 27 ± 2 °C and tested in a "
            "compression testing machine at the specified age.",
            "As per IS: 516, the compressive strength is the failure load divided by the cross-sectional area of "
            "the cube. The 28-day strength is used for acceptance, while the 7-day strength (about two-thirds of "
            "the 28-day value) gives an early indication of quality.",
        ],
        "formula": [
            "Compressive strength, f<sub>ck</sub> = P / A  (N/mm²)",
            "where P = failure load in N and A = area of cube in mm² (150 × 150 = 22500 mm²)",
            "Percentage gain at 7 days ≈ (7-day strength / 28-day strength) × 100",
        ],
        "procedure": [
            "The concrete mix (M25, 1:1:2 by mass, w/c 0.50) was prepared and its workability checked by the slump test.",
            "The cube moulds were cleaned, oiled and filled in three layers, each compacted by 35 strokes or on a "
            "vibrating table.",
            "The top surface was levelled and the cubes were kept covered for 24 hours.",
            "The cubes were demoulded and cured in water at 27 ± 2 °C until the date of testing.",
            "Three cubes were tested at 7 days and three at 28 days in the compression testing machine at a "
            "uniform rate of loading of 140 kg/cm² per minute.",
            "The compressive strength of each cube and the mean strength were calculated.",
        ],
        "observation": {
            "header": ["Age", "Cube No.", "Failure load (kN)", "Area (mm²)", "Strength (N/mm²)"],
            "rows": [
                ["7 days", "1", "430", "22500", "19.11"],
                ["7 days", "2", "445", "22500", "19.78"],
                ["7 days", "3", "438", "22500", "19.47"],
                ["28 days", "1", "665", "22500", "29.56"],
                ["28 days", "2", "672", "22500", "29.87"],
                ["28 days", "3", "668", "22500", "29.69"],
            ],
            "widths": [0.9, 0.8, 1.2, 1.2, 1.3],
            "note": "Mix M25; w/c ratio 0.50; slump 45 mm. Area of 150 mm cube = 22500 mm². Readings are sample values.",
         },
        "calculation": [
            "7-day mean strength = (19.11 + 19.78 + 19.47)/3 = <b>19.45 N/mm²</b>",
            "28-day mean strength = (29.56 + 29.87 + 29.69)/3 = <b>29.71 N/mm²</b>",
            "Sample calculation: 430 kN / 22500 mm² = 430000/22500 = 19.11 N/mm²",
            "Percentage gain at 7 days = (19.45/29.71) × 100 = <b>65.5 %</b>, which is normal.",
            "For M25 concrete, the target mean strength at 28 days is 25 + 1.65 × 4 = 31.6 N/mm²; the observed "
            "value of 29.71 N/mm² is about 94% of the target and requires slightly better control of the mix.",
        ],
        "result": "The compressive strength of the given concrete is <b>19.45 N/mm² at 7 days</b> and "
                  "<b>29.71 N/mm² at 28 days</b>. The 7-day strength is about 65% of the 28-day strength, showing "
                  "normal strength development of the mix.",
        "precautions": [
            "Compact the concrete uniformly; under-compaction reduces strength considerably.",
            "Keep the cube moulds on a level, rigid surface and do not disturb them during initial setting.",
            "Cure the cubes in water at 27 ± 2 °C until testing; do not allow them to dry.",
            "Test the cube with the loading faces parallel and at right angles to the compacted direction.",
        ],
        "code": "IS: 516 — 1959, Method of test for strength of concrete; IS: 456 — 2000.",
    },
    {
        "num": 17,
        "title": "Assessment of durability of concrete by Rapid Chloride Penetration Test / permeability test",
        "aim": "To assess the durability of the given concrete by measuring its resistance to chloride ion "
               "penetration using the Rapid Chloride Penetration Test (RCPT) as per ASTM C 1202.",
        "apparatus": [
            "RCPT apparatus with two cells, DC power supply (60 V), data logger",
            "Concrete disc specimen (100 mm diameter, 50 mm thick), vacuum saturation unit, 3% NaCl solution, 0.3 N NaOH solution",
        ],
        "theory": [
            "Durability of concrete depends mainly on its permeability, i.e. the ease with which water and "
            "aggressive ions can enter the concrete. The RCPT measures the electrical charge passed through a "
            "saturated concrete specimen in 6 hours under 60 V DC; a lower charge indicates a more impermeable "
            "and durable concrete.",
            "As per ASTM C 1202, the charge passed is classified as: &gt;4000 coulombs — high permeability; "
            "2000–4000 — moderate; 1000–2000 — low; 100–1000 — very low; &lt;100 — negligible.",
        ],
        "formula": [
            "Charge passed, Q = ∫ I dt  (coulombs, integrated over 6 hours)",
            "Total charge Q = current (amperes) × time (seconds)",
        ],
        "procedure": [
            "A 100 mm diameter core or disc specimen of 50 mm thickness was cut from the concrete sample.",
            "The specimen was vacuum-saturated with water and then placed between the two cells of the apparatus.",
            "The cell on one face was filled with 3% NaCl solution (cathode) and the other with 0.3 N NaOH "
            "solution (anode).",
            "A potential difference of 60 V DC was applied for 6 hours and the current was recorded every 30 minutes.",
            "The total charge passed was computed by integrating the current-time curve.",
        ],
        "observation": {
            "header": ["Time (min)", "Current (mA)", "Charge increment (C)", "Cumulative charge (C)"],
            "rows": [
                ["30", "78", "140", "140"],
                ["60", "82", "144", "284"],
                ["120", "85", "306", "689"],
                ["240", "88", "622", "1580"],
                ["360", "90", "640", "1800"],
            ],
            "widths": [1.2, 1.2, 1.5, 1.5],
            "note": "Specimen: M25 concrete, 28 days cured. Charge increment = average current × time interval.",
        },
        "calculation": [
            "Total charge passed in 6 hours = <b>1800 coulombs</b>",
            "Sample increment: average current 85 mA for 60 minutes → Q = 0.085 × 3600 = 306 C",
            "As per ASTM C 1202, 1800 C lies in the range 1000–2000 C, which indicates <b>low permeability</b>.",
        ],
        "result": "The charge passed through the concrete specimen is <b>1800 coulombs</b>, which corresponds to "
                  "<b>low chloride ion permeability</b> as per ASTM C 1202. Hence the concrete has good durability "
                  "against chloride attack.",
        "precautions": [
            "The specimen must be fully saturated; dry specimens give misleading low values.",
            "Maintain the applied voltage at exactly 60 V throughout the test.",
            "Seal the specimen properly in the cells to prevent leakage between the solutions.",
            "Handle the specimen carefully — cracks and broken edges increase the charge passed.",
        ],
        "code": "ASTM C 1202; IS: 3085 — 1965 (permeability of concrete).",
    },
    {
        "num": 18,
        "title": "Determination of strength of hardened concrete by non-destructive tests (rebound hammer and ultrasonic pulse velocity)",
        "aim": "To assess the in-situ strength and quality of hardened concrete using the rebound hammer test and "
               "the ultrasonic pulse velocity test.",
        "apparatus": [
            "Schmidt rebound hammer (concrete test hammer) with calibration anvil",
            "Ultrasonic pulse velocity apparatus with transducers, coupling gel, measuring tape",
        ],
        "theory": [
            "Non-destructive tests (NDT) are used to assess the quality of concrete in existing structures without "
            "damaging them. The rebound hammer measures surface hardness, which is correlated with compressive "
            "strength through a calibration curve. The ultrasonic pulse velocity test measures the velocity of "
            "an ultrasonic pulse through concrete, which depends on its density and uniformity.",
            "As per IS: 13311, pulse velocity above 4.5 km/s indicates excellent quality, 3.5–4.5 km/s good, "
            "3.0–3.5 km/s medium, and below 3.0 km/s doubtful concrete.",
        ],
        "formula": [
            "Rebound number = average of the rebound readings",
            "Pulse velocity, V = L / t  (km/s), where L = path length in mm and t = travel time in µs",
            "Compressive strength is read from the calibration curve supplied with the rebound hammer.",
        ],
        "procedure": [
            "The concrete surface was cleaned, rubbed smooth and divided into a grid of test points.",
            "The rebound hammer was pressed firmly against the surface and the plunger was released; ten readings "
            "were taken at different points and the mean rebound number was calculated.",
            "For the pulse velocity test, coupling gel was applied to the transducers and they were placed on "
            "opposite faces of the member.",
            "The travel time was measured and the path length was measured with a tape.",
            "The pulse velocity was calculated and the compressive strength was estimated from the calibration "
            "charts.",
        ],
        "observation": {
            "header": ["Test", "Observation", "Mean value"],
            "rows": [
                ["Rebound number (10 readings)", "34, 36, 35, 33, 37, 35, 34, 36, 35, 35", "35.0"],
                ["Path length, L", "—", "300 mm"],
                ["Travel time, t", "—", "72 µs"],
                ["Pulse velocity, V", "300/72", "4.17 km/s"],
            ],
            "widths": [2.0, 2.2, 1.1],
            "note": "Member tested: RCC column, 28 days old. Readings are sample values.",
        },
        "calculation": [
            "Mean rebound number = (34+36+35+33+37+35+34+36+35+35)/10 = <b>35.0</b>",
            "From the rebound hammer calibration curve for a horizontal surface, a rebound number of 35 "
            "corresponds to about <b>27–28 N/mm²</b>.",
            "Pulse velocity = 300 / 72 = <b>4.17 km/s</b>",
            "As per IS: 13311, a velocity of 4.17 km/s (3.5–4.5 km/s) indicates <b>good quality</b> concrete.",
        ],
        "result": "The average rebound number of the concrete is <b>35</b>, indicating a compressive strength of about "
                  "<b>27.5 N/mm²</b>, and the ultrasonic pulse velocity is <b>4.17 km/s</b>. Both results indicate "
                  "<b>good quality, uniform concrete</b> with no visible internal defects.",
        "precautions": [
            "Test only a smooth, dry and clean surface; rough or plastered surfaces give low readings.",
            "Hold the hammer perpendicular to the surface and take at least 10 readings at different points.",
            "Apply sufficient coupling gel for the pulse velocity test and ensure good contact between transducer "
            "and concrete.",
            "Measure the path length accurately and avoid testing near edges, cracks or reinforcement.",
        ],
        "code": "IS: 13311 (Part 1 &amp; Part 2) — 1992, Non-destructive testing of concrete.",
    },
]
