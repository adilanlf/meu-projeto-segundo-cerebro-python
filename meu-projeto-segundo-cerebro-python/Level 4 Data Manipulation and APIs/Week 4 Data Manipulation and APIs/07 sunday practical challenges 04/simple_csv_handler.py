# Simple CSV Handler (calculate averages)

# 1. Expected structure of the scores.csv file

#name,score
#Alice,85
#Bob,90
#Charlie,78.5
#David,not_a_number
#Eve,




import csv                      # Import the CSV module to read CSV files
import os                       # Import the OS module to work with file paths

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the full path to the CSV file named 'scores.csv' in the same directory
    csv_path = os.path.join(script_dir, "scores.csv")

    try:
        # Open the CSV file safely with UTF-8 encoding and no newline issues
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)  # Read the file as a dictionary per row (header-based)

            # Check if the expected 'score' column exists in the header
            if "score" not in reader.fieldnames:
                print(f"Error: The 'score' column was not found in the CSV file.")
                print(f"Available columns: {reader.fieldnames}")  # Show available columns for debugging
                return  # Exit the function early if the column is missing

            scores = []  # Initialize an empty list to store valid scores

            # Loop through each row starting from line 2 (line 1 is the header)
            for row_number, row in enumerate(reader, start=2):
                score_str = row.get("score", "").strip()  # Get the 'score' value and remove whitespace

                if not score_str:  # If the score is empty, skip this row with a warning
                    print(f"Warning: Line {row_number} - empty 'score' field, skipping.")
                    continue

                try:
                    score = float(score_str)  # Try converting the score to a float
                    scores.append(score)      # Add valid score to the list
                except ValueError:
                    # If conversion fails, the score is invalid (e.g., text instead of a number)
                    print(f"Warning: Line {row_number} - invalid value '{score_str}' in 'score' column, skipping.")

            if not scores:  # If no valid scores were found, notify and exit
                print("No valid values were found in the 'score' column.")
                return

            average = sum(scores) / len(scores)  # Calculate the average of all valid scores
            print(f"Average score: {average:.2f}")  # Display the average rounded to 2 decimal places

    except FileNotFoundError:
        # If the CSV file is missing, show an error message with the expected path
        print("Error: 'scores.csv' file not found.")
        print(f"Expected at path: {csv_path}")

# Entry point of the script (only runs when executed directly, not when imported)
if __name__ == "__main__":
    main()

# Example terminal output:

# Warning: Line 5 - invalid value 'not_a_number' in 'score' column, skipping.
# Warning: Line 6 - empty 'score' field, skipping.
# Average score: 84.50






# Summary of key concepts used:
#os.path.abspath(__file__): Gets the absolute path of the running script.

#csv.DictReader: Makes reading CSVs easier by using headers as keys.

#Graceful error handling with try/except for missing files and invalid data.

#Input validation: Skips empty or non-numeric score fields.

#Clear warnings and output to guide the user.