# SBTE Bihar — Diploma Civil Engineering, Semester III
## Practical / Term Work Files (PDF)

Ye folder 3rd semester Civil branch ke **lab practical files** aur **term work file** rakhta hai.
Sabhi files SBTE Bihar curriculum (2024-25, course codes 2415301–2415306) par aadharit hain.

| File | Subject | Code | Pages | Items |
|------|---------|------|-------|-------|
| [03_Basic_Surveying_2415301_Practical_File.pdf](03_Basic_Surveying_2415301_Practical_File.pdf) | Basic Surveying | 2415301 | 16 | 12 practicals |
| [02_Concrete_Technology_2415302_Practical_File.pdf](02_Concrete_Technology_2415302_Practical_File.pdf) | Concrete Technology | 2415302 | 22 | 18 practicals |
| [04_Strength_of_Material_2415303_Practical_File.pdf](04_Strength_of_Material_2415303_Practical_File.pdf) | Strength of Material | 2415303 | 17 | 13 practicals |
| [05_Building_Construction_Material_2415304_Practical_File.pdf](05_Building_Construction_Material_2415304_Practical_File.pdf) | Building Construction & Material | 2415304 | 16 | 12 practicals |
| [01_Water_Resource_Engineering_2415305_Term_Work_File.pdf](01_Water_Resource_Engineering_2415305_Term_Work_File.pdf) | Water Resource Engineering (no lab) | 2415305 | 12 | 8 term-work items |

### Har file mein kya hai
- **Cover page** — student ka naam, enrollment no., session, institute (haath se bharein)
- **Instructions page** — practical likhne ka format aur general instructions
- **Index** — practical number, title, page number, date aur signature ke columns
- **Har practical ek page par** — Aim, Apparatus, Theory, Formulae, Procedure, Observation table,
  Calculation, Result, Precautions, Date + Teacher's signature
- **References page** — textbooks aur IS codes ki list (viva ke liye)

### Zaroori baat
- Observation tables **sample readings** ke saath diye gaye hain, taaki format aur calculation samajh aaye.
  Apne lab mein actual readings le kar hi file final karein.
- Practical ki sankhya college ke lab manual ke anusaar thodi badal sakti hai.
- Surveying file ke saath **A1 size drawing sheet** (traverse plot) alag se jama hoti hai.
- Summer Internship–I (2415306) ki alag report + certificate jama hoti hai.

### Files dobara kaise banayein (regenerate)
```bash
cd pdf
python3 -m venv ../.venv && ../.venv/bin/pip install reportlab   # ek hi baar
for f in build_*.py; do ../.venv/bin/python "$f"; done
```
Content `pdf/content_*.py` mein hai — text edit karke dobara build kar sakte hain.

### Source
- SBTE Bihar official curriculum: `sbte.bihar.gov.in/uploads/Syllabus/2024-25/S03/15. Diploma in Civil Engineering.pdf`
- Subject-wise practical list aur marks split ke liye dekhein: [`../SBTE_Civil_3rd_Sem_Practical_File_List.md`](../SBTE_Civil_3rd_Sem_Practical_File_List.md)
