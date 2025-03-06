import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile


st.title("📊 Dashboard Analisis Penyewaan Sepeda 🚴")

zip_path = r"C:\Users\USER\Bike-sharing-dataset.zip"
csv_filename = "day.csv"

try:
  
    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open(csv_filename) as file:
            data = pd.read_csv(file)

   
    st.subheader("📋 Data Penyewaan Sepeda")
    st.write(data.head())

   
    data.rename(columns={"season": "Musim", "weathersit": "Cuaca", "cnt": "Jumlah Penyewaan", "temp": "Suhu"}, inplace=True)

    
    st.subheader("📅 Jumlah Penyewaan Sepeda Berdasarkan Musim")
    musim_avg = data.groupby("Musim")["Jumlah Penyewaan"].mean()

    fig, ax = plt.subplots()
    sns.barplot(x=musim_avg.index, y=musim_avg.values, palette="coolwarm", ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig)

   
    st.subheader("🌦️ Pengaruh Cuaca terhadap Penyewaan Sepeda")
    cuaca_avg = data.groupby("Cuaca")["Jumlah Penyewaan"].mean()

    fig, ax = plt.subplots()
    sns.barplot(x=cuaca_avg.index, y=cuaca_avg.values, palette="viridis", ax=ax)
    ax.set_xlabel("Cuaca")
    ax.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig)

    
    st.subheader("🌡️ Hubungan Suhu dan Penyewaan Sepeda")
    
    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(data=data, x="Suhu", y="Jumlah Penyewaan", alpha=0.5, ax=ax)
    ax.set_title("Hubungan Suhu dan Penyewaan Sepeda")
    ax.set_xlabel("Suhu Normalisasi")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

    st.subheader("📝 Kesimpulan")
    st.write(
        """
        - Penyewaan sepeda cenderung lebih tinggi di musim tertentu.
        - Cuaca juga berpengaruh terhadap jumlah penyewaan sepeda.
        - Penyewaan meningkat saat suhu optimal dan menurun saat terlalu panas/dingin.
        - Analisis lebih lanjut bisa dilakukan dengan mempertimbangkan faktor lain seperti hari kerja atau akhir pekan.
        """
    )

except FileNotFoundError:
    st.error(f"File {zip_path}")
