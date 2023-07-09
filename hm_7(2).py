class Journal:
    def __init__(self):
        self.students = []

    def add_student(self, name, *grades):
        if len(grades) != 5:
            return f"Ошибка: У студента {name} должно быть 5 оценок."
        for grade in grades:
            if not str(grade).isdigit() or int(grade) > 100:
                return f"Ошибка: Оценки должны состоять только из цифр и не больше 100."
        if not str(name).isalpha():
            return f"Ошибка: Имя студента должно состоять только из букв."
        self.students.append({name: grades})

    def avg (self, *grades):
        avg_grade = sum(grades) / len(grades)
        return avg_grade

    def get_best_student(self):
        best_student = ""
        highest_avg_grade = 0
        for student in self.students:
            name, grades = list(student.items())[0]
            avg_grade = self.avg (*grades)
            if avg_grade > highest_avg_grade:
                highest_avg_grade = avg_grade
                best_student = name
        return best_student, highest_avg_grade

journal = Journal()

print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣦⣄⠀⠀⠛⢿⣿⣿⡿⠛⠀⠀⣠⣴⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣤⡀⠀⢹⡏⠀⢀⣤⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⠀⠛⢿⣿⣦⣼⡇⠀⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣦⣀⠀⠉⠻⢿⣧⣴⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠹⣿⣿⣶⣄⠀⢸⣿⣿⣿⣿⣿⣿⠏⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣆⡀⠀⠙⠿⣿⠀⢸⡿⠋⣿⠿⠋⠀⢀⣰⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠉⠻⣦⣀⠀⠁⠀⢸⡇⠀⠈⠀⣀⣴⠟⠉⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠙⠿⣤⡀⢸⡇⢀⣤⠿⠋⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠈⠻⣿⣿⠟⠁⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
journal.add_student("Алексей", 85, 92, 78, 95, 88)
journal.add_student("Елена", 90, 92, 88, 95, 91)
journal.add_student("Максим", 80, 75, 85, 90, 82)
journal.add_student("Ольга", 95, 88, 92, 90, 89)
journal.add_student("Иван", 86, 92, 79, 88, 90)
best_student, average_grade = journal.get_best_student()
print(f"Лучший студент: {best_student}")
print(f"Средний балл: {average_grade}")
print("Coding by GVNZO")