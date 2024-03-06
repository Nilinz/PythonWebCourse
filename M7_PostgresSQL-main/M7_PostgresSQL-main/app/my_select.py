from sqlalchemy import func, desc
from models import Student, Subject, Grade, Teacher, Group, Base


#Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1(session):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
#Знайти студента із найвищим середнім балом з певного предмета.
def select_2(session, subject_id):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade, Student.id == Grade.student_id)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()
#Знайти середній бал у групах з певного предмета.
def select_3(session, subject_id):
    return session.query(Group.group_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Student, Group.id == Student.group_id)\
        .join(Grade, Student.id == Grade.student_id)\
        .filter(Grade.subject_id == subject_id)\
#Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4(session):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()
#Знайти які курси читає певний викладач.
def select_5(session, teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()
#Знайти список студентів у певній групі.
def select_6(session, group_id):
    return session.query(Student.fullname).filter(Student.group_id == group_id).all()
#Знайти оцінки студентів у окремій групі з певного предмета.
def select_7(session, group_id, subject_id):
    return session.query(Grade.grade).join(Student).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()
#Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(session, teacher_id):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Subject).filter(Subject.teacher_id == teacher_id).scalar()
#Знайти список курсів, які відвідує певний студент.
def select_9(session, student_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).all()
#Список курсів, які певному студенту читає певний викладач.
def select_10(session, student_id, teacher_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).all()