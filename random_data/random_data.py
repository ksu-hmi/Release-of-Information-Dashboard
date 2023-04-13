import csv
import random
from datetime import datetime, timedelta

names = ["Sophia Kim", "Liam Patel", "Elijah Nguyen", "Ava Singh", "Noah Rodriguez", "Karen Smith", "James McCarty"]
request_types = ["Continuing care", "Patient", "Insurance", "Attorney", "Work comp", "Law enforcement", "Regulatory"]

# Set start and end dates
start_date = datetime.strptime('1/1/2022', '%m/%d/%Y')
end_date = datetime.strptime('12/31/2023', '%m/%d/%Y')

# Open a new CSV file for writing
with open('random_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the headers
    writer.writerow(['date', 'name', 'calls', 'voicemail', 'call_time', 'request_type', 'number_done', 'pages_sent', 'time_spent', 'cds_created', 'images_clouded'])

    # Generate 20,000 rows of random data
    for i in range(20000):
        # Generate random values for each field
        date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        name = random.choice(names)
        calls = random.randint(0, 248)
        voicemail = random.randint(0, 74)
        call_time = random.randint(0, 8)
        request_type = random.choice(request_types)
        number_done = random.randint(0, 103)
        pages_sent = random.randint(0, 5000)
        time_spent = random.randint(0, 8)
        cds_created = random.randint(0, 44)
        images_clouded = random.randint(0, 199)

        # Write the row to the CSV file
        writer.writerow([date.strftime('%m/%d/%Y'), name, calls, voicemail, call_time, request_type, number_done, pages_sent, time_spent, cds_created, images_clouded])

print("Data generated and saved to random_data.csv")
