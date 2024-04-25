import streamlit as st
import math


st.title('Aplikasi perhitungan Normalitas dan Persentase kadar',)


st.write('Oleh Kelompok 4')
st.write('Amanda Adistya Pasya          (2360067)')
st.write('Aufa Azhzhahra Dalillah HFB   (2360079)')
st.write('Nayla Putri Dwinta            (2360209)')
st.write('Rizky Amelia Putri            (2360247)')
st.write('Zahra Yasmin Zafira           (2360296)')

tab1, tab2, tab3, tab4, tab5,= st.tabs(["Informasi tentang Normalitas","Perhitungan Normalitas","Informasi tentang Kadar", "Perhitungan Kadar %(b/v)","Perhitungan Kadar %(b/b)",])

with tab1:
    st.title('Informasi tentang Normalitas')
    st.write('Normalitas dapat diartikan sebagai jumlah mol ekuivalen dari suatu zat per liter larutan.')
    st.write('Normalitas adalah ukuran yang menunjukkan konsentrasi pada berat setara dalam gram per liter larutan. Berat ekivalen itu sendiri adalah ukuran kapasitas reaktif molekul yang dilarutkan dalam larutan. Dalam suatu reaksi, tugas zat terlarut adalah menentukan normalitas suatu larutan. Normalitas juga disebut satuan konsentrasi larutan ekivalen.')
    st.header('Jenis-jenis Normalitas dalam Kimia', divider='rainbow')
    st.write(' normalitas sering digunakan dalam tiga jenis reaksi, yaitu reaksi asam basa, reaksi redoks, dan reaksi pengendapan. Berikut penjelasan mengenai penggunaan normalitas dalam ketiga reaksi tersebut. ')
    st.write('~ Dalam reaksi asam basa, normalitas digunakan untuk menunjukkan konsentrasi ion hidronium (H3O+) atau ion hidroksida (OH) dalam suatu larutan')
    st.write('~ Dalam reaksi reduksi oksidasi atau reaksi redoks, normalitas digunakan untuk menentukan jumlah elektron yang dapat diberikan atau diterima oleh zat pereduksi atau pengoksidasi. ')
    st.write('~ Dalam reaksi deposisi atau pengendapan, normalitas digunakan untuk mengukur jumlah ion yang dilepaskan dalam larutan oleh endapan yang terbentuk dari suatu proses pengendapan. ')
    st.header('Rumus Normalitas', divider='rainbow')
    st.write('N= bobot baku primer/BE baku primer x V titrat ')

with tab2:
    st.header('Perhitungan Normalitas')
    
    massa = st.number_input('Masukkan nilai massa (mg):')
    volume = st.number_input('Masukkan nilai volume (mL):')
    BE1 = st.number_input('Masukkan nilai BE:')
    FP1 = st.number_input('Masukkan nilai Faktor Pengali/ jika tidak ada Faktor Pengali cukup menuliskan angka 1:')

    tombol = st.button('Hitung nilai normalitasnya')

    if tombol:
        nilai_normalitas1 = massa/(BE1*volume*FP1)
        st.success(f'nilai normalitas adalah {nilai_normalitas1}')

with tab3:
    st.title('Komponen Larutan')
    st.write('Larutan adalah campuran homogen (komposisinya sama), serba sama (ukuran partikelnya), tidak ada bidang batas antara zat pelarut dengan zat terlarut (tidak dapat dibedakan secara langsung antara zat pelarut dengan zat terlarut), partikel- partikel penyusunnya berukuran sama (baik ion, atom, maupun molekul) dari dua zat atau lebih. Dalam larutan fase cair, pelarutnya (solvent) adalah cairan, dan zat yang terlarut di dalamnya disebut zat terlarut (solute), bisa berwujud padat, cair, atau gas. Dengan demikian, larutan = pelarut (solvent) + zat terlarut (solute). Khusus untuk larutan cair, maka pelarutnya adalah volume terbesar.')
    st.header('informasi tentang Kadar%(b/v)', divider='rainbow')
    st.write('Persen berat volume %(b/v) menyatakan jumlah (gram) massa zat terlarut dalam 100(mL) larutan.')
    st.write('rumus kadar%(b/v)= (Vtitran x Ntitran x BE titrat)x10^-3 x 100% / Volume titran(mL).')
    st.header('informasi tentang Kadar%(b/b)', divider='rainbow')
    st.write('Persen berat volume %(b/v) menyatakan jumlah (gram) massa zat terlarut dalam 100(gram) larutan.')
    st.write('rumus kadar%(b/v)= (Vtitran x Ntitran x BE titrat)x10^-3 x 100% / Volume titran(mg).')
    


with tab4:
    st.header('Perhitungan Kadar %(b/v)')
    st.write('Jika sampel titratnya dipipet maka menggunakan Volume titrat (mL)')

    Vtitran = st.number_input('Masukkan nilai volume titran (mL)')
    Ntitran = st.number_input('Masukkan nilai normalitas titran (N):')
    BE2 = st.number_input('Masukkan nilai BEnya:')
    FP2 = st.number_input('Masukkan nilai Faktor Pengalinya/jika tidak ada Faktor Pengali cukup menuliskan angka 1:')
    Vtitrat = st.number_input('Masukkan nilai volume titrat (mL):')

    tombol = st.button('Hitung nilai kadarnya')

    if tombol:
        nilai_kadar = (Vtitran*Ntitran*BE2*10**-3*FP2*100)/Vtitrat 
        st.success(f'Persentase kadarnya adalah {nilai_kadar}')

with tab5:
    st.header('Perhitungan Kadar %(b/b)')
    st.write('Jika sampel titratnya ditimbang maka menggunakan Volume titrat (mg)')

    a = st.number_input('Masukkan nilai volume dari titran (ml)')
    b = st.number_input('Masukkan nilai normalitas dari titran (N):')
    c = st.number_input('Masukkan nilai dari BE:')
    d = st.number_input('Masukkan nilai dari Faktor Pengalinya/ jika tidak ada Faktor Pengali cukup menuliskan angka 1:')
    e = st.number_input('Masukkan nilai dari volume titrat (mg):')

    tombol = st.button('Hitung nilai kadar')

    if tombol:
        nilai_kadar1 = (a*b*c*d*100)/e 
        st.success(f'Persentase kadarnya adalah {nilai_kadar1}')