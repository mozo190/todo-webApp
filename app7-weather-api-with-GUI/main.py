import streamlit as st

st.title('Weather Forecast for the Next 5 Days')
place = st.text_input('Enter the name of the place:', 'Mumbai')

days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of days you want to forecast the weather for.')
option = st.selectbox('Select the type of weather data you want to see:',
                      ('Temperature', 'Humidity', 'Wind Speed', 'Pressure'))
st.subheader(f'{option} for {place} for the next {days} days:')
