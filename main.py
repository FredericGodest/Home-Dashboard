import streamlit as st
import twitter
import meteo
import sncf
import asyncio
from datetime import datetime

def hours():
    now = datetime.now()
    hour = f'{now.hour:02d}'
    minute = f'{now.minute:02d}'
    if hour < "06":
        st.markdown(f"# Bonjour de bon matin ! Il est {hour}:{minute}. (bonne piscine =D )")
    elif hour < "09":
        st.markdown(f"# Bonjour de bon matin ! Il est{hour}:{minute}.")
    elif hour <= "18":
        st.markdown(f"# Bonsoir ! Il est {hour}:{minute}.")


st.set_page_config(layout="wide")
hours()

col1, col2 = st.columns(2)
with col1:
    twitter.display("rouen", False)
    sncf.display()
with col2:
    meteo.display()
