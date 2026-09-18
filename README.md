# T. Vimala — Python Developer Portfolio

A production-ready personal portfolio website built with **Django**. It showcases skills, projects, education, certifications, and a working contact form, and it is configured for deployment on **Render** with PostgreSQL.

## Features

- Single-page, responsive portfolio with Home, About, Skills, Projects, Education, Certifications, Resume, and Contact
- Dynamic Django models for profile, skills, projects, education, certifications, and contact messages
- Django Admin for easy content updates
- Validated contact form that saves messages to the database
- Resume download from a static file or an uploaded media file
- Environment-based settings for local SQLite and production PostgreSQL
- WhiteNoise static files, Gunicorn, and a Render build script

## Tech stack

- Python 3
- Django 5.2
- HTML5, CSS3, JavaScript
- Bootstrap 5 and Bootstrap Icons
- SQLite (local)
- PostgreSQL (Render)
- Gunicorn
- WhiteNoise
- Pillow

## Project structure

```text
python_portfolio/
├── build.sh
├── manage.py
├── Procfile
├── render.yaml
├── requirements.txt
├── .env.example
├── .python-version
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── portfolio/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── context_processors.py
│   ├── management/commands/seed_portfolio.py
│   └── templates/portfolio/
├── static/portfolio/
│   ├── css/styles.css
│   ├── js/main.js
│   ├── img/
│   └── files/T_Vimala_Resume.pdf
└── media/
```

## Local setup

1. Install Python 3.10+ (3.12 recommended for Render; 3.14 works locally).
2. Clone or copy this project, then create a virtual environment.

**Windows (PowerShell)**

```powershell
cd D:\python_portfolio
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**macOS / Linux**

```bash
cd python_portfolio
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Copy environment variables:

```powershell
copy .env.example .env
```

4. Generate a new secret key and put it in `.env`:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Environment variables

| Variable | Local example | Production |
|---|---|---|
| `SECRET_KEY` | random Django secret | required, keep private |
| `DEBUG` | `True` | `False` |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | your Render hostname, e.g. `vimala-portfolio.onrender.com,.onrender.com` |
| `CSRF_TRUSTED_ORIGINS` | empty | `https://your-service.onrender.com` |
| `DATABASE_URL` | empty (uses SQLite) | Render PostgreSQL connection string |
| `SECURE_SSL_REDIRECT` | `False` | `True` |
| `RENDER_EXTERNAL_HOSTNAME` | unused | set automatically by Render |
| `MEDIA_ROOT` | optional | set this if you attach a Render disk |
| `SERVE_MEDIA` | `False` | `True` to serve uploaded images without a CDN |

Never commit `.env` or real secrets to GitHub.

## Database setup

Locally, Django uses **SQLite** (`db.sqlite3`) when `DATABASE_URL` is empty.

```powershell
python manage.py migrate
python manage.py seed_portfolio
python manage.py createsuperuser
```

`seed_portfolio` adds starter profile, skills, projects, education, and certifications if those tables are empty.

## How to run locally

```powershell
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Optional checks:

```powershell
python manage.py check
python manage.py collectstatic --no-input
```

## Customize these values

Update them in **Django Admin → Site profile** (and related models):

- GitHub URL
- LinkedIn URL
- Email
- College name and education years
- Certification issuers
- Project GitHub / live demo URLs
- Profile photo (`Site profile` → `profile_image`)
- Resume PDF (`Site profile` → `resume_file`, or replace `static/portfolio/files/T_Vimala_Resume.pdf`)

## GitHub instructions

```powershell
git init
git add .
git status
git commit -m "Add Django developer portfolio ready for Render."
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

Confirm `.env` and `venv/` are not staged.

## Render deployment

1. Push this project to GitHub.
2. In Render, create a **PostgreSQL** database. Copy the Internal Database URL.
3. Create a **Web Service** and connect the GitHub repository.
4. Set:
   - **Runtime:** Python
   - **Build command:** `./build.sh`
   - **Start command:** `gunicorn config.wsgi:application`
5. Add environment variables:

```text
PYTHON_VERSION=3.12.10
SECRET_KEY=<generate a long random value>
DEBUG=False
ALLOWED_HOSTS=.onrender.com,your-service.onrender.com
CSRF_TRUSTED_ORIGINS=https://your-service.onrender.com
DATABASE_URL=<Render PostgreSQL URL>
SECURE_SSL_REDIRECT=True
```

6. Deploy the service.
7. After the first deploy, create a superuser from the Render **Shell**:

```bash
python manage.py createsuperuser
python manage.py seed_portfolio
```

8. Open `/admin/` and update profile details, resume, and project links.

The included `render.yaml` can also be used with Render Blueprint. Free database plans change over time, so the Dashboard steps above are the most reliable path.

### Notes for production media files

Render’s filesystem is ephemeral unless you add a disk. Project images and uploaded resumes should either:

- stay as static files in `static/portfolio/`, or
- be stored on a Render persistent disk mounted at `MEDIA_ROOT`.

Static CSS, JS, images, and the default resume PDF are collected by WhiteNoise and work after deploy.

## How to create a Django admin user

Local:

```powershell
python manage.py createsuperuser
```

Render Shell:

```bash
python manage.py createsuperuser
```

Then sign in at `/admin/` to manage Projects, Skills, Education, Certifications, Site profile, and Contact messages.

## License

This project is provided for personal portfolio use.
