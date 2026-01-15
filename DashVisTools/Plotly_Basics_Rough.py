
# Scatter plot
fig=go.Figure()
fig.add_trace(go.Scatter(x=, y=, mode='markers', marker=dict(color='')))
fig.update_layout(title='', xaxis_title='', yaxis_title='')

# Line plot
fig=go.Figure()
fig.add_trace(go.Scatter(x=, y=, mode='lines', marker=dict(color='')))
fig.update_layout(title='', xaxis_title='', yaxis_title='')

# Bar plot
fig = px.bar(x=, y=, title='')
fig.show()

# Histogram
fig = px.histogram(x=, title='')
fig.show()

# Bubble plot
fig = px.scatter(<data>, x="", y="", size="",
                hover_name="", title='', size_max=)

# Pie chart
fig = px.pie(values=, names=, title='')
fig.show()

# Sunburst chart
fig = px.sunburst(
  data,
  names='',
  parents='',
  values='',
  title=""
)
fig.show()

## Questions
# Scatter plot
fig=go.Figure()
fig.add_trace(go.Scatter(x=data['Distance'], y=data['DepTime'], mode='markers', marker=dict(color='red')))
fig.update_layout(title='Distance vs Departure Time', xaxis_title='Distance', yaxis_title='DeptTime')

# Line plot
fig=go.Figure()
fig.add_trace(go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')


# Bar plot
fig = px.bar(x=bar_data['DestState'], y=bar_data['Flights'], title=
          'Total number of flights to the destination state split by reporting air')
fig.show()
# Histogram
fig = px.histogram(x=data['ArrDelay'], title=
        'Total number of flights to the destination state split by reporting air')
fig.show()
# Bubble plot
fig = px.scatter(bub_data, x="Reporting_Airline", y="Flights", size="Flights",
                hover_name="Reporting_Airline", title='Reporting Airline vs Number of Flights', size_max=60)
fig.show()

# Pie chart
fig = px.pie(data, values='Month', names='DistanceGroup', title='Distance group proprtion by month')
fig.show()
# Sunburst chart
fig = px.sunburst(
  data,
  # names='DesStateName',
  # parents='Month',
  path=['Month', 'DestStatename']
  values='values',
  title="Flight Distribution Hierarchy"
)
fig.show()
