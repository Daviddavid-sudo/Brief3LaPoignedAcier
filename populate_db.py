from faker import Faker
from model import Member, card_acces, Coachs, Course, Inscription
import random
from init_db import *
import datetime

fake = Faker()

def create_n_coach(n):
    specialities = ["Yoga", "CrossFit", "Musculation", "Boxe"]
    for i in range(1,n):
        sport = random.choice(specialities)
        coach = Coachs(name=fake.name(), specialty=sport)
        with Session(engine) as session:
            session.add(coach)
            session.commit()


def create_n_people(n):
    l = [x for x in range(99999,100000+n)]
    for i in range(1,n):
        x = random.choice(l)
        m = Member(name=fake.name(), email=fake.email(), card_acces_id=i)
        card = card_acces(unique_number=x)
        l.remove(x)
        with Session(engine) as session:
            session.add(m)
            session.add(card)
            session.commit()


def create_course_inscriptions():
    list_of_hours = [x for x in range(9,17)]
    count = 1
    for hr in list_of_hours:
        x = random.randint(1,4)
        specialities = ["Yoga", "CrossFit", "Musculation", "Boxe"]
        for i in range(x):
            with Session(engine) as session:
                sport = random.choice(specialities)
                statement = select(Coachs.id).where(Coachs.specialty == sport)
                results = session.exec(statement)
                list_of_possible_coachs = []
                for result in results:
                    list_of_possible_coachs.append(result)
                
                y = random.choice(list_of_possible_coachs)
                course = Course(name=sport, hours = hr, max_capacity=20, coach_id=y)
                session.add(course)
                session.commit()

                nb_of_participants = random.randint(1,20)
                list_of_participants = [x for x in range(1,40)]
                for member in range(1,nb_of_participants):
                    id = random.choice(list_of_participants)
                    inscription_hour = random.randint(0,23)
                    inscription_day = random.randint(1,28)
                    inscription_month = random.randint(1,12)
                    inscription = Inscription(member_id=id, course_id=count, date_inscription=datetime.datetime(2024,inscription_month,inscription_day,inscription_hour,0,0))
                    list_of_participants.remove(id)
                    with Session(engine) as session:
                        session.add(inscription)
                        session.commit()
            count += 1
            specialities.remove(sport)


create_n_people(40)
create_n_coach(20)
create_course_inscriptions()


