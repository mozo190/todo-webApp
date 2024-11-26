import glob
from pathlib import Path

import pandas as pd
from fpdf import FPDF

for file in glob.glob("invoices/*.xlsx"):
    df = pd.read_excel(file, engine='openpyxl')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()

    filename = Path(file).stem
    invoice_nr = filename.split("-")[0]
    invoice_date = filename.split("-")[1]

    pdf.set_font("Arial", size=16, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(100, 12, txt=f"Invoice nr. {invoice_nr}", ln=True, align='L')
    pdf.cell(0, 12, txt=f"Date: {invoice_date}", ln=True, align='L')

    columns = list(df.columns)
    columns = [column.replace("_", " ").title() for column in columns]
    pdf.set_font("Times", size=12, style='B')
    pdf.cell(25, 10, txt=columns[0], border=1, align='L')
    pdf.cell(45, 10, txt=columns[1], border=1, align='L')
    pdf.cell(45, 10, txt=columns[2], border=1, align='L')
    pdf.cell(35, 10, txt=columns[3], border=1, align='L')
    pdf.cell(40, 10, txt=columns[4], border=1, align='L')
    pdf.ln()

    for i, row in df.iterrows():
        pdf.set_font("Times", size=10)
        pdf.cell(25, 10, txt=str(row["product_id"]), border=1, align='L')
        pdf.cell(45, 10, txt=str(row["product_name"]), border=1, align='L')
        pdf.cell(45, 10, txt=str(row["amount_purchased"]), border=1, align='C')
        pdf.cell(35, 10, txt=str(row["price_per_unit"]), border=1, align='C')
        pdf.cell(40, 10, txt=str(row["total_price"]), border=1, align='C')
        pdf.ln()

    big_total = df["total_price"].sum()

    pdf.set_font("Times", size=10, style='B')
    pdf.cell(25, 10, txt="", border=1)
    pdf.cell(45, 10, txt="", border=1)
    pdf.cell(45, 10, txt="", border=1)
    pdf.cell(35, 10, txt="", border=1)
    pdf.cell(40, 10, txt=str(f"{big_total}"), border=1, align='C')
    pdf.ln()
    pdf.ln()

    pdf.cell(0, 10, txt=f"The total due amount is {big_total} Euros.", border=0, align='R')
    pdf.ln()
    pdf.image("py.png", x=pdf.get_x() + 75, y=pdf.get_y(), w=6)
    pdf.cell(0, 10, txt=f"Please transfer the amount to the following bank account: 1234567890", border=0, align='R')

    pdf.output(f"PDFs/{filename}.pdf")
