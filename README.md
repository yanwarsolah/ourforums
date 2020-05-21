# OurForums
Aplikasi forum sederhana yang dibangun menggunakan Django
3.0.6. Digunakan untuk kebutuhan belajar dan oprek.

## Instalasi
Clone project ini. Masuk ke direktori `ourforums`
dan buat virtual environment:

```
python -m venv .venv
.venv\Scripts\activate
```

Instal requirements:

```
pip install -r requirements.txt
```

Lakukan migrate:

```
python manage.py migrate
```

Buat superuser baru:

```
python manage.py createsuperuser
```

Jalankan development server:

```
python manage.py runserver
```

Buka `http://localhost:8000/`.