## Running server

### runserver
In the root folder just type in terminal:
```bash
.\venv\Scripts\python.exe .\django_lab\lab\manage.py runserver
```

### migrate
In the root folder just type in terminal:
```bash
.\venv\Scripts\python.exe .\django_lab\lab\manage.py migrate
```

### createsuperuser
In the root folder just type in terminal:
```bash
.\venv\Scripts\python.exe .\django_lab\lab\manage.py createsuperuser
```

### start app
In the root folder just type in terminal:
```bash
.\venv\Scripts\python.exe .\django_lab\lab\manage.py startapp authentication
```

## Create table in database
```bash
.\venv\Scripts\python.exe .\django_lab\lab\manage.py migrate
.\venv\Scripts\python.exe .\django_lab\lab\manage.py sqlmigrate news 0001
.\venv\Scripts\python.exe .\django_lab\lab\manage.py makemigrations news
```

## Linter
In the root folder just type in terminal:
```bash
mypy django_lab
```

## Format
In the root folder just type in terminal:
```bash
black django_lab
```

