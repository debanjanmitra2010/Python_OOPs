import webbrowser
from fpdf import FPDF
import os


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
        pdf.image('Files/house.png', w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', size=16, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=10)
        pdf.cell(w=100, h=20, txt=f"Total Amount: ${bill.amount}", border=0, ln=1)
        pdf.cell(w=100, h=20, txt=f"Total Flatmates: {len(flatmates)}", border=0, ln=1)
        pdf.cell(w=100, h=20, border=0, ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=12, style='B')
        pdf.cell(w=100, h=20, txt="Period", border=0)
        pdf.cell(w=120, h=20, txt=bill.period, border=0, ln=1)

        # Insert name and due amount for each flatmate
        pdf.set_font(family='Times', size=12)
        for flatmate in flatmates:
            pdf.cell(w=100, h=20, txt=flatmate.name, border=0)
            pdf.cell(w=120, h=20, txt=str(f"${round(flatmate.pays(bill, flatmates), 2)}"), border=0, ln=1)

        # Change Directory to Files
        os.chdir("Files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
