import plotly.express as px
import streamlit as st

from backend import get_data

st.title('Weather Forecast for the Next 5 Days')
place = st.text_input('Enter the name of the place:', 'Mumbai')

days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of days you want to forecast the weather for.')
option = st.selectbox('Select the type of weather data you want to see:',
                      ('Temperature', 'Sky'))
st.subheader(f'{option} for {place} for the next {days} days:')

images = {
    "Clear": "images/clear.png",
    "Clouds": "images/cloud.png",
    "Rain": "images/rain.png",
    "Snow": "images/snow.png",
}

if place.strip():
    try:
        filtered_data = get_data(place, days)

        if filtered_data:

            if option == 'Temperature':
                temperatures = [dict["main"]["temp"] - 273.15 for dict in filtered_data]
                dates = [dict["dt_txt"] for dict in filtered_data]
                # Create a temperature plot
                fig = px.line(x=dates, y=temperatures, title=f'{option} Forecast',
                              labels={'x': 'Date', 'y': 'Temperature (°C)'})
                st.plotly_chart(fig)
            elif option == 'Sky':
                sky_conditions = [dict['weather'][0]["main"] for dict in filtered_data]
                image_path = [images[sky] for sky in sky_conditions]

                # Display the sky conditions in columns
                cols = st.columns(5)
                for i, path in enumerate(image_path):
                    col = cols[i % 5]
                    col.image(path, width=100, caption=sky_conditions[i])

        else:
            st.error('No data found for the given place.')
    except Exception as e:
        st.error(f'An error occurred while fetching the data. {e}')
else:
    st.error('Please enter a place name.')
