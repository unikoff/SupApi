from pydantic import BaseModel


class Task_Base(BaseModel):
    title: str  
    description: str | None = None  
    complited: bool | None = None


class Task_Create(Task_Base):
    pass


class Task_Update(Task_Base):
    id: int
    title: str | None = None 


class Task(Task_Base):
    id: int
    
    class Config:
        orm_mode: True