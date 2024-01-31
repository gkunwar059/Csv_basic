import csv
# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0',
           'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1',
           'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3',
           'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5',
           'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8',
           'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1',
           'name': 'Sahil', 'year': '2'}]

fields=['name','branch','year','cgpa']
filename="university.csv"

with open(filename ,'w') as csvfile:
    # writing a csv dicts writer objects
   # Here, the file object (csvfile) is converted to a DictWriter object. Here, we specify the fieldnames as an argument. 
    writer=csv.DictWriter(csvfile,fieldnames=fields)
    # writing   headers(field names)
    writer.writeheader()
    # writing data rows
    writer.writerows(mydict)

    # writerows method simply writes all the rows but in each row, it writes only the values(not keys).


    # important thinks to know :
    # with open(filename,mode='w') as file:
    #     writer = csv.DictWriter(file, fieldnames = fields)
    #         # Here, the file object (csvfile) is converted to a DictWriter object. Here, we specify the fieldnames as an argument. 

#  writer.writeheader()
    # writeheader method simply writes the first row of your csv file using the pre-specified fieldnames.
        
