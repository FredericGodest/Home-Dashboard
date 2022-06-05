import streamlit as st
import twitter
import meteo
import sncf
from datetime import datetime, timedelta


def hours():
    now = datetime.now() + timedelta(hours=2)
    hour = f'{now.hour:02d}'
    minute = f'{now.minute:02d}'
    if int(hour) < 18:
        st.markdown(f"### Bonjour ! Il est {hour}:{minute}.")
    else:
        st.markdown(f"### Bonsoir ! Il est {hour}:{minute}.")


st.set_page_config(layout="wide")
hours()

col1, col2 = st.columns(2)
with col1:
    twitter.display("rouen", False)
    sncf.display()
with col2:
    meteo.display()
