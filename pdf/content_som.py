# -*- coding: utf-8 -*-
"""Content: Strength of Material for Civil Engineering (2415303) — 13 practicals."""

META = {
    "title": "Strength of Material — Laboratory Practical File",
    "subject": "Strength of Material for Civil Engg.",
    "code": "2415303 (P2415303)",
    "footer": "Strength of Material (2415303)  •  Diploma in Civil Engineering, Semester III  •  SBTE Bihar",
    "index_note": "Ye file SBTE Bihar curriculum P2415303 ke 13 practicals par aadharit hai. Page number index "
                  "mein bharein aur har practical par teacher ka signature lein.",
    "references": [
        'R.K. Bansal, <i>Strength of Materials</i>, Laxmi Publications.',
        'B.C. Punmia, <i>Strength of Materials and Mechanics of Structures</i>, Laxmi Publications.',
        'S. Ramamrutham, <i>Strength of Materials</i>, Dhanpat Rai Publishing Co.',
        'IS: 1608 — tensile testing; IS: 2408 — timber; IS: 1977 — Izod impact.',
        'IS: 1757 — Charpy impact; IS: 2281 — Brinell hardness; IS: 1586 (Part 2) — Rockwell hardness.',
        'SBTE Bihar curriculum for Strength of Material (2415303 / P2415303).',
    ],

}

PRACTICALS = [
    {
        "num": 1,
        "title": "Determination of moment of inertia of a flywheel and comparison with its theoretical value",
        "aim": "To determine the moment of inertia of a given flywheel experimentally and to compare it with the "
               "theoretical value calculated from its mass and dimensions.",
        "apparatus": [
            "Flywheel mounted on ball bearings with axle and pointer",
            "Set of weights, strong thread, stopwatch, vernier caliper, steel scale, weighing balance",
        ],
        "theory": [
            "The moment of inertia of a body about an axis is the sum of the products of the masses of its "
            "particles and the squares of their distances from that axis, I = Σmr²; it measures the resistance of "
            "the body to angular acceleration. In this experiment a weight m hangs from a thread wound round the "
            "axle of radius r, and when it falls through a height h in time t its potential energy is converted "
            "into the kinetic energy of the weight and the rotational kinetic energy of the flywheel, part of the "
            "energy being lost in friction.",
        ],
        "formula": [
            "Velocity of the falling weight, v = 2h / t",
            "Angular velocity of the flywheel, ω = v / r",
            "Loss of potential energy = m g h ; K.E. of weight = ½ m v² ; rotational K.E. of flywheel = ½ I ω²",
            "I = [ 2 m g h − m v² ] / ω²  (friction neglected)",
            "Theoretical value for a disc, I = ½ M R²",
        ],
        "procedure": [
            "The mass M and radius R of the flywheel, and the radius r of the axle, were measured.",
            "A thread carrying a weight of 2 kg was wound round the axle, the weight being kept at a known height h.",
            "The weight was released and the time t taken to reach the ground was measured with a stopwatch.",
            "The experiment was repeated five times with the same weight and the mean time was taken.",
            "The velocity v, angular velocity ω and the moment of inertia I were calculated.",
            "The experimental value was compared with the theoretical value ½MR².",
        ],
        "observation": {
            "header": ["Trial", "Height h (m)", "Time t (s)", "v = 2h/t (m/s)", "ω = v/r (rad/s)"],
            "rows": [
                ["1", "1.200", "8.10", "0.296", "11.85"],
                ["2", "1.200", "8.05", "0.298", "11.92"],
                ["3", "1.200", "8.00", "0.300", "12.00"],
                ["Mean", "1.200", "8.05", "0.298", "11.92"],
            ],
            "widths": [0.8, 1.1, 1.1, 1.3, 1.3],
            "note": "Mass of falling weight m = 2.0 kg; radius of axle r = 0.025 m; mass of flywheel M = 25.0 kg; "
                    "radius R = 0.160 m. Take g = 9.81 m/s². Readings are sample values.",
        },
        "calculation": [
            "v = 2 × 1.200 / 8.05 = 0.298 m/s ; ω = 0.298 / 0.025 = <b>11.92 rad/s</b>",
            "P.E. lost = m g h = 23.54 J; K.E. of weight = ½ × 2.0 × 0.298² = 0.089 J; hence rotational "
            "K.E. = 23.54 − 0.089 = 23.45 J = ½ I ω²",
            "I = (2 × 23.45) / (11.92)² = 46.90 / 142.09 = <b>0.330 kg·m²</b>",
            "Theoretical I = ½ M R² = 0.5 × 25.0 × 0.160² = <b>0.320 kg·m²</b>",
            "Percentage difference = (0.330 − 0.320)/0.320 × 100 = <b>3.1 %</b>",
        ],
        "result": "The moment of inertia of the flywheel determined experimentally is <b>0.330 kg·m²</b>, while its "
                  "theoretical value is <b>0.320 kg·m²</b>. The difference is 3.1%, which is due to friction at the "
                  "bearings and is within acceptable limits.",
        "precautions": [
            "The thread must be wound uniformly on the axle and should not overlap.",
            "Start the stopwatch exactly when the weight is released and stop it when the weight touches the ground.",
            "Avoid parallax while measuring the height and radius.",
            "Take several trials and use the mean time to reduce random error.",
        ],
        "code": "Curriculum — LSO 1.1 (P2415303); Engineering Mechanics laboratory manual.",
    },
    {
        "num": 2,
        "title": "Study of different components of a Universal Testing Machine (UTM) and their functions",
        "aim": "To study the construction and working of a Universal Testing Machine and to identify its different "
               "components with their functions.",
        "apparatus": [
            "Universal Testing Machine (capacity 400 kN / 1000 kN) with accessories",
            "Tension grips, compression platens, extensometer, dial gauge, measuring scale",
        ],
        "theory": [
            "A Universal Testing Machine is used to conduct tension, compression, bending and shear tests on "
            "metals, timber and concrete. It consists of a load frame with a fixed crosshead and a movable "
            "crosshead, a hydraulic loading system and a load-measuring arrangement.",
            "The load applied is measured either by a pendulum dynamometer or by a pressure gauge/load cell, and "
            "the deformation is measured by an extensometer or a dial gauge. From the load-deformation curve the "
            "yield strength, ultimate strength, modulus of elasticity and percentage elongation of the material "
            "can be determined.",
        ],
        "procedure": [
            "The machine was examined with the power supply switched off and the parts were identified.",
            "The load frame, upper fixed crosshead and lower movable crosshead were studied.",
            "The hydraulic pump, control valves, pressure gauge and load-indicating dial were identified.",
            "The tension grips, compression platens, bending and shear attachments were examined.",
            "The extensometer, dial gauge and the autographic recorder were studied along with their use.",
            "The working of the machine — gripping, loading, rate control and unloading — was demonstrated.",
        ],
        "observation": {
            "header": ["S. No.", "Component", "Function"],
            "rows": [
                ["1", "Base and columns", "Support the frame and guide the movable crosshead"],
                ["2", "Fixed (upper) crosshead", "Holds one end of the specimen through grips"],
                ["3", "Movable (lower) crosshead", "Applies load to the specimen by hydraulic pressure"],
                ["4", "Hydraulic pump and valves", "Generate and control the oil pressure for loading"],
                ["5", "Load measuring dial / load cell", "Indicates the load applied on the specimen"],
                ["6", "Extensometer / dial gauge", "Measures elongation or deformation of the specimen"],
                ["7", "Grips and platens", "Hold the specimen for tension, compression, bending or shear tests"],
                ["8", "Autographic recorder", "Plots the load-deformation curve automatically"],
            ],
            "widths": [0.7, 1.7, 3.0],
            "note": "Machine capacity: 400 kN; loading rate for steel test: 10 N/mm² per second.",
        },
        "calculation": [
            "No calculation is required in this study. The relation between load and stress is:",
            "Stress = Load / Cross-sectional area, and Strain = Change in length / Original length.",
            "Modulus of elasticity E = Stress / Strain, obtained from the initial straight portion of the "
            "load-deformation curve.",
        ],
        "result": "The different components of the Universal Testing Machine were studied and their functions were "
                  "understood. The machine can perform tension, compression, bending and shear tests, and the load "
                  "is measured by the pendulum dynamometer / load cell while deformation is measured by the "
                  "extensometer.",
        "precautions": [
            "Never operate the machine without the permission of the laboratory in charge.",
            "Ensure that the specimen is properly gripped and aligned before loading.",
            "Do not exceed the capacity of the machine.",
            "Keep hands away from the crossheads and grips during the test.",
        ],
        "code": "Curriculum — LSO 2.1 (P2415303); UTM operation manual; IS: 1608.",
    },
    {
        "num": 3,
        "title": "Tension test on mild steel bar as per IS: 1608",
        "aim": "To determine the yield strength, ultimate tensile strength, breaking strength and percentage "
               "elongation of a given mild steel bar by a tension test.",
        "apparatus": [
            "Universal Testing Machine with tension grips",
            "Mild steel specimen (12 mm diameter, gauge length 60 mm), punch, steel scale, vernier caliper",
        ],
        "theory": [
            "When a ductile material such as mild steel is subjected to a gradually increasing axial tensile load "
            "it passes through the proportional limit, elastic limit, upper and lower yield points, strain "
            "hardening and ultimate load, and finally fractures. The yield stress is the load at which plastic "
            "deformation begins and the ultimate stress is the maximum load divided by the original area, while "
            "the percentage elongation of the gauge length after fracture indicates the ductility of the material.",
        ],
        "formula": [
            "Area, A = π d² / 4",
            "Yield stress = yield load / original area ; Ultimate stress = maximum load / original area",
            "Percentage elongation = [ (L₂ − L₁) / L₁ ] × 100",
            "Percentage reduction in area = [ (A₁ − A₂) / A₁ ] × 100",
        ],
        "procedure": [
            "The diameter of the specimen was measured at three places with a vernier caliper and the mean was taken.",
            "A gauge length of 60 mm was marked on the specimen and the specimen was fitted in the grips of the UTM.",
            "The load was applied gradually and the yield point, maximum load and breaking load were noted.",
            "The load-deformation curve was recorded on the autographic recorder.",
            "The two broken pieces were joined and the final gauge length was measured.",
            "The stresses and percentage elongation were calculated.",
        ],
        "observation": {
            "header": ["Particular", "Value", "Unit"],
            "rows": [
                ["Original diameter / area", "12.0 / 113.1", "mm / mm²"],
                ["Original gauge length, L₁", "60.0", "mm"],
                ["Yield load / maximum load", "33.0 / 47.0", "kN"],
                ["Breaking load", "36.5", "kN"],
                ["Final gauge length, L₂", "78.0", "mm"],
                ["Diameter at fracture", "8.4", "mm"],
            ],
            "widths": [2.2, 1.0, 0.8],
            "note": "Material: mild steel (Fe 415 grade); rate of loading 10 N/mm²/s. Readings are sample values.",
        },
        "calculation": [
            "A = π × 12.0²/4 = <b>113.1 mm²</b>",
            "Yield stress = 33.0 × 10³ / 113.1 = <b>291.8 N/mm²</b>",
            "Ultimate tensile stress = 47.0 × 10³ / 113.1 = <b>415.6 N/mm²</b>",
            "Breaking stress = 36.5 × 10³ / 113.1 = <b>322.7 N/mm²</b>",
            "Percentage elongation = (78.0 − 60.0)/60.0 × 100 = <b>30.0 %</b>; final area = 55.4 mm², hence "
            "reduction in area = (113.1 − 55.4)/113.1 × 100 = <b>51.0 %</b>",
        ],
        "result": "For the given mild steel specimen, the yield stress is <b>291.8 N/mm²</b>, the ultimate tensile "
                  "strength is <b>415.6 N/mm²</b>, the breaking stress is <b>322.7 N/mm²</b>, the percentage "
                  "elongation is <b>30%</b> and the reduction in area is <b>51%</b>. The material is ductile and "
                  "conforms to Fe 415 grade steel.",
        "precautions": [
            "Measure the diameter accurately at three sections and use the mean value.",
            "Apply the load gradually and without shock, at the specified rate.",
            "Mark the gauge length before the test and measure the final length after joining the broken pieces.",
            "Note the yield point carefully — the pointer may pause or drop at the yield stage.",
        ],
        "code": "IS: 1608 — 2005, Metallic materials — tensile testing; IS: 1786 (HYSD bars).",
    },
    {
        "num": 4,
        "title": "Compression test on a mild steel specimen using Universal Testing Machine",
        "aim": "To determine the compressive strength and behaviour of a given mild steel specimen under axial "
               "compression using a Universal Testing Machine.",
        "apparatus": [
            "Universal Testing Machine with compression platens",
            "Mild steel specimen (12 mm diameter, 24 mm length), vernier caliper, steel scale",
        ],
        "theory": [
            "When a short specimen is subjected to axial compression it shortens and bulges laterally. For a "
            "ductile material such as mild steel, the specimen does not fracture but flattens, so the test gives "
            "the yield strength in compression rather than a breaking stress.",
            "The compressive stress is the load divided by the original cross-sectional area. For ductile "
            "materials the compressive yield stress is nearly equal to the tensile yield stress, whereas brittle "
            "materials are much stronger in compression than in tension.",
        ],
        "formula": [
            "Area, A = π d² / 4",
            "Compressive stress = load / original area",
            "Percentage decrease in height = [ (h₁ − h₂) / h₁ ] × 100",
        ],
        "procedure": [
            "The diameter and height of the specimen were measured with a vernier caliper.",
            "The specimen was placed centrally between the two compression platens of the UTM.",
            "The load was applied gradually and the yield load was noted from the dial/autographic record.",
            "Loading was continued until the specimen flattened to about half of its original height.",
            "The final height was measured and the compressive stress was calculated.",
        ],
        "observation": {
            "header": ["Particular", "Value", "Unit"],
            "rows": [
                ["Original diameter", "12.0", "mm"],
                ["Original height, h₁", "24.0", "mm"],
                ["Original area", "113.1", "mm²"],
                ["Yield load (compression)", "32.0", "kN"],
                ["Maximum load applied", "58.0", "kN"],
                ["Final height, h₂", "14.0", "mm"],
            ],
            "widths": [2.2, 1.0, 0.8],
            "note": "Material: mild steel; loading rate 10 N/mm²/s. Readings are sample values.",
        },
        "calculation": [
            "A = π × 12²/4 = <b>113.1 mm²</b>",
            "Compressive yield stress = 32.0 × 10³ / 113.1 = <b>283.0 N/mm²</b>",
            "Maximum compressive stress = 58.0 × 10³ / 113.1 = <b>512.8 N/mm²</b>",
            "Percentage decrease in height = (24.0 − 14.0)/24.0 × 100 = <b>41.7 %</b>",
            "The compressive yield stress (283 N/mm²) is nearly equal to the tensile yield stress of mild steel "
            "(about 292 N/mm²), which confirms the ductile behaviour of the material.",
        ],
        "result": "The compressive yield stress of the given mild steel specimen is <b>283.0 N/mm²</b> and the "
                  "specimen flattened by about 42% of its original height without fracture. The material behaves "
                  "as a ductile material in compression.",
        "precautions": [
            "Place the specimen exactly at the centre of the lower platen to avoid eccentric loading.",
            "Apply the load slowly and uniformly; avoid shock loading.",
            "Do not continue loading beyond the capacity of the machine or after heavy bulging.",
            "Measure the height and diameter before and after the test with the same instrument.",
        ],
        "code": "IS: 1608 — 2005; curriculum outcome LSO 4.1 (P2415303).",
    },
    {
        "num": 5,
        "title": "Flexural test on a timber beam in both orientations as per IS: 2408",
        "aim": "To determine the flexural strength (modulus of rupture) of a given timber beam by testing it in "
               "two orientations of the rectangular section.",
        "apparatus": [
            "Universal Testing Machine / flexure testing arrangement with two supports and a loading nose",
            "Timber specimen (50 mm × 75 mm × 750 mm), vernier caliper, steel scale, dial gauge",
        ],
        "theory": [
            "When a simply supported beam is loaded at the centre, bending stresses are set up in the section. The "
            "maximum bending stress at failure, called the modulus of rupture, is given by the flexure formula "
            "f = M/Z, where M is the maximum bending moment and Z the section modulus.",
            "For a rectangular section of width b and depth d, Z = bd²/6. The flexural strength therefore depends "
            "on the orientation of the section: a beam is much stronger when loaded on its narrower face, because "
            "the depth is then greater.",
        ],
        "formula": [
            "Maximum bending moment, M = W L / 4  (central point load)",
            "Section modulus, Z = b d² / 6",
            "Modulus of rupture, f = M / Z = 3 W L / (2 b d²)",
        ],
        "procedure": [
            "The dimensions of the timber specimen were measured accurately.",
            "The specimen was placed on the two supports of the testing arrangement with a span of 600 mm, on its "
            "wider face (orientation 1).",
            "The load was applied at the centre through the loading nose at a uniform rate.",
            "The maximum load at failure was noted and the modulus of rupture calculated.",
            "The test was repeated on an identical specimen placed on its narrower face (orientation 2).",
            "The two values were compared.",
        ],
        "observation": {
            "header": ["Orientation", "b (mm)", "d (mm)", "Span L (mm)", "Failure load W (kN)"],
            "rows": [
                ["1 — on wider face", "50", "75", "600", "3.20"],
                ["2 — on narrower face", "75", "50", "600", "1.42"],
            ],
            "widths": [1.7, 0.9, 0.9, 1.1, 1.4],
            "note": "Timber: teak; moisture content about 12%. Readings are sample values.",
        },
        "calculation": [
            "Orientation 1: f = 3 W L/(2 b d²) = (3 × 3200 × 600)/(2 × 50 × 75²) = 5,760,000/562,500 = "
            "<b>10.24 N/mm²</b>",
            "Orientation 2: f = (3 × 1420 × 600)/(2 × 75 × 50²) = 2,556,000/375,000 = <b>6.82 N/mm²</b>",
            "Ratio of strengths = 10.24/6.82 = 1.50, which equals the ratio of the depths (75/50 = 1.5), showing "
            "that the flexural strength is proportional to the depth of the section.",
        ],
        "result": "The modulus of rupture of the given timber is <b>10.24 N/mm²</b> when the beam is loaded on its "
                  "wider face and <b>6.82 N/mm²</b> when loaded on its narrower face. The strength in the first "
                  "orientation is 1.5 times that in the second, confirming that the flexural strength is "
                  "proportional to the square of the depth.",
        "precautions": [
            "The specimen must be free from knots, cracks and other visible defects.",
            "Apply the load exactly at the centre of the span and without impact.",
            "Measure the dimensions at the section of failure.",
            "Keep the supports and loading nose parallel and firmly in contact with the specimen.",
        ],
        "code": "IS: 2408 — 1991, Methods of test for wood — determination of strength properties.",
    },
    {
        "num": 6,
        "title": "Shear strength test on a given specimen",
        "aim": "To determine the ultimate shear strength of a given mild steel specimen by a single shear test.",
        "apparatus": [
            "Universal Testing Machine with shear test attachment (shear block and punch)",
            "Mild steel specimen (12 mm diameter), vernier caliper, steel scale",
        ],
        "theory": [
            "When a specimen is subjected to a force acting parallel to its cross-section, shear stress is "
            "developed. In a single shear test the specimen is held in a shear block and a punch shears it across "
            "one plane, so the resisting area is the cross-sectional area of the specimen.",
            "The shear strength is the maximum load divided by the sheared area. For mild steel the ultimate shear "
            "strength is approximately 0.5 to 0.6 times the ultimate tensile strength.",
        ],
        "formula": [
            "Sheared area, A = π d² / 4",
            "Ultimate shear strength, τ = shear load / sheared area",
        ],
        "procedure": [
            "The diameter of the specimen was measured and its cross-sectional area calculated.",
            "The specimen was inserted in the shear block of the attachment, which was placed in the UTM.",
            "The load was applied gradually until the specimen was sheared off.",
            "The maximum shear load was noted from the load indicating dial.",
            "The shear strength was calculated and compared with the tensile strength of the material.",
        ],
        "observation": {
            "header": ["Particular", "Value", "Unit"],
            "rows": [
                ["Diameter of specimen", "12.0", "mm"],
                ["Sheared area", "113.1", "mm²"],
                ["Shear load at failure", "24.0", "kN"],
                ["Type of shear", "Single shear", "—"],
            ],
            "widths": [2.2, 1.2, 0.9],
            "note": "Material: mild steel. Readings are sample values.",
        },
        "calculation": [
            "A = π × 12²/4 = <b>113.1 mm²</b>",
            "τ = 24.0 × 10³ / 113.1 = <b>212.2 N/mm²</b>",
            "Compare with tensile strength of mild steel (≈ 415 N/mm²): τ/f<sub>u</sub> = 212.2/415.6 = 0.51, "
            "which agrees with the usual relation τ ≈ 0.5 f<sub>u</sub>.",
        ],
        "result": "The ultimate shear strength of the given mild steel specimen is <b>212.2 N/mm²</b>, which is "
                  "about 51% of its ultimate tensile strength, as expected for ductile steel.",
        "precautions": [
            "Place the specimen exactly in the centre of the shear block to avoid bending.",
            "Tighten the attachment firmly so that the specimen does not slip.",
            "Apply the load slowly and uniformly until shear occurs.",
            "Measure the diameter at the sheared section after the test.",
        ],
        "code": "IS: 1608 — 2005; curriculum outcome LSO 6.1 (P2415303).",
    },
    {
        "num": 7,
        "title": "Izod impact test on a given specimen",
        "aim": "To determine the impact strength (toughness) of a given metal specimen by the Izod impact test.",
        "apparatus": [
            "Izod impact testing machine with a 167 J / 300 J pendulum hammer",
            "Izod test specimen with a V-notch (10 mm × 10 mm section, 75 mm length), vernier caliper",
        ],
        "theory": [
            "Toughness is the ability of a material to absorb energy before fracture. The Izod test measures this "
            "energy by breaking a notched specimen with a swinging pendulum; the specimen is held as a cantilever "
            "and struck at the notch.",
            "The energy absorbed by the specimen is the difference between the energy of the hammer before and "
            "after fracture, and the impact strength is expressed as the energy absorbed per unit area at the notch.",
        ],
        "formula": [
            "Energy absorbed, E = W (h₁ − h₂)  (J)",
            "Impact strength = energy absorbed / area of the notch (J/mm²)",
            "Impact value = energy absorbed by specimen / energy of the hammer × 100",
        ],
        "procedure": [
            "The dimensions of the specimen and the notch were measured.",
            "The machine was checked with the pointer at the zero position and the pendulum was raised to its "
            "starting position.",
            "The specimen was clamped in the vice with the notch facing the striker and the pointer was set.",
            "The pendulum was released and the energy absorbed by the specimen was read from the scale.",
            "The test was repeated on two more specimens and the mean impact strength was calculated.",
        ],
        "observation": {
            "header": ["Specimen", "Energy absorbed (J)", "Notch area (mm²)", "Impact strength (J/mm²)"],
            "rows": [
                ["1", "12.0", "80", "0.150"],
                ["2", "11.5", "80", "0.144"],
                ["3", "12.5", "80", "0.156"],
                ["Mean", "12.0", "80", "0.150"],
            ],
            "widths": [1.2, 1.5, 1.4, 1.6],
            "note": "Material: mild steel; notch 45° V-notch, 2 mm deep. Readings are sample values.",
        },
        "calculation": [
            "Mean energy absorbed = (12.0 + 11.5 + 12.5)/3 = <b>12.0 J</b>",
            "Notch area = 10 mm × (2 × 4 mm) = 80 mm² (approximate fractured area)",
            "Impact strength = 12.0 / 80 = <b>0.150 J/mm²</b>",
            "Impact value = (12.0 / 167) × 100 = <b>7.2 %</b> of the hammer energy",
        ],
        "result": "The Izod impact strength of the given mild steel specimen is <b>12.0 J</b> (0.150 J/mm²), which "
                  "indicates good toughness and ductility of the material.",
        "precautions": [
            "The pendulum must be locked in the raised position before the specimen is fixed.",
            "Keep clear of the swing path of the pendulum during the test.",
            "Locate the specimen accurately in the vice with the notch exactly opposite the striker.",
            "Do not touch the specimen or the machine before the pendulum comes to rest.",
        ],
        "code": "IS: 1977 — 1996, Izod impact test for metallic materials.",
    },
    {
        "num": 8,
        "title": "Charpy impact test on a metal specimen",
        "aim": "To determine the impact energy absorbed by a given metal specimen using the Charpy impact test.",
        "apparatus": [
            "Charpy impact testing machine with pendulum hammer and scale",
            "Charpy V-notch specimen (10 mm × 10 mm × 55 mm), vernier caliper, setting gauge",
        ],
        "theory": [
            "In the Charpy test the notched specimen is supported as a simple beam at both ends and is struck by "
            "the pendulum at the centre, on the face opposite the notch. Because the specimen is supported at both "
            "ends, the Charpy test gives a slightly different measure of toughness than the Izod test.",
            "The energy absorbed in breaking the specimen is read directly from the graduated scale of the machine "
            "and is a measure of the resistance of the material to sudden loading.",
        ],
        "formula": [
            "Energy absorbed, E = W (cos β − cos α)  (J)",
            "Impact strength = energy absorbed / cross-sectional area at the notch (J/mm²)",
        ],
        "procedure": [
            "The specimen was prepared with a 45° V-notch of 2 mm depth and its dimensions were measured.",
            "The pendulum was raised to the starting angle and the pointer was set to zero.",
            "The specimen was placed centrally on the supports with the notch away from the striker.",
            "The pendulum was released and the energy absorbed was read from the scale after the swing.",
            "The test was repeated on two more specimens and the mean value was taken.",
        ],
        "observation": {
            "header": ["Specimen", "Energy absorbed (J)", "Area at notch (mm²)", "Impact strength (J/mm²)"],
            "rows": [
                ["1", "15.0", "80", "0.188"],
                ["2", "14.5", "80", "0.181"],
                ["3", "15.5", "80", "0.194"],
                ["Mean", "15.0", "80", "0.188"],
            ],
            "widths": [1.2, 1.5, 1.4, 1.6],
            "note": "Material: mild steel; Charpy V-notch specimen. Readings are sample values.",
        },
        "calculation": [
            "Mean energy absorbed = (15.0 + 14.5 + 15.5)/3 = <b>15.0 J</b>",
            "Impact strength = 15.0 / 80 = <b>0.188 J/mm²</b>",
            "The Charpy value (15.0 J) is slightly higher than the Izod value (12.0 J) of the same material "
            "because the specimen is supported at both ends and the test geometry is different.",
        ],
        "result": "The Charpy impact energy absorbed by the given mild steel specimen is <b>15.0 J</b> "
                  "(0.188 J/mm²), indicating good impact toughness of the material.",
        "precautions": [
            "Place the specimen exactly on the supports using the setting gauge.",
            "Ensure that the notch is on the side away from the striker.",
            "Release the pendulum smoothly from the correct height.",
            "Read the scale after the pendulum has completed its forward swing.",
        ],
        "code": "IS: 1757 — 1988, Charpy impact test for metallic materials.",
    },
    {
        "num": 9,
        "title": "Brinell hardness test on a metal specimen",
        "aim": "To determine the Brinell hardness number (BHN) of a given metal specimen.",
        "apparatus": [
            "Brinell hardness testing machine with a hardened steel ball indenter (10 mm)",
            "Microscope or Brinell index measuring scale, specimen, standard test block",
        ],
        "theory": [
            "Hardness is the resistance of a material to indentation. In the Brinell test a hardened steel ball "
            "of diameter D is pressed into the surface of the specimen under a standard load P and the diameter d "
            "of the resulting indentation is measured after removing the load.",
            "The Brinell hardness number is the load divided by the curved surface area of the indentation, and is "
            "expressed in kg/mm² (or in MPa, numerically equal to BHN × 9.81).",
        ],
        "formula": [
            "BHN = 2P / [ π D ( D − √(D² − d²) ) ]",
            "where P = load in kg, D = diameter of ball in mm and d = diameter of indentation in mm",
            "Load P = 30 D² for steel (i.e. 3000 kg for a 10 mm ball)",
        ],
        "procedure": [
            "The surface of the specimen was ground smooth and cleaned.",
            "The specimen was placed on the anvil of the machine and the 10 mm ball indenter was brought into "
            "contact with the surface.",
            "A load of 3000 kg was applied and maintained for 15 seconds.",
            "The load was released, the specimen was removed and the diameter of the indentation was measured in "
            "two perpendicular directions with the microscope.",
            "The mean diameter was used to calculate the Brinell hardness number.",
        ],
        "observation": {
            "header": ["Test", "Load P (kg)", "Ball dia D (mm)", "Indentation dia d (mm)", "BHN"],
            "rows": [
                ["1", "3000", "10", "4.20", "207"],
                ["2", "3000", "10", "4.25", "202"],
                ["3", "3000", "10", "4.15", "212"],
                ["Mean", "3000", "10", "4.20", "207"],
            ],
            "widths": [0.8, 1.1, 1.2, 1.5, 0.9],
            "note": "Material: mild steel; dwell time 15 s. Readings are sample values.",
        },
        "calculation": [
            "For d = 4.20 mm: √(D² − d²) = √(100 − 17.64) = √82.36 = 9.075 mm",
            "BHN = 2 × 3000 / [π × 10 × (10 − 9.075)] = 6000 / (31.416 × 0.925) = 6000/29.06 = <b>206.5</b>",
            "Mean BHN of the three tests = (207 + 202 + 212)/3 ≈ <b>207</b>",
        ],
        "result": "The Brinell hardness number of the given mild steel specimen is <b>207</b> (≈ 2030 N/mm²).",
        "precautions": [
            "The test surface must be clean, smooth and flat, and free from scale.",
            "Keep the indentation away from the edge of the specimen (at least 2.5 d).",
            "Apply the load slowly and maintain it for the specified dwell time.",
            "Measure the indentation diameter in two perpendicular directions and use the mean.",
        ],
        "code": "IS: 2281 — 2005, Brinell hardness test for metallic materials.",
    },
    {
        "num": 10,
        "title": "Rockwell hardness test on a metal specimen",
        "aim": "To determine the Rockwell hardness (HRC) of a given hardened steel specimen.",
        "apparatus": [
            "Rockwell hardness testing machine with diamond cone indenter (120°)",
            "Specimen, standard test block, anvil",
        ],
        "theory": [
            "In the Rockwell test the depth of indentation is measured directly by the machine instead of the "
            "diameter, which makes the test very quick. A minor load of 10 kg is first applied to seat the "
            "indenter, and then a major load of 150 kg is applied; the Rockwell hardness is read on the dial after "
            "the major load is removed.",
            "The Rockwell C scale (HRC) uses a diamond cone indenter with a total load of 150 kg and is suitable "
            "for hardened steel. Higher hardness gives a higher HRC value, and each division of the dial "
            "corresponds to 0.002 mm of indentation depth.",
        ],
        "formula": [
            "HRC = 100 − (depth of indentation in divisions × 0.002 mm)",
            "The hardness is read directly on the dial gauge of the machine.",
        ],
        "procedure": [
            "The specimen surface was cleaned and polished, and the specimen was placed on the anvil.",
            "The diamond cone indenter was brought into contact with the surface and the minor load of 10 kg was applied.",
            "The dial was set to zero and the major load of 150 kg was applied for 10–15 seconds.",
            "The major load was removed and the hardness was read on the C scale of the dial.",
            "Five readings were taken at different points and the mean HRC was calculated.",
        ],
        "observation": {
            "header": ["Reading", "1", "2", "3", "4", "5", "Mean"],
            "rows": [
                ["HRC value", "42", "41", "43", "42", "41", "41.8"],
            ],
            "widths": [1.2, 0.8, 0.8, 0.8, 0.8, 0.8, 0.9],
            "note": "Material: hardened steel; indenter: diamond cone 120°; total load 150 kg (Scale C).",
        },
        "calculation": [
            "Mean HRC = (42 + 41 + 43 + 42 + 41)/5 = <b>41.8</b>",
            "Approximate tensile strength from HRC ≈ 3.5 × HRC = 3.5 × 41.8 ≈ <b>146 kg/mm²</b> (≈ 1435 N/mm²), "
            "which is typical of hardened and tempered steel.",
        ],
        "result": "The Rockwell hardness of the given hardened steel specimen is <b>41.8 HRC</b>, which indicates "
                  "that the material is hard and suitable for tools and machine parts.",
        "precautions": [
            "Test on a smooth, clean surface; roughness gives erroneous readings.",
            "Keep successive indentations at least 3 mm apart and away from the edges.",
            "Apply the minor load first and set the dial to zero before applying the major load.",
            "Clean the indenter and anvil after every test.",
        ],
        "code": "IS: 1586 (Part 2) — 2012, Rockwell hardness test.",
    },
    {
        "num": 11,
        "title": "Preparation of models of different types of trusses",
        "aim": "To prepare models of different types of trusses and to distinguish between them on the basis of "
               "their geometry and member arrangement.",
        "apparatus": [
            "Balsa wood / match sticks / straw, glue, thread, pins",
            "Drawing sheet, scale, protractor, cutting blade, sketch pens",
        ],
        "theory": [
            "A truss is a framework of straight members connected at their ends by pin joints so that the members "
            "carry mainly axial forces. A truss is called perfect if the number of members m and the number of "
            "joints j satisfy m = 2j − 3; if m &lt; 2j − 3 the truss is deficient (unstable), and if m &gt; 2j − 3 "
            "it is redundant.",
            "Common types of trusses are the king post truss (span up to 6 m), the queen post truss (6–9 m), the "
            "howe and pratt trusses, the warren truss, the fink truss and the north-light roof truss. The choice "
            "depends on the span, the load and the material used.",
        ],
        "formula": [
            "Degree of indeterminacy for a plane truss, m = 2j − 3 (perfect truss)",
            "where m = number of members and j = number of joints",
        ],
        "procedure": [
            "The required number of balsa wood pieces was cut to the calculated lengths of the members.",
            "The joints were marked on a drawing sheet and the members were assembled as per the geometry of "
            "the truss.",
            "The joints were glued and pinned and the model was allowed to dry.",
            "Three models — king post, queen post and warren truss — were prepared in the same manner.",
            "For every model, the number of members and joints were counted and the condition m = 2j − 3 was checked.",
            "The models were labelled and compared with sketches.",
        ],
        "observation": {
            "header": ["Type of truss", "Joints (j)", "Members (m)", "2j − 3", "Remarks"],
            "rows": [
                ["King post", "6", "9", "9", "Perfect truss"],
                ["Queen post", "8", "13", "13", "Perfect truss"],
                ["Warren truss", "10", "17", "17", "Perfect truss"],
                ["Deficient truss (without one diagonal)", "6", "8", "9", "Deficient — unstable"],
            ],
            "widths": [2.2, 0.9, 0.9, 0.8, 1.6],
            "note": "Models prepared to a scale of 1:50. Joints were pinned and glued.",
        },
        "calculation": [
            "King post: m = 2 × 6 − 3 = 9; actual members = 9 ✓ (perfect truss)",
            "Queen post: m = 2 × 8 − 3 = 13; actual members = 13 ✓ (perfect truss)",
            "Warren: m = 2 × 10 − 3 = 17; actual members = 17 ✓ (perfect truss)",
            "Model with one member removed: m = 8 &lt; 9, hence the truss becomes deficient and can collapse "
            "under load.",
        ],
        "result": "Models of the king post, queen post and warren trusses were prepared successfully, and all of "
                  "them satisfy the condition m = 2j − 3 for a perfect truss. The model with one member removed was "
                  "found to be deficient, confirming the need for the correct number of members.",
        "precautions": [
            "Cut the members to accurate lengths, otherwise the joints will not close properly.",
            "Keep the joints exactly at the marked points to maintain the geometry of the truss.",
            "Allow sufficient time for the adhesive to set before handling the model.",
            "Handle the models carefully while shifting and displaying them.",
        ],
        "code": "Curriculum — LSO 11 (P2415303); analysis of trusses — method of joints.",
    },
    {
        "num": 12,
        "title": "Shear force and bending moment diagrams for a simply supported beam under point and distributed loads",
        "aim": "To draw the shear force and bending moment diagrams for a simply supported beam carrying a point "
               "load and a uniformly distributed load, and to locate the point of maximum bending moment.",
        "apparatus": [
            "Drawing sheet, scale, pencil, French curves, calculator",
            "Data of the beam: span, loads and positions",
        ],
        "theory": [
            "Shear force at a section is the algebraic sum of all vertical forces on one side of the section, and "
            "bending moment is the algebraic sum of the moments of those forces about the section. The relation "
            "between load, shear force and bending moment is dM/dx = V and dV/dx = w.",
            "For a simply supported beam the bending moment is zero at both ends, and the maximum bending moment "
            "occurs where the shear force changes sign (point of zero shear).",
        ],
        "formula": [
            "Reactions: ΣM<sub>A</sub> = 0 and ΣV = 0",
            "Shear force V<sub>x</sub> = sum of upward forces on the left of the section",
            "Bending moment M<sub>x</sub> = Σ (force × lever arm)",
            "Maximum BM occurs at the section where V = 0",
        ],
        "procedure": [
            "The beam of span 6 m carrying a point load of 10 kN at 2 m from the left support and a UDL of "
            "2 kN/m over the whole span was considered.",
            "The reactions at the supports were calculated using the equations of equilibrium.",
            "Shear force was calculated at every critical section (supports, under the point load and points of "
            "zero shear).",
            "Bending moment was calculated at the same sections.",
            "The shear force and bending moment diagrams were drawn to a suitable scale below the beam sketch.",
        ],
        "observation": {
            "header": ["Section (m from A)", "Shear force (kN)", "Bending moment (kNm)", "Remarks"],
            "rows": [
                ["0 (A)", "+12.67", "0", "Left support"],
                ["2.0 (just left of load)", "+8.67", "+25.33", "Under 10 kN load"],
                ["2.0 (just right of load)", "−1.33", "+25.33", "Sign change"],
                ["2.67", "0", "+25.79", "Maximum BM (V = 0)"],
                ["6.0 (B)", "−9.33", "0", "Right support"],
            ],
            "widths": [1.6, 1.3, 1.5, 1.5],
            "note": "Span 6 m; point load 10 kN at 2 m from A; UDL 2 kN/m over the whole span.",
        },
        "calculation": [
            "Taking moments about A: R<sub>B</sub> × 6 = 10 × 2 + (2 × 6) × 3 = 20 + 36 = 56 → "
            "R<sub>B</sub> = <b>9.33 kN</b>",
            "R<sub>A</sub> = total load − R<sub>B</sub> = (10 + 12) − 9.33 = <b>12.67 kN</b>",
            "SF at A = +12.67 kN; just left of the load = 12.67 − 2 × 2 = +8.67 kN; just right = 8.67 − 10 = −1.33 kN",
            "Point of zero shear: 12.67 − 2x − 10 = 0 → x = <b>1.33 m</b> from the load, i.e. 2.67 m from A",
            "M at 2 m = 12.67 × 2 − 2 × 2²/2 = 25.33 − 4.00 = <b>21.33 kNm</b> (left of load)",
            "M<sub>max</sub> at x = 2.67 m = 12.67 × 2.67 − 2 × 2.67²/2 − 10 × 0.67 = 33.83 − 7.13 − 6.70 = "
            "<b>20.00 kNm</b>",
            "Check: M at B = 12.67 × 6 − 10 × 4 − 2 × 6²/2 = 76.02 − 40 − 36 = 0.02 ≈ <b>0</b> ✓",
        ],
        "result": "The reactions are R<sub>A</sub> = 12.67 kN and R<sub>B</sub> = 9.33 kN. The maximum bending moment "
                  "is <b>20.00 kNm</b> at 2.67 m from the left support, where the shear force changes sign, and the "
                  "bending moment is zero at both ends.",
        "precautions": [
            "Follow a proper sign convention throughout (upward force = positive shear).",
            "Calculate the reactions correctly before drawing the diagrams.",
            "Mark the points of zero shear and maximum bending moment clearly.",
            "Draw the diagrams to a stated scale and label the values at all critical sections.",
        ],
        "code": "Curriculum — LSO 12 (P2415303); B.C. Punmia, Strength of Materials.",
    },
    {
        "num": 13,
        "title": "Determination of principal stresses and their plane using Mohr's circle",
        "aim": "To determine the principal stresses, maximum shear stress and the position of the principal planes "
               "for a given state of stress using Mohr's circle.",
        "apparatus": [
            "Drawing sheet, compass, protractor, scale, pencil, calculator",
            "Given state of stress: σ<sub>x</sub> = 80 N/mm², σ<sub>y</sub> = 20 N/mm², τ = 30 N/mm²",
        ],
        "theory": [
            "At a point in a stressed body there are always two mutually perpendicular planes on which the shear "
            "stress is zero; the normal stresses on these planes are called principal stresses. Their values can be "
            "found analytically or graphically by Mohr's circle.",
            "In Mohr's circle the normal stresses are plotted on the horizontal axis and the shear stresses on the "
            "vertical axis. The circle is drawn with the centre at ((σ<sub>x</sub> + σ<sub>y</sub>)/2, 0) and "
            "radius equal to the maximum shear stress; the points where the circle cuts the horizontal axis give "
            "the principal stresses.",
        ],
        "formula": [
            "Centre of circle, C = (σ<sub>x</sub> + σ<sub>y</sub>) / 2",
            "Radius, R = √[ ((σ<sub>x</sub> − σ<sub>y</sub>)/2)² + τ² ]",
            "σ<sub>1</sub> = C + R ; σ<sub>2</sub> = C − R ; τ<sub>max</sub> = R",
            "tan 2θ = 2τ / (σ<sub>x</sub> − σ<sub>y</sub>)",
        ],
        "procedure": [
            "The given values of σ<sub>x</sub>, σ<sub>y</sub> and τ were noted.",
            "The centre C and radius R of Mohr's circle were calculated.",
            "The circle was drawn to a suitable scale with C as centre on the σ-axis.",
            "The points of intersection of the circle with the σ-axis were marked as σ<sub>1</sub> and σ<sub>2</sub>.",
            "The maximum shear stress was measured as the radius and the angle 2θ was measured from the circle.",
            "The values were compared with those obtained analytically.",
        ],
        "observation": {
            "header": ["Quantity", "Graphical value", "Analytical value", "Unit"],
            "rows": [
                ["Centre of circle", "50.0", "50.0", "N/mm²"],
                ["Radius (τ<sub>max</sub>)", "42.4", "42.43", "N/mm²"],
                ["Major principal stress σ<sub>1</sub>", "92.4", "92.43", "N/mm²"],
                ["Minor principal stress σ<sub>2</sub>", "7.6", "7.57", "N/mm²"],
                ["Angle of principal plane θ", "22.5°", "22.5°", "degree"],
            ],
            "widths": [2.2, 1.3, 1.3, 0.9],
            "note": "Scale: 1 cm = 10 N/mm². σ<sub>x</sub> = 80, σ<sub>y</sub> = 20, τ = 30 N/mm².",
        },
        "calculation": [
            "C = (80 + 20)/2 = <b>50 N/mm²</b>",
            "R = √[ ((80 − 20)/2)² + 30² ] = √(900 + 900) = √1800 = <b>42.43 N/mm²</b>",
            "σ<sub>1</sub> = 50 + 42.43 = <b>92.43 N/mm²</b>; σ<sub>2</sub> = 50 − 42.43 = <b>7.57 N/mm²</b>",
            "τ<sub>max</sub> = R = <b>42.43 N/mm²</b>",
            "tan 2θ = (2 × 30)/(80 − 20) = 60/60 = 1 → 2θ = 45° → θ = <b>22.5°</b>",
        ],
        "result": "For the given state of stress the principal stresses are <b>σ<sub>1</sub> = 92.43 N/mm²</b> and "
                  "<b>σ<sub>2</sub> = 7.57 N/mm²</b>, the maximum shear stress is <b>42.43 N/mm²</b>, and the "
                  "principal planes are inclined at <b>22.5°</b> to the plane of σ<sub>x</sub>. The graphical and "
                  "analytical values agree closely.",
        "precautions": [
            "Choose a suitable scale so that the circle fits on the sheet.",
            "Measure the angles from the correct reference axis (2θ on Mohr's circle).",
            "Plot the shear stress with the correct sign convention.",
            "Verify the graphical results with the analytical formulae.",
        ],
        "code": "Curriculum — LSO 13 (P2415303); R.K. Bansal, Strength of Materials.",
    },
]
