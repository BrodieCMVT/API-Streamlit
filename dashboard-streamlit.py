import streamlit as st
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

st.title('The API Conglomerate')

url = "https://api.coinlore.net/api/tickers/"
url2 = "https://www.affirmations.dev/"
url3 = "https://www.boredapi.com/api/activity"

resp = requests.get(url).json()
resp3 = requests.get(url3).json()

df = pd.DataFrame(resp['data'])
stdf = st.dataframe(df)

df = pd.DataFrame(resp['data'])
st.bar_chart(df,y='percent_change_24h',x='name',height=700)

col1, col2 = st.columns(2)

with col1:
    st.subheader('Affirmations')
    limit = st.slider('', 1, 5, 1, step=1)
    for i in range(limit):
        resp2 = requests.get(url2).json()
        st.text(resp2['affirmation'])

with col2:
    st.subheader('Bored? Try this.')
    st.text(resp3['activity'])
    col3, col4 = st.columns(2)
    with col3:
        st.text('Cost')
        cost = '$' + str(resp3['price'])
        st.text(cost)
    with col4:
        st.text('Activity Type')
        st.text(resp3['type'])