from sqlalchemy import Column, Integer, String, DECIMAL, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class BankAccount(Base):
    __tablename__ = "bank_accounts"
    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String(50), unique=True, index=True)
    bank_name = Column(String(100))
    branch = Column(String(100))
    ifsc_code = Column(String(20))
    is_active = Column(Boolean, default=True)
    vendors = relationship("Vendor", back_populates="bank_account")
    transactions = relationship("Transaction", back_populates="bank_account")

class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, index=True)
    vendor_name = Column(String(100))
    account_number = Column(String(50))
    bank_account_id = Column(Integer, ForeignKey("bank_accounts.id"))
    contact_info = Column(String(200))
    bank_account = relationship("BankAccount", back_populates="vendors")
    transactions = relationship("Transaction", back_populates="vendor")

class TransactionType(Base):
    __tablename__ = "transaction_types"
    id = Column(Integer, primary_key=True, index=True)
    type_name = Column(String(50), unique=True)
    description = Column(String(200))
    transactions = relationship("Transaction", back_populates="transaction_type")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    bank_account_id = Column(Integer, ForeignKey("bank_accounts.id"))
    transaction_type_id = Column(Integer, ForeignKey("transaction_types.id"))
    amount = Column(DECIMAL(18,2))
    transaction_date = Column(Date)
    description = Column(String(255))
    source = Column(String(20)) # 'CashBook' or 'BankStatement'
    matched = Column(Boolean, default=False)
    matched_transaction_id = Column(Integer, nullable=True)
    vendor = relationship("Vendor", back_populates="transactions")
    bank_account = relationship("BankAccount", back_populates="transactions")
    transaction_type = relationship("TransactionType", back_populates="transactions")