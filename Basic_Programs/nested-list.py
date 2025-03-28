#Find the Second Highest Score
#Given a list of student names and scores, find the second lowest score and print the names of students who have that score in alphabetical order.

students=[]
for x in range(int(input())):
        name = input()
        score = float(input())
        students.append ([name,score])
        
unique_student = sorted(set(score for name,score in students))

second_lowest = unique_student[1]

alphabet_order= sorted(name for name,score in students if score == second_lowest)

for i in alphabet_order:
        print("Second lowest score student"+ i)
