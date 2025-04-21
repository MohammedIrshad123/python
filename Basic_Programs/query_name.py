
# - Progame to find the average for a student in a dictionary and avergae value should be upto two decimal places

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

sum_student = student_marks[query_name]
avg = sum(sum_student)/len(sum_student)
two_decimal = "{:.2f}".format(avg)
print("Avera value upto two decimal places",format(two_decimal))

