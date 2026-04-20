from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)        # Nama pemesan
    start_time = Column(DateTime)     # Waktu mulai sewa
    duration_hours = Column(Integer)  # Durasi dalam jam
    field_id = Column(Integer, ForeignKey("fields.id")) # Menghubungkan ke tabel fields

    # Relasi balik ke tabel Field
    field = relationship("Field", back_populates="bookings")