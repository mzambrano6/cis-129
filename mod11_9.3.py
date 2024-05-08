import csv

file = open('grades.csv', 'w', newline='')

writer = csv.writer(file)

writer.writerow(['Name', 'Exam 1', 'Exam 2', 'Exam 3'])

num_student = int(input('Enter number of students: '))

for student in range(num_student):
    name = input("Enter students names: ")

    exam1 = int(input('Enter firt score: '))
    exam2 = int(input('Enter second score: '))
    exam3 = int(input('Enter third score: '))

    writer.writerow([name, exam1, exam2, exam3])

file.close
print('Data written to grades.csv')
