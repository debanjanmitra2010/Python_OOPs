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

    def pays(self, bill, other_flatmates):
        """Calculates payment considering all flatmates.
        """
        total_days = sum(flatmate.days_in_house for flatmate in other_flatmates) + self.days_in_house
        weight = self.days_in_house / total_days
        return bill.amount * weight


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their names,
    their due amount and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmates, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon (Make sure you actually have a 'house.png' file)
        pdf.image('house.png', w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=10)
        pdf.cell(w=100, h=20, txt=f"Total Amount: ${the_bill.amount}", border=0, ln=1)
        pdf.cell(w=100, h=20, txt=f"Total Flatmates: {len(flatmates)}", border=0, ln=1)
        pdf.cell(w=100, h=20, border=0, ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=12, style='B')
        pdf.cell(w=100, h=20, txt="Period", border=0)
        pdf.cell(w=120, h=20, txt=the_bill.period, border=0, ln=1)

        # Insert name and due amount for each flatmate
        pdf.set_font(family='Times', size=12)
        for flatmate in flatmates:
            pdf.cell(w=100, h=20, txt=flatmate.name, border=0)
            pdf.cell(w=120, h=20, txt=str(f"${round(flatmate.pays(bill, flatmates), 2)}"), border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


# Get user input
a = float(input("Hey user, enter the bill amount: "))
p = input("Enter the bill period: ")
num_flatmates = int(input("With how many flatmates do you want to divide the Bill: "))

# Collect flatmate data
flatmates = []
for i in range(num_flatmates):
    name = input(f"Enter the Name of Flatmate {i + 1}: ")
    days_in_house = int(input(f"Enter the days {name} stayed in the Flat: "))
    flatmates.append(Flatmates(name, days_in_house))

# Create bill object and generate report
the_bill = Bill(amount=a, period=p)
pdf_report = PdfReport(filename=f"{the_bill.period.replace(' ', '_')}_Report.pdf")
pdf_report.generate(flatmates, the_bill)
