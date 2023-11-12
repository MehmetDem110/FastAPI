from sqlalchemy.orm import Session

import models
import schemas


def get_snack(db: Session, snack_id: int):
    return db.query(models.Snack).filter(models.Snack.id == snack_id).first()


def get_snack_by_name(db: Session, name: str):
    return db.query(models.Snack).filter(models.Snack.name == name).first()


def get_snacks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Snack).offset(skip).limit(limit).all()


def create_snack(db: Session, snack: schemas.SnackCreate):
    db_snack = models.Snack(name=snack.name, description=snack.description)
    db.add(db_snack)
    db.commit()
    db.refresh(db_snack)
    return db_snack


def get_sodas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Soda).offset(skip).limit(limit).all()


def get_soda(db: Session, soda_id: int):
    return db.query(models.Soda).filter(models.Soda.id == soda_id).first()


def get_soda_by_name(db: Session, name: str):
    return db.query(models.Soda).filter(models.Soda.name == name).first()

def create_soda(db: Session, soda: schemas.SodaCreate):
    db_soda = models.Soda(name=soda.name, flavor=soda.flavor)
    db.add(db_soda)
    db.commit()
    db.refresh(db_soda)
    return db_soda


def delete_snack(db: Session, snack_id: int):
    snack = db.query(models.Snack).filter(models.Snack.id == snack_id).first()
    if snack:
        db.delete(snack)
        db.commit()
        db.refresh(snack)
        return snack
    return None


def delete_soda(db: Session, soda_id: int):
    soda = db.query(models.Soda).filter(models.Soda.id == soda_id).first()
    if soda:
        db.delete(soda)
        db.commit()
        db.refresh(soda)
        return soda
    return None