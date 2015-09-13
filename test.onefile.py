#!/usr/bin/env python

### first used bash to split the file on date: ### regex used to split file by date: split -p '[0-9]+/[0-9]+/[0-9]{4}' 2014-2015ChallengerTMClubMeetingMinutes.txt 

import re
import os
import csv


def get_text(f):
	filepath = './split_minutes/' + f
	fh = open(filepath)

		## read in lines
	lines = fh.readlines()
	return lines


## get the date
def get_date(lines_output): 
	date_pattern = r'\d+/\d+/\d{4}?'
	date_regex = re.compile(date_pattern)
	md = []
	for line in lines_output:
		md += date_regex.findall(line)
	return	str(md)

## get the roles and names
def get_role(role, lines_output):
	mr = []
	for line in lines_output:
		if re.search(role, line.lower()):
			mr.append(line)

	for index, line in enumerate(mr):
		mr[index] = line.replace('*', '')

	for index, line in enumerate(mr):
		mr[index] = line.replace(':', ',')

	for index, line in enumerate(mr):
		mr[index] = line.replace('//n', '')
	return mr


master_list = []
filenames = os.listdir('./split_minutes')
def get_all_roles(filename):
	list_of_roles = ['toastmaster:', 'thought of the day:', 'speaker:', 'evaluator:', 'table topics:', 'table topics master:', 'grammarian:', 'ah counter:', 'timer:', 'vote counter:']
	meeting_roles = []
	text_lines = get_text(filename)	
	meeting_date = get_date(text_lines)
	for role in list_of_roles:
		meeting_roles.append(get_role(role, text_lines))
		# put them together:
		print(meeting_roles)
	for row in meeting_roles:
		row.insert(0, meeting_date)
	return(meeting_roles)

for filename in filenames:
	master_list.append(get_all_roles(filename))


# with open('TMY2014attend.csv', 'w', newline = "\n") as mr:
# 	a  = csv.writer(mr, delimiter = ",")
# 	for y in range(len(master_list[0])):
# 		a.writerows(x[y] for x in master_list)



