# Praktyka Programowania Python / Projektowanie Aplikacji Internetowych - PHP, Python, Javascript / Organizacja i rozwój projektów Open Source [SSM]

## Python

### Creating VirtualEnv
```bash
deactivate
rmdir venv
py -3.10 -m pip install --upgrade pip
py -3.10 -m pip install virtualenv
py -3.10 -m virtualenv venv
.\venv\Scripts\activate
.\venv\Scripts\python.exe -m pip install -r .\requirements.txt
```

If any problem with activating venv try: 

```
For Windows 11, Windows 10, Windows 7, Windows 8, Windows Server 2008 R2 or Windows Server 2012, run the following commands as Administrator:

x86 (32 bit)
Open C:\Windows\SysWOW64\cmd.exe
Run the command: powershell Set-ExecutionPolicy RemoteSigned

x64 (64 bit)
Open C:\Windows\system32\cmd.exe
Run the command: powershell Set-ExecutionPolicy RemoteSigned
```

## Running server

### runserver
In the root folder just type in terminal:
```bash
.\venv\Scripts\python.exe .\lab\manage.py runserver
```

### migrate
In the root folder just type in terminal:
```bash
.\venv\Scripts\python.exe .\lab\manage.py migrate
```

### createsuperuser
In the root folder just type in terminal:
```bash
.\venv\Scripts\python.exe .\lab\manage.py createsuperuser
```

### start app
In the root folder just type in terminal:
```bash
.\venv\Scripts\python.exe .\lab\manage.py startapp books
```

## Create table in database
```bash
.\venv\Scripts\python.exe .\lab\manage.py migrate
.\venv\Scripts\python.exe .\lab\manage.py sqlmigrate books 0001
.\venv\Scripts\python.exe .\lab\manage.py makemigrations books
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


