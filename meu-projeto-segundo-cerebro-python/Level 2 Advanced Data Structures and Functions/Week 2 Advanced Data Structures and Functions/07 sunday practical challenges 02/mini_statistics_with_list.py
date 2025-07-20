# Mini-Statistics with List – Receive grades and calculate average, highest and lowest grades.

def stats(grades):                                    # Receives a list of grades
    avg = sum(grades) / len(grades)                   # Calculate average grade
    max_grade = max(grades)                           # Find highest grade
    min_grade = min(grades)                           # Find lowest grade
    print(f" Average: {avg:.2f}")                     # Print average with 2 decimals
    print(f" Highest: {max_grade}")                   # Print highest grade
    print(f" Lowest: {min_grade}")                    # Print lowest grade

grades = [8.5, 7.0, 9.2, 6.8, 10.0]                   # List of sample grades
stats(grades)                                         # Call function with grades

# Output:
#  Average: 8.30
#  Highest: 10.0
#  Lowest: 6.8




# Description:
# Receives a list of grades and shows the average, highest, and lowest values.
# Uses:
# - Lists with float values
# - sum(), max(), min() for calculations
# - Function to separate logic
# - f-strings with formatting for better output (e.g., {:.2f})