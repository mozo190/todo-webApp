import sqlite3

import plotly.express as px
import streamlit as st

st.title('Hello World!')
st.write('This is a simple Streamlit app.')

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute("SELECT date FROM events")
dates = cursor.fetchall()
date = [x[0] for x in dates]

cursor.execute("SELECT temperature FROM events")
temperatures = cursor.fetchall()
temperature = [x[0] for x in temperatures]

fig = px.line(x=date, y=temperature, title='Temperature over time',
              labels={'x': 'Date', 'y': 'Temperature (°C)'})

st.plotly_chart(fig)
