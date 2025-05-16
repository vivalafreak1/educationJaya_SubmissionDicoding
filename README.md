# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

Jumlah dropout mahasiswa adalah suatu permasalahan yang serius di institusi pendidikan. Tingkat dropout dapat dijadikan parameter kredibilitas dan kualitas institusi. Apabila kredibilitas suatu institusi rendah, maka jumlah penerimaan mahasiswa baru juga akan sedikit. Mahasiswa baru yang sedikit akan menyebabkan terjadinya ketidakseimbangan antara penempu pendidikan (mahasiswa) dengan penyelenggara pendidikan (dosen, dekan, rektor). Ketidakseimbangan akan menyebabkan keterlambatan penyampaian ilmu pendidikan kepada mahasiswa. Keterlambatan penyampaian ilmu pendidikan akan menghambat kemajuan suatu negara. Maka dari itu rumusan permasalahannya, antara lain:

- Berapa jumlah mahasiswa yang dropout?
- Apa yang menyebabkan mereka dropout?
- Apa solusi untuk mengurangi angka dropout?

### Cakupan Proyek

Proyek ini akan mencakup sebuah analisa berbentuk jupyter notebook yang berisi tentang proses analisis data dari persiapan hingga evaluasi, business dashboard menggunakan metabase yang digunakan untuk visualisasi secara interaktif yang dapat dipahami oleh semua orang, lalu model akan deploy menggunakan streamlit sebagai aplikasi web, sehingga dapat diakses di mobile maupun komputer.

### Persiapan

Sumber data:
https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

Setup environment:

- Membuat network (karena jalan di local)

```
docker network create pg-network
```

- Download postgres untuk Docker dan jalankan kontainer

```
docker run --name some-postgres --network=pg-network -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

- Mendownload image metabase di Docker

```
docker pull metabase/metabase:v0.46.4
```

- Buat Kontainer untuk metabase

```
docker run -p 3000:3000 --name metabase --network=pg-network metabase/metabase:v0.46.4
```

- Login ke metabase

```
username: arieftaufikrahman123@gmail.com
password: Admin_123
```

- Membuat python environment

```
python -m venv venv
```

- Aktifkan environment

```
venv\Scripts\activate
```

- Install dependencies

```
pip install -r requirements.txt
```

## Business Dashboard

Dashboard yang dibuat terdiri dari pie chart, bar chart, dan jumlah data aktual dengan memfokuskan pada

- Jumlah Mahasiswa
- Rata-rata usia
- Performa Akademik
- Faktor ekonomi (hutang)

## Menjalankan Sistem Machine Learning

Web aplikasi dibangun menggunakan streamlit karena memudahkan dan sederhana baik dari sisi developer maupun user. Di aplikasi tersebut, pengguna akan diminta memasukkan input agar mendapatkan hasil prediksi apakah Dropout, Enrolled, atau graduate.

Menjalankan secara Online

1. Masuk ke link berikut: https://educationjayainstitute.streamlit.app/
2. Masukan fitur pada widget inputan
3. Klik tombol Predict untuk mendapatkan hasil prediksi

## Conclusion

Analisis ini berhasil yang dibuktikan dengan pengembangan sebuah prototype sistem machine learning untuk memprediksi status mahasiswa (Dropout, Enrolled, Graduate) dengan membandingkan data `akademik dan ekonomi`. Dengan menggunakan model Random Forest dan antarmuka berbasis Streamlit, sistem ini memungkinkan pengguna untuk memasukkan data mahasiswa secara itneraktif dan mendapatkan prediksi secara langsung. Meskipun begitu, proses pengembangan menghadapi tantangan seperti kompatibilitas versi Python dan konflik dependensi seperti numpy dan seaborn, namun semua masalah telah diatasi dengan penyesuaian konfigurasi dan versi library. Implementasi di Streamlit Community Cloud dengan Python 3.10.17 menunjukkan bahwa sistem dapat dijalankan secara online, meskipun memerlukan penangan lebih untuk production environment.

### Rekomendasi Action Items

Berdasarkan dari analisis yang telah dilakukan, berikut beberapa solusi terhadap permasalahan dropout yang sedang dialami:

- `Memberikan bimbingan lebih lanjut` bagi mahasiswa yang memiliki risiko dropout lebih tinggi dengan program mentoring atau konseling akademik untuk meningkatkan retensi
- `Memberikan insentif bagi mahasiswa kurang mampu`, berikan bantuan finansial atau beasiswa kepada mahasiswa dengan status ekonomi rendah untuk mendukung kelangsungan pendidikan mereka.
