import build_pdf
from content_surveying import META, PRACTICALS

if __name__ == "__main__":
    pm = build_pdf.build(META, PRACTICALS, "../practical-files/03_Basic_Surveying_2415301_Practical_File.pdf")
    print(pm)
