import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for i, row in df.iterrows():
    pdf.add_page()

    pdf.set_font("Arial", size=24, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 12, txt=row["Topic"], ln=True, align='L')

    # lines with for loop
    for z in range(20, 280, 10):
        pdf.line(10, z, 200, z)

    # set the footer
    pdf.ln(265)
    pdf.set_font("Arial", size=8, style='I')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, txt=row["Topic"], align='R')

    for j in range(row["Pages"] - 1):
        pdf.add_page()

        # set the footer
        pdf.ln(275)
        pdf.set_font("Arial", size=8, style='I')
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 10, txt=row["Topic"], align='R')

        for y in range(10, 280, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
