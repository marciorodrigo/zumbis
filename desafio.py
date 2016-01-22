# -*- coding: utf-8 -*- 

import csv
import sys

from collections import defaultdict


mylist = defaultdict(list)

with open(sys.argv[1], 'rb') as inFile:
	reader = csv.reader(inFile, dialect='excel-tab')

	for row in reader:
		mylist[row[0]].append(row[1].replace('R$', ''))

with open(sys.argv[2], 'rb') as inFile:
	reader = csv.reader(inFile, dialect='excel-tab')

	for row in reader:
		mylist[row[0]].append(row[1].replace('R$', ''))

anotherlist = {}
for key, values in mylist.items():
	print key, sum([float(v.replace(',', '.')) for v in values])