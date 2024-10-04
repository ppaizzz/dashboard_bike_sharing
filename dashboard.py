# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
day_data = pd.read_csv('day.csv')
hour_data = pd.read_csv('hour.csv')

# Streamlit UI - Title and Description
st.title("Bike Sharing Data Dashboard")
st.markdown("""
    ### Analisis Peminjaman Sepeda
    Dashboard ini menampilkan visualisasi data peminjaman sepeda berdasarkan cuaca dan waktu.
    Anda dapat melihat analisis berdasarkan dataset harian (day.csv) dan per jam (hour.csv).
""")

# Sidebar for dataset selection
option = st.sidebar.selectbox('Pilih dataset:', ('Harian', 'Per Jam'))

# Display dataset
if option == 'Harian':
    st.subheader("Dataset Harian")
    st.dataframe(day_data)
    
    # Visualisasi data peminjaman sepeda per cuaca
    st.subheader("Distribusi Peminjaman Sepeda Berdasarkan Cuaca (Harian)")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=day_data, ax=ax1)
    plt.title('Distribusi Peminjaman Sepeda Berdasarkan Cuaca')
    st.pyplot(fig1)

elif option == 'Per Jam':
    st.subheader("Dataset Per Jam")
    st.dataframe(hour_data)
    
    # Visualisasi peminjaman sepeda berdasarkan jam
    st.subheader("Distribusi Peminjaman Sepeda Berdasarkan Jam (Per Jam)")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='hr', y='cnt', data=hour_data, ax=ax2)
    plt.title('Distribusi Peminjaman Sepeda Berdasarkan Jam')
    st.pyplot(fig2)

# Footer
st.markdown("""
    **Dashboard dibuat menggunakan Streamlit**.  
    Data diambil dari sistem peminjaman sepeda di Washington D.C.
""")