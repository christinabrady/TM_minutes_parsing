#!/usr/bin/env python
# run in python 2

import csv
import distance
import re

with open("roster_members.csv", 'rb') as rost:
	reader = csv.reader(rost)
	rname = list(reader)

# ### make a copy to index and use as a reference later
# rname_cp = rname

with open("minutes_members.csv", 'rb') as mem:
	reader2 = csv.reader(mem)
	mname = list(reader2)


### text processing with nltk, eliminate punctuation, make everything lower case, 
punct = re.compile(r'([^a-z ])')

# for indx, nme in enumerate(rname):
# 	rname[indx] = punct.sub("", str(nme).lower())

for indx, nme in enumerate(mname):
	mname[indx] = punct.sub("", str(nme).lower())

### eliminate both 'x's'
# rname.remove('x')
mname.remove('x')


###### match and print
matches = []
for r in rname:
	for m in mname:
		if distance.nlevenshtein(punct.sub("", str(r).lower()), m, method = 2) <= 0.4:
			matches.append([str(r), m, distance.nlevenshtein(r, m, method = 2)])

c = open('matches.csv', 'w')
cw = csv.writer(c)
cw.writerows(matches) 
