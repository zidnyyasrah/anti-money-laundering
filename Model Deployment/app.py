import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Pilih Halaman: ', ('EDA', 'Predict Money Laundering'))

if navigation == 'EDA':
    eda.run()
elif navigation == 'Predict Money Laundering':
    prediction.run()