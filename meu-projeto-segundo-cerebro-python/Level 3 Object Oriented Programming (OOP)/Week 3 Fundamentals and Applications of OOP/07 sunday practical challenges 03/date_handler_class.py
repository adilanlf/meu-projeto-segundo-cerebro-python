# Date Handler Class – Validation and Formatting

# A class to validate and format dates
class DateHandler:
    def __init__(self, day, month, year):     # Constructor
        self.day = day                        # Day attribute
        self.month = month                    # Month attribute
        self.year = year                      # Year attribute

    def is_valid(self):                       # Simple validation method
        return 1 <= self.day <= 31 and 1 <= self.month <= 12

    def format_date(self):                    # Method to return date in dd/mm/yyyy
        return f"{self.day:02}/{self.month:02}/{self.year}"

# Test valid date
date = DateHandler(5, 7, 2025)
if date.is_valid():                          # Check if date is valid
    print("Date is valid:", date.format_date())
else:
    print("Invalid date")
    
#Output:
# Date is valid: 05/07/2025