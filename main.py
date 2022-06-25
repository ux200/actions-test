import csv
f = open('out.csv', 'w')
data = ['あいうえお','12345']
writer = csv.writer(f)
writer.writerow(data)
f.close()