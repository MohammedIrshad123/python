students = []
threshold_score = 90

# Input student data
for _ in range(int(input("Enter number of students: "))):
    name = input("Enter name: ")
    score = int(input("Enter score: "))
    students.append([name, score])

# Filtering students who scored above the threshold
above_students = [name for name, score in students if score > threshold_score]

# Sorting names alphabetically
above_students.sort()

# Printing the results
for student in above_students:
    print(student)
