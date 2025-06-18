# HiFi Horizon Project
A database made for a school project using FastApi
Includes prerequisites, setup steps and steps to running locally

## Project Overview
This project provides an API for accessing and managing a database of HiFi equipment including:
- CD Players
- Amplifiers
- Turntables
- Speakers

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
### 1. Python 3.11 or higher required
- Check installation: `python --version`
- [Download Python](https://www.python.org/downloads/) if not installed already


### 2. Install PostgreSQL:
- [Windows installer](https://www.postgresql.org/download/windows/)
- macOS: `brew install postgresql@14`
- Linux: `sudo apt install postgresql postgresql-contrib`

## Setup Steps (Ignore if running locally)
### 1. Create database:
```bash
sudo -u postgres psql
CREATE DATABASE "DB_name";
CREATE USER "user" WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE "DB_name" TO "user";
```

### 2. Install dependencies:
```bash
python -m venv .venv 
or, if that doesn't work
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure environment:
```
DATABASE_URL=postgresql://user:password@localhost:5432/DB_name
```

### 4. Initialize database:
```bash
python -m app.init_db
python -m app.load_data
```

### 5. Start server:
```bash
uvicorn app.main:app --reload
```
## Running Locally
### 1. Clone the repo

### 2. Create virtual enviroment and install dependencies:
This step is necessary because projects need to be able to specify their package and interpreter dependencies in isolation from other projects.
```bash
# Create and activate virtual environment
python -m venv .venv
or, if that doesn't work:
python3 -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 3. Start server:
```bash
uvicorn app.main:app --reload
```
### 4. Verify Installation
- Open http://localhost:8000/docs in your browser
- You should see the Swagger documentation

## API Features

### Product Endpoints
- `GET /products/`
  - List all products
  - Filter by category, brand, or color
  - Sort by price (ascending/descending)

## Troubleshooting

### Common Issues
1. "Port already in use":
   ```bash
   # Find and kill process on port 8000
   sudo lsof -i :8000
   kill <PID>
   ```

2. "Database connection failed":
   - Check PostgreSQL is running
   - Verify credentials in `.env`

3. "Module not found":
   - Make sure virtual environment is activated
   - Reinstall requirements

Need help? Open an issue on GitHub!