import plotly.express as px
import streamlit as st
from backend import get_data

st.title('Weather Forecast for the Next 5 Days')
place = st.text_input('Enter the name of the place:', 'Mumbai')

days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of days you want to forecast the weather for.')
option = st.selectbox('Select the type of weather data you want to see:',
                      ('Temperature', 'Humidity', 'Wind Speed', 'Pressure'))
st.subheader(f'{option} for {place} for the next {days} days:')


data = get_data(place, days, option)


d, t = get_data(days)

fig = px.line(x=d, y=t, title=f'{option} Forecast', labels={'x': 'Date', 'y': 'Temperature (°C)'})
st.plotly_chart(fig)
