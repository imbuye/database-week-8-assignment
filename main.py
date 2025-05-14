from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----- USERS -----
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return crud.get_users(db=db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# ----- TASKS -----
@app.post("/users/{user_id}/tasks/", response_model=schemas.Task)
def create_task(user_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task, user_id=user_id)

@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return crud.get_tasks(db=db, skip=skip, limit=limit)

@app.get("/users/{user_id}/tasks/", response_model=list[schemas.Task])
def read_user_tasks(user_id: int, db: Session = Depends(get_db)):
    return crud.get_tasks_by_user(db=db, user_id=user_id)
