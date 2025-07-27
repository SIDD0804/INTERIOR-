# BRS Banking Demo (Bank Reconciliation System)

This repository provides a demo backend for a Bank Reconciliation System, using Python, FastAPI, SQLAlchemy, and SQLite.  
You can preview and test the functionality without any database setup.

## Live Preview

- [Open in GitHub Codespaces](https://github.com/codespaces/new?repo=YOUR_REPO) (replace YOUR_REPO after pushing)
- Or deploy on [Render](https://render.com/), [Railway](https://railway.app/), [Replit](https://replit.com/).

## Quick Start (Locally)

```bash
git clone https://github.com/YOURUSER/YOURREPO.git
cd YOURREPO
pip install -r requirements.txt
python init_db.py
uvicorn main:app --reload
```

Then visit: http://127.0.0.1:8000/docs

## Functionality

- CRUD for Bank Accounts, Vendors, Transaction Types, Transactions
- SQLite for demo (file: `brs_demo.db`)
- Ready to extend with reconciliation logic and file upload

## Switching to MSSQL

Change `DATABASE_URL` in `database.py` to your MSSQL connection string.

---