#using python to read, write, append CSV files
import csv

def csv_write(filename):
    header = ['Fname', 'Lname', 'Phone']
    data = [['Sapna', 'Nimkar', '9993882313'], ['Supratim', 'Samantray', '9903834200']]
    with open('./{}'.format(filename), 'w') as myfile:
        writer = csv.writer(myfile)
        writer.writerow(header)
        writer.writerows(data)

def csv_read(filename):
    rows = []
    with open('./{}'.format(filename), 'r') as myfile:
        reader = csv.reader(myfile)
        #print(list(reader))
        header = next(reader)
        for row in reader:
            rows.append(row)
    print(header)
    print(rows)

if __name__ == '__main__':
    filename = 'csv_file'
    #csv_write(filename)
    csv_read(filename)