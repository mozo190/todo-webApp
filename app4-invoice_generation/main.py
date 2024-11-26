import os.path

import pandas as pd
from fpdf import FPDF
import glob

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for file in glob.glob("invoices/*.xlsx"):
    df = pd.read_excel(file, engine='openpyxl')

pdf.add_page()
pdf.set_font("Arial", size=16, style='B')
pdf.set_text_color(100, 100, 100)
pdf.cell(100, 12, txt=f"Invoice nr. 10001", ln=True, align='L')
pdf.cell(0, 12, txt=f"Date: 2023.1.18", ln=True, align='L')

pdf.set_font("Times", size=12, style='B')
pdf.cell(25, 10, txt=f"Product ID", border=1, align='L')
pdf.cell(65, 10, txt=f"Product Name", border=1, align='L')
pdf.cell(25, 10, txt=f"Amount", border=1, align='L')
pdf.cell(35, 10, txt=f"Prize per Unit", border=1, align='L')
pdf.cell(40, 10, txt=f"Total Price", border=1, align='L')
pdf.ln()

for i, row in df.iterrows():
    pdf.set_font("Times", size=10)
    pdf.cell(25, 10, txt=str(row["product_id"]), border=1, align='L')
    pdf.cell(65, 10, txt=str(row["product_name"]), border=1, align='L')
    pdf.cell(25, 10, txt=str(row["amount_purchased"]), border=1, align='C')
    pdf.cell(35, 10, txt=str(row["price_per_unit"]), border=1, align='C')
    pdf.cell(40, 10, txt=str(row["total_price"]), border=1, align='C')
    pdf.ln()

big_total = df["total_price"].sum()

pdf.set_font("Times", size=10)
pdf.cell(25, 10, txt="", border=1, align='L')
pdf.cell(65, 10, txt="", border=1, align='L')
pdf.cell(25, 10, txt="", border=1, align='L')
pdf.cell(35, 10, txt="", border=1, align='L')
pdf.cell(40, 10, txt=str(f"{big_total}"), border=1, align='C')
pdf.ln()
pdf.ln()

pdf.cell(0, 10, txt=f"The total due amount is {big_total} Euros.", border=0, align='R')
pdf.ln()
pdf.image("py.png", x=pdf.get_x() + 83, y=pdf.get_y(), w=6)
pdf.cell(0, 10, txt=f"Please transfer the amount to the following bank account: 1234567890", border=0, align='R')

pdf.output("10001-2023.1.18.pdf")
