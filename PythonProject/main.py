import glob

from fpdf import FPDF
from pathlib import Path

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for file in glob.glob("files/*.txt"):
    with open(file, "r") as f:
        text = f.read()

    filename = Path(file).stem
    pdf.add_page()

    pdf.set_font("Arial", size=16, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 12, txt=f"{filename}", ln=True, align='L')
    pdf.ln()

    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 10, txt=text)

pdf.output(f"output.pdf")

