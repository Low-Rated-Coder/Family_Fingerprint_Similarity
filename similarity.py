import csv
import math
import sys
import glob

data = []

for file1 in glob.iglob('.\CSVFiles\*.csv'):
	temp = []
	FirstCount = []
	with open(file1) as csvfile1:
		readCSV1 = csv.reader(csvfile1, delimiter=',')
		for row in readCSV1:
			FirstCount.append((row[0],row[1]))
	for file2 in glob.iglob('.\CSVFiles\*.csv'):
		SecondCount = []
		with open(file2) as csvfile2:
			readCSV2 = csv.reader(csvfile2, delimiter=',')
			for row in readCSV2:
  				SecondCount.append((row[0],row[1]))
		
		count = 0
		for i in range(0,10):
			(c1,d1) = FirstCount[i];
			(c2,d2) = SecondCount[i];
			if c1 == c2 and d1 == d2:
				count += 1;
		temp.append(count/10)
	data.append(temp)

with open('.\CSVFiles\similarities.csv', 'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)