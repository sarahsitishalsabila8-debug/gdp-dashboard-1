import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Database Bahan Kimia",
    page_icon="🧪",
    layout="wide"
)

data = {
    "Asam Klorida": {
        "rumus": "HCl",
        "wujud": "Cairan tidak berwarna",
        "bahaya": "Korosif, Iritan",
        "ghs": "☣️"
    },
    "Asam Sulfat": {
        "rumus": "H₂SO₄",
        "wujud": "Cairan kental tidak berwarna",
        "bahaya": "Korosif",
        "ghs": "☣️"
    },
    "Asam Nitrat": {
        "rumus": "HNO₃",
        "wujud": "Cairan bening",
        "bahaya": "Korosif, Oksidator",
        "ghs": "☣️🔥"
    },
    "Kalium Hidroksida": {
        "rumus": "KOH",
        "wujud": "Padatan putih",
        "bahaya": "Korosif",
        "ghs": "☣️"
    },
    "Benzoil Peroksida": {
        "rumus": "C₁₄H₁₀O₄",
        "wujud": "Kristal tidak berwarna",
        "bahaya": "Oksidator, Mudah Terbakar, Iritan",
        "ghs": "🔥☣️"
    }
}

st.title("🧪 Database Bahan Kimia Laboratorium")

pilihan = st.sidebar.selectbox(
    "Pilih Bahan Kimia",
    list(data.keys())
)

bahan = data[pilihan]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Informasi Bahan")
    st.write("*Nama Bahan:*", pilihan)
    st.write("*Rumus Kimia:*", bahan["rumus"])
    st.write("*Wujud/Warna:*", bahan["wujud"])

with col2:
    st.subheader("Bahaya")
    st.write("*Klasifikasi:*", bahan["bahaya"])
    st.write("*Piktogram:*", bahan["ghs"])

st.success("Data diambil dari database bahan kimia laboratorium.")
