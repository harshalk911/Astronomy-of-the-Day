import streamlit as st
import requests

st.set_page_config(layout="wide")

url = "https://api.nasa.gov/planetary/apod?api_key=TEnOQ9VTaMy71KKY9rUiLsYbECXms6cZn1a3ihG4"
response = requests.get(url)
content = response.json()

st.markdown(
    """
    <style>
    .fancy-header {
        color: #e91e63;
        font-size: 64px;
        font-weight: bold;
        text-shadow: 1px 1px 2px #000000;
    }
    </style>
    <div class='fancy-header'>Astronomy of the Day</div>
    """,
    unsafe_allow_html=True
)

st.markdown(f"<h1>Today's Date: {content["date"]}</h1>", unsafe_allow_html=True)

title = content["title"]
st.markdown(
    f"<h1 style='color: #1f77b4;'>{title}</h1>",
    unsafe_allow_html=True
)

image = content["hdurl"]
st.image(image)

details = content["explanation"]
st.subheader(details)
