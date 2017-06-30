"""this is tutorial module for linear regression"""

import csv
with open('values.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['x'], row['y'])
