from flat import Bill, Flatmate
from reports import PdfReport, FileSharer


amount = float(input("Hey user, enter the bill amount: "))
period = input("What is a bill period? E.g. May 2024: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period: "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period: "))

# print("entered bill amount is: ", amount)

my_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)
print(f"{flatmate1.name} pays: ", flatmate1.pays(bill=my_bill, mate=flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill=my_bill, mate=flatmate1))

pdf_report = PdfReport(filename=f"{my_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=my_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())