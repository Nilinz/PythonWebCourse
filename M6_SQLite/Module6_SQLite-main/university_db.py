import sqlite3
from faker import Faker
import random

fake = Faker()

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створюємо таблицю студентів
cursor.execute('''CREATE TABLE students
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   group_id INTEGER)''')

# Створюємо таблицю груп
cursor.execute('''CREATE TABLE groups
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT)''')

# Створюємо таблицю викладачів
cursor.execute('''CREATE TABLE teachers
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT)''')

# Створюємо таблицю предметів
cursor.execute('''CREATE TABLE subjects
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   teacher_id INTEGER)''')

# Створюємо таблицю оцінок студентів
cursor.execute('''CREATE TABLE grades
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_id INTEGER,
                   subject_id INTEGER,
                   grade INTEGER,
                   date_received DATE)''')

# Дані для груп
group_names = ['Група 1', 'Група 2', 'Група 3']
for group_name in group_names:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))
    group_id = cursor.lastrowid

    # Дані для студентів у кожній групі
    for _ in range(random.randint(10, 20)):
        student_name = fake.name()
        cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (student_name, group_id))

# Дані для викладачів
teacher_names = [fake.name() for _ in range(3)]
for teacher_name in teacher_names:
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher_name,))
    teacher_id = cursor.lastrowid

    # Дані для предметів, які викладає викладач
    for _ in range(random.randint(3, 5)):
        subject_name = fake.word()
        cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject_name, teacher_id))

# Дані для оцінок студентів
for student_id in range(1, len(group_names) * 20 + 1):
    for subject_id in range(1, len(teacher_names) * 5 + 1):
        grade = random.randint(60, 100)
        date_received = fake.date_between(start_date='-3y', end_date='today')
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)",
                       (student_id, subject_id, grade, date_received))


conn.commit()
conn.close()
