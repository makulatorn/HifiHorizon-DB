# HiFi Horizon Project
A database made for a school project using FastApi
Includes prerequisites, setup steps and steps to running locally
## Project Structure
```
hifi-horizon/
├── app/
│   ├── models/          # Database models
│   ├── routers/         # API endpoints
│   ├── database.py      # DB connection
│   └── main.py         # FastAPI app
├── static/             # Image files
├── .env               # Configuration
└── data.json         # Product data
```

## Key Components
- **FastAPI** - Web framework
- **SQLAlchemy** - Database ORM
- **PostgreSQL** - Database
- **Python-dotenv** - Environment management

## Prerequisites
1. Python 3.11 or higher required
- Check installation: `python --version`
- [Download Python](https://www.python.org/downloads/) if not installed already


2. Install PostgreSQL:
- [Windows installer](https://www.postgresql.org/download/windows/)
- macOS: `brew install postgresql@14`
- Linux: `sudo apt install postgresql postgresql-contrib`

## Setup Steps (Ignore if running locally)
1. Create database:
```bash
sudo -u postgres psql
CREATE DATABASE "DB_name";
CREATE USER "user" WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE "DB_name" TO "user";
```

2. Install dependencies:
```bash
python -m venv .venv (or python3 -m venv .venv for macOS/Linux)
source .venv/bin/activate
pip install -r requirements.txt
```

3. Configure environment:
```
DATABASE_URL=postgresql://user:password@localhost:5432/DB_name
```

4. Initialize database:
```bash
python -m app.init_db
python -m app.load_data
```

5. Start server:
```bash
uvicorn app.main:app --reload
```
## Running Locally
1. Clone the repo

2. Install dependencies:
```bash
# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

3. Start server:
```bash
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for API documentation.

## API Endpoints
- `GET /products/` - List all products
- `GET /docs` - API documentation
