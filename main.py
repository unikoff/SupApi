import uvicorn
from fastapi import FastAPI, Depends, HTTPException

import models, schemas, crud
from databese import engine, Session_local
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()


@app.get("/tasks", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks


@app.get("/task/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(404, detail='Task not found')
    return task


@app.post("/create_task", response_model=schemas.Task)
def create_tasks(task: schemas.Task_Create, db: Session = Depends(get_db)):
    return crud.create_tasks(db, task=task)


@app.put("/update_task", response_model=schemas.Task)
def create_tasks(task: schemas.Task_Update, db: Session = Depends(get_db)):
    return crud.update_tasks(db, task=task)


@app.delete("/delete_task/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_tasks(db=db, task_id=task_id)
    if task is None:
        raise HTTPException(404, detail='Task not found')
    return task


if __name__ == '__main__':
    uvicorn.run(app='main:app', port= 8001)