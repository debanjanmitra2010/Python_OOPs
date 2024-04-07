from flat import Bill, Flatmates
from reports import PdfReport


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
