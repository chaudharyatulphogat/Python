# Read text file:

#Below code will read file and print all. 
'''
f=open("Textfiletoread.rtf", "r")
print(f.read())
'''

# Below code is to use with open() as it closes file after use. 
'''
with open("Textfiletoread.rtf", "r") as f:
    #content = f.read(54)
    #content = f.readline()
    #content = f.readlines()[0:1]
    print(content)
'''

#Open a csv file. 
'''
import csv

with open("CSVtoreadAsset.csv", "r") as f:
    csvcontent=csv.reader(f)
    print(csvcontent)
    header = next(csvcontent)
    print(f'Headers:{header}')
    for row in csvcontent:
        print(row)
'''

# Above saves csv file in a list.   
import csv

with open('CSVtoreadAsset.csv', 'r') as f:
    csvcontent = csv.DictReader(f)
    print(csvcontent)
    for row in csvcontent:
        #print(row)
        print(f'ASSET {row["ASSET#"]} Serial number: {row["ASSET_SERIAL#"]}')


