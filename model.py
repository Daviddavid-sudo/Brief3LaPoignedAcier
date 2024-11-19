from sqlmodel import Field, SQLModel
from typing import Optional
import datetime
# from init_db import main


class Member(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    card_acces_id: int | None = Field(default=None, foreign_key="card_acces.id")

class card_acces(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    unique_number: int

class Coachs(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    specialty: str

class Course(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    hours: datetime
    max_capacity: int = None
    coach_id: int | None = Field(default=None, foreign_key="coachs.id")
  
class Inscription(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    member_id: int | None = Field(default=None, foreign_key="member.id")
    course_id: int | None = Field(default=None, foreign_key="course.id")
    date_inscription: datetime
