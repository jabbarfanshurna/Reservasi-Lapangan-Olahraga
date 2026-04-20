from fastapi import FastAPI
from database import engine, Base
from models import field, booking, user
from routers import field_router # Import router yang baru dibuat
from routers import field_router, booking_router
from routers import field_router, booking_router, auth_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistem Reservasi Lapangan Olahraga")

# Daftarkan router di sini
app.include_router(field_router.router)
app.include_router(field_router.router)
app.include_router(booking_router.router)

app.include_router(auth_router.router) # Tambahkan baris ini di atas router lainnya
app.include_router(field_router.router)
app.include_router(booking_router.router)

@app.get("/")
def root():
    return {"message": "Router Berhasil Terpasang!"}