import config
import streamlit as st
import requests, redis
from iex import IEXStock
from datetime import datetime, timedelta


symbol = st.sidebar.text_input("Symbol", value="AAPL") 

stock = IEXStock(config.API_KEY, symbol)
#client = redis.Redis(host="localhost", port=6379)

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News')) #, 'Ownership', 'Technicals'))
st.title(screen) 

if screen == "Overview" :
    
    company_info = stock.get_company_info()
    st.subheader(company_info['companyName'])
    logo = stock.get_logo()  
    st.image(logo['url'])  

    st.subheader('Description')
    st.write(company_info['description'])
    st.subheader('Industry')
    st.write(company_info['industry'])
    st.subheader('CEO')
    st.write(company_info['CEO'])

if screen == "Fundamentals" :
    stats = stock.get_stats()

    st.subheader('Company Name')
    st.write(stats['companyName'])
    st.subheader('market cap')
    st.write(stats['marketcap'])
    st.subheader('week52high')
    st.write(stats['week52high'])
    st.subheader('week52low')
    st.write(stats['week52low'])
    st.subheader('week52highSplitAdjustOnly')
    st.write(stats['week52highSplitAdjustOnly'])
    st.subheader('week52lowSplitAdjustOnly')
    st.write(stats['week52lowSplitAdjustOnly'])
    st.subheader('week52change')
    st.write(stats['week52change'])
    st.subheader('sharesOutstanding')
    st.write(stats['sharesOutstanding'])
    st.subheader('float')
    st.write(stats['float'])
    st.subheader('avg10Volume')
    st.write(stats['avg10Volume'])
    st.subheader('avg30Volume')
    st.write(stats['avg30Volume'])
    st.subheader('day200MovingAvg')
    st.write(stats['day200MovingAvg'])
    st.subheader('day50MovingAvg')
    st.write(stats['day50MovingAvg'])
    st.subheader('employees')
    st.write(stats['employees'])
    st.subheader('ttmEPS')
    st.write(stats['ttmEPS'])
    st.subheader('ttmDividendRate')
    st.write(stats['ttmDividendRate'])
    st.subheader('dividendYield')
    st.write(stats['dividendYield'])
    st.subheader('nextDividendDate')
    st.write(stats['nextDividendDate'])
    st.subheader('exDividendDate')
    st.write(stats['exDividendDate'])
    st.subheader('nextEarningsDate')
    st.write(stats['nextEarningsDate'])
    st.subheader('peRatio')
    st.write(stats['peRatio'])
    st.subheader('beta')
    st.write(stats['beta'])
    st.subheader('maxChangePercent')
    st.write(stats['maxChangePercent'])
    st.subheader('year5ChangePercent')
    st.write(stats['year5ChangePercent'])
    st.subheader('year2ChangePercent')
    st.write(stats['year2ChangePercent'])
    st.subheader('year1ChangePercent')
    st.write(stats['year1ChangePercent'])
    st.subheader('ytdChangePercent')
    st.write(stats['ytdChangePercent'])
    st.subheader('month6ChangePercent')
    st.write(stats['month6ChangePercent'])
    st.subheader('month3ChangePercent')
    st.write(stats['month3ChangePercent'])
    st.subheader('month1ChangePercent')
    st.write(stats['month1ChangePercent'])
    st.subheader('day30ChangePercent')
    st.write(stats['day30ChangePercent'])
    st.subheader('day5ChangePercent')
    st.write(stats['day5ChangePercent'])

if screen == 'News':

    news = stock.get_company_news()

    for article in news:
        st.subheader(article['headline'])
        dt = datetime.utcfromtimestamp(article['datetime']/1000).isoformat()
        st.write(f"Posted by {article['source']} at {dt}")
        st.write(article['url'])
        st.write(article['summary'])
        st.image(article['image'])

if screen == 'Ownership': # paid subscription needed for this
    st.subheader("Institutional Ownership")


    institutional_ownership = stock.get_institutional_ownership()

    for institution in institutional_ownership:
        st.write(institution['date'])
        st.write(institution['entityProperName'])
        st.write(institution['reportedHolding'])

    st.subheader("Insider Transactions")


 
    insider_transactions = stock.get_insider_transactions()

    for transaction in insider_transactions:
        st.write(transaction['filingDate'])
        st.write(transaction['fullName'])
        st.write(transaction['transactionShares'])
        st.write(transaction['transactionPrice'])
