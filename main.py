import streamlit as st
import pandas as pd
from auth import AuthManager
from data_processor import FinancialDataProcessor
from visualizations import DashboardVisualizer
from styles import apply_custom_styles
import streamlit.components.v1 as components
from models import init_db

# Initialize database
init_db()

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'username' not in st.session_state:
    st.session_state.username = None

# Initialize components
auth_manager = AuthManager()
data_processor = FinancialDataProcessor()
visualizer = DashboardVisualizer()

# Apply custom styles
st.markdown(apply_custom_styles(), unsafe_allow_html=True)

def login_page():
    st.title("Financial Dashboard Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if auth_manager.verify_user(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Invalid credentials")

def main_dashboard():
    st.title("Financial Metrics Dashboard")

    # Sidebar
    st.sidebar.title(f"Welcome, {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.rerun()

    # File upload section
    uploaded_file = st.file_uploader("Upload Excel File", type=['xlsx', 'xls'])
    if uploaded_file:
        df, error = data_processor.process_excel(uploaded_file)
        if error:
            st.error(error)
        else:
            st.success("Data loaded successfully!")

    # Display dashboard content
    try:
        df = data_processor.get_all_data()
        if not df.empty:
            # Summary metrics
            metrics = data_processor.get_summary_metrics(df)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Revenue", f"${metrics['total_revenue']:,.2f}")
            with col2:
                st.metric("Total Expenses", f"${metrics['total_expenses']:,.2f}")
            with col3:
                st.metric("Net Profit", f"${metrics['net_profit']:,.2f}")

            # Charts
            st.plotly_chart(visualizer.create_revenue_trend(df), use_container_width=True)
            st.plotly_chart(visualizer.create_profit_margin_chart(df), use_container_width=True)

            # Data table
            st.subheader("Financial Data Table")
            st.dataframe(df.style.highlight_max(axis=0))
        else:
            st.info("No data available. Please upload an Excel file to view the dashboard")
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")

def main():
    if not st.session_state.authenticated:
        login_page()
    else:
        main_dashboard()

if __name__ == "__main__":
    main()