class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pay(self, bill):
        return bill.amount / 2

class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


my_bill = Bill(amount=150, period="June 2024")
marc = Flatmate(name = "Marcel", days_in_house=15)
ola = Flatmate(name="Aleksandra", days_in_house=19)

print(marc.pay(bill=my_bill))
print(ola.pay(bill=my_bill))
