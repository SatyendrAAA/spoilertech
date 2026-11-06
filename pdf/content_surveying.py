# -*- coding: utf-8 -*-
"""Content: Basic Surveying (2415301) — 12 practicals."""

META = {
    "title": "Basic Surveying — Laboratory Practical File",
    "subject": "Basic Surveying (CE, AE)",
    "code": "2415301 (P2415301)",
    "footer": "Basic Surveying (2415301)  •  Diploma in Civil Engineering, Semester III  •  SBTE Bihar",
    "index_note": "Practical exam (ELA) mein viva hota hai — har practical ka aim, formula aur result yaad rakhein. "
                  "Page number index mein khud bhar lein (ya teacher ke kehne par).",
    "references": [
        'B.C. Punmia, <i>Surveying</i> Vol. I, Laxmi Publications, New Delhi.',
        'S.K. Duggal, <i>Surveying and Levelling</i>, McGraw Hill Education.',
        'R. Agor, <i>A Text Book of Surveying and Levelling</i>, Khanna Publishers.',
        'SBTE Bihar curriculum for Basic Surveying (2415301 / P2415301) — LSO 1.1 to 12.1.',
        'Operating manual of the digital planimeter used in the laboratory.',
    ],

}

PRACTICALS = [
    {
        "num": 1,
        "title": "Measurement of distance between two inter-visible stations using chain, tape and ranging rods",
        "aim": "To measure the horizontal distance between two inter-visible survey stations A and B with a "
               "20 m chain, a metallic tape and ranging rods, and to compare the two measurements.",
        "apparatus": [
            "20 m metric chain (100 links) with brass handles",
            "30 m metallic tape",
            "Ranging rods (2 m) — 3 nos.",
            "Arrows (pegs) — 10 nos., plumb bob, cross staff, field book and pencil",
        ],
        "theory": [
            "Chaining is the process of measuring the horizontal distance between two points with a chain or tape. "
            "Before chaining, the line AB is made straight by ranging, i.e. by fixing intermediate points exactly in "
            "line with the end stations using ranging rods.",
            "Direct ranging is used when the two stations are inter-visible and the ground is fairly level. The "
            "follower holds the zero end of the chain at A and the leader drags the chain towards B, inserting an "
            "arrow at every chain length. The last portion is measured with the tape or by counting links.",
        ],
        "procedure": [
            "Station A and station B were marked with pegs and ranging rods were fixed vertically at both ends.",
            "Both ranging rods were sighted and intermediate points were fixed at every 20 m so that all points lie in one straight line.",
            "The zero end of the chain was held at A and the chain was stretched along the ranged line; an arrow was fixed at the end of each chain length.",
            "The number of full chain lengths and the remaining links/tape length were recorded in the field book.",
            "The same distance was measured independently with the metallic tape.",
            "The measurement was repeated three times in each case and the mean value was calculated.",
        ],
        "observation": {
            "header": ["Trial No.", "Chain measurement (m)", "Tape measurement (m)", "Difference (m)"],
            "rows": [
                ["1", "24.380", "24.372", "0.008"],
                ["2", "24.365", "24.360", "0.005"],
                ["3", "24.375", "24.368", "0.007"],
                ["Mean", "24.373", "24.367", "0.006"],
            ],
            "widths": [1.0, 1.5, 1.5, 1.3],
            "note": "Average chain length = 20.0 m; average tape temperature ≈ 30 °C. Readings are sample values.",
        },
        "calculation": [
            "Mean chain distance = (24.380 + 24.365 + 24.375) / 3 = <b>24.373 m</b>",
            "Mean tape distance = (24.372 + 24.360 + 24.368) / 3 = <b>24.367 m</b>",
            "Difference = 24.373 − 24.367 = 0.006 m = 6 mm, which is within permissible chaining error "
            "(1 in 1000 for ordinary chaining, i.e. about 24 mm for 24 m).",
        ],
        "result": "The distance between stations A and B is <b>24.37 m</b> (chain) and <b>24.37 m</b> (tape); the "
                  "difference of 6 mm is within permissible limits and the measurement is accepted.",
        "precautions": [
            "The chain must be perfectly straight and free from kinks before use.",
            "Ranging rods should be held truly vertical; check with a plumb bob on sloping ground.",
            "Arrows must be inserted exactly at the chain end and counted at the end of the day.",
            "Care should be taken to apply a uniform pull; dragging the chain over hard surfaces damages it.",
        ],
        "code": "Textbook — B.C. Punmia, Surveying Vol. I; curriculum outcome LSO 1.1 (P2415301).",
    },
    {
        "num": 2,
        "title": "Reciprocal ranging and measurement of distance between two non-inter-visible stations",
        "aim": "To carry out reciprocal ranging between two stations A and B which are not inter-visible due to a "
               "rising ground/hill, and to measure the horizontal distance between them.",
        "apparatus": [
            "Ranging rods — 4 nos.",
            "20 m chain, 30 m tape, arrows, plumb bob, field book",
        ],
        "theory": [
            "When two end stations are not inter-visible because of an intervening obstruction such as a hillock or "
            "a building, direct ranging is not possible. In such a case two intermediate points are selected and "
            "shifted alternately until both lie on the line AB — this is called reciprocal or indirect ranging.",
            "Two chainmen stand at M1 and N1, each sighting the other and the far station. The point nearer to the "
            "line is shifted successively until the four points A, M, N, B are exactly in one line. Thereafter the "
            "distance is measured in two parts AM and MB (or AN and NB).",
        ],
        "procedure": [
            "Ranging rods were fixed at stations A and B and the obstruction was located.",
            "Two points M1 and N1 were selected on either side of the obstruction, roughly in line with AB.",
            "The person at M1 directed the person at N1 to move sideways until N1 appeared in line with M1 and B.",
            "The person at N1 then directed the person at M1 to shift until M1 appeared in line with N1 and A.",
            "The process was repeated until both M and N were exactly on the line AB.",
            "The distance was measured as AM and MB separately with the chain and the total AB was obtained.",
        ],
        "observation": {
            "header": ["Portion measured", "No. of full chains", "Remaining (m)", "Distance (m)"],
            "rows": [
                ["A to M", "0", "15.420", "15.420"],
                ["M to B", "0", "18.235", "18.235"],
                ["Total AB", "—", "—", "33.655"],
            ],
            "widths": [1.4, 1.4, 1.3, 1.3],
            "note": "Readings are sample values; the intermediate point was near the top of the obstruction.",
        },
        "calculation": [
            "AB = AM + MB = 15.420 + 18.235 = <b>33.655 m</b>",
            "Check: repeat measurement in reverse direction = 33.650 m; difference = 0.005 m = 5 mm, "
            "well within the permissible limit of 1 in 1000.",
        ],
        "result": "The distance between the non-inter-visible stations A and B is <b>33.655 m</b> and the points "
                  "A, M, N, B were found to be exactly in one straight line.",
        "precautions": [
            "Ranging rods must be held vertical and exactly on the peg point.",
            "Both chainmen should sight the rods with one eye closed to avoid parallax error.",
            "The shifting should be done in small steps, otherwise the process does not converge.",
            "The chain must not be lifted while dragging over uneven ground.",
        ],
        "code": "Textbook — B.C. Punmia, Surveying Vol. I; curriculum outcome LSO 2.1 (P2415301).",
    },
    {
        "num": 3,
        "title": "Determination of area of an open field by chain and cross-staff survey",
        "aim": "To determine the area of a given open field by measuring a base line and taking offsets with a "
               "cross-staff at regular intervals.",
        "apparatus": [
            "Cross-staff (with optical square), ranging rods, 20 m chain, 30 m tape",
            "Arrows, plumb bob, field book, drawing sheet and scale",
        ],
        "theory": [
            "In chain survey, the area of an irregular field is found by dividing it into triangles and trapezoids. "
            "A base line is run through the field and perpendicular offsets are measured to the boundary at regular "
            "intervals. The area is then computed by the trapezoidal rule or by dividing the figure into triangles.",
            "Trapezoidal rule: A = d [ (O<sub>1</sub> + O<sub>n</sub>)/2 + O<sub>2</sub> + O<sub>3</sub> + ... + "
            "O<sub>n−1</sub> ], where d is the equal interval between offsets and O are the offset lengths.",
        ],
        "formula": [
            "Area (trapezoidal rule) = d × [ (O<sub>1</sub> + O<sub>n</sub>)/2 + Σ (intermediate offsets) ]",
            "Area of a triangle = ½ × base × height",
        ],
        "procedure": [
            "A base line AB was selected through the middle of the field and station pegs were fixed at both ends.",
            "The line was ranged and chained; the total length was found to be 40 m.",
            "Offsets were taken on both sides at intervals of 10 m using a cross-staff, the perpendicularity being checked by the optical square.",
            "The chainage and offset readings were entered in the field book in the tabular form.",
            "The field book was plotted to a suitable scale on a drawing sheet.",
            "The area was calculated by the trapezoidal rule and verified by counting squares/graphically.",
        ],
        "observation": {
            "header": ["Chainage (m)", "Offset to left (m)", "Offset to right (m)", "Mean offset (m)"],
            "rows": [
                ["0 (A)", "0.00", "0.00", "0.00"],
                ["10", "8.00", "6.20", "7.10"],
                ["20", "10.00", "8.40", "9.20"],
                ["30", "6.40", "5.60", "6.00"],
                ["40 (B)", "0.00", "0.00", "0.00"],
            ],
            "widths": [1.2, 1.4, 1.4, 1.3],
            "note": "Interval d = 10 m. Offsets were measured on both sides of the base line.",
        },
        "calculation": [
            "Area on left = 10 × [ (0 + 0)/2 + 8.00 + 10.00 + 6.40 ] = 10 × 24.40 = <b>244.0 m²</b>",
            "Area on right = 10 × [ (0 + 0)/2 + 6.20 + 8.40 + 5.60 ] = 10 × 20.20 = <b>202.0 m²</b>",
            "Total area = 244.0 + 202.0 = <b>446.0 m²</b> = 0.0446 hectare",
            "Check by plotting: area measured with planimeter on the plotted sheet = 4.45 cm² at 1:100 scale "
            "= 445 m², which agrees within 1%.",
        ],
        "result": "The area of the given open field is <b>446 m²</b> (0.0446 hectare).",
        "precautions": [
            "Offsets must be taken exactly perpendicular to the base line; check with optical square.",
            "The base line should be chosen on the longest available line through the field.",
            "Cross-staff must be held vertical and readings taken at eye level.",
            "All measurements should be entered in the field book at the site itself, never from memory.",
        ],
        "code": "Textbook — B.C. Punmia, Surveying Vol. I; curriculum outcome LSO 3.1 (P2415301).",
    },
    {
        "num": 4,
        "title": "Measurement of fore bearing and back bearing of survey lines of an open traverse using prismatic compass",
        "aim": "To measure the fore bearing and back bearing of the lines of an open traverse with a prismatic "
               "compass and to check the difference between them.",
        "apparatus": [
            "Prismatic compass with tripod stand",
            "Ranging rods, tape, pegs, field book, pencil, plumb bob",
        ],
        "theory": [
            "The prismatic compass is a magnetic compass in which the graduated ring is attached to the needle and "
            "rotates with it; the reading is taken through a prism while sighting the object. Bearings are measured "
            "clockwise from the magnetic north.",
            "Fore bearing (FB) is the bearing of a line taken in the direction of the survey; back bearing (BB) is "
            "the bearing taken in the opposite direction. For a line free from local attraction, BB = FB ± 180°. "
            "Any difference from 180° indicates either local attraction or an observational error.",
        ],
        "formula": [
            "BB = FB + 180° (if FB &lt; 180°)   or   BB = FB − 180° (if FB &gt; 180°)",
        ],
        "procedure": [
            "The compass was set up over station A, levelled with the ball and socket arrangement, and the magnetic needle was allowed to settle.",
            "The line AB was sighted through the prism and the fore bearing was read and recorded.",
            "The compass was then taken to station B and the back bearing of AB was measured by sighting A.",
            "In the same manner the compass was shifted to successive stations and FB/BB of each line were recorded.",
            "The difference between FB and BB of every line was worked out and compared with 180°.",
        ],
        "observation": {
            "header": ["Line", "Fore bearing (FB)", "Back bearing (BB)", "Difference (FB − BB)", "Remark"],
            "rows": [
                ["AB", "42°30′", "222°30′", "180°00′", "Correct"],
                ["BC", "96°00′", "275°30′", "179°30′", "Error 30′"],
                ["CD", "152°15′", "332°15′", "180°00′", "Correct"],
                ["DE", "236°45′", "56°45′", "180°00′", "Correct"],
            ],
            "widths": [0.7, 1.2, 1.2, 1.2, 1.1],
            "note": "Readings are sample values. Line BC shows a discrepancy of 30′, which indicates local attraction at station B or C.",
        },
        "calculation": [
            "For line AB: FB = 42°30′, BB should be 42°30′ + 180° = 222°30′ — observed 222°30′, hence no local attraction.",
            "For line BC: FB = 96°00′, expected BB = 276°00′, observed 275°30′ — discrepancy of 30′.",
            "For line CD: FB = 152°15′, expected BB = 332°15′ — correct.",
            "For line DE: FB = 236°45′, expected BB = 56°45′ — correct.",
            "Since three lines are correct, the error of 30′ is due to local attraction at station B (or C); "
            "all bearings taken at that station should be corrected by ±30′.",
        ],
        "result": "The fore and back bearings of all the lines of the open traverse were measured. Lines AB, CD and DE "
                  "are free from local attraction; line BC shows a difference of 30′, which is attributed to local "
                  "attraction near station B.",
        "precautions": [
            "Remove metal objects such as watch, keys, chain and steel tape from near the compass.",
            "Do not take readings under overhead electric lines or near magnetic material.",
            "Always read the bearing with the object exactly bisected by the vertical hair.",
            "Note the local time and date; the magnetic declination must be applied if true bearings are required.",
        ],
        "code": "Textbook — B.C. Punmia, Surveying Vol. I; curriculum outcome LSO 4.1 (P2415301).",
    },
    {
        "num": 5,
        "title": "Closed traverse of five sides by prismatic compass — correction of bearings for local attraction and calculation of included angles",
        "aim": "To measure the fore and back bearings of a closed traverse of five sides, to correct the bearings "
               "for local attraction, and to compute the included angles and check their sum.",
        "apparatus": [
            "Prismatic compass with tripod",
            "Ranging rods, tape, pegs (5 nos.), field book, protractor and drawing sheet",
        ],
        "theory": [
            "In a closed traverse the difference between the fore and back bearing of every line must be exactly "
            "180°. If for any line it is not 180°, one or both of its stations are affected by local attraction. "
            "Lines whose FB and BB differ by exactly 180° are free from local attraction, and corrections for the "
            "remaining stations are worked out from these lines. The included angle at a station is the back "
            "bearing of the preceding line minus the fore bearing of the next line, and the sum of the interior "
            "angles of an n-sided closed traverse is (2n − 4) × 90°, i.e. 540° for a pentagon.",
        ],
        "formula": [
            "BB = FB ± 180°",
            "Interior angle at station = BB (previous line) − FB (next line) [+ 360° if negative]",
            "Σ interior angles = (2n − 4) × 90° = 540° for n = 5",
        ],
        "procedure": [
            "Five stations A, B, C, D and E were fixed forming a closed traverse around the given area and pegs were driven.",
            "The compass was set at station A and the bearing of AB was measured as FB, then at B the BB of AB was measured.",
            "The instrument was shifted successively to C, D and E and the FB and BB of every line were observed.",
            "The differences between FB and BB were computed to identify the station affected by local attraction.",
            "Corrections were applied to the bearings observed at the affected station.",
            "The included angles were calculated from the corrected bearings and their sum was checked against 540°.",
        ],
        "observation": {
            "header": ["Line", "Observed FB", "Observed BB", "FB − BB", "Correct FB", "Correct BB"],
            "rows": [
                ["AB", "60°00′", "240°00′", "180°00′", "60°00′", "240°00′"],
                ["BC", "132°00′", "312°00′", "180°00′", "132°00′", "312°00′"],
                ["CD", "204°00′", "26°00′", "178°00′", "204°00′", "24°00′"],
                ["DE", "278°00′", "96°00′", "182°00′", "276°00′", "96°00′"],
                ["EA", "348°00′", "168°00′", "180°00′", "348°00′", "168°00′"],
            ],
            "widths": [0.7, 1.1, 1.1, 1.0, 1.0, 1.0],
            "note": "Lines AB, BC and EA show a difference of exactly 180°, hence stations A, B, C and E are free from "
                    "local attraction. Station D is affected by +2°, so all bearings observed at D are reduced by 2°.",
        },
        "calculation": [
            "Correction at D = −2°; corrected BB of CD = 26°00′ − 2° = 24°00′ and corrected FB of DE = 278°00′ − 2° = 276°00′.",
            "Angle A = BB of EA − FB of AB = 168° − 60° = <b>108°</b>",
            "Angle B = BB of AB − FB of BC = 240° − 132° = <b>108°</b>",
            "Angle C = BB of BC − FB of CD = 312° − 204° = <b>108°</b>",
            "Angle D = BB of CD − FB of DE = 24° + 360° − 276° = <b>108°</b>",
            "Angle E = BB of DE − FB of EA = 96° + 360° − 348° = <b>108°</b>",
            "Sum = 108° × 5 = <b>540°</b> = (2 × 5 − 4) × 90° — hence the traverse is closed and the corrections are correct.",
        ],
        "result": "The local attraction was found only at station D (+2°) and was corrected. The included angles are "
                  "A = B = C = D = E = 108°, and their sum is 540°, which is equal to the theoretical value for a "
                  "five-sided closed traverse.",
        "precautions": [
            "Keep the compass away from iron and steel objects, mobile phones and magnetic material.",
            "The same instrument and observer should be used throughout the traverse.",
            "Read bearings to the nearest 30′ or better, and take two readings at each station.",
            "Check the closure of the traverse before leaving the field so that any gross error can be re-measured.",
        ],
        "code": "Textbook — B.C. Punmia, Surveying Vol. I; curriculum outcome LSO 5.1 (P2415301).",
    },
    {
        "num": 6,
        "title": "Survey project — chain and compass closed traverse around a building (minimum five sides)",
        "aim": "To carry out a chain and compass survey of a closed traverse of five sides around a building and to "
               "prepare the field book for plotting.",
        "apparatus": [
            "Prismatic compass, 20 m chain, 30 m tape, ranging rods",
            "Pegs, arrows, plumb bob, field book, chalk for marking",
        ],
        "theory": [
            "A survey project combines linear (chain) and angular (compass) measurements to fix the position of "
            "points around an obstruction such as a building. The traverse is run around the building, keeping all "
            "lines clear of the structure, and each line is measured in length as well as bearing.",
            "For plotting, the length and bearing of each line are converted into latitude and departure: "
            "Latitude = L cos θ and Departure = L sin θ, where θ is the reduced bearing. The algebraic sums of "
            "latitudes and departures should be zero for a closed traverse; the residual is the closing error, "
            "which is distributed by Bowditch's rule.",
        ],
        "formula": [
            "Latitude = L cos θ ; Departure = L sin θ",
            "Closing error = √( (ΣL)² + (ΣD)² )",
            "Correction in latitude/departure = total error × (length of line / perimeter)",
        ],
        "procedure": [
            "The building was inspected and five traverse stations A, B, C, D and E were fixed around it, clear of the walls.",
            "The compass was set up at A, levelled and centred, and the bearing of AB was observed. The line AB was then chained.",
            "The instrument was shifted to B and the FB of BC together with the BB of AB was recorded; the line BC was measured.",
            "The process was repeated for lines CD, DE and EA and all readings were entered in the field book.",
            "The FB–BB differences were checked in the field and any line showing a large discrepancy was re-measured.",
            "The traverse was plotted on a drawing sheet to a scale of 1:200 and the closing error was adjusted graphically.",
        ],
        "observation": {
            "header": ["Line", "Length (m)", "FB", "BB", "Difference"],
            "rows": [
                ["AB", "24.30", "30°00′", "210°00′", "180°00′"],
                ["BC", "18.55", "118°00′", "298°00′", "180°00′"],
                ["CD", "27.10", "196°30′", "16°30′", "180°00′"],
                ["DE", "16.40", "264°00′", "84°00′", "180°00′"],
                ["EA", "21.25", "330°30′", "150°30′", "180°00′"],
            ],
            "widths": [0.7, 1.2, 1.2, 1.2, 1.2],
            "note": "Perimeter = 24.30 + 18.55 + 27.10 + 16.40 + 21.25 = 107.60 m. Readings are sample values.",
        },
        "calculation": [
            "Perimeter of the traverse = <b>107.60 m</b>",
            "Plotting scale selected: 1:200, so that the longest side (27.10 m) occupies 135.5 mm on an A1 sheet.",
            "Sum of observed interior angles = 540°00′ (check with the theoretical value), hence no angular error.",
            "Closing error obtained after plotting = 0.06 m in 107.60 m, i.e. about 1 in 1790, which is within "
            "the permissible limit of 1 in 1000 for a compass traverse.",
            "The closing error was distributed by Bowditch's rule and the traverse was redrawn.",
        ],
        "result": "The chain and compass traverse of five sides around the building was completed with a perimeter of "
                  "<b>107.60 m</b>; the closing error was 0.06 m (1 in 1790), which is within permissible limits, and "
                  "the corrected traverse was plotted to a scale of 1:200.",
        "precautions": [
            "Keep the traverse lines clear of the building and of iron grills or gates that cause local attraction.",
            "Measure each line twice — forward and backward — and record the mean.",
            "Fix the stations permanently so that they can be re-occupied if required.",
            "Plot the traverse the same day while the field book is fresh.",
        ],
        "code": "Curriculum — Survey Project, LSO 6.1 (P2415301); B.C. Punmia, Surveying Vol. I.",
    },
    {
        "num": 7,
        "title": "Plotting of the chain and compass traverse on an A1 size imperial drawing sheet",
        "aim": "To plot the traverse data collected in Practical No. 6 on an A1 size imperial drawing sheet to a "
               "suitable scale and to adjust the closing error.",
        "apparatus": [
            "A1 size imperial drawing sheet, drawing board, T-square, set squares",
            "Protractor, scale (engineer's), drawing pins, sharp pencil, eraser, tracing paper",
        ],
        "theory": [
            "Plotting is the graphical representation of the field data. The scale is chosen so that the whole "
            "traverse fits on the sheet with a margin: RF = length of drawing / length on ground. For a site of "
            "about 100 m on an A1 sheet (594 × 841 mm), a scale of 1:200 is convenient.",
            "Each line is drawn with the help of its bearing (measured with a protractor from the magnetic meridian) "
            "and its length (scaled from the engineer's scale). A closing error, if any, is adjusted by shifting the "
            "plotted stations proportionally — graphically, this is done by drawing a closing line and dividing the "
            "error in proportion to the perimeter.",
        ],
        "formula": [
            "Representative fraction, RF = distance on paper / distance on ground",
            "Scale for the sheet: Scale = drawing length / ground length",
        ],
        "procedure": [
            "The drawing sheet was fixed on the board and a border with a title block was drawn.",
            "A north line was drawn at station A and the magnetic meridian was marked with the help of the protractor.",
            "The bearing of AB was set out from the meridian and the length was scaled; point B was marked.",
            "The same procedure was repeated for BC, CD, DE and EA using a parallel ruler/protractor at each station.",
            "The end of the last line (A′) was compared with the starting point A and the closing error AA′ was measured.",
            "The closing error was distributed in proportion to the length of the lines and the corrected traverse was inked.",
            "The building outline, north arrow, scale, title and legend were added to complete the sheet.",
        ],
        "observation": {
            "header": ["Line", "Ground length (m)", "Scale 1:200 (mm)", "Bearing", "Remarks"],
            "rows": [
                ["AB", "24.30", "121.5", "30°00′", "Plotted"],
                ["BC", "18.55", "92.8", "118°00′", "Plotted"],
                ["CD", "27.10", "135.5", "196°30′", "Plotted"],
                ["DE", "16.40", "82.0", "264°00′", "Plotted"],
                ["EA", "21.25", "106.3", "330°30′", "Plotted"],
            ],
            "widths": [0.7, 1.3, 1.3, 1.1, 1.0],
            "note": "A1 imperial sheet = 594 mm × 841 mm. Title block shows name, roll number, scale and date.",
        },
        "calculation": [
            "RF = 1:200, hence 1 m on ground = 5 mm on paper.",
            "AB = 24.30 m × 5 = 121.5 mm; BC = 18.55 × 5 = 92.8 mm; CD = 27.10 × 5 = 135.5 mm;",
            "DE = 16.40 × 5 = 82.0 mm; EA = 21.25 × 5 = 106.3 mm.",
            "Closing error AA′ measured on the sheet = 0.3 mm, i.e. 0.06 m on ground — within permissible limit.",
        ],
        "result": "The traverse was plotted to a scale of 1:200 on an A1 size imperial sheet; the closing error was "
                  "0.06 m on ground (0.3 mm on the sheet) and was adjusted. The completed sheet shows the building "
                  "outline, north line, scale and title block.",
        "precautions": [
            "Use a sharp HB pencil for plotting and a 2H pencil for construction lines.",
            "Set every bearing from the north line at each station, not from the previous line.",
            "Keep the protractor centred exactly on the station point to avoid angular error.",
            "Do not fold the A1 sheet; roll it and submit it in a tube.",
        ],
        "code": "Curriculum — LSO 7.1 (P2415301); B.C. Punmia, Surveying Vol. I.",
    },
    {
        "num": 8,
        "title": "Simple levelling with dumpy level / auto level to determine reduced levels of given points",
        "aim": "To determine the reduced levels (RL) of a few given points with respect to a bench mark using a "
               "dumpy level (or auto level) and a levelling staff by simple levelling.",
        "apparatus": [
            "Dumpy level / auto level with tripod",
            "Levelling staff (self-reading, 4 m)",
            "Pegs, arrows, field book, umbrella",
        ],
        "theory": [
            "Levelling is the operation of finding the relative elevations of points on or below the surface of the "
            "earth. The level establishes a horizontal line of collimation, and the staff readings taken on it give "
            "the vertical distances of the points from that line.",
            "Simple levelling is used when the instrument can be set up between two points without any change of "
            "station: RL of the new point = HI − staff reading, where HI (height of instrument) = RL of bench mark + "
            "back sight.",
        ],
        "formula": [
            "Height of instrument, HI = RL of BM + Back sight (BS)",
            "RL of any point = HI − staff reading at that point",
        ],
        "procedure": [
            "The level was set up roughly midway between the bench mark and the points to be levelled and levelled with the foot screws.",
            "The temporary adjustments — setting, levelling and focusing — were carried out.",
            "A back sight was taken on the bench mark of known RL and recorded.",
            "Intermediate sights were taken on points P, Q and R by turning the telescope only in the horizontal plane.",
            "The HI was computed and the RL of every point was calculated.",
            "The arithmetic check (ΣBS − ΣFS = last RL − first RL) was applied.",
        ],
        "observation": {
            "header": ["Station", "Staff reading (m)", "Type of sight", "HI (m)", "RL (m)", "Remarks"],
            "rows": [
                ["BM", "1.455", "BS", "101.455", "100.000", "Bench mark"],
                ["P", "1.720", "IS", "101.455", "99.735", ""],
                ["Q", "2.105", "IS", "101.455", "99.350", "Lowest point"],
                ["R", "1.980", "IS", "101.455", "99.475", ""],
            ],
            "widths": [0.8, 1.3, 1.1, 1.0, 1.0, 1.2],
            "note": "RL of bench mark = 100.000 m (assumed). Readings are sample values.",
        },
        "calculation": [
            "HI = RL of BM + BS = 100.000 + 1.455 = <b>101.455 m</b>",
            "RL of P = 101.455 − 1.720 = <b>99.735 m</b>",
            "RL of Q = 101.455 − 2.105 = <b>99.350 m</b>",
            "RL of R = 101.455 − 1.980 = <b>99.475 m</b>",
            "Check: ΣBS − ΣFS = 1.455 − 0 = 1.455; last RL − first RL cannot be applied for IS readings, hence "
            "the HI is verified by comparing the difference of RLs with the difference of staff readings "
            "(2.105 − 1.455 = 0.650 = 100.000 − 99.350 ✓).",
        ],
        "result": "The reduced levels are: P = <b>99.735 m</b>, Q = <b>99.350 m</b>, R = <b>99.475 m</b> with respect "
                  "to the bench mark of RL 100.000 m. Point Q is the lowest point of the area.",
        "precautions": [
            "The level must be set up on firm ground and the tripod legs pressed down well.",
            "Always take the back sight first and the fore sight last at every setting.",
            "Keep the staff truly vertical; use a bubble in the staff or wave it slightly to get the minimum reading.",
            "Protect the instrument from direct sun with an umbrella to avoid expansion errors.",
        ],
        "code": "Textbook — B.C. Punmia, Surveying Vol. I; curriculum outcome LSO 8.1 (P2415301).",
    },
    {
        "num": 9,
        "title": "Differential levelling — determination of reduced levels by Height of Instrument and Rise and Fall methods",
        "aim": "To determine the reduced levels of points along a profile by differential levelling and to reduce "
               "the levels by (i) the Height of Instrument method and (ii) the Rise and Fall method.",
        "apparatus": [
            "Dumpy level / auto level with tripod, levelling staff",
            "Pegs, arrows, field book, pencil, umbrella",
        ],
        "theory": [
            "Differential levelling is used when the points are far apart or the difference of level is large, so "
            "that the instrument has to be shifted several times; the point on which both a fore sight and a back "
            "sight are taken is called a change point. In the HI method the RL is obtained by subtracting the staff "
            "reading from the height of instrument, while in the Rise and Fall method the rise or fall between "
            "successive readings is added to or subtracted from the previous RL.",
        ],
        "formula": [
            "HI = RL + BS ; RL = HI − IS or FS",
            "Rise = previous reading − next reading (positive) ; Fall = next reading − previous reading (positive)",
            "Arithmetic check: ΣBS − ΣFS = ΣRise − ΣFall = last RL − first RL",
        ],
        "procedure": [
            "The level was set up at a convenient position and the first back sight was taken on the bench mark.",
            "Intermediate and fore sights were taken on the points in the line; the fore sight point was used as a change point.",
            "The instrument was shifted beyond the change point and a new back sight was taken on the same point.",
            "The process was repeated until the last point was reached.",
            "The RLs were computed first by the HI method and then independently by the Rise and Fall method.",
            "The arithmetic checks were applied to both methods and the results were compared.",
        ],
        "observation": {
            "header": ["Station", "BS (m)", "IS (m)", "FS (m)", "HI (m)", "RL (m)", "Remarks"],
            "rows": [
                ["BM", "1.560", "—", "—", "101.560", "100.000", "Bench mark"],
                ["A", "—", "1.230", "—", "101.560", "100.330", ""],
                ["CP1", "1.860", "—", "2.150", "101.270", "99.410", "Change point"],
                ["B", "—", "1.410", "—", "101.270", "99.860", ""],
                ["CP2", "2.010", "—", "2.340", "100.940", "98.930", "Change point"],
                ["C", "—", "—", "1.480", "100.940", "99.460", "Last point"],
            ],
            "widths": [0.8, 0.85, 0.8, 0.8, 0.95, 0.95, 1.2],
            "note": "ΣBS = 5.430 m, ΣFS = 5.970 m. Readings are sample values.",
        },
        "calculation": [
            "HI<sub>1</sub> = 100.000 + 1.560 = 101.560 m; RL of A = 101.560 − 1.230 = <b>100.330 m</b>; "
            "RL of CP1 = 101.560 − 2.150 = <b>99.410 m</b>",
            "HI<sub>2</sub> = 99.410 + 1.860 = 101.270 m; RL of B = 101.270 − 1.410 = <b>99.860 m</b>; "
            "RL of CP2 = 101.270 − 2.340 = <b>98.930 m</b>",
            "HI<sub>3</sub> = 98.930 + 2.010 = 100.940 m; RL of C = 100.940 − 1.480 = <b>99.460 m</b>",
            "Check: ΣBS − ΣFS = 5.430 − 5.970 = −0.540 m; last RL − first RL = 99.460 − 100.000 = −0.540 m ✓",
            "<b>By Rise and Fall method:</b> BM → A rise 0.330 (100.330); A → CP1 fall 0.920 (99.410); "
            "CP1 → B rise 0.450 (99.860); B → CP2 fall 0.930 (98.930); CP2 → C rise 0.530 (99.460).",
            "Check: ΣRise − ΣFall = (0.330 + 0.450 + 0.530) − (0.920 + 0.930) = 1.310 − 1.850 = −0.540 m ✓ "
            "— the same as ΣBS − ΣFS.",
        ],
        "result": "The reduced levels obtained are A = 100.330 m, CP1 = 99.410 m, B = 99.860 m, CP2 = 98.930 m and "
                  "C = 99.460 m. Both reduction methods give identical results and the arithmetic checks are satisfied.",
        "precautions": [
            "A change point must be a firm, permanent object; the staff must not be lifted from it between the two settings.",
            "Take the fore sight and the next back sight on the same point before shifting the instrument.",
            "Avoid very long sights and keep the backsight and foresight distances nearly equal.",
            "Enter readings in the field book immediately and never rub out a wrong entry — strike it out and rewrite.",
        ],
        "code": "Textbook — B.C. Punmia, Surveying Vol. I; curriculum outcome LSO 9.1 (P2415301).",
    },
    {
        "num": 10,
        "title": "Fly levelling with double check using dumpy level / auto level",
        "aim": "To carry out fly levelling from a bench mark to a distant point and to check the accuracy by "
               "levelling back to the starting bench mark (double check).",
        "apparatus": [
            "Dumpy level / auto level with tripod, levelling staff",
            "Pegs, arrows, field book, umbrella, measuring tape",
        ],
        "theory": [
            "Fly levelling is a quick method of differential levelling used to connect a distant point to a bench "
            "mark; intermediate sights are avoided and only back sights and fore sights are taken. Since the "
            "instrument is shifted many times, the total error accumulates, and it is therefore checked by running "
            "the levelling back to the same bench mark.",
            "The difference between the forward and backward differences of level is the closing error (misclosure). "
            "The permissible closing error for ordinary levelling is about ±5√K mm, where K is the distance in km.",
        ],
        "formula": [
            "Difference of level = ΣBS − ΣFS",
            "Closing error = (forward difference of level) − (backward difference of level)",
            "Permissible error = ± 5 √K mm (K in km)",
        ],
        "procedure": [
            "The level was set up near the bench mark and a back sight was taken.",
            "The instrument was shifted forward and a fore sight was taken on a firm point before shifting, which became the new back sight.",
            "Only back sights and fore sights were taken until the destination point was reached, and the forward difference of level was computed.",
            "The levelling was then repeated in the reverse direction from the destination back to the bench mark.",
            "The backward difference of level was computed and compared with the forward value.",
            "The closing error was worked out and compared with the permissible limit.",
        ],
        "observation": {
            "header": ["Leg of run", "ΣBS (m)", "ΣFS (m)", "Difference of level (m)", "Remarks"],
            "rows": [
                ["Forward run (BM → P)", "8.465", "9.710", "−1.245", "Fall of 1.245 m"],
                ["Backward run (P → BM)", "9.706", "8.461", "+1.245", "Rise of 1.245 m"],
                ["Mean", "—", "—", "−1.245", "Accepted value"],
            ],
            "widths": [1.6, 1.1, 1.1, 1.5, 1.4],
            "note": "Total length of the run = 0.60 km. Readings are sample values.",
        },
        "calculation": [
            "Forward run: 8.465 − 9.710 = <b>−1.245 m</b> (point P is 1.245 m below the bench mark).",
            "Backward run: 9.706 − 8.461 = <b>+1.245 m</b> (BM is 1.245 m above P).",
            "Misclosure = 1.245 − 1.245 = <b>0.000 m</b> (in the sample data); for field data a small misclosure of "
            "3–5 mm is normal.",
            "Permissible error = ±5√0.60 = ±3.9 mm ≈ <b>±4 mm</b>. A misclosure within this value is acceptable.",
        ],
        "result": "Fly levelling was completed over a run of 0.60 km. The difference of level between the bench mark "
                  "and point P is <b>1.245 m</b> (P below BM) and the closing error is within the permissible limit "
                  "of ±4 mm, hence the work is accepted.",
        "precautions": [
            "Keep the lengths of back sight and fore sight nearly equal at each setting to cancel collimation error.",
            "Never take an intermediate sight in fly levelling; only BS and FS are recorded.",
            "Use a firm and stable change point and take the reading without lifting the staff.",
            "Complete both forward and backward runs on the same day under similar atmospheric conditions.",
        ],
        "code": "Textbook — B.C. Punmia, Surveying Vol. I; curriculum outcome LSO 10.1 (P2415301).",
    },
    {
        "num": 11,
        "title": "Survey project — contour map of a 150 m × 150 m block by block contouring (grid 10 m × 10 m)",
        "aim": "To prepare a contour map of a given 150 m × 150 m block by the block (grid) contouring method using "
               "a 10 m × 10 m grid and a dumpy level/auto level.",
        "apparatus": [
            "Auto level / dumpy level with tripod, levelling staff",
            "30 m tape, ranging rods, pegs (16 × 16 grid), field book, drawing sheet, french curves",
        ],
        "theory": [
            "A contour is an imaginary line joining points of equal elevation. In the indirect (block) method the "
            "area is divided into squares by a grid, the RL of every grid point is obtained by levelling, and the "
            "contours are then interpolated between the grid points.",
            "Interpolation is done on the assumption that the ground slope between two adjacent grid points is "
            "uniform: distance of a contour point from a grid point = (contour value − RL of that point) / "
            "(difference of RL between the two points) × grid interval.",
        ],
        "formula": [
            "x = (h<sub>c</sub> − h<sub>1</sub>) / (h<sub>2</sub> − h<sub>1</sub>) × d",
            "where x = distance of the contour point from grid point 1, h<sub>c</sub> = contour RL, "
            "h<sub>1</sub>, h<sub>2</sub> = RLs of adjacent grid points, d = grid interval (10 m)",
        ],
        "procedure": [
            "The 150 m × 150 m block was divided into a 10 m × 10 m grid (16 lines each way) and pegs were fixed at every node.",
            "The level was set up at a central position and the RL of the first node was obtained by a back sight on a bench mark.",
            "The RLs of all grid points were obtained by taking staff readings, shifting the instrument whenever necessary.",
            "The grid RLs were entered in a block-level table and the contour interval was selected as 0.50 m.",
            "Contour points on the grid lines were interpolated and joined by smooth curves.",
            "The contour map was inked with the index contours thickened, and a north arrow, scale and legend were added.",
        ],
        "observation": {
            "header": ["Grid line (Northing)", "0 m", "10 m", "20 m", "30 m"],
            "rows": [
                ["0 m", "100.20", "100.35", "100.50", "100.70"],
                ["10 m", "100.30", "100.45", "100.62", "100.85"],
                ["20 m", "100.42", "100.58", "100.76", "101.00"],
                ["30 m", "100.55", "100.72", "100.90", "101.15"],
            ],
            "widths": [1.5, 1.0, 1.0, 1.0, 1.0],
            "note": "Sample block-level table (part of the 16 × 16 grid). Contour interval = 0.50 m.",
        },
        "calculation": [
            "Take grid points (10 m, 0 m) with RL 100.35 and (20 m, 0 m) with RL 100.50. For the 100.50 m contour:",
            "x = (100.50 − 100.35) / (100.50 − 100.35) × 10 = <b>10.00 m</b>, i.e. the contour passes through the "
            "grid point (20 m, 0 m).",
            "For grid points (0 m, 10 m) RL 100.30 and (10 m, 10 m) RL 100.45, the 100.40 m contour lies at "
            "x = (100.40 − 100.30)/(100.45 − 100.30) × 10 = <b>6.67 m</b> from the first point.",
            "The slopes obtained from the grid show a general rise towards the north-east, with a maximum RL of "
            "101.15 m at (30 m, 30 m) and a minimum of 100.20 m at the origin.",
        ],
        "result": "A contour map of the 150 m × 150 m block was prepared with a contour interval of 0.50 m. The ground "
                  "rises uniformly from the south-west corner (RL 100.20 m) towards the north-east, and the contours "
                  "are nearly parallel and evenly spaced, indicating a uniform gentle slope.",
        "precautions": [
            "The grid must be set out accurately with the tape; errors in the grid shift all contours.",
            "Take readings quickly to minimise changes in the level due to temperature.",
            "Interpolate contours only between adjacent grid points and never across a break in the slope.",
            "Draw contours as smooth flowing curves — they should never cross each other or branch.",
        ],
        "code": "Curriculum — LSO 11.1 (P2415301); B.C. Punmia, Surveying Vol. I.",
    },
    {
        "num": 12,
        "title": "Measurement of area of an irregular figure using a digital planimeter",
        "aim": "To measure the area of a given irregular figure (map/plan) with a digital planimeter and to convert "
               "it to the actual ground area using the map scale.",
        "apparatus": [
            "Digital planimeter with tracer arm and roller",
            "Given map/plan, drawing sheet fixed on a smooth board, pencil, scale",
        ],
        "theory": [
            "A planimeter is a mechanical/digital integrating instrument used to measure the area of an irregular "
            "figure directly by tracing its boundary. When the tracer point is moved along the outline, the "
            "measuring wheel (or the digital counter) records the area in terms of an instrument constant.",
            "Area = C × (final reading − initial reading) × M, where C is the planimeter constant (value of one unit "
            "of the counter) and M is the map multiplier, M = (scale of map)².",
        ],
        "formula": [
            "Area on map = C × (F.R. − I.R.)",
            "Actual area = Area on map × M, where M = (denominator of RF)²",
        ],
        "procedure": [
            "The plan was fixed flat on a smooth drawing board and the planimeter was placed near the figure.",
            "The tracer point was set on a convenient starting point on the boundary and the initial reading was noted.",
            "The tracer point was moved slowly and steadily along the boundary in a clockwise direction until it returned to the starting point.",
            "The final reading was noted; the operation was repeated three times and the mean was taken.",
            "The area on the map was computed as C × (F.R. − I.R.) and converted to the actual area using the map scale.",
            "The result was verified by measuring the area of a known circle/square.",
        ],
        "observation": {
            "header": ["Trial", "Initial reading (I.R.)", "Final reading (F.R.)", "Difference", "Area on map (cm²)"],
            "rows": [
                ["1", "2.436", "8.452", "6.016", "60.16"],
                ["2", "2.438", "8.449", "6.011", "60.11"],
                ["3", "2.441", "8.455", "6.014", "60.14"],
                ["Mean", "—", "—", "6.014", "60.14"],
            ],
            "widths": [0.8, 1.3, 1.3, 1.0, 1.3],
            "note": "Planimeter constant C = 10 cm² per unit reading; map scale 1:100.",
        },
        "calculation": [
            "Mean difference = (6.016 + 6.011 + 6.014) / 3 = 6.014",
            "Area on map = C × (F.R. − I.R.) = 10 × 6.014 = <b>60.14 cm²</b>",
            "Map scale = 1:100, hence M = (100)² = 10,000 and 1 cm² on map = 1 m² on ground",
            "Actual area = 60.14 × 1 = <b>60.14 m²</b>",
            "Check: the known 50 m² plot gave a reading of 5.002 units → 50.02 m² (error 0.04%), hence the "
            "instrument constant is correct.",
        ],
        "result": "The area of the given irregular figure is <b>60.14 cm²</b> on the map, which corresponds to an "
                  "actual area of <b>60.14 m²</b> at a map scale of 1:100.",
        "precautions": [
            "Fix the map firmly so that it does not shift while tracing.",
            "Move the tracer point slowly and exactly along the boundary; do not lift it during the run.",
            "Set the starting point on a straight portion of the boundary for better repeatability.",
            "Always check the planimeter against a known area before taking readings.",
        ],
        "code": "Curriculum — LSO 12.1 (P2415301); digital planimeter operating manual.",
    },
]
