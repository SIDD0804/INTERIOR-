from pydantic import BaseModel
from typing import Optional
from datetime import date

class BankAccountBase(BaseModel):
    account_number: str
    bank_name: str
    branch: str
    ifsc_code: str
    is_active: Optional[bool] = True

class BankAccountCreate(BankAccountBase):
    pass

class BankAccount(BankAccountBase):
    id: int
    class Config:
        orm_mode = True

class VendorBase(BaseModel):
    vendor_name: str
    account_number: str
    bank_account_id: int
    contact_info: Optional[str]

class VendorCreate(VendorBase):
    pass

class Vendor(VendorBase):
    id: int
    class Config:
        orm_mode = True

class TransactionTypeBase(BaseModel):
    type_name: str
    description: Optional[str]

class TransactionTypeCreate(TransactionTypeBase):
    pass

class TransactionType(TransactionTypeBase):
    id: int
    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    vendor_id: int
    bank_account_id: int
    transaction_type_id: int
    amount: float
    transaction_date: date
    description: Optional[str]
    source: Optional[str] = "CashBook"
    matched: Optional[bool] = False
    matched_transaction_id: Optional[int] = None

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    class Config:
        orm_mode = True