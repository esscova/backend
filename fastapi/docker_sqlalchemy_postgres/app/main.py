from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import actions, models, schemas
from . database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


@app.post('/users/', response_model=schemas.User)
def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)):
	db_user = actions.get_user_by_email(db, email=user.email)
	if db_user:
		raise HTTPException(
			status_code=400,
			detail='Email already registered'
			)
	return actions.create_user(db=db, user=user)

@app.get('/users/', response_model=list[schemas.User])
def read_users(skip:int=0, limit:int=100, db:Session = Depends(get_db)):
	users = actions.get_users(db, skip=skip, limit=limit)
	return users

@app.get('/users/{user_id}/', response_model=schemas.User)
def read_user(user_id:int, db:Session = Depends(get_db)):
	db_user = actions.get_user(db, user_id=user_id)
	if db_user is None:
		raise HTTPException(
			status_code=404,
			detail='user not found'
			)
	return db_user

@app.get('/healthcheck')
def healthcheck():
	return {'status':'ok'}