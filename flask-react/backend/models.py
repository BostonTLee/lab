from sqlalchemy import Table, Column, MetaData, Integer, Computed, String
from sqlalchemy.orm import declarative_base

#metadata = MetaData()

Base = declarative_base()

class TestData(Base):
    __tablename__ = "data"
    id = Column(
        Integer, primary_key=True
    )
    data = Column(String)
