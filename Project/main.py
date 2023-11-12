from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/snacks/", response_model=schemas.Snack)
def create_snack(snack: schemas.SnackCreate, db: Session = Depends(get_db)):
    db_snack = crud.get_snack_by_name(db, name=snack.name)
    if db_snack:
        raise HTTPException(status_code=400, detail="Snack with this name already exists")
    return crud.create_snack(db=db, snack=snack)


@app.get("/snacks/", response_model=list[schemas.Snack])
def read_snacks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    snacks = crud.get_snacks(db, skip=skip, limit=limit)
    return snacks


@app.get("/snacks/{snack_id}", response_model=schemas.Snack)
def read_snack(snack_id: int, db: Session = Depends(get_db)):
    db_snack = crud.get_snack(db, snack_id=snack_id)
    if db_snack is None:
        raise HTTPException(status_code=404, detail="Snack not found")
    return db_snack


@app.post("/sodas/", response_model=schemas.Soda)
def create_soda(soda: schemas.SodaCreate, db: Session = Depends(get_db)):
    db_soda = crud.get_soda_by_name(db, name=soda.name)
    if db_soda:
        raise HTTPException(status_code=400, detail="Soda with this name already exists")
    return crud.create_soda(db=db, soda=soda)


@app.get("/sodas/", response_model=list[schemas.Soda])
def read_sodas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sodas = crud.get_sodas(db, skip=skip, limit=limit)
    return sodas


@app.get("/sodas/{soda_id}", response_model=schemas.Soda)
def read_soda(soda_id: int, db: Session = Depends(get_db)):
    db_soda = crud.get_soda(db, soda_id=soda_id)
    if db_soda is None:
        raise HTTPException(status_code=404, detail="Soda not found")
    return db_soda


@app.delete("/snacks/{snack_id}", response_model=schemas.Snack)
def delete_snack(snack_id: int, db: Session = Depends(get_db)):
    db_snack = crud.get_snack(db, snack_id=snack_id)
    if db_snack is None:
        raise HTTPException(status_code=404, detail="Snack not found")

    crud.delete_snack(db=db, snack_id=snack_id)
    return db_snack


@app.delete("/sodas/{soda_id}", response_model=schemas.Soda)
def delete_soda(soda_id: int, db: Session = Depends(get_db)):
    db_soda = crud.get_soda(db, soda_id=soda_id)
    if db_soda is None:
        raise HTTPException(status_code=404, detail="Soda not found")

    crud.delete_soda(db=db, soda_id=soda_id)
    return db_soda