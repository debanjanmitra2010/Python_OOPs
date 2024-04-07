import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmates:
    """
    Create a flatmate person who lives in the flat and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their names,
    their due amount and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image('house.png', w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=12, style='B')
        pdf.cell(w=100, h=20, txt="Period", border=0)
        pdf.cell(w=120, h=20, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=120, h=20, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=120, h=20, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


a = float(input("Hey user, enter the bill amount: "))
p = input("Enter the bill period: ")
name1 = input("Enter the Name of Flatmate1: ")
name2 = input("Enter the Name of Flatmate2: ")
f1_days_in_house = int(input(f"Enter the days {name1} stayed in the Flat: "))
f2_days_in_house = int(input(f"Enter the days {name2} stayed in the Flat: "))


the_bill = Bill(amount=float(a), period=p)

# Two Flatmate objects
f1 = Flatmates(name=name1, days_in_house=f1_days_in_house)
f2 = Flatmates(name=name2, days_in_house=f2_days_in_house)

print(f"{name1} Pays:", f1.pays(the_bill, flatmate2=f2))
print(f"{name2} Pays:", f2.pays(the_bill, flatmate2=f1))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=f1, flatmate2=f2, bill=the_bill)