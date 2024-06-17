import webbrowser
import os
from fpdf import FPDF
from filestack import Client


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))

        pdf = FPDF(orientation="P", unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert a title
        pdf.set_font(family="Times", size=22, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill:", border=0, align='C', ln=1)

        # Insert period label
        pdf.set_font(family="Times", size=15, style='B')
        pdf.cell(w=100, h=30, txt="Period:", border=0)
        pdf.cell(w=160, h=30, txt=bill.period, border=0, ln=1)

        # Insert the name and amount of the 1th flatmate
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=100, h=15, txt=flatmate1.name, border=0)
        pdf.cell(w=160, h=15, txt=flatmate1_pay, border=0, ln=1)

        # Insert the name and amount of the 2td flatmate
        pdf.cell(w=100, h=15, txt=flatmate2.name, border=0)
        pdf.cell(w=160, h=15, txt=flatmate2_pay, border=0, ln=1)

        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)

class FileSharer:

    def __init__(self, filepath, api_key="AU4Borz6YTzGiV3m0LfOjz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)

        filelink = client.upload(filepath=self.filepath)
        return filelink.url
