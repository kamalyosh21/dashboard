import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import os

# Judul Dashboard
st.title("📊 Dashboard Analisis Penyewaan Sepeda 🚴")


zip_path = "Bike-sharing-dataset.zip"
csv_filename = "day.csv"
if not os.path.exists(zip_path):
    st.error(f"File {zip_path} tidak ditemukan. Pastikan file ZIP tersedia di lokasi yang benar!")
else:

    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open(csv_filename) as f:
            data = pd.read_csv(f)

    st.subheader("📋 Data Penyewaan Sepeda")
    st.write(data.head())

    
    data.rename(columns={"season": "Musim", "weathersit": "Cuaca", "cnt": "Jumlah Penyewaan"}, inplace=True)

    st.subheader("📅 Jumlah Penyewaan Sepeda Berdasarkan Musim")
    musim_avg = data.groupby("Musim")["Jumlah Penyewaan"].mean()

    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=musim_avg.index, y=musim_avg.values, palette="coolwarm", ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig)


    st.subheader("🌦️ Pengaruh Cuaca terhadap Penyewaan Sepeda")
    cuaca_avg = data.groupby("Cuaca")["Jumlah Penyewaan"].mean()

    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=cuaca_avg.index, y=cuaca_avg.values, palette="viridis", ax=ax)
    ax.set_xlabel("Cuaca")
    ax.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig)

    st.subheader("🔥 Hubungan Suhu dan Penyewaan Sepeda")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(data=data, x="temp", y="Jumlah Penyewaan", alpha=0.5)
    ax.set_xlabel("Suhu Normalisasi")
    ax.set_ylabel("Jumlah Penyewaan")
    plt.title("Hubungan Suhu dan Penyewaan Sepeda")
    st.pyplot(fig)

    
    st.subheader("📝 Kesimpulan")
    st.write(
        """
        - Penyewaan sepeda cenderung lebih tinggi di musim tertentu.
        - Cuaca juga berpengaruh terhadap jumlah penyewaan sepeda.
        - Semakin tinggi suhu, cenderung semakin banyak sepeda yang disewa.
        - Analisis lebih lanjut bisa dilakukan dengan mempertimbangkan faktor lain seperti hari kerja dan libur nasional.
        """
    )
