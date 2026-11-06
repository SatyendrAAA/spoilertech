import build_pdf
from content_concrete import META, PRACTICALS

if __name__ == "__main__":
    pm = build_pdf.build(META, PRACTICALS, "../practical-files/02_Concrete_Technology_2415302_Practical_File.pdf")
    print(len(pm), "practicals; pages:", sorted(pm.values())[-1])
