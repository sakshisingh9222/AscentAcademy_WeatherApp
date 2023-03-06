

import streamlit as st
import requests
import json
import streamlit.components.v1 as components
import datetime
from streamlit_lottie import st_lottie
from datetime import datetime as dt

st.set_page_config(page_title = "Weather App", page_icon = "⛅") 
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


lottie_animation_url = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_qqhrsksk.json")
st_lottie(lottie_animation_url , height = 300 , key= "weather")

components.html(
        """
        <h1 style="text-align:center;font-style:sans-serif;font-size:40px;color:dodgerblue;border:2px dotted white">Ascent Academy Weather App</h1>
        """
    )
def api_test(url):
    r1 = requests.get(url)
    if r1.status_code != 200:
        return None
    return r1.json()
def weather_api_run():
    dataapi = api_test("https://api.openweathermap.org/data/2.5/weather?q="+location+"&units=metric&appid=340cd2b1b0e606514e466c281a16b819") 
   
    city = (dataapi["name"])
    country = (dataapi["sys"]["country"])
    tempreature= (dataapi["main"]["temp"])
    min_tempreature= (dataapi["main"]["temp_min"])
    max_tempreature= (dataapi["main"]["temp_max"])
    weather_desc = (dataapi["weather"][0]["description"])
    wind_speed = (dataapi["wind"]["speed"])
    humidity = (dataapi["main"]["humidity"])
    now = dt.now()
   
    dtt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f'City: {city}')
       
        st.write(f'Country: {country}')
        st.write(f'Local Date and Time: {dtt_string}')
        st.write(f'Wind Speed : {round((wind_speed*3.6),3)}km/h')
        st.write(f'Feels like: {tempreature} ℃')

    with col2: 

        st.write(f'Minimum Tempreature: {min_tempreature}℃')
        st.write(f'Maximum Tempreature: {max_tempreature} ℃')
        st.write(f'Condition: {weather_desc}')
        st.write(f'Humidity: {humidity}')


location = st.text_input("Enter the Location: ", "")
if location:
    weather_api_run()
components.html(
        """
        <p style = "color:white; text-align: center">© Copyright2023, Made by Sakshi Singh</p>
        """
    )




