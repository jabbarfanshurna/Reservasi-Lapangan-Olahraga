# 🏟️ Sistem Reservasi Lapangan Olahraga - API

Proyek ini adalah sistem **Microservice RESTful API** untuk manajemen reservasi lapangan olahraga yang dibangun menggunakan **FastAPI**. Proyek ini dikerjakan sebagai tugas **Ujian Tengah Semester (UTS)** mata kuliah Pemrograman Web Lanjutan.

## 🚀 Fitur Utama

- **Autentikasi JWT**: Sistem pendaftaran dan masuk pengguna yang aman menggunakan JSON Web Token.
- **Manajemen Lapangan (Fields)**: Operasi CRUD lengkap untuk mengelola data lapangan olahraga.
- **Sistem Reservasi (Bookings)**: Operasi CRUD lengkap untuk melakukan pemesanan lapangan berdasarkan jadwal.
- **Relasi Database (ORM)**: Implementasi relasi *One-to-Many* antara tabel Lapangan dan Reservasi menggunakan SQLAlchemy.
- **Validasi Data**: Validasi input yang ketat menggunakan Pydantic Schemas.
- **Dokumentasi API Otomatis**: Integrasi penuh dengan Swagger UI (`/docs`).

## 🛠️ Stack Teknologi

- **Framework**: FastAPI
- **Bahasa**: Python 3.9+
- **Database**: SQLite (SQLAlchemy ORM)
- **Keamanan**: Passlib (Bcrypt) & Python-Jose (JWT)
- **Server**: Uvicorn

## 📂 Struktur Proyek

Sesuai dengan panduan proyek, kode diatur secara modular:

```text
.
├── main.py              # Entry point aplikasi
├── database.py          # Koneksi & session database
├── auth/
│   └── security.py      # Logika JWT & enkripsi password
├── models/              # SQLAlchemy models (Database)
│   ├── user.py
│   ├── field.py
│   └── booking.py
├── schemas/             # Pydantic schemas (Validasi)
│   ├── user.py
│   ├── field.py
│   └── booking.py
├── routers/             # Endpoint per domain
│   ├── auth_router.py
│   ├── field_router.py
│   └── booking_router.py
└── requirements.txt     # Daftar dependensi
