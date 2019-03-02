import csv
import json

res = {}

with open("course.csv", "r") as f:
    fieldname = ["Code", "Prereq"]
    reader = csv.DictReader(f)
    for row in reader:
        course_id = row[fieldname[0]]
        prereq = row[fieldname[1]].split(",")
        
        res[course_id] = {}
        res[course_id]["prev"] = []
        for c in prereq:
            res[course_id]["prev"] .append(c)

with open("course.json", "w") as f:
    json.dump(res, f)

    
