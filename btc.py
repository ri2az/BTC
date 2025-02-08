import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
from datetime import datetime

def get_bitcoin_price():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if 'EUR' in data:
            return float(data['EUR'])
        else:
            st.error("Les données de prix sont manquantes dans la réponse de l'API.")
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la récupération des données : {e}")
    return None

@st.cache_data(ttl=600)  # Cache pour éviter un blocage API
def get_historical_data(days=30):
    url = f"https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=EUR&limit={days}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if 'Data' in data and 'Data' in data['Data']:
            df = pd.DataFrame(data['Data']['Data'])
            df['time'] = pd.to_datetime(df['time'], unit='s')
            return df[['time', 'open', 'high', 'low', 'close']]
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la récupération des données historiques : {e}")
    return pd.DataFrame(columns=['time', 'open', 'high', 'low', 'close'])

st.title("📊 Suivi du Bitcoin en temps réel")

# Bouton pour rafraîchir les données
if st.button("🔄 Rafraîchir les données"):
    st.rerun()

# Prix actuel du Bitcoin
current_price = get_bitcoin_price()
if current_price is not None:
    st.metric(label="💰 Prix actuel du Bitcoin (EUR)", value=f"{current_price:,.2f}")
else:
    st.error("Impossible de récupérer le prix du Bitcoin. Vérifiez l'API.")

# Sélection de la période avec ajout de 1 an et 3 ans
periods = {
    "7 jours": 7,
    "30 jours": 30,
    "90 jours": 90,
    "1 an": 365,
    "3 ans": 1095
}
selected_period = st.selectbox("📅 Sélectionnez une période :", list(periods.keys()))
days = periods[selected_period]

data = get_historical_data(days)

if not data.empty:
    # 🔹 Graphique en ligne (évolution du prix avec points)
    st.subheader("📈 Évolution du prix du Bitcoin")
    line_fig = go.Figure()
    
    # Courbe avec lignes et points
    line_fig.add_trace(go.Scatter(
        x=data['time'], 
        y=data['close'], 
        mode='lines+markers',  # Ajoute des points sur chaque valeur
        name='Prix de clôture',
        marker=dict(size=6, color="red")  # Points rouges pour une meilleure visibilité
    ))

    line_fig.update_layout(
        title="Évolution du prix du Bitcoin",
        xaxis_title="Date",
        yaxis_title="Prix (EUR)",
        xaxis=dict(showgrid=True),  # Ajout des grilles
        yaxis=dict(showgrid=True),
        template="plotly_dark"
    )
    st.plotly_chart(line_fig)

    # 🔹 Graphique en chandeliers (candlestick)
    st.subheader("🕯️ Graphique en chandeliers")
    candle_fig = go.Figure()
    candle_fig.add_trace(go.Candlestick(
        x=data['time'],
        open=data['open'],
        high=data['high'],
        low=data['low'],
        close=data['close'],
        name="Chandeliers"
    ))

    candle_fig.update_layout(
        title="Graphique en chandeliers du Bitcoin",
        xaxis_title="Date",
        yaxis_title="Prix (EUR)",
        xaxis=dict(showgrid=True),  # Ajout des grilles
        yaxis=dict(showgrid=True),
        template="plotly_dark"
    )
    st.plotly_chart(candle_fig)

else:
    st.error("Impossible de récupérer les données historiques du Bitcoin.")