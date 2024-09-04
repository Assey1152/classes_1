class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = 0

    def __str__(self):
        info = [f'Имя: {self.name}',
                f'Фамилия: {self.surname}',
                f'Средняя оценка за домашние задания: {self.avg_grade}',
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}',
                f'Завершенные курсы: {", ".join(self.finished_courses)}']
        return '\n'.join(info)

    def __lt__(self, other):
        return self.avg_grade < other.avg_grade

    def __le__(self, other):
        return self.avg_grade <= other.avg_grade

    def __eq__(self, other):
        return self.avg_grade == other.avg_grade

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            lecturer.update_avg_grade()
        else:
            return 'Ошибка'

    def update_avg_grade(self):
        self.avg_grade = sum([sum(grade_list) / len(grade_list) for grade_list in self.grades.values()])
        self.avg_grade /= len(self.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grade = 0

    def __str__(self):
        info = [f'Имя: {self.name}',
                f'Фамилия: {self.surname}',
                f'Средняя оценка за лекции: {self.avg_grade}']
        return '\n'.join(info)

    def __lt__(self, other):
        return self.avg_grade < other.avg_grade

    def __le__(self, other):
        return self.avg_grade <= other.avg_grade

    def __eq__(self, other):
        return self.avg_grade == other.avg_grade

    def update_avg_grade(self):
        self.avg_grade = sum([sum(grade_list) / len(grade_list) for grade_list in self.grades.values()])
        self.avg_grade /= len(self.grades)


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            student.update_avg_grade()
        else:
            return 'Ошибка'


def avg_student_grade(students, course):
    suma = 0
    cnt = 0
    for student in students:
        if course in student.grades:
            suma += sum(student.grades[course])
            cnt += len(student.grades[course])
    return suma/cnt


def avg_lecturer_grade(lecturers, course):
    suma = 0
    cnt = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            suma += sum(lecturer.grades[course])
            cnt += len(lecturer.grades[course])
    return suma/cnt


best_student = Student('Ruoy', 'Eman', 'Female')
best_student.courses_in_progress += ['Python', 'Java']

avg_student = Student('Peter', 'Parker', 'Spider')
avg_student.courses_in_progress += ['Python', 'C']

cool_lecturer = Lecturer('Cool', 'Lecturer')
cool_lecturer.courses_attached += ['Python', 'Java']

norm_lecturer = Lecturer('Normal', 'Lecturer')
norm_lecturer.courses_attached += ['Python', 'C']

cool_reviewer = Reviewer('Some', 'Reviewer')
cool_reviewer.courses_attached += ['Python', 'Java']

norm_reviewer = Reviewer('Normal', 'Man')
norm_reviewer.courses_attached += ['Python', 'C']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 5)

norm_reviewer.rate_hw(avg_student, 'Python', 5)
norm_reviewer.rate_hw(avg_student, 'C', 7)

best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Java', 5)

avg_student.rate_lecturer(norm_lecturer, 'Python', 5)
avg_student.rate_lecturer(norm_lecturer, 'C', 7)

print(best_student)
print(cool_lecturer)
print(cool_reviewer)

print(best_student > avg_student)
print(best_student == avg_student)
print(best_student <= avg_student)

print(cool_lecturer > norm_lecturer)
print(cool_lecturer == norm_lecturer)
print(cool_lecturer <= norm_lecturer)

print(avg_student_grade([best_student, avg_student], 'Python'))
print(avg_lecturer_grade([cool_lecturer, norm_lecturer], 'Python'))
