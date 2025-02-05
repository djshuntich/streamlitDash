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
    from sqlalchemy import inspect, text

    inspector = inspect(engine)
    try:
        # Check if table exists first
        if not inspector.has_table('financial_records'):
            Base.metadata.create_all(engine)
        print("Database initialization completed successfully")
    except Exception as e:
        print(f"Error initializing database: {e}")
        # Clean up any partial initialization
        with engine.connect() as connection:
            connection.execute(text("DROP TABLE IF EXISTS financial_records CASCADE"))
            connection.execute(text("DROP SEQUENCE IF EXISTS financial_records_id_seq CASCADE"))
        # Try one more time
        Base.metadata.create_all(engine)

def get_session():
    return Session()