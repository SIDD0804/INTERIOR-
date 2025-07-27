from sqlalchemy.orm import Session
import models, schemas

# BankAccount CRUD
def create_bank_account(db: Session, bank_account: schemas.BankAccountCreate):
    db_obj = models.BankAccount(**bank_account.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_bank_accounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BankAccount).offset(skip).limit(limit).all()

# Vendor CRUD
def create_vendor(db: Session, vendor: schemas.VendorCreate):
    db_obj = models.Vendor(**vendor.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_vendors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vendor).offset(skip).limit(limit).all()

# TransactionType CRUD
def create_transaction_type(db: Session, transaction_type: schemas.TransactionTypeCreate):
    db_obj = models.TransactionType(**transaction_type.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_transaction_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TransactionType).offset(skip).limit(limit).all()

# Transaction CRUD
def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_obj = models.Transaction(**transaction.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transaction).offset(skip).limit(limit).all()