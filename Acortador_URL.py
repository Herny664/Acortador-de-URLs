import pyshorteners
import streamlit as st

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

#Creación de App Web con Streamlit
st.set_page_config(page_title="URL Shortener", page_icon="🔗", layout="centered")
st.image("img/url.png", use_column_width=True)
st.title("URL Shortener")
st.subheader("Simple and efective")
url = st.text_input("Enter the URL")
if st.button("Generate new URL"):
    st.write("URL shortened: ", shorten_url(url))