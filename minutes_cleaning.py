#!/usr/bin/env python

### first used bash to split the file on date: ### regex used to split file by date: split -p '[0-9]+/[0-9]+/[0-9]{4}' 2014-2015ChallengerTMClubMeetingMinutes.txt 

import re
import os
import csv



all_meeting_roles = []

def get_date(file_lines): 
	date_pattern = r'\d+/\d+/\d{4}?'
	date_regex = re.compile(date_pattern)
	meeting_date = []
	for line in file_lines:
		meeting_date += date_regex.findall(line)
	return	meeting_date

def get_role(role, fl_lines):
	meeting_roles = []
	for line in fl_lines:
		if re.search(role, line.lower()):
			meeting_roles.append(line)
	return meeting_roles

def clean_roles(roles_output):
	for index, line in enumerate(roles_output):
		roles_output[index] = line.replace('*', '')

	for index, line in enumerate(roles_output):
		roles_output[index] = line.replace(':', ',')

	for index, line in enumerate(roles_output):
		roles_output[index] = line.replace('//n', '')
	return roles_output

def get_meeting_roles(fl):
		## open files
		
		fh = open(filepath)

		## read in lines
		lines = fh.readlines()

		## get the date
		m_date = get_date(lines)

		## get the roles
		list_of_roles = ['toastmaster', 'thought of the day', 'general evaluator', 'speaker', 'evaluator', 'table topics', 'table topics master', 'grammarian', 'ah counter', 'timer', 'vote counter']
		meeting_role_list = []
		for role in list_of_roles:
			meeting_role_list.append(get_role(role, lines))

		## clean roles:
		# clean_roles(meeting_role_list)
		print(meeting_role_list)

		## add date:

		for index, line in enumerate(meeting_role_list):
			meeting_role_list[index] = str(line) + "," + str(m_date)

		return meeting_role_list


for flname in filenames:
	all_meeting_roles.append(get_meeting_roles(flname))	


print(all_meeting_roles)
	# with open('meeting_roles.csv', 'w', newline = "\n") as mr:
	# 	a  = csv.writer(mr, delimiter = ",")
	# 	w.writerows(meeting_roles)





# for each file:
# 	readlines 
# 	pull date
# 	pull roles
# 	add date to roles
# 	write 1 file: roles:

# for each file:
# 	pull date:
# 	pull attendance
# 	add date to attendance
# 	write one file: 

