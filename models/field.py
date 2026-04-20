from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Field(Base):
    __tablename__ = "fields"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True) # Contoh: "Lapangan Futsal A"
    type = Column(String)             # Contoh: "Futsal"
    price_per_hour = Column(Integer)  # Contoh: 100000

    # Relasi: Satu lapangan bisa punya banyak booking (One-to-Many)
    bookings = relationship("Booking", back_populates="field")