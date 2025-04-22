import streamlit as st
import requests
from click import style
from streamlit import exception, columns

st.set_page_config(layout="wide")

url = "https://api.nasa.gov/planetary/apod?api_key=TEnOQ9VTaMy71KKY9rUiLsYbECXms6cZn1a3ihG4"
response = requests.get(url)
content = response.json()

st.image("logo1.png")

st.markdown(
    """
    <style>
    .fancy-header {
        color: #1f77b4;
        font-size: 50px;
        font-weight: bold;
        text-shadow: 1px 1px 2px #000000;
    }
    </style>
    <div class='fancy-header'>Nasa's Astronomy Picture of the Day</div>
    """,
    unsafe_allow_html=True
)

with st.form(key="date_form"):
    date = st.text_input("Enter a date: (yyyy-mm-dd)", placeholder="yyyy-mm-dd")
    button = st.form_submit_button("Submit")

if button:
    try:
        url1 = f"https://api.nasa.gov/planetary/apod?api_key=TEnOQ9VTaMy71KKY9rUiLsYbECXms6cZn1a3ihG4&date={date}"
        response2 = requests.get(url1)
        content2 = response2.json()

        st.markdown(f"<h1>Date: {content2["date"]}</h1>", unsafe_allow_html=True)

        title2 = content2["title"]
        st.markdown(
            f"<h1 style='color: #1f77b4;'>{title2}</h1>",
            unsafe_allow_html=True
        )

        col3, col4 = st.columns(2)

        with col3:
            image2 = content2["hdurl"]
            st.image(image2)

        with col4:
            details2 = content2["explanation"]
            st.subheader(details2)

    except KeyError:
        st.warning("Please enter date in correct format")
        st.rerun()
else:
    st.markdown(f"<h1>Today's Date: {content["date"]}</h1>", unsafe_allow_html=True)

    title = content["title"]
    st.markdown(
        f"<h1 style='color: #1f77b4;'>{title}</h1>",
        unsafe_allow_html=True
    )

    col1 , col2 = st.columns(2)
    with col1:
        image = content["hdurl"]
        st.image(image)

    with col2:
        details = content["explanation"]
        st.subheader(details)

