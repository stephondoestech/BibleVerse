import csv

with open('email.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)