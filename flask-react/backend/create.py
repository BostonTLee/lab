from sqlalchemy import create_engine
from models import Base, TestData

if __name__ == "__main__":
    engine = create_engine("sqlite:////home/boston/test.db", echo=True, future=True)
    Base.metadata.create_all(engine)
