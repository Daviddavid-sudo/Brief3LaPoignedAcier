from init_db import *
from model import Course, Inscription, Member, card_acces, Coachs
import datetime
import pandas as pd

def course_available():
    with Session(engine) as session:
        course_list = select(Course).join(Inscription).group_by(Inscription.course_id).having(20-func.count(Inscription.id)>0)
        results = session.exec(course_list)
        list_of_courses = []
        for course in results:
            list_of_courses.append({
                "course_id": course.id,
                "name": course.name,
                "coach_id": course.coach_id,
                "Time": str(course.hours) + "h"
            })
    
    df = pd.DataFrame(list_of_courses)
    return df

def course_available_list():
    with Session(engine) as session:
        course_list = select(Course).join(Inscription).group_by(Inscription.course_id).having(20-func.count(Inscription.id)>0)
        results = session.exec(course_list)
        list_of_courses = []
        for course in results:
            list_of_courses.append(course)
    
    return list_of_courses


def register_course(coach_id, hour, name, id_member):
    with Session(engine) as session:
        statement = select(Course).where(Course.coach_id == coach_id).where(Course.hours == hour)
        id = session.exec(statement)
        test = []
        value = False
        for result in id:
            test.append(result)

        for i in test:
            value = True

        if value:
            cid = select(Course.id).where(Course.coach_id == coach_id).where(Course.hours == hour)
            testid = session.exec(cid)
            courseid = []
            for i in testid:
                courseid.append(i)
            mb = select(Inscription.member_id).where(Inscription.course_id == courseid[0])
            test3 = session.exec(mb)
            list_of_members = []
            for t in test3:
                list_of_members.append(t)

            if id_member in list_of_members:
                text = 'already subscribed'
                return text
            else:
                new_inscription = Inscription(member_id=id_member,course_id=courseid[0], date_inscription=datetime.datetime.now())
                session.add(new_inscription)
                session.commit()
                text = "sent"
                return text

        else:
            text = "no class available"
            return text

# register_course(coach_id=7,hour=11,name="Boxe", id_member=5)


def Cancel_registration(id):
    with Session(engine) as session:
        statement = select(Inscription).where(Inscription.id == id)
        results = session.exec(statement)
        test = []
        for result in results:
            test.append(result)
            session.delete(result)
            session.commit()

        if len(test) == 0:
            return False
        else:
            return True

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

def class_possible(hr, id_coach, name):
    with Session(engine) as session:
        course = select(Course).where(Course.coach_id == id_coach).where(Course.hours == hr)
        results = session.exec(course)
        course2 = select(Course).where(Course.name == name).where(Course.hours == hr)
        results2 = session.exec(course2)
        test = []
        for result in results:
            test.append(result)
        for result in results2:
            test.append(result)
    return test

# print(class_possible(10,2, "Musculation"))
def add_class(name, hours, max_capacity, coach_id):
    if len(class_possible(hours, coach_id)) == 0 :
        course = Course(name=name, hours=hours, max_capacity=max_capacity, coach_id=coach_id)
        with Session(engine) as session:
            session.add(course)
            session.commit()
        print("possible")
    else:
        print("not possible")

# add_class("Boxe", 15, 20, 1)

def update_class(id, name, hours, max_capacity, coach_id):
    with Session(engine) as session:
        statement = select(Course).join(Coachs).group_by(Course.coach_id).having(Coachs.specialty == name and Course.hours != hours and Course.id == id)
        results = session.exec(statement)
        if len(class_possible(hours, coach_id)) == 0:
            for result in results:
                result.name = name
                result.hours = hours
                result.max_capacity = max_capacity
                result.coach_id = coach_id
                session.add(result)
                session.commit()
        else:
            print("not possible")


# update_class(24, "CrossFit", 15, 20, 5)

def delete_class(id):
    with Session(engine) as session:
        statement = select(Course).where(Course.id == id)
        results = session.exec(statement)
        for result in results:
            session.delete(result)
            session.commit()

# delete_class(24)

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
    df = pd.DataFrame(history)
    return df

# print(registration_history())
