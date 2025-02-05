import pandas as pd
import numpy as np
from datetime import datetime

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
            
            return df, None
        except Exception as e:
            return None, f"Error processing file: {str(e)}"
    
    def get_summary_metrics(self, df):
        return {
            'total_revenue': df['Revenue'].sum(),
            'total_expenses': df['Expenses'].sum(),
            'net_profit': df['Net_Revenue'].sum(),
            'avg_profit_margin': df['Profit_Margin'].mean(),
            'total_payroll': df['Payroll'].sum()
        }
