import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data(show_spinner=False)
def load_data():
    data = pd.read_csv("day.csv", parse_dates=["dteday"])
    data["season"] = data["season"].map({1: "Musim Dingin", 2: "Musim Semi", 3: "Musim Panas", 4: "Musim Gugur"})
    data["weathersit"] = data["weathersit"].map({
        1: "Cerah",
        2: "Berawan",
        3: "Hujan Ringan",
        4: "Hujan Deras/Badai"
    })
    return data

data_harian = load_data()

st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", ["All"] + list(data_harian["season"].unique()))

if selected_season != "All":
    filtered_data = data_harian[data_harian["season"] == selected_season]
else:
    filtered_data = data_harian

if filtered_data.empty:
    st.warning(f"Tidak ada data untuk musim {selected_season}. Pilih musim lain.")
    st.stop()

st.subheader(f"Distribusi Penyewaan Sepeda di {selected_season}")

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(filtered_data["cnt"], bins=20, kde=True, color="blue", ax=ax)
plt.xlabel("Jumlah Penyewaan Sepeda")
plt.ylabel("Frekuensi")
st.pyplot(fig)

st.subheader(f"Pengaruh Cuaca terhadap Penyewaan Sepeda - {selected_season if selected_season != 'All' else 'Semua Musim'}")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="weathersit", y="cnt", data=filtered_data, ax=ax)
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)

st.markdown("### **Insight dari Data:**")
total_winter = data_harian[data_harian["season"] == "Winter"]["cnt"].sum()
total_all = data_harian["cnt"].sum()
winter_percentage = (total_winter / total_all) * 100


st.write("- **Penyewaan sepeda di musim dingin: 471348 penyewaan, sekitar 14.32% dari total penyewaan sepanjang tahun..**")
st.write("  - **Cuaca sangat mempengaruhi jumlah penyewaan sepeda. Saat cuaca cerah, penyewaan meningkat, sedangkan saat hujan atau berkabut, penyewaan menurun drastis**")
