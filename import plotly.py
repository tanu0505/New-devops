import plotly.graph_objects as go
import pandas as pd

data = { 'Date': pd.date_range(start='2025-01-01' , periods=10,freq='D'),
         'StockPrice':[150,152,149,153,155,158,157,160,162,165]
         }

df= pd.DataFrame(data)

fig=go.Figure()

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['StockPrice'],
    mode='lines+markers',
    name='Stock Price',
    line=dict(color='blue',width=2),
    marker=dict(size=6)
    ))

fig.update_layout(
    title='Stock Price Time Series',
    xaxis_title='Date',
    yaxis_title='Price(USD)',
    xaxis=dict(showgrid=True),
    yaxis=dict(showgtid=True))
fig.show()
