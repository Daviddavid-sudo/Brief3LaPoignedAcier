from faker import Faker
from model import Member, card_acces, Coachs, Course, Inscription
import random
from init_db import *


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

# person1=Member(name="david",email="david@gmail.com", card_acces_id=1)
# with Session(engine) as session:
#     session.add(person1)
#     # session.add(card)
#     session.commit()


create_n_people(10)
# create_n_coach(5)
