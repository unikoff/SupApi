from sqlalchemy import Column, Integer, String, Boolean
from databese import Base

class Task(Base):
    __tablename__ = 'Task'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True) 
    complited = Column(Boolean, default=False)