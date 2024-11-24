from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for i, row in df.iterrows():
    pdf.add_page()

    pdf.set_font("Arial", size=24, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 12, txt=row["Topic"], ln=True, align='L')
    pdf.line(10, 20, 200, 20)

    pdf.ln(265)

    #set the footer
    pdf.set_font("Arial", size=8, style='I')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0,10,txt=row["Topic"], align='R')

    for j in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(278)
        # set the footer
        pdf.set_font("Arial", size=8, style='I')
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 10, txt=row["Topic"], align='R')

pdf.output("output.pdf")