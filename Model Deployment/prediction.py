import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import joblib

# Menggunakan joblib untuk meload model
pipeline = joblib.load('rf_model.pkl')

def run():
    # create the title
    st.title('Predict Transaction')
    st.markdown('---')
    
    # Membuat Title
    st.title('Fill Your Transaction Data')
    with st.form('key=form_employee'):

 
        From_Bank = st.number_input('Sender Bank', value=70, min_value=1, max_value=356217, help='Bank Code')
        Account = st.text_input('Sender Account',value='80E40A2C0', help='Account Code')
        To_Bank = st.number_input('Receiver Bank', value=70, min_value=1, max_value=356217, help='Bank Code')
        Account1 = st.text_input('Receiver Account',value='80E40A2C0', help='Account Code')
        Amount_Paid = st.slider('Transaction Amount (US Dollar)', min_value=0.01, max_value=16620608535.74) 
        Payment_Format = st.selectbox('Transaction Format',('Wire', 'Cheque', 'Credit Card', 'ACH', 'Reinvestment', 'Cash', 'Bitcoin'))
        st.write('You selected:', Payment_Format)
        date = st.date_input('Transaction Date')
        time = st.time_input('Transaction Time')

        same_bank=0
        if From_Bank == To_Bank:
            same_bank=1
        else:
            same_bank=0
        
        day = date.day
        hour = time.hour
        minute = time.minute

        submitted = st.form_submit_button('Predict')

    # Membuat data inference baru
    data_inf = {
    'From Bank': From_Bank,
    'Account': Account,
    'To Bank': To_Bank,
    'Account.1': Account1,
    'Amount Paid': Amount_Paid,
    'Payment Format': Payment_Format,
    'Day': day,
    'Hour': hour,
    'Minute': minute,
    'same_bank': same_bank,
}

    data_inf = pd.DataFrame([data_inf])

    if submitted:
        # Melakukan prediksi dengan model dari data baru
        prediksi = pipeline.predict(data_inf)
        prediksi = int(prediksi)
        value = ''
        if prediksi == 0:
            value = "Safe Transaction"
        elif prediksi == 1:
            value = "Money Laundering scheme Detected"
        st.write('# Prediction :', value)
   
        
if __name__ == '__main__':
   run()