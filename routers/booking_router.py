from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.booking import Booking as BookingModel
from models.field import Field as FieldModel
from schemas.booking import Booking, BookingCreate
from auth.security import oauth2_scheme

router = APIRouter(prefix="/bookings", tags=["Bookings"])

# 1. CREATE: Membuat Reservasi Baru
@router.post("/", response_model=Booking, status_code=201)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    # Cek dulu apakah ID lapangan yang dimasukkan ada di database
    db_field = db.query(FieldModel).filter(FieldModel.id == booking.field_id).first()
    if not db_field:
        raise HTTPException(status_code=404, detail="Lapangan tidak ditemukan, tidak bisa booking.")
    
    db_booking = BookingModel(**booking.model_dump())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

# 2. READ: Melihat Semua Reservasi
@router.get("/", response_model=List[Booking])
def read_bookings(db: Session = Depends(get_db)):
    return db.query(BookingModel).all()

# 3. UPDATE: Mengubah Data Reservasi (Terproteksi)
@router.put("/{booking_id}", response_model=Booking)
def update_booking(booking_id: int, booking_update: BookingCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=404, detail="Reservasi tidak ditemukan")
    
    # Cek apakah field_id yang baru valid
    db_field = db.query(FieldModel).filter(FieldModel.id == booking_update.field_id).first()
    if not db_field:
        raise HTTPException(status_code=404, detail="Lapangan baru tidak ditemukan")

    db_booking.user_name = booking_update.user_name
    db_booking.start_time = booking_update.start_time
    db_booking.duration_hours = booking_update.duration_hours
    db_booking.field_id = booking_update.field_id
    
    db.commit()
    db.refresh(db_booking)
    return db_booking

# 4. DELETE: Menghapus Reservasi (Terproteksi)
@router.delete("/{booking_id}", status_code=204)
def delete_booking(booking_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=404, detail="Reservasi tidak ditemukan")
    
    db.delete(db_booking)
    db.commit()
    return None