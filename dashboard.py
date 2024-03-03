# Import library yang diperlukan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Atur opsi untuk menyembunyikan pesan peringatan PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Data Wrangling
## Gathering Data
bike_hour_df = pd.read_csv("hour.csv", delimiter=",")

# Menentukan Pertanyaan Bisnis
st.title("Proyek Analisis Data: Bike Sharing Dataset")
st.write("Nama          : Eldad Vikorian")
st.write("Email         : eldadrian05@gmail.com")
st.write("ID Dicoding   : Eldad Vikorian")

st.write("# Menentukan Pertanyaan Bisnis")
st.write("Pertanyaan 1: Bagaimana pola penggunaan sepeda berdasarkan waktu (bulanan)?")
st.write("Pertanyaan 2: Apakah faktor cuaca seperti suhu, kelembaban, dan kondisi cuaca memengaruhi penggunaan sepeda?")

# Cleaning Data
## Mengecek missing values
missing_values = bike_hour_df.isnull().sum()
st.write("Missing Values:")
st.write(missing_values)

# Exploratory Data Analysis (EDA)
## Menampilkan ringkasan statistik
st.write("Ringkasan Statistik:")
st.write(bike_hour_df.describe())

# Visualization & Explanatory Analysis
## Pertanyaan 1: Bagaimana pola penggunaan sepeda berdasarkan waktu (misalnya, harian, mingguan, bulanan)?
st.write("## Pertanyaan 1: Bagaimana pola penggunaan sepeda berdasarkan waktu?")
st.write("Grafik waktu penggunaan sepeda per bulan:")
# Mengubah kolom 'dteday' menjadi tipe data datetime
bike_hour_df['dteday'] = pd.to_datetime(bike_hour_df['dteday'])
# Ekstraksi bulan dari kolom 'dteday'
bike_hour_df['month'] = bike_hour_df['dteday'].dt.month_name()
# Mengurutkan bulan sesuai urutan kalender
bulan_urut = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
monthly_usage = bike_hour_df.groupby('month')['cnt'].sum().reset_index()
monthly_usage['month'] = pd.Categorical(monthly_usage['month'], categories=bulan_urut, ordered=True)
monthly_usage = monthly_usage.sort_values('month')
# Mendapatkan bulan dengan jumlah pengguna sepeda tertinggi
max_month = monthly_usage.loc[monthly_usage['cnt'].idxmax(), 'month']
# Membuat diagram batang
plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='cnt', data=monthly_usage, palette=['red' if month == max_month else 'gray' for month in monthly_usage['month']])
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pengguna')
plt.title('Jumlah Pengguna Sepeda per Bulan')
plt.xticks(rotation=45)  # Rotasi label bulan agar terbaca dengan baik
plt.tight_layout()
plt.savefig('jumlah_pengguna_sepeda_per_bulan.png')  # Menyimpan visualisasi
st.pyplot()

## Pertanyaan 2: Apakah faktor cuaca seperti suhu, kelembaban, dan kondisi cuaca memengaruhi penggunaan sepeda?
st.write("## Pertanyaan 2: Apakah faktor cuaca memengaruhi penggunaan sepeda?")
st.write("Korelasi antara variabel cuaca dan jumlah pengguna sepeda:")
plt.figure(figsize=(10,6))
sns.heatmap(bike_hour_df[['temp', 'hum', 'windspeed', 'cnt']].corr(), annot=True, cmap='coolwarm')
plt.title('Korelasi antara Variabel Cuaca dan Jumlah Pengguna Sepeda')
st.pyplot()

# Conclusion
st.write("# Conclusion")
st.write("## Conclusion pertanyaan 1")
st.write("Dari analisis pola penggunaan sepeda berdasarkan bulan, dapat dilihat bahwa penggunaan sepeda cenderung lebih tinggi di bulan-bulan dengan cuaca yang lebih hangat, seperti bulan-bulan musim panas. Bulan-bulan dengan cuaca dingin cenderung memiliki jumlah pengguna sepeda yang lebih rendah. lebih tinggi di bulan-bulan dengan cuaca yang lebih hangat..")
st.write("## Conclusion pertanyaan 2")
st.write("Hasil analisis korelasi antara variabel cuaca (suhu, kelembaban, kecepatan angin) dan jumlah pengguna sepeda menunjukkan bahwa suhu memiliki korelasi positif yang signifikan dengan penggunaan sepeda. Artinya, semakin tinggi suhu, semakin tinggi juga jumlah pengguna sepeda. Di sisi lain, kelembaban dan kecepatan angin memiliki korelasi negatif yang lebih rendah dengan penggunaan sepeda, meskipun tidak sekuat korelasi positif suhu.")
st.write("Dari kedua temuan ini, dapat disimpulkan bahwa faktor cuaca seperti suhu memengaruhi penggunaan sepeda secara signifikan, sedangkan faktor lain seperti kelembaban dan kecepatan angin memiliki pengaruh yang lebih kecil. Oleh karena itu, pemahaman tentang faktor-faktor cuaca ini dapat membantu dalam perencanaan dan pengelolaan layanan penyewaan sepeda, terutama dalam menentukan waktu dan lokasi promosi serta alokasi sumber daya.")
