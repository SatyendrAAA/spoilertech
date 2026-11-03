import build_pdf
from content_bcm import META, PRACTICALS

if __name__ == "__main__":
    pm = build_pdf.build(META, PRACTICALS, "../practical-files/05_Building_Construction_Material_2415304_Practical_File.pdf")
    print(len(pm), "practicals; last page:", sorted(pm.values())[-1])
