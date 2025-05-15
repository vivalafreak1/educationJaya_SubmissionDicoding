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

Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning

Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
