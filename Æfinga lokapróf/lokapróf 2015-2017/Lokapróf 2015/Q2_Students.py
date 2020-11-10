class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = int(grade)

    # def __gt__(self, other):
    #     return self.rating > other.rating

    def get_grade(self):
        return self.grade
    def __str__(self):
        return ('Name: {}\nGrade: {}'.format(self.name, self.grade))


def read_students():
        student = input('Name: ')
        grade = float(input('Grade: '))
        print()
        return student, grade


def get_average_grade(grades):
    total = 0

    for grade in grades:
        total += grade.get_grade()
    return total / len(grades)
def get_highest_grade(student_grades):
    highest_grade = student_grades[0]
    for grade in student_grades:
        if grade.get_grade() > highest_grade.get_grade():
            highest_grade = grade
    return highest_grade




def main():
    student_grades = []
    nr_of_students = int(input('Input nr. of students: '))
    for i in range(nr_of_students):

        student, grade = read_students()
        student_grade = Student(student,grade)
        student_grades.append((student_grade))

    highest_grade = get_highest_grade(student_grades)
    print('Highest student: ')
    print(highest_grade)
    print()
    average_grade = get_average_grade(student_grades)
    print('Average grade: {}'.format(average_grade))

main()