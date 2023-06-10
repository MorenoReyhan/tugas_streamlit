import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Menggunakan distribusi Chi-kuadrat
def chi2_distribution(df, x):
    return chi2.pdf(x, df)

# Menampilkan halaman aplikasi
def main():
    st.title("Distribusi Chi-Kuadrat App")
    st.sidebar.header("Parameter Distribusi Chi-Kuadrat")

    # Mengatur parameter distribusi Chi-kuadrat
    df = st.sidebar.slider("Derajat kebebasan (df)", 1, 100, 10)

    # Menghasilkan sampel distribusi Chi-kuadrat
    x = np.linspace(0, 30, 100)
    y = chi2_distribution(df, x)

    # Menampilkan plot distribusi Chi-kuadrat
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.fill_between(x, y, 0, alpha=0.3)
    ax.set_xlabel("Nilai")
    ax.set_ylabel("Probabilitas")
    ax.set_title(f"Distribusi Chi-Kuadrat (df={df})")
    st.pyplot(fig)

    # Melakukan pengujian hipotesis
    st.header("Pengujian Hipotesis")
    observed_value = st.number_input("Nilai Observasi")
    p_value = 1 - chi2.cdf(observed_value, df)
    st.write(f"Nilai p: {p_value}")

if __name__ == "__main__":
    main()
