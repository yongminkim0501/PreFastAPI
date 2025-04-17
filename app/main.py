'''
CRUD 기능 구현

검사 결과 입력 / 수정 / 삭제
치료 결과 입력 / 수정 / 삭제
환자     추가 / 삭제/ 수정

환자부터 구현 예정
'''
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()