import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_excel("invoices/10001-2023.1.18.xlsx", engine='openpyxl')
print(df.columns)

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
    pdf.cell(25, 10, txt=str(row["amount_purchased"]), border=1, align='L')
    pdf.cell(35, 10, txt=str(row["price_per_unit"]), border=1, align='L')
    pdf.cell(40, 10, txt=str(row["total_price"]), border=1, align='L')
    pdf.ln()

pdf.output("output.pdf")
