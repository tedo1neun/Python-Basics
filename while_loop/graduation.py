name = input()
grade = 0
sum_grades = 0
bad_grade = 0

while True:
    year_grades = float(input())

    if year_grades < 4.00:
        bad_grade += 1
        if bad_grade == 2:
            grade += 1
            print(f'{name} has been excluded at {grade} grade')
            break

    if year_grades >= 4.00:
        sum_grades += year_grades
        grade += 1

    if grade == 12:
        print(f'{name} graduated. Average grade: {sum_grades / grade:.2f}')
        break




