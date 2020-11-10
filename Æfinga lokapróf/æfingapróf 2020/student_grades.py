# æfingpróf 2020
# dæmi 1

MAX_STUDENTS = 2
MAX_GRADES = 3
# nota dict með values sem er einkunnalist raða key í stafrósröð



def students_and_grades():
    ''' takes input of students and grades and puts in dictionary '''
    student_count = 0
    student_grades_dict = dict()
    while student_count != MAX_STUDENTS:
        name = input('Student name: ')
        grade_count = 1 # byrjar á einum fyrir input
        grade_list = []
        while grade_count != MAX_GRADES +1:
            grade = float(input(f'Input grade number {grade_count}: '))
            grade_list.append(grade)
            grade_count += 1
        student_count += 1
        student_grades_dict[name] = grade_list
    sorted_dict = dict(sorted(student_grades_dict.items()))
    return sorted_dict

def print_students(students_grades):
    outcome = ''
    for key in students_grades:
        print('Student list:')
        print(f'{key}: {students_grades[key]}')

def grade_avg(students_grades):
    students_grades_avg = dict()
    for key in students_grades:
        students_grades_avg[key] = sum(students_grades[key]) / len(students_grades[key])
    return students_grades_avg

def pick_the_dux(students_grades_avg):
    inverse = [(value, key) for key, value in students_grades_avg.items()]
    print(max(inverse))
    print('Student with highest average grade:')
    print('%s has an average grade of %.2f'% (max(inverse)[1],students_grades_avg[max(inverse)[1]]))


def get_student_with_highest_average_grade(students_dict): # fall úr lausnum, avg og stdent eru saman
    ''' Finds the student with the highest average.
        Returns both the student name and the corresponding average grade '''
    highest_average_grade = 0.0
    name = ""
    for student, grades in sorted(students_dict.items()):
        average_grade = sum(grades) / len(grades)
        if average_grade > highest_average_grade:
            highest_average_grade = average_grade
            name = student
    return (name, highest_average_grade)


def main():
    students_grades = students_and_grades()
    # print(students_grades)
    print_students(students_grades)
    students_grades_avg = grade_avg(students_grades)
    pick_the_dux(students_grades_avg)
main()










