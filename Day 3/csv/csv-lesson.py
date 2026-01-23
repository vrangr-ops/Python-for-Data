#read csv

#
# 
# 
import csv
from fileinput import filename

print(csv.__file__)
rows =  []
with open("employers.csv", newline="") as csvfile:
    csvreader =csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

print (f"the headers of the csv is:{header}")
print (rows)

header=['name','age']
data = [['alex',25],['Brad',30],['daisy',18]]

with open('student_info.csv', mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(header)
    csvwriter.writerows(data)



#read from csv part 2
#csv.dictreader() module



with open('employers.csv', newline='') as csvfile:
    reader =csv.DictReader(csvfile)

    for row in reader:
        print(row ["Name"])
        print(row)


#write to csv file
#csv.DictWriter() module -maps dictionaries to output rows

headers=['name','age']
data = [['alex',25],['Brad',35],['daisy',18]]

with open('student_info.csv', mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames= headers)
    writer.writeheader()
    for student in data:
        writer.writerow({'name':student[0],'age':student[1]})