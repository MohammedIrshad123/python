# Find the Second Highest Score
# Given a list of student names and scores, find the second highest score and print the names of students who have that score in alphabetical order.
students=[]
for x in range(int(input())):
        name = input()
        score = float(input())
        students.append ([name,score])
        
unique_student = sorted(set(score for name,score in students), reverse=True)
second_largest = unique_student[1]
alphabet_order= sorted(name for name,score in students if score == second_largest)
for i in alphabet_order:
        print("Second largest score student" + i)
