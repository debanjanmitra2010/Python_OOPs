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
