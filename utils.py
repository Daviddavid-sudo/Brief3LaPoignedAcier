from sqlmodel import session, select
from model import Course, Inscription, Member, card_acces, Coachs
import datetime

def course_available():
    course_list = session.exec(select(Course)).all()
    result = []

    for Course in course_list:
        inscriptions = session.exec(select(Inscription).where(Inscription.course_id == Course.id)).all()

    remaining_space = Course.max_capacity - len(inscriptions)
     
    result.append({
            "id": Course.id,
            "nom": Course.name,
            "horaire": Course.hours,
            "remaining_space": remaining_space,
        })


def register_course():
    Course = session.get(Course.id)
    if not Course:
       return "untraceable"
   
    inscription = session.exec(select(Inscription).where(Inscription.course_id == Course.id)).all()

    if len(inscription) == Course.max_capacity:
       return "full course"
   
    Member.inscription = session.exec(select(Course).join(Inscription).where(Inscription.member_id == Member.id).all)

    if any(Course.hours == Course.hours for Course in Member.inscription):
        return "Conflit d'horaires avec un autre cours."

    # Si toutes les vérifications sont réussies, on crée une nouvelle inscription
    inscription = Inscription(
        member_id = Member.id,
        cours_id = Course.id,
        date_inscription = datetime.now()  
    )
    session.add(inscription)  
    session.commit()  
    return "Inscription réussie."



def Cancel_registration():
    Inscription = session.get(Inscription.id)

    session.delete(Inscription)
    session.commit()
    return "Inscription annulée"
