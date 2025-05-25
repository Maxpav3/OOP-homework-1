class Student:
    student_list = []
    def __init__(self, student_name, student_surname):
        self.student_name = student_name
        self.student_surname = student_surname
        self.student_course = []
        self.finished_courses = []
        self.grade = {}
        Student.student_list.append(self)

    @classmethod
    def get_instances(cls):
        return cls.student_list

    @classmethod
    def stulist(cls):
        for student in cls.student_list:
            print(f'{student.student_name}')


    def grading_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.teaching_course and course in self.student_course:
            if course not in lecturer.grade_f_stu:
                lecturer.grade_f_stu[course] = grade
            else:
                lecturer.grade_f_stu[course] += grade
        else:
            print('Error')

    def average_rating(self):
        counts = len(self.grade)
        sums = 0
        for grade in self.grade.values():
            sums += grade
        return sums / counts

    def __str__(self):
        return f' Name: {self.student_name}\n Surname: {self.student_surname}\n Средняя оценка за домашние задания: {self.average_rating()}\n Курсы в процессе изучени: {self.student_course}\n Завершенные курсы: {self.finished_courses}'
    def __eq__(self, other):
        return self.average_rating() == other.average_rating()
    def __lt__(self, other):
        return self.average_rating() < other.average_rating()
    def __le__(self, other):
        return self.average_rating() <= other.average_rating()


class Mentor:

    def __init__(self, mentor_name, mentor_surname):
        self.mentor_name = mentor_name
        self.mentor_surname = mentor_surname
        self.teaching_course = []


class Reviewer(Mentor):

    def __init__(self, mentor_name, mentor_surname):
        super().__init__(mentor_name, mentor_surname)

    def grading_student(self, course, grade, student):
        if isinstance(student, Student) and course in student.student_course and course in self.teaching_course:
            if course not in student.grade:
                student.grade[course] = grade
            else:
                student.grade[course] += grade
        else:
            print("Error")

    def __str__(self):
        return f' Name: {self.mentor_name}\n Surname: {self.mentor_surname}'


class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, mentor_name, mentor_surname):
        super().__init__(mentor_name, mentor_surname)
        self.grade_f_stu = {}
        Lecturer.lecturer_list.append(self)

    @classmethod
    def get_instances(cls):
        return cls.lecturer_list

    @classmethod
    def lectlist(cls):
        for lecturer in cls.lecturer_list:
            print(f'{lecturer.mentor_name}')

    def avarage_rating(self):
        counts = len(self.grade_f_stu)
        sums = 0
        for grade in self.grade_f_stu.values():
            sums += grade
        return sums / counts
    def __str__(self):
        return f' Name: {self.mentor_name}\n Surname: {self.mentor_surname}\n Средняя оценка за лекций: {self.avarage_rating()}'

    def __eq__(self, other):
        return self.avarage_rating() == other.avarage_rating()
    def __lt__(self, other):
        return self.avarage_rating() < other.avarage_rating()
    def __le__(self, other):
        return self.avarage_rating() <= other.avarage_rating()

def average_homework_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grade:
            total += student.grade[course]
            count += 1
    if count == 0:
        return "No grades available"
    return total / count

def average_lecture_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grade_f_stu:
            total += lecturer.grade_f_stu[course]
            count += 1
    if count == 0:
        return "No grades available"
    return total / count


#Студенты
student_alex = Student('alex','pavlov')
student_alex.student_course.append('math')
student_gleb = Student('gleb','kostin')
student_gleb.student_course.append('math')
#Лекторы
lecturer_ivan = Lecturer('ivan', 'abrekosov')
lecturer_ivan.teaching_course.append('math')
lecturer_slav = Lecturer('slav', 'rostik')
lecturer_slav.teaching_course.append('math')
#Проверяюшие
reviewer_evgeny = Reviewer('evgeny', 'dostoevski')
reviewer_evgeny.teaching_course.append('math')
reviewer_tomas = Reviewer('tomas', 'krostin')
reviewer_tomas.teaching_course.append('math')

print()
reviewer_evgeny.grading_student('math', 10, student_alex)
reviewer_tomas.grading_student('math', 9, student_gleb)
print()
print(student_alex)
print()
print(student_gleb)
print()
print(f'Alex grade >= Student grade: {student_alex >= student_gleb}')
print(f'Alex grade >= Student grade: {student_alex == student_gleb}')
print(f'Alex grade >= Student grade: {student_alex > student_gleb}')
print()
student_alex.grading_lecturers(lecturer_ivan, 'math', 8)
student_gleb.grading_lecturers(lecturer_slav, 'math', 9)
print()
print(lecturer_ivan)
print()
print(lecturer_slav)
print()
print(f'lecturer_ivan <= lecturer_slav: {lecturer_ivan <= lecturer_slav}')
print(f'lecturer_ivan != lecturer_slav: {lecturer_ivan != lecturer_slav}')
print(f'lecturer_ivan < lecturer_slav: {lecturer_ivan < lecturer_slav}')
print()
print()
print(reviewer_evgeny)
print()

print(f'Средняя оценка студентов: {average_lecture_grade(Lecturer.get_instances(), 'math')}')

print(f'Средняя оценка лекторов: {average_homework_grade(student_alex.get_instances(), 'math')}')