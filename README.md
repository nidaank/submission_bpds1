# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding

### Latar Belakang

Jaya Jaya Maju merupakan perusahaan multinasional yang telah beroperasi sejak tahun 2000, dengan lebih dari 1.000 karyawan tersebar di berbagai lokasi. Perusahaan ini telah menunjukkan pertumbuhan yang signifikan dan skala operasional yang luas. Namun, seiring dengan perkembangan tersebut, muncul tantangan serius dalam pengelolaan sumber daya manusia, khususnya terkait dengan tingginya tingkat attrition atau pengunduran diri karyawan yang mencapai lebih dari 10%.

Attrition yang tinggi dapat berdampak langsung terhadap keberlangsungan operasional perusahaan, menurunkan produktivitas, serta meningkatkan biaya rekrutmen dan pelatihan karyawan baru. Oleh karena itu, pemahaman mendalam terhadap faktor-faktor yang mendorong karyawan keluar dari perusahaan menjadi sangat penting bagi strategi retensi dan pertumbuhan berkelanjutan Jaya Jaya Maju.

### Permasalahan Bisnis

Departemen HR Jaya Jaya Maju menghadapi berbagai tantangan dalam menangani attrition, di antaranya:

- Belum teridentifikasinya penyebab utama attrition: Kurangnya pemahaman mengenai faktor-faktor spesifik yang paling berpengaruh terhadap keputusan karyawan untuk keluar.
- Minimnya pemahaman terhadap pola attrition: Tidak adanya insight berbasis data mengenai pola perilaku atau karakteristik karyawan yang cenderung resign.
- Keterbatasan monitoring dan deteksi dini: Sulitnya melakukan pemantauan secara proaktif dan real-time terhadap faktor-faktor risiko.
- Kurangnya dukungan data dalam pengambilan keputusan: Keputusan HR belum sepenuhnya didukung oleh analisis data yang kuat dan komprehensif.
- Tidak adanya sistem prediktif: Belum terdapat model prediksi yang dapat mengidentifikasi karyawan dengan risiko tinggi untuk keluar sehingga intervensi dini belum bisa dilakukan secara optimal.

### Tujuan Proyek

Untuk menjawab permasalahan bisnis tersebut, proyek ini bertujuan untuk:
- Mengidentifikasi faktor-faktor kunci attrition: Melakukan analisis menyeluruh terhadap data karyawan untuk menemukan variabel-variabel yang secara signifikan berkaitan dengan attrition.
- Membangun model prediktif attrition berbasis machine learning: Mengembangkan model klasifikasi yang mampu memperkirakan kemungkinan seorang karyawan akan mengundurkan diri.
- Membangun dashboard interaktif berbasis data: Menyediakan visualisasi informatif bagi HR untuk memahami kondisi attrition secara real-time dan berbasis data.
- Memberikan insight dan rekomendasi strategis: Menyajikan temuan utama dari hasil analisis dan prediksi untuk mendukung strategi retensi karyawan.

### Cakupan Proyek

Proyek ini akan mencakup tahapan-tahapan berikut:

1. **Data Understanding**
   Mengumpulkan data karyawan yang relevan dan memahami struktur, sumber, serta potensi masalah kualitas data. Tahap ini bertujuan untuk mendapatkan pemahaman mendalam tentang konteks data yang digunakan.

2. **Data Preparation**
   Membersihkan data dari nilai hilang (*missing values*), pencilan (*outliers*), dan inkonsistensi. Melakukan transformasi data yang diperlukan, seperti encoding variabel kategorikal dan normalisasi, agar data siap untuk dianalisis dan dimodelkan.

3. **Exploratory Data Analysis (EDA)**
   Melakukan analisis deskriptif dan visualisasi data untuk mengidentifikasi pola, tren, dan hubungan antar variabel. Tujuan utama dari tahap ini adalah menemukan faktor-faktor potensial yang memengaruhi tingkat attrition.

4. **Pemodelan Machine Learning**
   Membagi dataset menjadi data pelatihan dan data pengujian. Memilih algoritma yang sesuai, melatih model dengan data pelatihan, dan melakukan tuning hyperparameter jika diperlukan untuk meningkatkan performa model.

5. **Evaluasi Model**
   Mengukur kinerja model menggunakan data pengujian dengan metrik evaluasi seperti akurasi, precision, recall, dan F1-score, guna menentukan model terbaik dalam memprediksi risiko attrition.

6. **Pengembangan Business Dashboard**
   Merancang dan membangun dashboard interaktif yang memungkinkan tim HR memantau metrik penting terkait attrition, mengeksplorasi faktor risiko utama, dan melihat hasil prediksi model secara real-time.

7. **Penyusunan Laporan dan Rekomendasi**
   Mendokumentasikan seluruh proses proyek, mulai dari analisis hingga deployment. Menyajikan temuan utama dan memberikan rekomendasi berbasis data yang dapat ditindaklanjuti oleh manajemen untuk menekan angka attrition.

### Persiapan

Sumber data: [Dataset Karyawan Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

**1. Jalankan notebook.ipynb:**

  * **Instal Dependensi:** Di terminal proyek, jalankan perintah berikut.
    ```
    pip install -r requirements.txt
    ```

  * **Jalankan Notebook:** Gunakan `jupyter notebook` atau `jupyter lab` (lokal) atau unggah ke Google Colab dan jalankan semua sel.

**2. Jalankan prediction.py:**

  * **Verifikasi Direktori Model:** Pastikan path model dan encoder di `prediction.py` sudah benar. Ubah jika perlu.
    ```
    model = joblib.load("model/rf_model.pkl")
    encoder = joblib.load("model/onehot_encoder.pkl")
    ```
  * **Instal Dependensi (jika belum):** 
    ```
    pip install pandas joblib scikit-learn
    ```
  * **Jalankan Skrip:** Di terminal proyek, jalankan 
    ```
    python prediction.py
    ```
    Hasil prediksi akan ditampilkan sebagai output.

**3. Jalankan Dashboard (Metabase dengan Docker):**

  * **Instal Docker Desktop:** Unduh dan instal dari [www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).
  * **Pindahkan Database:** Letakkan `metabase.db.mv.db` di direktori yang mudah diakses (misalnya, direktori proyek).
  * **Tarik Image:** Di terminal, jalankan 
    ```
    docker pull metabase/metabase:latest
    ```
  * **Jalankan Container (Mount Volume):** Ganti `/path/ke/direktori/anda` dengan path absolut ke direktori `metabase.db.mv.db`:
    ```
    docker run -d -p 3000:3000 --name metabase -v /path/ke/direktori/anda:/metabase-data metabase/metabase
    ```
  * **Akses Metabase:** Buka `http://localhost:3000` di browser.
  * **Login:** Email: `root@mail.com`, Password: `root123`.
  * **Hubungkan Database:** Tambahkan database H2. Path database di container: `/metabase-data/metabase.db.mv.db`. Tidak ada kredensial tambahan biasanya. Uji koneksi.

## Business Dashboard

![Dashboard 1](<needkh-dashboard 1.png>)
![Dashboard 2](<needkh-dashboard 2.png>)
![Dashboard 3](<needkh-dashboard 3.png>)

**Tujuan Utama Dashboard:**

Dashboard ini bertujuan untuk memberikan gambaran visual dan ringkas mengenai faktor-faktor yang memengaruhi *attrition* (karyawan keluar) di perusahaan Anda, serta memprediksi potensi karyawan yang akan keluar. Informasi ini sangat penting bagi departemen HR untuk mengambil tindakan pencegahan dan meningkatkan retensi karyawan.

**Komponen-Komponen Utama Dashboard:**

1.  **Metrik Tingkat Tinggi:**
    * **1,058 Total Karyawan:** Menunjukkan jumlah total karyawan saat ini dalam perusahaan, baik yang masih aktif bekerja maupun yang sudah meninggalkan perusahaan.
    * **879 Total Karyawan yang Masih Bekerja:** Jumlah karyawan yang aktif bekerja.
    * **179 Total Karyawan yang Keluar:** Jumlah karyawan yang telah meninggalkan perusahaan.
    * **Distribusi Employee berdasarkan Attrition (Pie Chart):** Memvisualisasikan proporsi karyawan yang masih bekerja (Masih Bekerja) dan yang keluar (Keluar) dari total karyawan. Ini memberikan gambaran umum tingkat attrition.
    * **188 Total Karyawan yang Berpotensi Keluar:** Hasil prediksi model Random Forest yang mengidentifikasi jumlah karyawan dengan potensi untuk keluar.
    * **10 Total Karyawan yang Berpotensi Tinggi Keluar (>0.65):** Jumlah karyawan yang memiliki probabilitas tinggi (lebih dari 65%) untuk keluar berdasarkan model prediksi. Ini adalah kelompok yang perlu mendapatkan perhatian khusus.

2.  **Faktor-Faktor Penting Penyebab Karyawan Keluar (Bar Chart):**
    * Menampilkan 10 fitur atau faktor teratas yang paling berpengaruh terhadap keputusan karyawan untuk keluar. Semakin panjang barnya, semakin penting fitur tersebut. Berdasarkan visualisasi ini, **MonthlyIncome** (Gaji Bulanan) menjadi faktor yang paling signifikan, diikuti oleh **Age** (Usia) dan **TotalWorkingYears** (Total Tahun Bekerja).

3.  **Distribusi Attrition Berdasarkan Berbagai Faktor:**
    * **Distribusi OverTime berdasarkan Attrition (Stacked Bar Chart):** Membandingkan jumlah karyawan yang masih bekerja dan keluar berdasarkan status lembur (No vs. Yes). Terlihat bahwa karyawan yang sering lembur (Yes) memiliki jumlah yang keluar lebih tinggi dibandingkan yang tidak.
    * **Distribusi Monthly Income berdasarkan Attrition (Stacked Bar Chart):** Menunjukkan distribusi gaji bulanan karyawan yang masih bekerja dan yang keluar. Terlihat pola bahwa karyawan dengan rentang gaji yang lebih rendah cenderung memiliki jumlah yang keluar lebih tinggi.
    * **Distribusi Gender berdasarkan Attrition (Stacked Bar Chart):** Membandingkan jumlah karyawan yang masih bekerja dan keluar berdasarkan jenis kelamin (Female vs. Male). Terlihat perbedaan jumlah karyawan berdasarkan gender, dan juga proporsi attrition di antara keduanya.
    * **Distribusi Years at Company berdasarkan Attrition (Stacked Bar Chart):** Menunjukkan distribusi lama bekerja karyawan (dalam tahun) yang masih bekerja dan yang keluar. Terlihat bahwa karyawan dengan masa kerja awal cenderung memiliki tingkat attrition yang lebih tinggi.
    * **Distribusi Total Working Years berdasarkan Attrition (Stacked Bar Chart):** Mirip dengan Years at Company, namun ini melihat total pengalaman kerja karyawan. Pola serupa mungkin terlihat.
    * **Distribusi Age berdasarkan Attrition (Stacked Bar Chart):** Menunjukkan distribusi usia karyawan yang masih bekerja dan yang keluar. Ini memperkuat insight dari fitur penting usia di atas.

4.  **Tabel Prediksi Karyawan yang Berpotensi Keluar:**
    * Menampilkan daftar sebagian karyawan beserta informasi relevan dan hasil prediksi model. Kolom-kolom penting di sini adalah:
        * **Attrition (Actual):** Nilai aktual apakah karyawan tersebut keluar (1) atau tidak (0) (mungkin untuk evaluasi performa model).
        * **PredictedAttrition:** Hasil prediksi model (kemungkinan 0 atau 1).
        * **Probability:** Probabilitas (kemungkinan) karyawan tersebut akan keluar berdasarkan model.
        * **MonthlyIncome, Age, TotalWorkingYears, OverTime:** Beberapa fitur penting yang digunakan model untuk prediksi.

**Insight Utama dari Dashboard:**

* **Gaji Bulanan, Usia, dan Total Pengalaman Kerja** adalah faktor-faktor yang sangat berpengaruh terhadap keputusan karyawan untuk keluar.
* **Lembur** juga berkorelasi dengan tingkat attrition yang lebih tinggi.
* Karyawan dengan **gaji lebih rendah** dan **masa kerja awal** cenderung lebih mungkin untuk keluar.
* Model prediksi telah mengidentifikasi sejumlah karyawan yang berpotensi keluar, terutama mereka dengan **probabilitas yang lebih tinggi**.

**Kesimpulan:**

Dashboard ini adalah alat yang sangat berharga bagi departemen HR untuk memahami dinamika attrition di perusahaan Anda. Dengan memantau metrik utama, mengidentifikasi faktor-faktor penting, dan memanfaatkan prediksi model, perusahaan dapat mengambil tindakan yang lebih terarah dan efektif untuk mengurangi tingkat attrition dan meningkatkan retensi karyawan, yang pada akhirnya akan berdampak positif pada stabilitas dan produktivitas perusahaan.

## Conclusion

Proyek ini bertujuan untuk mengidentifikasi faktor-faktor yang berkontribusi terhadap tingginya tingkat *attrition* karyawan di Jaya Jaya Maju dan menyediakan alat visualisasi (*business dashboard*) untuk memonitor faktor-faktor tersebut serta memprediksi potensi karyawan yang akan keluar.

Melalui analisis data eksploratif dan pemodelan *machine learning* menggunakan algoritma Random Forest, beberapa temuan signifikan berhasil diidentifikasi. Berdasarkan hasil *feature importance*, **Gaji Bulanan (MonthlyIncome)** menjadi faktor prediktif terkuat terhadap *attrition*, diikuti oleh **Usia (Age)** dan **Total Tahun Bekerja (TotalWorkingYears)**. Selain itu, status **Lembur (OverTime_Yes)** dan **lama bekerja di perusahaan (YearsAtCompany)** juga menunjukkan pengaruh yang cukup besar terhadap kemungkinan seorang karyawan meninggalkan perusahaan.

Model Random Forest yang dikembangkan menunjukkan performa yang sangat baik dalam memprediksi *attrition*, dengan **akurasi sebesar 93.41%** dan **AUC ROC sebesar 0.9943**. Hasil *classification report* juga menunjukkan nilai *precision*, *recall*, dan *f1-score* yang tinggi untuk kedua kelas (bertahan dan keluar), mengindikasikan kemampuan model dalam mengklasifikasikan karyawan dengan cukup baik.

*Business dashboard* yang telah dibuat menyajikan visualisasi yang informatif mengenai distribusi *attrition* berdasarkan berbagai faktor demografis dan terkait pekerjaan, serta menampilkan daftar karyawan yang diprediksi berpotensi keluar beserta probabilitasnya. Dashboard ini diharapkan dapat membantu departemen HR dalam memantau tren *attrition*, memahami faktor-faktor pendorongnya, dan mengambil tindakan proaktif untuk mengurangi tingkat *attrition*.

### Rekomendasi Action Items

Berdasarkan temuan dari analisis dan model prediksi, berikut adalah beberapa rekomendasi *action items* yang dapat dipertimbangkan oleh Jaya Jaya Maju:

* **Evaluasi dan Penyesuaian Kompensasi:** Mengingat gaji bulanan menjadi faktor terpenting, perusahaan perlu melakukan evaluasi menyeluruh terhadap struktur gaji dan mempertimbangkan penyesuaian yang kompetitif untuk meningkatkan retensi karyawan, terutama pada level dan departemen dengan tingkat *attrition* yang tinggi.
* **Program Engagement Karyawan Berdasarkan Usia dan Masa Kerja:** Mengembangkan program engagement yang ditargetkan untuk kelompok usia dan masa kerja tertentu yang menunjukkan tingkat *attrition* lebih tinggi. Misalnya, program pengembangan karir untuk karyawan muda atau program apresiasi untuk karyawan dengan masa kerja lebih pendek.
* **Manajemen Beban Kerja dan Kebijakan Lembur:** Meninjau kebijakan lembur dan memastikan beban kerja karyawan dapat dikelola dengan baik. Jika lembur tidak dapat dihindari, pertimbangkan kompensasi atau fleksibilitas yang lebih baik untuk karyawan yang sering melakukan lembur.
* **Intervensi Proaktif Berdasarkan Prediksi Model:** Departemen HR dapat secara proaktif menghubungi karyawan yang teridentifikasi memiliki probabilitas tinggi untuk keluar berdasarkan model prediksi. Tujuannya adalah untuk memahami kekhawatiran mereka dan menawarkan solusi atau insentif yang sesuai untuk mencegah mereka meninggalkan perusahaan.
* **Analisis Mendalam pada Faktor-faktor Penting Lainnya:** Melakukan analisis lebih lanjut terhadap faktor-faktor penting lainnya seperti *Job Involvement*, *Job Level*, dan *Business Travel* untuk memahami nuansa yang lebih dalam tentang bagaimana faktor-faktor ini berinteraksi dengan keputusan *attrition*.