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
    weathers = [forecast.forecast[i]["weather"]["desc"] for i in range(hours)]
    weather = max(weathers,key=weathers.count)
    rains = [forecast.forecast[i]["rain"]["1h"] for i in range(hours)]

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(go.Bar(x=time, y=rains,
                         marker_color='blue',
                         opacity=0.5,
                         name='pluie [mm]'),
                  secondary_y=True)
    fig.add_trace(go.Scatter(x=time, y=temperatures,
                             mode='lines',
                             name='température [°C]',
                             marker_color='red',
                             textposition="top center"),
                  secondary_y=False)


    fig.update_layout(yaxis_title="°C")

    fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

    fig.update_yaxes(title_text="Temp [°C]", secondary_y=False)
    fig.update_yaxes(title_text="Pluie [%]", secondary_y=True, range=[0, 10])
    fig.update_layout(xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False))

    st.markdown(f'### Météo globale à Rouen: **{weather}**')
    st.plotly_chart(fig, use_container_width=True)