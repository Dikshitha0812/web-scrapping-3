import csv

data1=[]
data2=[]

with open ("data 2.csv")as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data1.append(row)

with open ( "data 1sorted.csv") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data2.append(row)

header1=data1[0]
planetdata1=data1[1:]

header2=data2[0]
planetdata2=data2[1:]
headers=header1+header2

planetdata=[]
for index,row in enumerate(planetdata1) :
    planetdata.append(planetdata1[index]+planetdata2[index])

with open ("final.csv","a+")as f:
    csv_writter =csv.writer(f)
    csv_writter.writerow(headers)
    csv_writter.writerows(planetdata)