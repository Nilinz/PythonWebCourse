from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy.orm import configure_mappers
from models import Student, Subject, Grade, Teacher, Group, Base
from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10

# Підключення до бази даних
engine = create_engine("postgresql://postgres:mysecretpassword@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()

# Здійснюємо вибірку 1
result_1 = select_1(session)
print("Результат вибірки 1:")
print(result_1)

# Здійснюємо вибірку 2
subject_id = 1  # Припустимо, що ви хочете знайти студента з предмета з ID=1
result_2 = select_2(session, subject_id)
print("Результат вибірки 2:")
print(result_2)

# Здійснюємо вибірку 3
result_3 = select_3(session, subject_id)
print("Результат вибірки 3:")
print(result_3)

# Здійснюємо вибірку 4
result_4 = select_4(session)
print("Результат вибірки 4:")
print(result_4)

# Здійснюємо вибірку 5
teacher_id = 2  # Припустимо, що ви хочете знайти курси викладача з ID=1
result_5 = select_5(session, teacher_id)
print("Результат вибірки 5:")
print(result_5)

# Здійснюємо вибірку 6
group_id = 1  # Припустимо, що ви хочете знайти студентів у групі з ID=1
result_6 = select_6(session, group_id)
print("Результат вибірки 6:")
print(result_6)

# Здійснюємо вибірку 7
result_7 = select_7(session, group_id, subject_id)
print("Результат вибірки 7:")
print(result_7)

# Здійснюємо вибірку 8
result_8 = select_8(session, teacher_id)
print("Результат вибірки 8:")
print(result_8)

# Здійснюємо вибірку 9
student_id = 1  # Припустимо, що ви хочете знайти курси студента з ID=1
result_9 = select_9(session, student_id)
print("Результат вибірки 9:")
print(result_9)

# Здійснюємо вибірку 10
result_10 = select_10(session, student_id, teacher_id)
print("Результат вибірки 10:")
print(result_10)

# Закриваємо сесію
session.close()
