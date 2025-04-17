from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

#from database import get_db
#import models, schemas
router = APIRouter(
    prefix= "/patients",
    tags=["patients"],
    responses={404:{"description":"Not found"}}
)

@router.post("/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

