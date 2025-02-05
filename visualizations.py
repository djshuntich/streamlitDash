import plotly.graph_objects as go
import plotly.express as px

class DashboardVisualizer:
    def __init__(self):
        self.colors = {
            'primary': '#032844',
            'secondary': '#012239',
            'tertiary': '#011B2D',
            'accent': '#FEE960',
            'text': '#FEFEFB'
        }
    
    def create_revenue_trend(self, df):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['Revenue'],
            name='Revenue',
            line=dict(color=self.colors['accent'])
        ))
        fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df['Expenses'],
            name='Expenses',
            line=dict(color=self.colors['text'])
        ))
        
        fig.update_layout(
            title='Revenue vs Expenses Trend',
            template='plotly_dark',
            paper_bgcolor=self.colors['primary'],
            plot_bgcolor=self.colors['secondary'],
            font=dict(color=self.colors['text'])
        )
        return fig
    
    def create_profit_margin_chart(self, df):
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df['Date'],
            y=df['Profit_Margin'],
            marker_color=self.colors['accent']
        ))
        
        fig.update_layout(
            title='Profit Margin Over Time',
            template='plotly_dark',
            paper_bgcolor=self.colors['primary'],
            plot_bgcolor=self.colors['secondary'],
            font=dict(color=self.colors['text'])
        )
        return fig
