from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 40)
pdf.cell(0, 30, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=10, y=60, w=190)
pdf.set_font("Arial", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 130)
pdf.cell(210, 10, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")