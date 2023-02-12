import csv

def display_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        print('Column names:', headers)
        print('-' * 50)

        for row in reader:
            for i, value in enumerate(row):
                print(f"{headers[i]}: {value}")
            print('-' * 50)

file_path = 'data.csv'
display_csv("addresses.csv")
