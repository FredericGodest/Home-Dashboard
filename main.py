import streamlit as st
import twitter
import meteo

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    twitter.display("rouen", True)
with col2:
    meteo.display()


