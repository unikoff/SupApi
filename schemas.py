from pydantic import BaseModel


class Task_Base(BaseModel):
    '''the base class that will be inherited in further classes'''
    
    title: str  
    description: str | None = None  
    complited: bool | None = None


class Task_Create(Task_Base):
    '''the class is inherited from the base one, in this case nothing was added'''
    
    pass


class Task_Update(Task_Base):
    '''a clause has been added in the class that the title may not be passed'''
    
    id: int
    title: str | None = None 


class Task(Task_Base):
    '''a class created for the API response'''
    
    id: int
    
    class Config:
        orm_mode: True