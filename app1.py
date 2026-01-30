# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 09:48:48 2026

@author: ntoto
"""

import streamlit as st
import pandas as pd
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Trading Plan & Performance Analyzer",
    page_icon="📊",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("📈 Trading Plan & Performance Analyzer")
st.write(
    "Log your trades, analyze your performance, identify weaknesses, "
    "and get actionable tips to improve your trading."
)

st.divider()

# ---------------- SESSION STATE ----------------
if "trades" not in st.session_state:
    st.session_state.trades = pd.DataFrame(
        columns=[
            "Date", "Symbol", "Trade Type",
            "Entry Price", "Exit Price",
            "Position Size", "Result"
        ]
    )

# ---------------- TRADE ENTRY ----------------
st.header("📝 Enter a Trade")

with st.form("trade_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        date = st.date_input("Trade Date")
        symbol = st.text_input("Symbol (e.g. XAUUSD, EURUSD)")
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
        "Symbol": symbol.upper(),
        "Trade Type": trade_type,
        "Entry Price": entry,
        "Exit Price": exit,
        "Position Size": size,
        "Result": result
    }])

    st.session_state.trades = pd.concat(
        [st.session_state.trades, new_trade],
        ignore_index=True
    )

    st.success("Trade added successfully!")

st.divider()

# ---------------- TRADE JOURNAL ----------------
st.header("📒 Trade Journal")

if st.session_state.trades.empty:
    st.info("No trades entered yet.")
else:
    st.dataframe(st.session_state.trades, use_container_width=True)

# ---------------- ANALYSIS ----------------
st.header("📊 Performance Analysis")

if not st.session_state.trades.empty:

    df = st.session_state.trades.copy()

    total_trades = len(df)
    wins = len(df[df["Result"] == "Win"])
    losses = len(df[df["Result"] == "Loss"])
    breakeven = len(df[df["Result"] == "Break-even"])

    win_rate = (wins / total_trades) * 100 if total_trades > 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Trades", total_trades)
    col2.metric("Wins", wins)
    col3.metric("Losses", losses)
    col4.metric("Win Rate (%)", f"{win_rate:.2f}")

    st.divider()

    # ---------------- SYMBOL ANALYSIS ----------------
    st.subheader("📌 Performance by Symbol")

    symbol_perf = df.groupby("Symbol")["Result"].value_counts().unstack(fill_value=0)
    st.dataframe(symbol_perf, use_container_width=True)

    # ---------------- WEAKNESS DETECTION ----------------
    st.subheader("⚠ Identified Weak Points")

    weaknesses = []

    if win_rate < 40:
        weaknesses.append("Low overall win rate")

    if losses > wins:
        weaknesses.append("More losses than wins")

    frequent_losses = symbol_perf.get("Loss", pd.Series()).sort_values(ascending=False)
    if not frequent_losses.empty:
        worst_symbol = frequent_losses.idxmax()
        if frequent_losses.max() >= 3:
            weaknesses.append(f"Frequent losses on {worst_symbol}")

    if weaknesses:
        for w in weaknesses:
            st.warning(w)
    else:
        st.success("No major weaknesses detected. Good discipline!")

    # ---------------- IMPROVEMENT TIPS ----------------
    st.subheader("💡 Improvement Tips")

    tips = []

    if win_rate < 40:
        tips.append("Refine your entry criteria and wait for higher-probability setups.")

    if losses > wins:
        tips.append("Reduce position size and focus on risk management.")

    if "Frequent losses on" in " ".join(weaknesses):
        tips.append("Consider avoiding or backtesting that symbol further.")

    if total_trades < 20:
        tips.append("Log more trades to get a clearer performance picture.")

    if tips:
        for t in tips:
            st.info(t)
    else:
        st.success("Your trading plan looks solid. Stay consistent!")

else:
    st.info("Enter trades to unlock analysis and insights.")

st.divider()
st.caption("© 2026 | Trading Plan & Performance Analyzer")
