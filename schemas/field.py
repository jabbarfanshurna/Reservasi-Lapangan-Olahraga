from pydantic import BaseModel
from typing import List, Optional

# Skema dasar (apa yang dibutuhkan saat input)
class FieldBase(BaseModel):
    name: str
    type: str
    price_per_hour: int

# Skema saat membuat data baru (bisa ditambahkan validasi lebih lanjut nanti)
class FieldCreate(FieldBase):
    pass

# Skema saat data dikirim balik ke user (Output)
class Field(FieldBase):
    id: int

    class Config:
        from_attributes = True # Agar Pydantic bisa membaca data dari SQLAlchemy model  