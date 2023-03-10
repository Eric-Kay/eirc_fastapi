from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from ..database import engine, get_db
from typing import List



router = APIRouter(
    prefix= '/users',
    tags= ['Users']
   
)

@router.post("/", status_code= status.HTTP_201_CREATED, response_model= schemas.UserOut)
def create_user(user: schemas.userCreate, db: Session = Depends(get_db)):


    hashed = utils.hash(user.password)
    user.password = hashed
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", status_code= status.HTTP_201_CREATED, response_model= schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    getUser = db.query(models.User).filter(models.User.id == id).first()

    if not getUser:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f"this id: {id} cannot be found")

    return getUser

