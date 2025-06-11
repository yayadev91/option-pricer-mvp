import streamlit as st
import pandas as pd
import greeks
from pricer import bs_price
from strategies import covered_call
from backtest import backtest_strategy

st.set_page_config(page_title="Option Pricer BS & Backtest", layout="wide")

st.title("📈 Option Pricer Black-Scholes & Backtest")

st.header("1. Paramètres de l'option")
S = st.number_input("Spot (S)", value=100.0)
K = st.number_input("Strike (K)", value=100.0)
T = st.number_input("Maturité (en années)", value=1.0)
r = st.number_input("Taux sans risque (r)", value=0.05)
sigma = st.number_input("Volatilité (σ)", value=0.2)
option_type = st.selectbox("Type d'option", ['call', 'put'])

st.subheader("📊 Résultats du pricing")
price = bs_price(S, K, T, r, sigma, option_type)
st.metric("Prix BS", f"{price:.2f}")
st.write(f"Delta: {delta(S, K, T, r, sigma, option_type):.4f}")
st.write(f"Gamma: {gamma(S, K, T, r, sigma):.4f}")
st.write(f"Rho: {rho(S, K, T, r, sigma, option_type):.4f}")
st.write(f"Theta: {theta(S, K, T, r, sigma, option_type):.4f}")
st.write(f"vega: {vega(S, K, T, r, sigma):.4f}")

st.divider()

st.header("2. Backtest : Covered Call")
ticker = st.text_input("Ticker (ex: AAPL)", "AAPL")
start = st.date_input("Date de début", value=pd.to_datetime("2023-01-01"))
end = st.date_input("Date de fin", value=pd.to_datetime("2023-12-31"))

if st.button("Lancer le backtest"):
    premium = price
    strategy = covered_call(S, K, premium)
    dates, pnl = backtest_strategy(ticker, strategy, start, end)
    df_result = pd.DataFrame({'Date': dates, 'PnL': pnl}).set_index('Date')
    st.line_chart(df_result)
