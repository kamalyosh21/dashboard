# dashboard
# 📊 Dashboard Analisis Penyewaan Sepeda 🚴

## Deskripsi
Dashboard ini menyajikan analisis mengenai penyewaan sepeda yang diambil dari dataset *Capital Bikeshare*. Dataset ini mencakup data penyewaan sepeda yang teragregasi berdasarkan hari dan cuaca, serta faktor musiman dan suhu yang mempengaruhi perilaku penyewaan sepeda.

### Fitur Analisis:
1. **Jumlah Penyewaan Sepeda Berdasarkan Musim**: Menampilkan rata-rata penyewaan sepeda berdasarkan musim.
2. **Pengaruh Cuaca terhadap Penyewaan Sepeda**: Menampilkan rata-rata penyewaan sepeda berdasarkan kondisi cuaca.
3. **Hubungan Suhu dan Penyewaan Sepeda**: Menampilkan scatter plot hubungan antara suhu dan jumlah penyewaan sepeda.
4. **Kesimpulan**: Menyediakan insight umum terkait temuan dari analisis.

## Prasyarat

Pastikan Anda memiliki lingkungan yang sesuai untuk menjalankan dashboard ini. Berikut adalah beberapa prasyarat yang dibutuhkan:
1. **Python 3.x**
2. **Library Python**:
   - `streamlit`
   - `pandas`
   - `matplotlib`
   - `seaborn`
   - `zipfile`
   - `os`

## Instalasi

Ikuti langkah-langkah berikut untuk menjalankan dashboard ini di sistem Anda:

1. **Unduh Berkas**
   Jika belum memiliki berkas, Anda bisa mengunduhnya atau melakukan clone dari repository ini.

2. **Instalasi Library**
   Pastikan Anda telah menginstal semua library yang diperlukan. Jalankan perintah berikut untuk menginstalnya menggunakan `pip`:

   ```bash
   pip install streamlit pandas matplotlib seaborn
