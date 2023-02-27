from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import engine, get_db
from .. import oauth2
from typing import List, Optional
from sqlalchemy import func


router = APIRouter(
    prefix= '/posts',
    tags = ['Posts']
    
)


@router.get("/")
def root(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user), limit: int = 5, skip:int = 0, search: Optional[str] = " "):

    new_post= db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join( 
        models.Vote, models.Post.id == models.Vote.post_id, isouter = True ).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
       

    # cursor.execute("""SELECT * FROM posts""")
    # post = cursor.fetchall()
    return  results




@router.get("/{id}", response_model= schemas.Post)
def get_post(id: int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user) ):

    post_index = db.query(models.Post).filter(models.Post.id == id).first()

    # cursor.execute("""SELECT *FROM posts WHERE id = %s """, str((id)))
    # post_index = cursor.fetchone()

    if not post_index:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)

    if post_index.owner_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=f"not authorised to perorm this action")

    return post_index



@router.post("/", status_code= status.HTTP_201_CREATED, response_model= schemas.Post)
def create_post(post:schemas.PostCreate,  db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    # cursor.execute("""INSERT INTO posts (content,title, published) VALUES (%s,%s, %s) RETURNING * """,(post.content, post.title, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    return  new_post


@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    delete_post = db.query(models.Post).filter(models.Post.id == id)

    post = delete_post.first()


    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", str((id)))
    # delete_post = cursor.fetchone()
    # conn.commit()

    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)

    if post.owner_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=f"not authorised to perorm this action")

    delete_post.delete(synchronize_session= False)
    db.commit()
    



@router.put("/{id}", response_model= schemas.Post)
def update_post(id: int, updated_post:schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    update_post = db.query(models.Post).filter(models.Post.id == id)
    post = update_post.first()

    # cursor.execute("""UPDATE posts SET content = %s, title = %s, published = %s WHERE id = %s RETURNING * """, (post.content, post.title, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)

    if post.owner_id != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=f"not authorised to perorm this action")

    update_post.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return update_post.first()
