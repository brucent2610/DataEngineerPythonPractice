import csv

def read_csv(fn, delimiter=','):
    with open(fn, 'r') as f:
        rows = csv.reader(f, delimiter=delimiter)
        for row in rows:
            print(row)

def write_csv(fn, header, row):
    with open(fn, mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(row)

# read_csv('files_to_read/names.csv')
# write_csv('files_to_read/names2.csv', ['First Name', 'Last Name'], ['John', 'Doe'])  
