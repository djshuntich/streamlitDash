import pandas as pd
import numpy as np
from datetime import datetime
from models import FinancialRecord, get_session

class FinancialDataProcessor:
    def __init__(self):
        self.required_columns = [
            'Date', 'Expenses', 'Operating_Credits', 'Operating_Debit',
            'Revenue', 'Payroll', 'One_Time_Charges', 'Gross_Payout_Revenue'
        ]

    def process_excel(self, uploaded_file):
        try:
            df = pd.read_excel(uploaded_file)

            # Validate columns
            missing_cols = set(self.required_columns) - set(df.columns)
            if missing_cols:
                return None, f"Missing columns: {', '.join(missing_cols)}"

            # Convert date column
            df['Date'] = pd.to_datetime(df['Date'])

            # Calculate derived metrics
            df['Net_Revenue'] = df['Revenue'] - df['Expenses']
            df['Profit_Margin'] = (df['Net_Revenue'] / df['Revenue'] * 100).round(2)

            # Save to database
            self.save_to_db(df)

            return df, None
        except Exception as e:
            return None, f"Error processing file: {str(e)}"

    def save_to_db(self, df):
        session = get_session()
        try:
            for _, row in df.iterrows():
                record = FinancialRecord(
                    date=row['Date'].date(),
                    expenses=float(row['Expenses']),
                    operating_credits=float(row['Operating_Credits']),
                    operating_debit=float(row['Operating_Debit']),
                    revenue=float(row['Revenue']),
                    payroll=float(row['Payroll']),
                    one_time_charges=float(row['One_Time_Charges']),
                    gross_payout_revenue=float(row['Gross_Payout_Revenue']),
                    net_revenue=float(row['Net_Revenue']),
                    profit_margin=float(row['Profit_Margin'])
                )
                session.add(record)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_data(self):
        session = get_session()
        try:
            records = session.query(FinancialRecord).order_by(FinancialRecord.date).all()
            data = {
                'Date': [r.date for r in records],
                'Expenses': [r.expenses for r in records],
                'Operating_Credits': [r.operating_credits for r in records],
                'Operating_Debit': [r.operating_debit for r in records],
                'Revenue': [r.revenue for r in records],
                'Payroll': [r.payroll for r in records],
                'One_Time_Charges': [r.one_time_charges for r in records],
                'Gross_Payout_Revenue': [r.gross_payout_revenue for r in records],
                'Net_Revenue': [r.net_revenue for r in records],
                'Profit_Margin': [r.profit_margin for r in records]
            }
            return pd.DataFrame(data)
        finally:
            session.close()

    def get_summary_metrics(self, df):
        return {
            'total_revenue': df['Revenue'].sum(),
            'total_expenses': df['Expenses'].sum(),
            'net_profit': df['Net_Revenue'].sum(),
            'avg_profit_margin': df['Profit_Margin'].mean(),
            'total_payroll': df['Payroll'].sum()
        }