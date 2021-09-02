import csv
data=[]
with open("data 2.csv","r")as f:
    csv_reader=csv.reader(f)
    for row in csv_reader :
        data.append(row)

headers=data[0]
planetdata=data[1:]
for datapoint in planetdata :
    datapoint[2]=datapoint[2].lower()
planetdata.sort(key=lambda planetdata:planetdata[2])
with open("data 1sorted.csv","a+")as f:
    csv_writter=csv.writer(f)
    csv_writter.writerow(headers)
    csv_writter.writerows(planetdata)
    
