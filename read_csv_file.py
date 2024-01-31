# reading csv file 

import csv
# Dummy data
dummy_data = [
    ["ID", "Name", "Age"],
    [1, "John", 25],
    [2, "Jane", 22],
    [3, "Bob", 30]
]

# writing the in the csv file 
header=['a','b','c']
with open ('simpleread_csvfile.csv','w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(dummy_data)

# reading the csv file 
with open ('simpleread_csvfile.csv' ,'r') as csvfile:
    reader=csv.reader(csvfile)
    # skip the header if it exists
    header=next(reader,None)
    if header:
        print("Header:",header)

    # printing the rest of the data 
    for row in reader:
        print(row)