import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title='EDA - Anti Money Laundering',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():



    # Membuat Title
    st.title('Money Laundering Analysis')
    # Menambahkan Deskripsi
    st.write('Page ini dibuat oleh _Zidny Yasrah Sallum_')
    st.markdown('---')
    st.write("<span style='font-size: 25px;'><b>Apa itu Pencucian Uang?</b></span>", unsafe_allow_html=True)
    moneyLaundering = '''
    Money Laundering atau pencucian uang adalah upaya menyembunyikan atau menyamarkan uang atau dana yang diperoleh 
    dari suatu aksi kejahatan atau hasil tindak pidana sehingga seolah-olah tampak menjadi harta kekayaan yang sah. 
    
    Ada 3 tahapan dari Money laundering yaitu:

    * **Placement**, ketika dana ilegal tersebut masuk ke dalam sistem finansial.
    * **Layering**, aktivitas yang dilakukan untuk menjauhkan uang yang diperoleh dari tindakan kejahatan tersebut.
    * **Integration**, upaya untuk menggabungkan atau menggunakan uang hasil money laundering untuk dinikmati langsung

    source : https://sikapiuangmu.ojk.go.id/FrontEnd/CMS/Article/10470, 
    https://www.bfi.co.id/id/blog/money-laundering-adalah-definisi-jenis-dan-cara-mencegah#toc-2

    ---

    '''
    st.write(moneyLaundering)

    # Show DataFrame
    st.write('## Dataset Quick Peek')
    data = pd.read_csv('dataset_AML.csv')
    st.dataframe(data.head())
    st.markdown('---')



    # Membuat dan menampilkan pie chart
    laundry = data['Is Laundering'].value_counts()
    explode = [0.1, 0]
    fig = plt.figure(figsize=(15,5)) 
    plt.subplot(1,3,1)
    sns.histplot(data=data, x='Amount Paid', kde=True, bins=40)
    
    plt.subplot(1,3,2)
    laundry.plot(kind='pie', title='Money Laundering Distribution', explode=explode, shadow = True, autopct='%.2f%%')


    plt.subplot(1,3,3)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='%Y/%m/%d %H:%M')
    # Membuat kolom baru day yang diextract dari kolom timestamp
    data['day'] = data['Timestamp'].dt.date
    # Menghitung frekuensi dari transaksi setiap harinya
    day_counts = data['day'].value_counts().sort_index()

    # Plot untuk menampilkan perubahan transaksi tiap harinya
    plt.plot(day_counts.index, day_counts.values, marker='o')
    plt.xlabel('Hari')
    plt.ylabel('Frekuensi')
    plt.title('Frekuensi Transaksi Setiap Harinya')
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)
    st.write(laundry)
    
    # Membuat Histogram Berdasarkan Input User
    st.write('#### Histogram Plot')
    choice = st.radio('Select Columns : ', ('Payment Currency','Receiving Currency','Payment Format'))
    fig = plt.figure(figsize=(15,5))
    sns.countplot(data=data, x=choice)
    plt.xticks(rotation=20)
    st.pyplot(fig)

    




if __name__ == '__main__':
    run()