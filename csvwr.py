import csv
with open('test.csv') as read:
     reader = csv.DictReader(read, ['ID','Timestamp','Value','Property','Plug','HH_ID','H_ID'])
     with open('HH0_H0.csv', 'w') as write:
         writer = csv.DictWriter(write,['ID','Timestamp','Value','Property','Plug','HH_ID','H_ID'])
         writer.writeheader()
         for row in reader:
             if row['HH_ID'] == '0' and row['H_ID']== '0':
                 writer.writerow(row)
