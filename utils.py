from init_db import *
from model import Course, Inscription, Member, card_acces, Coachs
import datetime

def course_available():
    with Session(engine) as session:
        course_list = select(Course).join(Inscription).group_by(Inscription.course_id).having(20-func.count(Inscription.id)>0)
        results = session.exec(course_list)
        list_of_courses = []
        for course in results:
            list_of_courses.append(course)
    
    return list_of_courses

def class_possible(coach_id,name,hours,id):
    with Session(engine) as session:
        statement = select(Course).join(Coachs).group_by(Course.coach_id).having(Coachs.specialty == name and Course.hours != hours and Course.id == id and Coachs.id == coach_id)
        results = session.exec(statement)
        list_of_courses=[]
        for course in results:
            list_of_courses.append(course)

# print(course_available())

def register_course(id, coach_id, hour, name, id_member):
    with Session(engine) as session:
        if Course(id=id,max_capacity=20, hours=hour,name=name,coach_id=coach_id) in course_available():
            member_hours = select(Course).join(Inscription).group_by(Course.hours, Inscription.member_id).having(Inscription.member_id == id_member)
            results = session.exec(member_hours)
            list_of_impossible_hours = []
            for result in results:
                list_of_impossible_hours.append(result.hours)
                print(result)

            if hour not in list_of_impossible_hours:
                new_inscription = Inscription(member_id=id_member,course_id=id, date_inscription=datetime.datetime.now())
                session.add(new_inscription)
                session.commit()
                print('sent')
            
            else:
                print("already another class at this time")
            
        
        else:
            print("untraceable")


# register_course(id=1,coach_id=4,hour=10,name="Boxe", id_member=1)


def Cancel_registration(id):
    with Session(engine) as session:
        statement = select(Inscription).where(Inscription.id == id)
        results = session.exec(statement)
        for result in results:
            session.delete(result)
            session.commit()


# Cancel_registration(5)

def add_coach(name, specaility):
    coach = Coachs(name=name, specialty=specaility)
    with Session(engine) as session:
        session.add(coach)
        session.commit()

# add_coach('David Scott', "CrossFit")

def update_coach(id, name, speciality):
    with Session(engine) as session:
        statement = select(Coachs).where(Coachs.id == id)
        results = session.exec(statement)
        for result in results:
            result.name = name
            result.specialty = speciality
            session.add(result)
            session.commit()


# update_coach(6, 'David David', "Yoga")

def delete_coach(id):
    with Session(engine) as session:
        statement = select(Coachs).where(Coachs.id == id)
        results = session.exec(statement)
        for result in results:
            session.delete(result)
            session.commit()

# delete_coach(3)

def add_class(id, name, hours, max_capacity, coach_id):
    course = Course(id=id, name=name, hours=hours, max_capacity=max_capacity, coach_id=coach_id)
    if class_possible(coach_id,name,hours,id) is not None:
        with Session(engine) as session:
            session.add(course)
            session.commit()
        print("possible")
    else:
        print("not possible")

# add_class(2, "Boxe", 9, 20, 5)

def update_class(id, name, hours, max_capacity, coach_id):
    with Session(engine) as session:
        statement = select(Course).join(Coachs).group_by(Course.coach_id).having(Coachs.specialty == name and Course.hours != hours and Course.id == id)
        results = session.exec(statement)
        for result in results:
            result.name = name
            result.hours = hours
            result.max_capacity = max_capacity
            result.coach_id = coach_id
            session.add(result)
            session.commit()


# update_class(2, "Boxe", 14, 20, 5)

def delete_class(id):
    with Session(engine) as session:
        statement = select(Course).where(Course.id == id)
        results = session.exec(statement)
        for result in results:
            session.delete(result)
            session.commit()

# delete_class(2)

def registration_history():
    with Session(engine) as session:
        statement = (select(
            Inscription.member_id,
            Inscription.course_id,
            Inscription.date_inscription,
            Course.name,
            Course.hours
            )
        .join(Course, Course.id == Inscription.course_id)  
        )
        results = session.exec(statement)
        session.commit()

        history = []
        for row in results:
            history.append({
                "member_id": row.member_id,
                "cours_id": row.course_id,
                "nom": row.name,
                "horaire": row.hours,
                "date_inscription": row.date_inscription,
            })
    return history
print(registration_history())
