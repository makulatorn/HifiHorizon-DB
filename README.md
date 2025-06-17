# HiFi Horizon Project
A database made for a school project using FastApi
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

## Setup Steps
1. Create database:
```bash
sudo -u postgres psql
CREATE DATABASE "DB_name";
CREATE USER "user" WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE "DB_name" TO "user";
```

2. Install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Configure environment:
```
DATABASE_URL=postgresql://user:password@localhost:5432/DB_name
```

4. Run application:
```bash
uvicorn app.main:app --reload
```

## API Endpoints
- `GET /products/` - List all products
- `GET /docs` - API documentation