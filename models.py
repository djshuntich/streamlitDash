from sqlalchemy import create_engine, Column, Integer, Float, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime

Base = declarative_base()
engine = create_engine(os.environ['DATABASE_URL'])
Session = sessionmaker(bind=engine)

class FinancialRecord(Base):
    __tablename__ = 'financial_records'
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    expenses = Column(Float, nullable=False)
    operating_credits = Column(Float, nullable=False)
    operating_debit = Column(Float, nullable=False)
    revenue = Column(Float, nullable=False)
    payroll = Column(Float, nullable=False)
    one_time_charges = Column(Float, nullable=False)
    gross_payout_revenue = Column(Float, nullable=False)
    net_revenue = Column(Float, nullable=False)
    profit_margin = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

def init_db():
    Base.metadata.create_all(engine)

def get_session():
    return Session()
