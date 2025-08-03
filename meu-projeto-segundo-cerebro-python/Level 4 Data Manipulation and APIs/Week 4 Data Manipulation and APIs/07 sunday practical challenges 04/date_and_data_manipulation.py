# Date and Data Manipulation (date differences)

from datetime import datetime

# Input two dates as strings
date1_str = "2025-08-01"
date2_str = "2025-08-15"

# Convert strings to datetime objects
date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

# Calculate difference in days
diff = (date2 - date1).days

print(f"Days between {date1_str} and {date2_str}: {diff}")

#Output:
# Days between 2025-08-01 and 2025-08-15: 14