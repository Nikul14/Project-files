import plotly.express as px
x= [1,2,3,4,5,6,7]
y=[6,5,4,3,2,1,7]
fig=px.line(x=x,y=y)
fig.show()

import plotly.graph_objects as go
fig=go.Figure(go.Scatter(x=x,y=y))
fig.update_layout(title='this is plotly line graph',xaxis='x',yaxis='y')
fig.show()

# to draw multiple line 
import plotly.graph_objects as go

# Sample data
x = [1, 2, 3, 4, 5, 6, 7]
y1 = [6, 5, 4, 3, 2, 1, 7]  # First line
y2 = [1, 3, 5, 7, 6, 4, 2]  # Second line
y3 = [2, 4, 6, 8, 7, 5, 3]  # Third line

# Create figure
fig = go.Figure()

# Add multiple line traces
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Line 1', line=dict(color='red')))
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Line 2', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=x, y=y3, mode='lines', name='Line 3', line=dict(color='green')))

# Update layout
fig.update_layout(
    title='Multiple Line Plot in Plotly',
    xaxis=dict(title='X-Axis'),
    yaxis=dict(title='Y-Axis'),
    legend=dict(title='Legend')
)

# Show figure
fig.show()

import plotly.graph_objects as go

# Sample data
data1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
data2 = [15, 25, 35, 45, 55, 65, 75, 85, 95]

# Create a Figure
fig = go.Figure()

# Add box plots
fig.add_trace(go.Box(y=data1, name="Dataset 1", marker_color="blue"))
fig.add_trace(go.Box(y=data2, name="Dataset 2", marker_color="red"))

# Update layout
fig.update_layout(
    title="Box Plot in Plotly",
    yaxis=dict(title="Values"),
    xaxis=dict(title="Dataset"),
)

# Show the plot
fig.show()

