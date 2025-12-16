import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
import os

st.set_page_config(page_title="Quant Dashboard", layout="wide")

# ---------------- Sidebar ----------------
st.sidebar.title("Controls")

window = st.sidebar.slider("Z-Score Window", 10, 100, 30)
threshold = st.sidebar.slider("Alert Threshold", 1.0, 3.0, 2.0)

# ---------------- Title ----------------
st.markdown(
    "## 📊 Real-Time Quant Analytics Dashboard",
    unsafe_allow_html=True
)

# ---------------- Load Data ----------------
DATA_FILE = "ticks.csv"

if not os.path.exists(DATA_FILE):
    st.warning("Waiting for live data...")
    st.stop()

df = pd.read_csv(DATA_FILE)

if df.empty or df['symbol'].nunique() < 2:
    st.warning("Waiting for both BTCUSDT and ETHUSDT data...")
    st.stop()

# ---------------- Prepare Data ----------------
btc = df[df["symbol"] == "BTCUSDT"].tail(300)
eth = df[df["symbol"] == "ETHUSDT"].tail(300)

btc = btc.reset_index(drop=True)
eth = eth.reset_index(drop=True)

min_len = min(len(btc), len(eth))
btc = btc.tail(min_len)
eth = eth.tail(min_len)

spread = btc["price"].values - eth["price"].values

zscore = (
    pd.Series(spread)
    .rolling(window)
    .apply(lambda x: (x.iloc[-1] - x.mean()) / x.std() if x.std() != 0 else 0)
)

# ---------------- Layout ----------------
col1, col2, col3 = st.columns(3)

# BTC Price Chart
with col1:
    st.subheader("BTC Price")
    fig_btc = px.line(btc, y="price")
    st.plotly_chart(fig_btc, use_container_width=True)

# Spread Chart
with col2:
    st.subheader("BTC - ETH Spread")
    fig_spread = px.line(spread)
    st.plotly_chart(fig_spread, use_container_width=True)

# Z-Score Chart
with col3:
    st.subheader("Z-Score")
    fig_z = px.line(zscore)
    st.plotly_chart(fig_z, use_container_width=True)

# ---------------- Alert ----------------
latest_z = zscore.iloc[-1]

if abs(latest_z) > threshold:
    st.error(f"🚨 Z-Score Alert Triggered: {latest_z:.2f}")
else:
    st.success(f"✅ Z-Score Normal: {latest_z:.2f}")

# ---------------- Auto Refresh ----------------
time.sleep(2)
st.rerun()
