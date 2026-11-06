import build_pdf
from content_som import META, PRACTICALS

if __name__ == "__main__":
    pm = build_pdf.build(META, PRACTICALS, "../practical-files/04_Strength_of_Material_2415303_Practical_File.pdf")
    print(len(pm), "practicals; last page:", sorted(pm.values())[-1])
