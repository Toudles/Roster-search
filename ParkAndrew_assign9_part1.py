"""
Assignment #9, Part 1
Andrew Park
"""

print ("NYU Computer Science Registration System")
courses = {}
enroll = {}
with open ("class_data.txt") as file:
    for line in file:
        line = line.strip().split(',')
        courses[line[0]] = line[1]

with open ("enrollment_data.txt") as file:
    for line in file:
        line = line.strip().split(',')
        if line[0] in enroll:
            enroll[line[0]].append (line[1] + "," + line[2])
        else:
            enroll[line[0]] = [line[1] + "," + line[2]]

course = ""
while course not in courses:
    course = input ("Enter a course ID (i.e. CS0002, CS0004): ")
    if course not in courses:
        print ("Cannot find this course")

print ("The title of this class is:", courses[course])
if course in enroll:
    count = len (enroll[course])
else:
    count = 0
print ("The course has {} students enrolled".format (count))
if count > 0:
    for student in enroll[course]:
        print ("*", student)