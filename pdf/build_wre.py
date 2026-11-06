import build_pdf
from content_wre import META, ITEMS

if __name__ == "__main__":
    pm = build_pdf.build_generic(META, ITEMS, "../practical-files/01_Water_Resource_Engineering_2415305_Term_Work_File.pdf",
                                 notes=["Is subject mein lab/practical paper nahi hota — total 150 marks (100 theory "
                                        "+ 50 term work) hote hain, isliye assignment, micro project, seminar aur "
                                        "visit report hi jama karne hote hain."])
    print(len(pm), "items; last page:", sorted(pm.values())[-1])
