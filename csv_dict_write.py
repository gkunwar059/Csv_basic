# Writing to a CSV file
# to write the csv file in write mode .the file object is converted to csv.writer object and further operation takes place 
import csv 
# fields name
fields=['Name','Branch','Year','CGPA']
# data rows of csv files
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]
# name of the csv file 
filename="tu.csv"
# writing to csv file 
with open(filename,'w') as csvfile:
    # create a csv writer objects
    csvwriter=csv.writer(csvfile)
    # writing the fields
    
    

    csvwriter.writerow(fields)
    # writing the data rows

    # We use writerows method to write multiple rows at once.
    csvwriter.writerows(rows)

# lets understand the above code below ............
 