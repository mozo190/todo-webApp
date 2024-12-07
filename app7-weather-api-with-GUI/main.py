import plotly.express as px
import streamlit as st
from backend import get_data

st.title('Weather Forecast for the Next 5 Days')
place = st.text_input('Enter the name of the place:', 'Mumbai')

days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of days you want to forecast the weather for.')
option = st.selectbox('Select the type of weather data you want to see:',
                      ('Temperature', 'Weather', 'Humidity', 'Wind Speed', 'Pressure'))
st.subheader(f'{option} for {place} for the next {days} days:')

if place:

    filtered_data = get_data(place, days)

    if option == 'Temperature':
        temperatures = [dict["main"]["temp"] - 273.15 for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Create a temperature plot
        fig = px.line(x=d, y=t, title=f'{option} Forecast', labels={'x': 'Date', 'y': 'Temperature (°C)'})
        st.plotly_chart(fig)

    if option == 'Sky':
        filtered_data = [dict['weather'][0]["main"] for dict in filtered_data]
        # Create a weather plot
        st.image('weather.png')