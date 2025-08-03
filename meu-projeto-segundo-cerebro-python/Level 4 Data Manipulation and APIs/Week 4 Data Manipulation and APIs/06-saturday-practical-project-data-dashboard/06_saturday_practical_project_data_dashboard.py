# Practical Project: Data Dashboard

# 1. Expected structure of the users.csv file

#nome,email,salario
#Ana,ana@email.com,3000
#Bruno,bruno@email.com,4500
#Carlos,carlos@email.com,2800




#Python Code

import csv                             # For reading and writing CSV files
import requests                        # For making HTTP requests to APIs
from datetime import datetime          # For generating timestamps
import os                              # For handling file paths
import sys                             # For exiting the program with error codes

# === Function to fetch the USD to BRL exchange rate ===
def get_exchange_rate():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"  # API URL to get USD-BRL rate
    try:
        response = requests.get(url)           # Send a GET request to the API
        response.raise_for_status()           # Raise error if response status is not 200
        data = response.json()                # Parse the response as JSON
        return float(data["USDBRL"]["bid"])   # Extract and convert the exchange rate to float
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Error retrieving exchange rate: {e}")  # Print error if request or parsing fails
        return None                                   # Return None to indicate failure

# === Function to read user data from a CSV file ===
def read_users_csv(filename):
    # Build the full file path based on the script's directory
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    # Check if the file exists
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File '{filename}' not found at path: {filepath}")
    
    users = []  # Initialize an empty list to store user dictionaries

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Read each CSV row as a dictionary
        for row in reader:
            try:
                # Normalize salary string by converting comma to dot and removing thousand separators
                salary_str = row["salario"].replace(".", "").replace(",", ".")
                row["salario"] = float(salary_str)  # Convert salary to float
                users.append(row)                   # Append the processed user to the list
            except (KeyError, ValueError) as e:
                print(f"Error processing row: {row} | Error: {e}")  # Handle and show data issues
    return users  # Return the complete list of users

# === Function to generate a report with BRL and USD salaries ===
def generate_report(users, exchange_rate):
    report = []  # Initialize empty list to store report lines
    for user in users:
        salary_usd = user["salario"] / exchange_rate   # Convert BRL salary to USD
        # Create a formatted string with name, BRL salary, and USD salary
        line = f'{user["nome"]} | R${user["salario"]:.2f} | ${salary_usd:.2f}'
        report.append(line)  # Add the line to the report
    return report  # Return the full report list

# === Function to save the report to both TXT and CSV files ===
def save_report(report, txt_filename, csv_filename):
    # Write the text report (.txt file)
    with open(txt_filename, 'w', encoding='utf-8') as txtfile:
        txtfile.write("User Salary Report - " + datetime.now().strftime("%d/%m/%Y %H:%M") + "\n\n")
        for line in report:
            txtfile.write(line + '\n')  # Write each report line to the file

    # Write the structured report (.csv file)
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write CSV header
        writer.writerow(['Name', 'Salary (BRL)', 'Salary (USD)'])
        for line in report:
            parts = line.split('|')  # Split the formatted string into parts
            if len(parts) == 3:
                # Write the cleaned parts to the CSV
                writer.writerow([parts[0].strip(), parts[1].strip(), parts[2].strip()])
            else:
                # Handle improperly formatted lines
                print(f"Malformed line in report: {line}")

# === Main script execution ===
if __name__ == "__main__":
    try:
        users = read_users_csv("users.csv")  # Attempt to read the user data from CSV
    except FileNotFoundError as e:
        print(e)  # Show file error message
        sys.exit(1)  # Exit the program if file is missing

    rate = get_exchange_rate()  # Get current USD-BRL exchange rate
    if rate is None:
        sys.exit("Failed to retrieve exchange rate. Exiting.")  # Stop if API failed

    report = generate_report(users, rate)  # Generate the report with converted salaries

    for r in report:
        print(r)  # Print each report line to the console

    save_report(report, "report.txt", "report.csv")  # Save report as TXT and CSV

# Example terminal output:

# Ana | R$3000.00 | $535.71
# Bruno | R$4500.00 | $803.57
# Carlos | R$2800.00 | $500.00
# (considering exchange rate of R$5.60/USD)






#Generated files:

#report.txt – Simple report formatted for reading
#report.csv – Structured report for use in spreadsheets




#  Technologies Used

# requests – to consume REST APIs (fetch real-time exchange rates)
# csv – for structured reading and writing of CSV files
# datetime – to add date and time stamps in reports
# with open() – for safe file handling, ensuring files are properly closed