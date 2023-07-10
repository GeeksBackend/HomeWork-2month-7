class Journal:
    def __init__(self):
        self.students = {}

    def add_grades(self, student_name, *grades):
        if len(grades) != 5:
            print("Ошибка: Количество оценок должно быть равно 5.")
            return

        if student_name not in self.students:
            self.students[student_name] = []

        self.students[student_name].extend(grades)

    def calculate_average_grade(self, *grades):
        if len(grades) != 5:
            print("Ошибка: Количество оценок должно быть равно 5.")
            return

        average_grade = sum(grades) / len(grades)
        return average_grade

    def get_best_student(self):
        best_student = ""
        best_average_grade = 0

        for student, grades in self.students.items():
            average_grade = self.calculate_average_grade(*grades)

            if average_grade > best_average_grade:
                best_student = student
                best_average_grade = average_grade

        return best_student, best_average_grade

journal = Journal()
journal.add_grades("Lol", 85, 92, 78, 90, 88)
journal.add_grades("Aigerim", 75, 80, 82, 79, 88)
journal.add_grades("Nurbolot", 95, 98, 92, 96, 90)
journal.add_grades("Asema", 88, 85, 82, 86, 90)
journal.add_grades("Nurs", 92, 94, 89, 91, 90)

best_student, best_average_grade = journal.get_best_student()
print("Лучший ученик:", best_student)
print("Средний балл:", best_average_grade)