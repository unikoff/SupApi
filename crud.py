from sqlalchemy.orm import Session
import models, schemas


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Task).offset(skip).limit(limit).all()



def create_tasks(db: Session, task: schemas.Task_Create):
    db_task = models.Task(title=task.title, description=task.description, complited=task.complited)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task



def update_tasks(db: Session, task: schemas.Task_Update):
    db_task = get_task(db, task_id=task.id)
    db_task.title = db_task.title if task.title is None else task.title
    db_task.description = db_task.description if task.description is None else task.description
    db_task.complited = db_task.complited if task.complited is None else task.complited
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_tasks(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return db_task
    return None