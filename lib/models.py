from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    urgency = Column(Integer, nullable=False)
    importance = Column(Integer, nullable=False)
    priority_score = Column(Integer)

    def __init__(self, title, description, urgency, importance):
        self.title = title
        self.description = description
        self.urgency = urgency
        self.importance = importance
        self.priority_score = urgency * importance

engine = create_engine("sqlite:///tasks.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
