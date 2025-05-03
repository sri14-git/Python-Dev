from pathlib import Path
import pandas as pd
import glob
from fpdf import FPDF
filepath = glob.glob("invoices/*.xlsx")

for file in filepath:

    pdf=FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    inv_nr = Path(file).stem.split("-")[0]
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice No: {inv_nr}",ln=1)
    pdf.set_font(family="Times",size=16,style="B")
    Date = Path(file).stem.split("-")[1]

    pdf.cell(w=50,h=8,txt=f"Date: {Date}",ln=4)
    df = pd.read_excel(file, sheet_name="Sheet 1")
    col=df.columns
    listcol=[ item.replace("-"," ").title() for item in col]
    pdf.set_font(family="Times", size=10)
    pdf.cell(w=30, h=8, txt=listcol[0], border=1)
    pdf.cell(w=70, h=8, txt=listcol[1], border=1)
    pdf.cell(w=30, h=8, txt=listcol[2], border=1)
    pdf.cell(w=30, h=8, txt=listcol[3], border=1)
    pdf.cell(w=30, h=8, txt=listcol[4], border=1, ln=1)
    for ind,rows in df.iterrows():
        print(rows)
        pdf.set_font(family="Times",size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30,h=8,txt=str(rows["product_id"]),border=1)
        pdf.cell(w=70,h=8,txt=str(rows["product_name"]),border=1)
        pdf.cell(w=30,h=8,txt=str(rows["amount_purchased"]),border=1)
        pdf.cell(w=30,h=8,txt=str(rows["price_per_unit"]),border=1)
        pdf.cell(w=30,h=8,txt=str(rows["total_price"]),border=1,ln=1)
    pdf.output(f"PDFs\\{inv_nr}.pdf")