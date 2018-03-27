import csv
with open('HH0_H0.csv') as read:
     reader = csv.DictReader(read)
     with open('indv_hour2.csv', 'w') as write:
         writer = csv.DictWriter(write,fieldnames=['hour','plug','value'])
         writer.writeheader()
         w, h = 12, 718;
         max1 = 0
         max2 = 0
         matrix = [[0 for x in range(w)] for y in range(h)] 
         for row in reader:
            if row['Property'] == '1':
                time = (int(row['Timestamp']) - 1377993633)//3600
                matrix[time][int(row['Plug'])] += float(row['Value'])
                if int(row['Timestamp']) > max1:
                    max1 = int(row['Timestamp'])
                if time > max2:
                    max2 = time

         for x in range(0,718):
            for y in range (0,12):
                if y != 10 and matrix[x][y] > 0:
                    writer.writerow({'hour': x, 'plug': y, 'value': matrix[x][y]})
                
         print(max1)
         print(max2)
                


#, ['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.1.1', 'agg','hourspater','class0','class1','class2','class3','class4',
 #       'class5','class6','class7','class8','class9','class11','timestamp','hoursbyone','hoursbytwo','hoursbythree','hoursbyfour','hoursbysix',
  #      'hoursbyeight','hoursbytwelve']
#1380578399- 1377993633