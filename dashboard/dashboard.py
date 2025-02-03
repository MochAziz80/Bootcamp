import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data_gucheng = pd.read_csv("cleaned_data.csv")

# Judul Dashboard
st.title("Dashboard Kualitas Udara")

# Deskripsi
st.write("""
    Dashboard ini menunjukkan analisis kualitas udara dan cuaca,
    serta perubahan kualitas udara setelah hujan.
""")

# Menampilkan Data
st.header("Data Kualitas Udara")
st.dataframe(data_gucheng.head())

# Korelasi Antar Variabel
st.header("Korelasi antara Kualitas Udara dan Cuaca")
correlation_matrix = data_gucheng[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "TEMP", "PRES", "DEWP", "RAIN"]].corr()

# Tampilkan heatmap korelasi
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# Bandingkan PM2.5 Sebelum dan Sesudah Hujan
st.header("Perubahan Kualitas Udara Setelah Hujan")
data_gucheng["rain_status"] = data_gucheng["RAIN"].apply(lambda x: "Hujan" if x > 0 else "Tidak Hujan")

# Boxplot PM2.5
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x="rain_status", y="PM2.5", data=data_gucheng, ax=ax)
st.pyplot(fig)

# Tampilkan Rata-Rata PM2.5 Hujan vs Tidak Hujan
st.write("Rata-rata PM2.5:")
st.write(data_gucheng.groupby("rain_status")["PM2.5"].mean())
