import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu


st.image("download.jpg")

# Tampilan Login

if 'login' not in st.session_state:
    st.session_state.login = False

def login():
    st.title ("Welcome To LaundrIN")
    
    choice = st.selectbox('Login/Sign Up', ['Login', 'Sign Up'])
    if choice == 'Login':
        username = st.text_input('Username')
        password = st.text_input('Password', type="password")
        
        if st.button('Login'):
            if username == 'admin' and password == 'admin':
                st.session_state.login = True
                st.success('Anda berhasil login')
                st.rerun()
    else:
        email = st.text_input('Email')
        password = st.text_input('Password', type="password")
        
        username = st.text_input('Masukan username anda')
        
        st.button('Buat Akun Saya')
        st.success("Selamat anda berhasil membuat akun") 

def main():
    # Main title centered below
    st.title("🔼LaundrIN")

    logout_container = st.container()
    with logout_container:
        col1, col2 = st.columns([6, 1])  
        if col2.button("Logout"):
            st.session_state.login = False
            st.rerun()
    
    # Header navigasi
    Beranda, Data_Pelanggan, Pendapatan_Bulanan, Harga, Tentang_Kami = st.tabs(["Beranda","Data Pelanggan","Pendapatan Bulanan", "Harga", "Tentang Kami"])

    # Beranda
    with Beranda:
        st.title('Beranda')
        # konten pertama
        st.write("Cuci dan keringkan pakaian Anda dengan metode cuci kering.")
        st.image("setrika kering.jpg")
        st.text("Cuci kering (dry cleaning) adalah metode pencucian pakaian menggunakan pelarut kimia khusus, bukan air. Proses dimulai dengan pemeriksaan dan penyortiran pakaian, lalu dicuci menggunakan pelarut seperti Perchloroethylene (PERC), dikeringkan dalam mesin khusus, dan diakhiri dengan pressing/setrika.")
        # konten kedua
        st.write("Cuci pakaian Anda dengan metode cuci basah")
        st.image("cuci basah.jpg")
        st.text("Cuci basah adalah metode pencucian menggunakan air dan deterjen, biasanya untuk pakaian sehari-hari. Prosesnya meliputi sortir pakaian, perendaman, pencucian dengan mesin/manual, pembilasan, pengeringan, dan penyetrikaan. Metode ini lebih murah tapi tidak cocok untuk bahan sensitif seperti sutra.")
        # konten ketiga
        st.write ("Kami juga menyediakan layanan setrika untuk pakaian Anda.")
        st.image("setrika.jpg")
        st.text("Untuk usaha laundry, setrika uap merupakan pilihan yang tepat karena dapat memberikan hasil setrikaan yang rapi dan halus. Berikut ini adalah beberapa tips menggunakan setrika uap untuk laundry")
        # price List
        st.write("Harga Cuci dan Keringkan Pakaian")
        st.image("poto.jpg")

         # Footer
        st.write("Terima kasih telah menggunakan layanan kami!")

        
    # Input Data
    with Harga:
        st.title("Input Data")
        nama_pelanggan = st.text_input("Nama Pelanggan  👤")
        jenis_layanan = st.selectbox("Jenis Layanan", ["Cuci kering", "Cuci Basah", "Setrika"])
        berat_barang = st.number_input("Berat Barang (kg)", min_value=0.0, step=0.5)

    # Harga Layanan
        harga_cuci = 5000
        harga_setrika = 2000
        harga_cuci_setrika = 7000

    # Total Harga
        if jenis_layanan == "Cuci":
            total_harga = harga_cuci * berat_barang
        elif jenis_layanan == "Setrika":
            total_harga = harga_setrika * berat_barang
        else:
            total_harga = harga_cuci_setrika * berat_barang

        # Tampilkan Total Harga
        st.header("Total Harga")
        st.write(f"Total Harga: Rp {total_harga:,.2f}")

        # Tombol Bayar
        if st.button("Bayar"):
            st.success("Pembayaran Berhasil!")
            st.write("Terima kasih telah menggunakan jasa kami!")

    # Table Pendapatan Harian
    with Pendapatan_Bulanan: 
        st.title("Table Pendapatan Bulanan")
        
        # Data Pendapatan Harian
        Pendapatan_Bulanan = {
            "Bulan": ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"],
            "Pendapatan": [1000000, 1200000, 1500000, 1000000, 2000000, 4000000, 2500000, 2800000, 3000000, 2200000, 3500000, 3800000]
        }

        df = pd.DataFrame(Pendapatan_Bulanan)

        # Buat Grafik
        fig = px.bar(df, x="Bulan", y="Pendapatan", title="Pendapatan Bulanan")
        st.plotly_chart(fig)

    with Tentang_Kami:
        st.title("TentangKami")
        st.write("Aplikasi ini dibuat oleh kelompok 3, yang terdiri dari Fathan, Ipan, Siti, Shinta")

        col1, col2, col3, col4 = st.columns(4, gap="small")
        col1.image("patan.png", caption="Fathan Anwar")
        col2.image("ipan.jpg", caption="Muhammad Irfan Fadhilah")
        col3.image("siti.jpg", caption="Siti Mufathonah")
        col4.image("shinta.jpg", caption="Shinta Maulida Distiandini")

        
    # Data pelanggan
        with Data_Pelanggan:
            st.title("Data Pelanggan")
            col1, col2 = st.columns(2)
            with col1:
                nama_pelanggan = st.text_input("Nama Pelanggan")
                jenis_layanan = st.selectbox(
                    "Jenis Layanan",
                    ("Cuci", "Setrika", "Cuci+Setrika"),
                )

            with col2:
                berat_barang = st.number_input("Berat Barang (kg)", step=0.5)
                tanggal_masuk = st.date_input("Tanggal Masuk")
                tanggal_keluar = st.date_input("Tanggal Keluar")

            if st.button("Simpan"):
                st.success("Data Pelanggan Berhasil Disimpan!")
                st.write("Terima kasih telah menggunakan jasa kami!")

                st.header("Data Pelanggan")
                data_pelanggan = {
                    "Nama Pelanggan": [nama_pelanggan],
                    "Jenis Layanan": [jenis_layanan],
                    "Berat Barang": [berat_barang],
                    "Tanggal Masuk": [tanggal_masuk],
                    "Tanggal Keluar": [tanggal_keluar]
                }
                df = pd.DataFrame(data_pelanggan)
                st.write(df)

if not st.session_state.login:
    login()
else:
    main()





