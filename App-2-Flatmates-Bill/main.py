import webbrowser
import os

from fpdf import FPDF


class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, mate):
        weight = self.days_in_house / (self.days_in_house + mate.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))

        pdf = FPDF(orientation="P", unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("house.png", w=30, h=30)

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

        pdf.output(self.filename)
        webbrowser.open('file://' + os.path.realpath(self.filename))


bill_amount = float(input("Hey user, enter the bill amount: "))120
print("entered bill amount is: ", bill_amount)

my_bill = Bill(amount=bill_amount, period="June 2024")
marc = Flatmate(name="Marcel", days_in_house=9)
nina = Flatmate(name="Nina", days_in_house=10)
print("Marcel pays: ", marc.pays(bill=my_bill, mate=nina))
print("Nina pays: ", nina.pays(bill=my_bill, mate=marc))

pdf_report = PdfReport(filename="Report_nr1.pdf")
pdf_report.generate(flatmate1=marc, flatmate2=nina, bill=my_bill)
