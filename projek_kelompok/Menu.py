import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta


st.image("download.jpg")

# Tampilan Login OOOOOOOO

if 'login' not in st.session_state:
    st.session_state.login = False

def login():
    import streamlit as st
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
    
    # Tampilkan halaman login/signup 
    # choice = st.selectbox('Login/Sign Up', ['Login', 'Sign Up'])
    # if choice == 'Login':
    #     username = st.text_input('Username')
    #     password = st.text_input('Password', type="password")
        
    #     if st.button('Login'):
    #         if username == 'admin' and password == 'admin':
    #             st.session_state.login = True
    #             st.success('Anda berhasil login')
    #             st.rerun()
    # else:
    #     email = st.text_input('Email')
    #     password = st.text_input('Password', type="password")
        
    #     username = st.text_input('Masukan username anda')
        
    #     st.button('Buat Akun Saya')
    #     st.success("Selamat anda berhasil membuat akun") 

    

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

    # Beranda OOOOOOOOOOOO1
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

    # Data pelanggan 0000000000002
    with Data_Pelanggan:
        st.title("Data Pelanggan")
        layanan = {
            "Paket Hemat": {
                "Paket 1 (48 jam)": {"waktu": 2, "harga": 12000},  # 2 hari
                "Paket 2 (24 jam)": {"waktu": 1, "harga": 20000},  # 1 hari
                "Paket 3 (12 jam)": {"waktu": 0, "harga": 25000},  # 0.5 hari (12 jam)
                "Paket 4 (8 jam)": {"waktu": 0, "harga": 30000},   # 0.33 hari (8 jam)
                "Paket 5 (4 jam)": {"waktu": 0, "harga": 35000},   # 0.1667 hari (4 jam)
            },
            "Cuci Kering": {
                "Regular": {"waktu": 1, "harga": 5000},
                "Express": {"waktu": 0, "harga": 10000},
            },
            "Cuci Basah": {
                "Regular": {"waktu": 1, "harga": 7000},
                "Express": {"waktu": 0, "harga": 12000},
            },
            "Setrika": {
                "Regular": {"waktu": 1, "harga": 3000},
                "Express": {"waktu": 0, "harga": 7000},
            },
        }

            # Inisialisasi session state untuk menyimpan data pelanggan
        if 'data_pelanggan' not in st.session_state:
                st.session_state.data_pelanggan = []

            # Inisialisasi ID pelanggan
        if 'customer_id_counter' not in st.session_state:
            st.session_state.customer_id_counter = 0  # Inisialisasi ID pelanggan   


            # Input data pelanggan
        st.header("Tambah Data Pelanggan")
        col1, col2 = st.columns(2)

        with col1:
                nama_pelanggan = st.text_input("Nama Pelanggan")
                jenis_layanan = st.selectbox("Pilih Layanan Laundry", list(layanan.keys()))
                
                # Pilih paket atau jenis layanan
                if jenis_layanan in layanan:
                    harga_pilih = st.selectbox("Pilih Tipe Layanan", list(layanan[jenis_layanan].keys()))
                    hari_tambahan = layanan[jenis_layanan][harga_pilih]["waktu"]
                else:
                    hari_tambahan = 4  # Default jika tidak ada layanan yang dipilih

        with col2:
                berat_barang = st.number_input("Berat Barang (kg)", step=0.5)
                tanggal_masuk = st.date_input("Tanggal Masuk", value=datetime.now())
                
                # Hitung tanggal keluar berdasarkan hari_tambahan
                if hari_tambahan >= 0:
                    tanggal_keluar = tanggal_masuk + timedelta(days=hari_tambahan)
                else:
                    tanggal_keluar = tanggal_masuk

            # Tombol untuk menambahkan pelanggan
        if st.button("Tambah Pelanggan"):
                st.session_state.customer_id_counter += 1  # Tambah ID pelanggan
                
                if nama_pelanggan and tanggal_masuk:
                    # Tambahkan data pelanggan ke session state
                    pelanggan = {
                        'Kode': st.session_state.customer_id_counter,
                        'Nama': nama_pelanggan,
                        'Jenis Layanan': jenis_layanan,
                        'Tipe': harga_pilih,
                        'Berat Barang (kg)': berat_barang,
                        'Tanggal Masuk': tanggal_masuk,
                        'Tanggal Keluar': tanggal_keluar,
                        'Durasi Tinggal (hari)': hari_tambahan
                    }
                    st.session_state.data_pelanggan.append(pelanggan)
                    st.success(f"Data pelanggan {nama_pelanggan} berhasil ditambahkan. Tanggal keluar: {tanggal_keluar}.")
                else:
                    st.error("Semua field harus diisi!")

            # Tampilkan data pelanggan
        st.header("Data Pelanggan")
        if st.session_state.data_pelanggan:
                df = pd.DataFrame(st.session_state.data_pelanggan)
                df.index = df.index + 1
                st.write(df)
                #df_reset = df.reset_index(drop=True)
                
                
                
        else:
            st.write("Tidak ada data pelanggan.")    

    # Table Pendapatan Harian OOOOOOOOOO3
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

    # Harga 0000000000004
    with Harga:
        st.title("Pembayaran")
        if st.session_state.data_pelanggan:
            # Ambil nama pelanggan yang unik
            unique_names = list(set(pelanggan['Nama'] for pelanggan in st.session_state.data_pelanggan))
            selected_name = st.selectbox("Pilih Nama Pelanggan untuk Pembayaran", unique_names)
    
        # Filter pelanggan berdasarkan nama yang dipilih
        filtered_customers = [pelanggan for pelanggan in st.session_state.data_pelanggan if pelanggan['Nama'] == selected_name]
    
        # Pilih pelanggan untuk dibayar
        selected_customers = st.multiselect("Pilih Pelanggan untuk Pembayaran", [f"{cust['Kode']} - {cust['Nama']}" for cust in filtered_customers])
    
        # Inisialisasi total_biaya
        total_biaya = 0
        if selected_customers:
            for selected in selected_customers:
                # Ambil ID dari string yang dipilih
                customer_id = int(selected.split(" - ")[0])
                customer_data = [item for item in st.session_state.data_pelanggan if item['Kode'] == customer_id]

                # Tampilkan detail biaya untuk setiap layanan
                for data in customer_data:
                    jenis_layanan = data['Jenis Layanan']
                    tipe_layanan = data['Tipe']
                    berat_barang = data['Berat Barang (kg)']

                    # Hitung total biaya
                    harga_per_kg = layanan[jenis_layanan][tipe_layanan]["harga"]
                    total_biaya += harga_per_kg * berat_barang

                    # Tampilkan detail biaya
                    st.write(f"**Nama:** {data['Nama']}, **Jenis Layanan:** {jenis_layanan}, **Tipe:** {tipe_layanan}, **Berat:** {berat_barang} kg")
                    st.write(f"**Harga per kg:** Rp {harga_per_kg}, **Biaya untuk layanan ini:** Rp {harga_per_kg * berat_barang}")

        # Tampilkan total biaya
        st.write(f"**Total Biaya untuk {len(selected_customers)} layanan: Rp {total_biaya}**")
        
        if st.button("Proses Pembayaran"):
            # Logika untuk memproses pembayaran
            st.success(f"Pembayaran untuk {len(selected_customers)} layanan sebesar Rp {total_biaya} berhasil diproses.")
            st.write("Terima kasih telah menggunakan layanan kami!")
        else:
            st.write("Tidak ada data pelanggan untuk pembayaran.")

    # Tentang Kami OOOOOOOOOOOOOOOO5
    with Tentang_Kami:
        st.title("TentangKami")
        st.write("Aplikasi ini dibuat oleh kelompok 3, yang terdiri dari Fathan, Ipan, Siti, Shinta")

        col1, col2, col3, col4 = st.columns(4, gap="small")
        col1.image("patan.png", caption="Fathan Anwar")
        col2.image("ipan.jpg", caption="Muhammad Irfan Fadhilah")
        col3.image("siti.jpg", caption="Siti Mufathonah")
        col4.image("shinta.jpg", caption="Shinta Maulida Distiandini")


if not st.session_state.login:
    login()
else:
    main()





