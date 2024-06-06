import streamlit as st
import requests

# URL de consulta de precios de Binance
url = '"https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=1"'

# Consulta de precio de Bitcoin
response = requests.get(url)
data = response.json()
price = data['price']

# Interfaz de usuario con Streamlit
st.title('Consulta de precio de Bitcoin en Binance')
st.write('Precio actual:', price)

# Consulta de precio por parte del usuario
symbol_user = st.text_input('Ingrese un símbolo de moneda (por ejemplo, ETHUSDT):')
if symbol_user:
    params = {'symbol': symbol_user}
    response = requests.get(url, params=params)
    data = response.json()
    if 'price' in data:
        price_user = data['price']
        st.write('Precio de', symbol_user, ':', price_user)
    else:
        st.write('Símbolo de moneda no válido:', symbol_user)
