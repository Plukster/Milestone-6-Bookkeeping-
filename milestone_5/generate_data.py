from faker import Faker
import csv

fake = Faker()

def generate_employee_data(num_employees=100):
    with open('database.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Hiring Date', 'Department', 'Birthday'])

        for _ in range(num_employees):
            name = fake.name()
            hiring_date = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d')
            department = fake.job()
            birthday = fake.date_of_birth().strftime('%Y-%m-%d')

            writer.writerow([name, hiring_date, department, birthday])

if __name__ == "__main__":
    generate_employee_data(100)