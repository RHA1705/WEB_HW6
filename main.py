from faker import Faker
from random import randint, choice
from datetime import datetime, date

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3

fake = Faker()

# Generowanie listy 20 nazw wykładów
# nazwy_wykladow = [fake.text(max_nb_chars=30) for _ in range(20)]
nazwy_wykladow = []

# Wyświetlenie wygenerowanych nazw
for _ in range(1, 6):
    nazwy_wykladow.append(fake.name())

def generate_groups(groups, students):
    for_groups = []
    for group in range(1, students + 1):
        for_groups.append((randint(1, groups), group))

    return for_groups

def generate_grades():
    for_grades = []
    for month in range(1, 12 + 1):
        # Виконуємо цикл за місяцями'''
        grade_date = datetime(2021, month, randint(1, 31)).date()
        for student in range(1, ):
            # Виконуємо цикл за кількістю співробітників
            for_grades.append((emp, grade_date, randint(1000, 10000)))

if __name__ == '__main__':
    result = generate_groups(NUMBER_GROUPS, NUMBER_STUDENTS)
    print(result)
