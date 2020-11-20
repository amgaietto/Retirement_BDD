class Retiree:

    def __init__(self):

        self.month_dict = {1: "January", 2: "February", 3: "March",
                      4: "April",
                      5: "May", 6: "June", 7: "July", 8: "August",
                      9: "September", 10: "October", 11: "November",
                      12: "December"}

        self.year = None
        self.month = None
        self.age = None
        self.months = None
        self.final_month = None
        self.final_year = None

    def get_birth_year(self):
        while True:
            choice = input("Please enter the year of your birth or hit "
                           "return to exit: ")
            if not choice:
                exit()
            try:
                year = int(choice)
                if year < 1900 or year > 2020:
                    raise ()
                self.year = year
                return year
            except:
                return "Invalid input."

    def get_birth_month(self):
        while True:
            try:
                month = int(input("Please enter the month of your birth (number 1-12): "))
                if month < 1 or month > 12:
                    raise()
                self.month = month
                return month
            except:
                return "Invalid input."

    def calculate_receipt_age(self, year):
        if year <= 1937:
            self.age = 65
            self.months = 0
        elif 1938 <= year <= 1942:
            self.age = 65
            self.months = (year - 1937) * 2
        elif 1943 <= year <= 1954:
            self.age = 66
            self.months = 0
        elif 1955 <= year <= 1959:
            self.age = 66
            self.months = (year - 1954) * 2
        else:
            self.age = 67
            self.months = 0
        return self.age, self.months

    def calculate_retirement_date(self, birth_year, birth_month):
        retirement_age, number_months = self.calculate_receipt_age(birth_year)
        self.final_year = retirement_age + birth_year
        month_count = number_months + birth_month
        if month_count > 12:
            self.final_year += 1
            month_count -= 12
        self.final_month = self.month_dict[month_count]
        return self.final_year, self.final_month
