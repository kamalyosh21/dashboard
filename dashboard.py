import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


@st.cache_data
def load_data():
    data_harian = pd.read_csv("day.csv", parse_dates=["dteday"])
    return data_harian

data_harian = load_data()


st.title("📊 Dashboard Analisis Penyewaan Sepeda 🚴")


st.subheader("🔍 Korelasi Antar Variabel")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(data_harian.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)




st.subheader("📅 Tren Penyewaan Sepeda Harian")
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x=data_harian["dteday"], y=data_harian["cnt"], ax=ax)
plt.xticks(rotation=45)
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Penyewaan")
plt.title("Tren Penyewaan Sepeda Harian")
st.pyplot(fig)


st.subheader("⛅ Pengaruh Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="weathersit", y="cnt", data=data_harian, ax=ax)
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Penyewaan")
plt.title("Pengaruh Cuaca terhadap Penyewaan Sepeda")
st.pyplot(fig)

st.markdown(
    """
    ✅ **Insight:**  
    - Jumlah penyewaan sepeda cenderung lebih rendah di musim dingin dibandingkan musim lainnya.  
    - Cuaca sangat berpengaruh terhadap jumlah penyewaan sepeda. Saat cuaca cerah, jumlah penyewaan meningkat, sedangkan saat hujan atau berkabut, penyewaan cenderung turun drastis.
    """
)
