from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
import init_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="BRS Banking Demo API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"msg": "BRS Banking Demo API is running"}

# --- Bank Accounts ---
@app.post("/bankaccounts/", response_model=schemas.BankAccount)
def create_bank_account(bank_account: schemas.BankAccountCreate, db: Session = Depends(get_db)):
    return crud.create_bank_account(db, bank_account)

@app.get("/bankaccounts/", response_model=list[schemas.BankAccount])
def list_bank_accounts(db: Session = Depends(get_db)):
    return crud.get_bank_accounts(db)

# --- Vendors ---
@app.post("/vendors/", response_model=schemas.Vendor)
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
    return crud.create_vendor(db, vendor)

@app.get("/vendors/", response_model=list[schemas.Vendor])
def list_vendors(db: Session = Depends(get_db)):
    return crud.get_vendors(db)

# --- Transaction Types ---
@app.post("/transactiontypes/", response_model=schemas.TransactionType)
def create_transaction_type(ttype: schemas.TransactionTypeCreate, db: Session = Depends(get_db)):
    return crud.create_transaction_type(db, ttype)

@app.get("/transactiontypes/", response_model=list[schemas.TransactionType])
def list_transaction_types(db: Session = Depends(get_db)):
    return crud.get_transaction_types(db)

# --- Transactions ---
@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, transaction)

@app.get("/transactions/", response_model=list[schemas.Transaction])
def list_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)