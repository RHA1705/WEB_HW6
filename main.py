from faker import Faker
from random import randint, choice

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3

fake = Faker()

# Generowanie listy 20 nazw wykładów
# nazwy_wykladow = [fake.text(max_nb_chars=30) for _ in range(20)]
nazwy_wykladow = []

# Wyświetlenie wygenerowanych nazw
for _ in range(1, 6):
    nazwy_wykladow.append(fake.name())

def generate(groups, students):
    for_groups = []
    for group in range(1, students + 1):
        for_groups.append((group, randint(1, groups)))

    return for_groups

if __name__ == '__main__':
    result = generate(NUMBER_GROUPS, NUMBER_STUDENTS)
    print(result)
