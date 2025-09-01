import csv
from datetime import datetime

def generate_report(database_file, target_month):
    # Convert target_month to lowercase to handle case insensitivity
    target_month = target_month.lower()
    
    # Initialize counters for birthdays and anniversaries
    birthday_counts = {}
    anniversary_counts = {}

    with open(database_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            name = row['Name']
            hiring_date = datetime.strptime(row['Hiring Date'], '%Y-%m-%d')
            department = row['Department']
            birthday = datetime.strptime(row['Birthday'], '%Y-%m-%d')
            
            # Check if the birthday is in the target month
            if birthday.month == datetime.strptime(target_month, '%B').month:
                if department not in birthday_counts:
                    birthday_counts[department] = 0
                birthday_counts[department] += 1
            
            # Check if the hiring anniversary is in the target month
            if hiring_date.month == datetime.strptime(target_month, '%B').month:
                if department not in anniversary_counts:
                    anniversary_counts[department] = 0
                anniversary_counts[department] += 1

    # Calculate total counts
    total_birthdays = sum(birthday_counts.values())
    total_anniversaries = sum(anniversary_counts.values())

    # Print the report
    print(f"Report for {target_month.capitalize()} generated")
    print("--- Birthdays ---")
    print(f"Total: {total_birthdays}")
    print("By department:")
    for dept, count in sorted(birthday_counts.items()):
        print(f"- {dept}: {count}")

    print("\n--- Anniversaries ---")
    print(f"Total: {total_anniversaries}")
    print("By department:")
    for dept, count in sorted(anniversary_counts.items()):
        print(f"- {dept}: {count}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python report.py <database_file> <month>")
    else:
        database_file = sys.argv[1]
        target_month = sys.argv[2]
        generate_report(database_file, target_month)