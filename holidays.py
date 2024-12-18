from datetime import date

class holidays:
    def __init__(self):
        # Initialize the array to store Madrid public holidays
        self.holiday_days = []

        # Add public holidays
        # 2024
        self.add_holiday("New Year's Day", date(2024, 1, 1))
        self.add_holiday("Epiphany", date(2024, 1, 6))
        self.add_holiday("Holy Thursday", date(2024, 3, 28))
        self.add_holiday("Good Friday", date(2024, 3, 29))
        self.add_holiday("Worker's Day", date(2024, 5, 1))
        self.add_holiday("Festival of the Community of Madrid", date(2024, 5, 2))
        self.add_holiday("Festival of the Community of Madrid", date(2024, 5, 15))
        self.add_holiday("Santiago Apóstol", date(2024, 7, 25))
        self.add_holiday("Assumption of the Virgin", date(2024, 8, 15))
        self.add_holiday("National Holiday of Spain", date(2024, 10, 12))
        self.add_holiday("All Saints' Day", date(2024, 11, 1))
        self.add_holiday("Spanish Constitution Day", date(2024, 12, 6))
        self.add_holiday("Nativity of the Lord", date(2024, 12, 25))

        # 2025
        self.add_holiday("New Year's Day", date(2025, 1, 1))
        self.add_holiday("Epiphany", date(2025, 1, 6))
        self.add_holiday("Holy Thursday", date(2025, 4, 17))
        self.add_holiday("Good Friday", date(2025, 4, 18))
        self.add_holiday("Worker's Day", date(2025, 5, 1))
        self.add_holiday("Festival of the Community of Madrid", date(2025, 5, 2))  # Confirmed, no changes
        self.add_holiday("San Isidro", date(2025, 5, 15))  # Festival of San Isidro
        self.add_holiday("Santiago Apóstol", date(2025, 7, 25))
        self.add_holiday("Assumption of the Virgin", date(2025, 8, 15))
        self.add_holiday("National Holiday of Spain", date(2025, 10, 12))
        self.add_holiday("All Saints' Day", date(2025, 11, 1))
        self.add_holiday("Spanish Constitution Day", date(2025, 12, 6))
        self.add_holiday("Spanish Constitution Day", date(2025, 12, 8))
        self.add_holiday("Nativity of the Lord", date(2025, 12, 25))


        # Add private holidays
        
        # 2024
        self.add_holiday("Private Holiday", date(2024, 1, 8))
        self.add_holiday("Private Holiday", date(2024, 1, 9))
        self.add_holiday("Private Holiday", date(2024, 1, 10))
        self.add_holiday("Private Holiday", date(2024, 1, 11))
        self.add_holiday("Private Holiday", date(2024, 1, 12))

        self.add_holiday("Private Holiday", date(2024, 1, 24))

        self.add_holiday("Private Holiday", date(2024, 4, 19))
        self.add_holiday("Private Holiday", date(2024, 4, 22))
        self.add_holiday("Private Holiday", date(2024, 4, 23))
        self.add_holiday("Private Holiday", date(2024, 4, 24))
        self.add_holiday("Private Holiday", date(2024, 4, 25))
        self.add_holiday("Private Holiday", date(2024, 4, 26))

        self.add_holiday("Private Holiday", date(2024, 6, 24))
        self.add_holiday("Private Holiday", date(2024, 6, 25))
        self.add_holiday("Private Holiday", date(2024, 6, 26))
        self.add_holiday("Private Holiday", date(2024, 6, 27))
        self.add_holiday("Private Holiday", date(2024, 6, 28))
        self.add_holiday("Private Holiday", date(2024, 6, 29))

        self.add_holiday("Private Holiday", date(2024, 8, 2))
        self.add_holiday("Private Holiday", date(2024, 8, 3))
        self.add_holiday("Private Holiday", date(2024, 8, 4))
        self.add_holiday("Private Holiday", date(2024, 8, 5))
        self.add_holiday("Private Holiday", date(2024, 8, 6))

        self.add_holiday("Private Holiday", date(2024, 12, 19))
        self.add_holiday("Private Holiday", date(2024, 12, 24))

        self.add_holiday("Private Holiday", date(2025, 1, 7))
        self.add_holiday("Private Holiday", date(2025, 1, 8))
        self.add_holiday("Private Holiday", date(2025, 1, 9))
        self.add_holiday("Private Holiday", date(2025, 1, 10))


    def add_holiday(self, name, date):
        # Add a public holiday to the array
        self.holiday_days.append({"name": name, "date": date})

    def get_holidays(self):
        # Return the array of public holidays
        return self.holiday_days

