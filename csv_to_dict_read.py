# Reading CSV Files Into a Dictionary With csv

import csv
# open csv file for reading 
with open('employee.csv',mode='r' ) as file:
    # create a csv reader with the 
    csv_reader=csv.DictReader(file)

    # initalize an empty list to store the dictonaries
    data_list=[]

    # iterate through each row in the csv file 
    for row in csv_reader:
        data_list.append(row)

for data in data_list:
    print(data)
