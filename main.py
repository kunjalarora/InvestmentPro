import langchain_helper as lch
import api_footer_data_gen as afdg
import streamlit as st
import requests
import time
import yfinance as yf

# AUTO-REFRESH LOGIC
if 'last_update' not in st.session_state:
    st.session_state.last_update = 0

if time.time() - st.session_state.last_update > 30:
    st.session_state.last_update = time.time()
    st.rerun()

#Main App
st.title("Investment Pro")
st.subheader("Find the best investment options based on your preferences")
user_investment_type = st.sidebar.selectbox("what kind of investment do you want to make?", ("long term", "short term", "mutual funds", "etfs", "stocks"))

user_currency_type = st.sidebar.selectbox("what currency do you to trade in", ("USD Dollar", "CAD Dollar", "INR Rupee", "Euro", "Pound Sterling", "Any")) 
if user_currency_type and user_investment_type:
    response = lch.generate_ticker_name(user_investment_type, user_currency_type)
    st.text(response['ticker_name']) 

# ADD TICKER FOOTER
ticker_html = afdg.create_ticker()
st.markdown(ticker_html, unsafe_allow_html=True)

