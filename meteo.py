import requests
import meteofrance_api
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from collections import Counter
import streamlit as st

def display():
    latitude = 49.443232
    longitude = 1.099971
    hours = 12

    meteo = meteofrance_api.MeteoFranceClient()
    forecast = meteo.get_forecast(latitude, longitude, language='fr')

    timestamps = [forecast.forecast[i]["dt"] for i in range(hours)]
    time = [datetime.fromtimestamp(timestamp) for timestamp in timestamps]
    temperatures = [forecast.forecast[i]["T"]["value"] for i in range(hours)]
    weathers = [forecast.forecast[0]["weather"]["desc"] for i in range(hours)]
    weather = list(Counter(weathers).keys())[0]
    rains = [forecast.forecast[0]["rain"]["1h"] for i in range(hours)]

    for i in range(hours):
        if rains[i] == 0:
            rains[i] = 1

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(go.Scatter(x=time, y=temperatures,
                             mode='lines',
                             name='température [°C]',
                             marker_color='indianred',
                             textposition="top center"),
                  secondary_y=False)
    fig.add_trace(go.Bar(x=time, y=rains,
                         marker_color='blue',
                         name='pluie [%]'),
                  secondary_y=True)

    fig.update_layout(yaxis_title="°C")

    fig.update_yaxes(title_text="Temp [°C]", secondary_y=False)
    fig.update_yaxes(title_text="Pluie [%]", secondary_y=True, range=[0, 100])
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False))

    st.markdown(f"## Météo à Rouen")
    st.markdown(f'### Météo globale : **{weather}**')
    st.plotly_chart(fig, use_container_width=True)