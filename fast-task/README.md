# FastTask API

A simple FastAPI-based CRUD backend for managing tasks.  
Built with async SQLAlchemy and SQLite.

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/fast-task.git
cd fast-task
```
### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
# OR
venv\Scripts\activate     # For Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the application
```bash
uvicorn app.main:app --reload
```
The API will be accessible at `http://127.0.0.1:8000/docs`.

#Project Structure
```
app/
│
├── main.py        # FastAPI app entry
├── database.py    # DB connection and engine setup
├── models.py      # SQLAlchemy ORM models
├── schemas.py     # Pydantic request/response schemas
├── crud.py        # Database operations
└── routers/
    └── tasks.py   # Task API routes
```
