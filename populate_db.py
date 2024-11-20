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


def create_n_cours_inscriptions(n):
    for i in range(1,n):
        random_coach = random.randint(1,6)
        hour = random.randint(9,16)
        with Session(engine) as session:
            statement = select(Coachs.specialty).where(Coachs.id == random_coach)
            results = session.exec(statement)
            for result in results:
                sport = result
            course = Course(name=sport,hours=hour,max_capacity=20,coach_id=random_coach)
            with Session(engine) as session:
                session.add(course)
                session.commit()

            nb_of_participants = random.randint(1,20)
            list_of_participants = [x for x in range(20)]
            for member in range(1,nb_of_participants):
                id = random.choice(list_of_participants)
                inscription_hour = random.randint(0,23)
                inscription_day = random.randint(1,28)
                inscription_month = random.randint(1,12)
                inscription = Inscription(member_id=id, course_id=i, date_inscription=datetime.datetime(2024,inscription_month,inscription_day,inscription_hour,0,0))
                list_of_participants.remove(id)
                with Session(engine) as session:
                    session.add(inscription)
                    session.commit()

create_n_people(20)
create_n_coach(6)
create_n_cours_inscriptions(20)
