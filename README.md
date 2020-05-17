# covid19_platform
Covid-19 Backend


# Development Setup
- Create virtual environment
    `python3 -m venv .venv`

- Activate virtual environment
    `source .venv/bin/activate`

- Install development requirement
    `pip install -r requirements.dev.txt `

- Create Database
    `CREATE DATABASE covid19 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci`

- Create local setting file, Copy covid19.settings.local.py.template and 
create new file local.py at directory covid19.settings

- Setup Database Table
    `python manage.py migrate`

- Run Local development server
    `python manage.py runserver`

- Access Django Admin at http://localhost:8000/admin/  
