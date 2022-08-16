#To write in a file we can use file.write() or the file.writelines() method. 
#data = "Atul is a good boy. Pallavi is a bad girl but she might be good at times.\n"

'''
#while i<=5:
with open("Textfiletoswrite.txt", "a") as f:
        f.write(data *20)
    
with open("Textfiletoswrite.txt", "r") as x:
    print(x.read())
'''

'''
data = ["switch1", "\n", "switch2","\n", "switch3"]
with open("Textfiletoswrite.txt", "a") as f:	
        f.writelines(data)
        f.write('\n')
with open("Textfiletoswrite.txt", "r") as x:
    print(x.read())
'''

# Write into CSV file now. 

import csv
data = [["HName", "Number", "SN"], ["Switch1", "1", "werw"], ["switch2", "2", "dswr"]]

with open("CSVfiletowrite.csv", "a") as f:
    devices = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
    #The variable “f” is the file object of newdevices.csv and quoting tells the writer what you want quotes. QUOTE_NONNUMERIC means to put quotes around everything except numeric values.
    for row in data:
        devices.writerow(row)

with open("CSVfiletowrite.csv", "r") as f:
    print(f.read())

#print(data, file=CSVfiletowrite.csv)
