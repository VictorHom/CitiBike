import json
import csv

def read_in_json(filename):
	f = open(filename)
	return json.load(f)

def read_in_csv(filename):
	f = open(filename)
	return csv.reader(f)

def merge(name):
	if name == "Stuyvesant Town":
		return "Flatiron District"
	elif name == "Murray Hill":
		return "Flatiron District"
	elif name == "Battery Park City":
		return "Financial District"
	elif name == "Central Park":
		return "Upper Manhattan"
	elif name == "Upper West Side":
		return "Upper Manhattan"
	elif name == "Little Italy/Chinatown":
		return "Lower East Side"
	else: return name

sections = read_in_json("parsed_data.json")
data = read_in_csv("processed_data.csv")
f = open("categorized_data.csv", "w")
writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)

beginning = 1
for row in data:
	bothInManhattan = 0
	if beginning == 1:
		row.insert(0,"end_section_name")
		row.insert(0,"start_section_name")
		beginning = 0
		bothInManhattan = 2
	else:
		for section in sections:
			if row[8] in section["stations"]:
				row.insert(0,merge(section["name"]))
				bothInManhattan += 1
		for section in sections:
			if row[5] in section["stations"]:
				row.insert(0,merge(section["name"]))
				bothInManhattan += 1
	if bothInManhattan == 2:
		writer.writerow(row)



	