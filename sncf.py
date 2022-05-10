import pandas as pd
from datetime import datetime
import requests
import streamlit as st
from datetime import timedelta


def convert_time(timestamp):
    hour = timestamp[9:11]
    sec = timestamp[11:13]
    time = f"{hour}:{sec}"

    return time


def time_request_func():
    now = datetime.now() + timedelta(hours=2)
    month = f'{now.month:02d}'
    day = f'{now.day:02d}'
    hour = f'{now.hour:02d}'
    minute = f'{now.minute:02d}'
    second = f'{now.second:02d}'
    request_el = f"{now.year}{month}{day}T{hour}{minute}{second}"

    return request_el


def get_data(time_request):
    lines_url = f'https://api.navitia.io/v1/coverage/sncf/stop_areas/stop_area%3ASNCF%3A87411017/departures?from_datetime={time_request}&'
    token = "174d73b4-dfae-4d27-aca5-05dcb0ba16e3"
    response = requests.get(url=lines_url, auth=(token, ''))
    response_code = response
    json_res = response.json()

    return json_res, response_code

def display():
    time_request = time_request_func()
    json_res, response_code = get_data(time_request)

    data_dict = {
        "Numéros de train": [],
        "Directions": [],
        "Heure de départ": [],
        "Programmé": []
    }
    for i in range(len(json_res["departures"])):
        stops = json_res["departures"][i]["display_informations"]["label"]
        if "VERNON" in stops:
            direction = json_res["departures"][i]["display_informations"]["direction"]
            train_number = json_res["departures"][i]["display_informations"]["trip_short_name"]
            departure_time = json_res["departures"][i]["stop_date_time"]["departure_date_time"]
            departure_time = convert_time(departure_time)
            scheduled = json_res["departures"][i]["stop_date_time"]["data_freshness"]
            if scheduled == "base_schedule":
                scheduled = "A l'heure"

            data_dict["Numéros de train"].append(train_number)
            data_dict["Directions"].append(direction)
            data_dict["Heure de départ"].append(departure_time)
            data_dict["Programmé"].append(scheduled)

    df = pd.DataFrame(data=data_dict).drop_duplicates()
    df = df.set_index("Numéros de train")
    df = df[["Heure de départ", "Programmé"]]

    st.markdown(f"### Prochains trains pour Vernon")
    st.dataframe(df)









