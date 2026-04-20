from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.field import Field as FieldModel
from schemas.field import Field, FieldCreate
from auth.security import oauth2_scheme

router = APIRouter(prefix="/fields", tags=["Fields"])

# 1. CREATE: Menambah Lapangan Baru
# Tambahkan token: str = Depends(oauth2_scheme) di dalam kurung parameter
@router.post("/", response_model=Field, status_code=201)
def create_field(field: FieldCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_field = FieldModel(**field.model_dump())
    db.add(db_field)
    db.commit()
    db.refresh(db_field)
    return db_field

# 2. READ: Melihat Semua Lapangan
@router.get("/", response_model=List[Field])
def read_fields(db: Session = Depends(get_db)):
    return db.query(FieldModel).all()

# 3. READ: Melihat 1 Lapangan Berdasarkan ID
@router.get("/{field_id}", response_model=Field)
def read_field(field_id: int, db: Session = Depends(get_db)):
    db_field = db.query(FieldModel).filter(FieldModel.id == field_id).first()
    if db_field is None:
        raise HTTPException(status_code=404, detail="Lapangan tidak ditemukan")
    return db_field

# 4. UPDATE: Mengubah Data Lapangan (Terproteksi)
@router.put("/{field_id}", response_model=Field)
def update_field(field_id: int, field_update: FieldCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_field = db.query(FieldModel).filter(FieldModel.id == field_id).first()
    if not db_field:
        raise HTTPException(status_code=404, detail="Lapangan tidak ditemukan")
    
    # Update data ke database
    db_field.name = field_update.name
    db_field.type = field_update.type
    db_field.price_per_hour = field_update.price_per_hour
    
    db.commit()
    db.refresh(db_field)
    return db_field

# 5. DELETE: Menghapus Data Lapangan (Terproteksi)
@router.delete("/{field_id}", status_code=204)
def delete_field(field_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_field = db.query(FieldModel).filter(FieldModel.id == field_id).first()
    if not db_field:
        raise HTTPException(status_code=404, detail="Lapangan tidak ditemukan")
    
    db.delete(db_field)
    db.commit()
    return None # Status 204 (No Content) tidak mengembalikan body