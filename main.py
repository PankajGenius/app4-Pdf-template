from fpdf import FPDF
import pandas as pd

# P for Portrait and #L can landscape
pdf = FPDF(orientation="P", unit="mm", format="A4")


df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    pdf.add_page()

    pdf.set_font(family="Helvetica", style="B", size=12)
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"],  align="L", ln=1)
    # w for width , h for height, ln = line break
    pdf.line(10,21, 200, 21)

    for i in range(row["Pages"]-1):
        pdf.add_page()

pdf.output("Output.pdf")
