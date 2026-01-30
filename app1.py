# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 09:48:48 2026

@author: ntoto
"""

import streamlit as st
import pandas as pd
import altair as alt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Trading Journal & Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📈 Trading Journal & Performance Analytics")
st.write(
    "Analyze your trading performance with charts, daily win rates, "
    "and personalized improvement insights."
)

st.divider()

# ---------------- DEMO DATA ----------------
def demo_data():
    return pd.DataFrame({
        "Date": pd.to_datetime([
            "2024-01-02", "2024-01-02", "2024-01-03",
            "2024-01-04", "2024-01-04", "2024-01-05",
            "2024-01-06", "2024-01-07"
        ]),
        "Symbol": ["XAUUSD", "EURUSD", "XAUUSD", "GBPUSD", "EURUSD", "XAUUSD", "EURUSD", "XAUUSD"],
        "Trade Type": ["Buy", "Sell", "Buy", "Sell", "Buy", "Sell", "Buy", "Buy"],
        "Entry Price": [2030, 1.0950, 2045, 1.2700, 1.1000, 2050, 1.0900, 2060],
        "Exit Price": [2040, 1.0920, 2035, 1.2650, 1.1050, 2040, 1.0950, 2070],
        "Position Size": [0.5, 0.3, 0.4, 0.2, 0.3, 0.5, 0.4, 0.6],
        "Result": ["Win", "Win", "Loss", "Win", "Win", "Loss", "Win", "Win"]
    })

# ---------------- SESSION STATE ----------------
if "mode" not in st.session_state:
    st.session_state.mode = "demo"

if "trades" not in st.session_state:
    st.session_state.trades = demo_data()

# ---------------- MODE SELECTION ----------------
st.subheader("🔁 Choose Mode")
col1, col2 = st.columns(2)
with col1:
    if st.button("📊 Use Demo Data"):
        st.session_state.mode = "demo"
        st.session_state.trades = demo_data()
with col2:
    if st.button("✍️ Enter My Own Trades"):
        st.session_state.mode = "user"
        st.session_state.trades = pd.DataFrame(
            columns=[
                "Date", "Symbol", "Trade Type",
                "Entry Price", "Exit Price",
                "Position Size", "Result"
            ]
        )

st.divider()
df = st.session_state.trades

# ---------------- TRADE ENTRY (USER MODE ONLY) ----------------
if st.session_state.mode == "user":
    st.header("📝 Add a Trade")
    with st.form("trade_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            date = st.date_input("Trade Date")
            symbol = st.text_input("Symbol (e.g. XAUUSD)").upper()
            trade_type = st.selectbox("Trade Type", ["Buy", "Sell"])
        with col2:
            entry = st.number_input("Entry Price", format="%.5f")
            exit = st.number_input("Exit Price", format="%.5f")
            size = st.number_input("Position Size (Lots)", min_value=0.01, step=0.01)
        with col3:
            result = st.selectbox("Result", ["Win", "Loss", "Break-even"])
        submit = st.form_submit_button("➕ Add Trade")
    if submit:
        new_trade = pd.DataFrame([{
            "Date": date,
            "Symbol": symbol,
            "Trade Type": trade_type,
            "Entry Price": entry,
            "Exit Price": exit,
            "Position Size": size,
            "Result": result
        }])
        st.session_state.trades = pd.concat([st.session_state.trades, new_trade], ignore_index=True)
        st.success("Trade added successfully!")

st.divider()

# ---------------- TRADE HISTORY ----------------
st.header("📒 Trade History")
if df.empty:
    st.info("No trades available.")
    st.stop()
st.dataframe(df, use_container_width=True)

# ---------------- OVERALL METRICS ----------------
st.header("📊 Overall Performance")
total = len(df)
wins = len(df[df["Result"] == "Win"])
losses = len(df[df["Result"] == "Loss"])
breakeven = len(df[df["Result"] == "Break-even"])
win_rate = (wins / total) * 100 if total > 0 else 0
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Trades", total)
col2.metric("Wins", wins)
col3.metric("Losses", losses)
col4.metric("Win Rate (%)", f"{win_rate:.2f}")

st.divider()

# ---------------- PIE CHARTS ----------------
st.header("🥧 Trade Distribution")

# Pie chart: Results
result_counts = df["Result"].value_counts().reset_index()
result_counts.columns = ["Result", "Count"]
pie_results = alt.Chart(result_counts).mark_arc(innerRadius=40).encode(
    theta="Count:Q",
    color="Result:N",
    tooltip=["Result", "Count"]
)
st.subheader("Results Distribution")
st.altair_chart(pie_results, use_container_width=True)

# Pie chart: Symbols
symbol_counts = df["Symbol"].value_counts().reset_index()
symbol_counts.columns = ["Symbol", "Count"]
pie_symbols = alt.Chart(symbol_counts).mark_arc(innerRadius=40).encode(
    theta="Count:Q",
    color="Symbol:N",
    tooltip=["Symbol", "Count"]
)
st.subheader("Symbols Traded")
st.altair_chart(pie_symbols, use_container_width=True)

st.divider()

# ---------------- DAILY PERFORMANCE ----------------
st.header("📅 Daily Performance")
daily = df.groupby(["Date", "Result"]).size().unstack(fill_value=0).reset_index()
daily["Total Trades"] = daily.drop(columns=["Date"]).sum(axis=1)
daily["Win Rate (%)"] = (daily.get("Win", 0) / daily["Total Trades"] * 100).round(2)
st.dataframe(daily, use_container_width=True)

st.divider()

# ---------------- WEAKNESSES & TIPS ----------------
st.header("⚠ Weaknesses & 💡 Tips")
if win_rate < 40:
    st.warning("Low win rate detected. Improve trade selection.")
if losses > wins:
    st.warning("More losses than wins. Review risk management.")
if win_rate >= 40 and losses <= wins:
    st.success("Good trading discipline detected. Stay consistent.")
st.info("Tip: Always journal your trades immediately after closing them.")

st.divider()
st.caption("© 2026 | Trading Journal with Demo & User Mode (Altair Charts, Streamlit Cloud Ready)")
