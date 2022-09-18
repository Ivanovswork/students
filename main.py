class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_of_students.keys():
                lecturer.grades_of_students[course] += [grade]
            else:
                lecturer.grades_of_students[course] = [grade]
        else:
            return 'Ошибка'

    def _average_value(self):
        count_of_grades = 0
        abs_value = 0
        for elem in self.grades.values():
            count_of_grades += len(elem)
            elem = list(map(int, elem))
            abs_value += sum(elem)
        return abs_value / count_of_grades

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашнее задание: {Student._average_value(self)} \n' \
               f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)} \n' \
               f'Завершенные курсы: {" ".join(self.finished_courses)}'

    def __lt__(self, other):
        # if self._average_value() > other._average_value():
        #     return f"у {self}больше чем у {other}"
        # elif self._average_value() == other._average_value():
        #     return f"у {self} такая жекак и у {other}"
        # else:
        #     return f"у {other} больше чем у {self}"
        if isinstance(other, Student):
            return self._average_value() > other._average_value()
        else:
            return 'ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_of_students = {}

    def _average_value(self):
        count_of_grades = 0
        abs_value = 0
        for elem in self.grades_of_students.values():
            count_of_grades += len(elem)
            elem = list(map(int, elem))
            abs_value += sum(elem)
        return abs_value / count_of_grades

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {Lecturer._average_value(self)}'

    def __lt__(self, other):
        # if self.average_value() > other.average_value():
        #     return f"у {self} больше чем у {other}"
        # elif self.average_value() == other.average_value():
        #     return f"у {self} такая же как и у {other}"
        # else:
        #     return f"у {other} больше чем у {self}"
        if isinstance(other, Lecturer):
            return self._average_value() > other._average_value()
        else:
            return 'ошибка'


def value_students(list_of_names, course):
    count_of_student = 0
    value = 0
    for student in list_of_names:
        if isinstance(student, Student) and course in student.courses_in_progress:
            value += student._average_value()
            count_of_student += 1
    return value / count_of_student


def value_lecturers(list_of_names, course):
    count_of_lecturer = 0
    value = 0
    for lecturer in list_of_names:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            value += lecturer._average_value()
            count_of_lecturer += 1
    return value / count_of_lecturer


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
bad_student = Student('Pall', 'Derfantos', 'your_gender')
bad_student.courses_in_progress += ['Python']

lector1 = Lecturer('lec', 'tor')
lector1.courses_attached += ['Python']
lector2 = Lecturer('asdf', 'fdsa')
lector2.courses_attached += ['Python']

reviewer1 = Reviewer('qwert', 'trewq')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('bnm', 'mnb')
reviewer2.courses_attached += ['Python']

best_student.rate_lecturer(lector1, 'Python', 10)
best_student.rate_lecturer(lector1, 'Python', 5)
best_student.rate_lecturer(lector1, 'Python', 9)

best_student.rate_lecturer(lector2, 'Python', 10)
best_student.rate_lecturer(lector2, 'Python', 5)
best_student.rate_lecturer(lector2, 'Python', 9)

reviewer1.rate_hw(bad_student, 'Python', 2)
reviewer1.rate_hw(bad_student, 'Python', 2)
reviewer1.rate_hw(bad_student, 'Python', 2)

reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 10)

l = [best_student, bad_student]
course = 'Python'

l2 = [lector1, lector2]
course2 = 'Python'

print(best_student > bad_student)
print(lector2 > lector1, '\n')
print(best_student, "\n")
print(lector1, "\n")
print(reviewer1, "\n")
print(value_students(l, course))
print(value_lecturers(l2, course2))
