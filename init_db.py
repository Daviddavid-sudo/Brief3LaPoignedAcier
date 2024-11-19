from sqlmodel import Field, Session, SQLModel, create_engine
import model


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():  
    create_db_and_tables()   


if __name__ == "__main__":  
    main()