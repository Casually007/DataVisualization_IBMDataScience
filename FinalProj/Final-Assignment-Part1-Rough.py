'''
    columns:
    'Date'  'Year' 'Month' 'Recession' 'Consumer_Confidence' 'Seasonality_Weight'
    'Price' 'Advertising_Expenditure' 'Competition' 'GDP' 'Growth_Rate' 'unemployment_rate'
    'Automobile_Sales' 'Vehicle_Type' 'City'
'''


'''
    recession period 1 - year 1980
    recession period 2 - year 1981 to 1982
    recession period 3 - year 1991
    recession period 4 - year 2000 to 2001
    recession period 5 - year end 2007 to mid 2009
    recession period 6 - year 2020 -Feb to April (Covid-19 Impact)
'''

# Line chart (pandas): Automobile sales fluctuation year by year
df_new = df.groupby('Year')['Automobile_Sales'].mean().reset_index()
plt.figure(figsize=(10,8))
df_new.plot(x='Year', y='Automobile_Sales', kind='line')
plt.title('Year by year fluctuation in automobile sales')
plt.xlabel('Year')
plt.ylabel('Automobile sales')
plt.show()

# add x ticks to pandas plot

df_new = df.groupby('Year')['Automobile_Sales'].mean().reset_index()
plt.figure(figsize=(10,8))
df_new.plot(x='Year', y='Automobile_Sales', kind='line')
plt.xticks(list(range(1980,2024)), rotation=60)
plt.title('Year by year fluctuation in automobile sales')
plt.xlabel('Year')
plt.ylabel('Automobile sales')
plt.text(1991, 650, '1991 Recession')
plt.text(2009, 650, 'end 2007-mid 2009 Recession')
plt.legend()
plt.show()


# Task 1.2 - Different lines for categories of vehicle type

df_new = df[df['Recession'] == 1] 
df_new = df_new.groupby(['Year', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
df_new.set_index('Year', inplace=True)
df_new = df_new.groupby(['Vehicle_Type'])['Automobile_Sales']
df_new.plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Average automobile sales')
plt.title('Vehicle-wise Sales Trend during Recession')
plt.legend()
plt.show

# Task 1.3 - Seaborn barplot comparing sales trend per vehicle during recession and non-recession
df_new = df.groupby(['Vehicle_Type', 'Recession'])['Automobile_Sales'].mean().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x='Recession', y='Automobile_Sales', hue='Vehicle_Type', data=df_new)
plt.xticks(ticks=[0,1], labels=['Non-Recession', 'Recession'])
plt.xlabel('Recession indicator')
plt.ylabel('Automobile sales')
plt.title('Vehicle-wise Sales during Recession and Non-Recession Period')
plt.show()

# Task 1.4 - GDP Variation during recession and non-recession
df_res = df[df['Recession'] == 1]
df_nonres = df[df['Recession'] == 0]
fig = plt.figure(figsize=(12,6))
ax0 = fig.add_subplot(1,2,1)
ax1 = fig.add_subplot(1,2,2)

# First plot
sns.lineplot(x='Year', y='GDP', data=df_res, label='Recession', ax=ax0)
ax0.set_xlabel('Year')
ax0.set_ylabel('GDP')
ax0.set_title('GDP Variation during Recession Period')

# Second plot
sns.lineplot(x='Year', y='GDP', data=df_nonres, label='Non-Recession', ax=ax1)
ax0.set_xlabel('Year')
ax0.set_ylabel('GDP')
ax0.set_title('GDP Variation during Non-Recession Period')

plt.tight_layout()
plt.show()

# Task 1.5 - Bubble plot displaying impact of seasonality on automobile sale
df_ses = df[df['Recession'] == 0]
size = df_ses['Seasonality_Weight']
df_ses = df_ses.groupby('Month')['Automobile_Sales'].mean().reset_index()
# Seasonality
df_ses.columns = ['Month', 'Avg_Sales']

ax0 = df_ses.plot(kind='scatter',
            x='Month',
            y='Avg_Sales',
            figsize=(10,6),
            alpha=0.5,
            color='blue',
            s='Seasonality_Weight',
            )
ax0.set_ylabel('Automobile Sales')
ax0.set_title('Seasonality impact on Automobile Sales')

# Task 1.6: Scatter plot between average vehicle price vs sales volume during recession

# Consumer Confidence and Automobile Sales during Recession
df_res = df[df['Recession'] == 1]
plt.scatter(df_res['Consumer_Confidence'], df_res['Automobile_Sales'])
plt.xlabel('Consumer Confidence')
plt.ylabel('Automobile Sales')
plt.title('Consumer Confidence and Automobile Sales during Recessions')
plt.show()


df_res = df[df['Recession'] == 1]
plt.scatter(df_res['Price'], df_res['Automobile_Sales'])
plt.xlabel('Automobile Price')
plt.ylabel('Automobile Sales')
plt.title('Relationship between Average Vehicle Price and Sales during Recessions')
plt.show()

# Task 1.7
df_res = df[df['Recession'] == 1]
df_nonres = df[df['Recession'] == 0]

resTot = df_res['Advertising_Expenditure'].sum()
nonresTot = df_nonres['Advertising_Expenditure'].sum()

# Pie chart
plt.figure(figsize=(8,6))

labels = ['Recession', 'Non-Recession']
sizes = [resTot, nonresTot]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Advertising Expenditure during Recession and Non-Recession')
plt.show()


# Task 1.8
df_res = df[df['Recession'] == 1]

df_res = df_res.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()

# Pie chart
plt.figure(figsize=(8,6))

labels = df_res.labels
sizes = df_res.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Advertising Expenditure for Each Vehicle Type during Recession')
plt.show()

# Task 1.9
df_new = df[df['Recession'] == 1]
sns.lineplot(data=df_new, x='unemployment_rate', y='Automobile_Sales',
             hue='Vehicle_Type', style='Vehicle_Type', markers='o',
             err_style=None)
plt.ylim(0,850)
plt.legend(loc=(0.05,0.30))

# Task 1.10
df_new = df[df['Recession'] == 1]
df_new = df_new.groupby('City')['Automobile_Sales'].sum().reset_index()

# Base map
usMap = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# choropleth layer
choropleth = folium.Choropleth(
    geo_data='us-states.json',
    data=df_new,
    columns=['City', 'Automobile_Sales'],
    key_on='feature.properites.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Automobile Sales during Recession'
).add_to(usMap)

# Tooltips
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['name'], labels=True)
)

# Display the map
usMap
