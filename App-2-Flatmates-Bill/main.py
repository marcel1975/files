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
        return  to_pay

class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass

my_bill = Bill(amount=150, period="June 2024")
marc = Flatmate(name = "Marcel", days_in_house=9)
ola = Flatmate(name="Aleksandra", days_in_house=10)
print("Marcel pays: ", marc.pays(bill=my_bill, mate=ola))
print("Aleksandra pays: ", ola.pays(bill=my_bill, mate=marc))
#print(ola.pay(bill=my_bill))
