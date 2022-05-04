import requests
import streamlit as st

def display(hashtag, test):
    data_test = {'best_RT': 41,
                 'best_account': 'JeunesFI_Rouen',
                 'best_account_name': 'Jeunes Insoumis•es ROUEN',
                 'best_fav': 56,
                 'best_sentiment': 0.4083333333333333,
                 'best_tweet': "\U0001f7e3 Rendez-vous demain à 14 h pour une caravane de l'union populaire, rue François-Couperin (à proximité du centre André-Malraux) !\n#Rouen #UnionPopulaire #Melenchon1erMinistre https://t.co/7D7ShzZp5E",
                 'final_score': 0.23503526963992086,
                 'hashtag': '#Rouen',
                 'max_RT': 41,
                 'max_fav': 56,
                 'total_RT': 83,
                 'total_fav': 159}
    
    path = "https://twittetrandapi.herokuapp.com/" + hashtag
    if not test:
        r = requests.get(path)
        data = r.json()
    else:
        data = data_test

    st.markdown(f"## Tweets pour #{hashtag.capitalize()}")
    st.markdown(f'### Meilleur tweet de : {data["best_account_name"]}')
    st.markdown(data["best_tweet"])
    st.markdown(f'**{data["best_RT"]} RT**')
