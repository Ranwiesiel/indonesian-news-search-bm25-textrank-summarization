# Sistem Pencarian dan Peringkasan Berita Indonesia dengan Algoritma BM25 dan TextRank

Aplikasi web untuk pencarian artikel berita Indonesia menggunakan algoritma BM25 (Best Matching 25) dengan framework Whoosh dan fitur peringkasan menggunakan TextRank dengan Cosine Similarity.

## Deskripsi

Aplikasi ini memungkinkan pengguna untuk mencari artikel berita dan mendapatkan ringkasan dari dataset Tempo ([link dataset](https://www.kaggle.com/datasets/rizkia14/berita-indo/data)) dengan menggunakan algoritma ranking BM25 dan peringkasan TextRank. Aplikasi ini melakukan preprocessing teks bahasa Indonesia yang mencakup pembersihan teks, tokenisasi, stemming, dan penghapusan stopwords.

## Fitur

- **Pencarian BM25**: Menggunakan algoritma BM25 untuk ranking dokumen berdasarkan relevansi
- **Peringkasan TextRank**: Menggunakan algoritma TextRank untuk meringkas dokumen secara
- **Preprocessing Bahasa Indonesia**: 
  - Pembersihan teks (cleaning)
  - Tokenisasi kalimat
  - Stemming menggunakan Sastrawi
  - Penghapusan stopwords bahasa Indonesia
  - Penghapusan tanda baca
- **Indexing Whoosh**: Membuat index yang dapat dicari dengan cepat
- **Interface Web**: Antarmuka web sederhana untuk pencarian

## Struktur File

```
search_bm25_app/
├── app.py                                    # Aplikasi Flask utama
├── modeling.py                               # Script untuk membuat index
├── preprocessing.py                          # Fungsi-fungsi preprocessing teks
├── schema.py                                 # Definisi schema Whoosh
├── Text_Mining_Text_SE&Sumarization.ipynb  # Jupyter notebook untuk analisis dan eksperimen
├── datasets/                                 # Folder dataset
│   ├── tempo Jun19 May20.csv                # Dataset asli dari Kaggle
│   └── tempo_with_summaries.csv             # Dataset dengan ringkasan
├── indexdir/                                # Folder index Whoosh
├── templates/                               # Template HTML
│   └── index.html
└── README.md                                # File ini
```

## Instalasi

### Prasyarat

Pastikan Python 3.7+ sudah terinstall di sistem Anda.

### Langkah Instalasi

1. Clone atau download repository ini
2. Install dependencies yang diperlukan:

```powershell
pip install whoosh pandas sastrawi nltk regex flask kagglehub jupyter
```

3. Download data NLTK yang diperlukan (akan otomatis dilakukan saat pertama kali menjalankan):
```python
import nltk
nltk.download('punkt')
```

## Penggunaan

### 1. Eksplorasi dan Analisis (Opsional)

Untuk memahami dataset dan eksperimen dengan preprocessing, Anda dapat menggunakan Jupyter notebook:

```powershell
jupyter notebook Text_Mining_Text_SE&Sumarization.ipynb
```

Notebook ini berisi:
- Analisis eksploratori data (EDA)
- Eksperimen preprocessing teks
- Demonstrasi algoritma BM25 dan TextRank
- Evaluasi hasil pencarian dan summarization

### 2. Membuat Index

Sebelum menggunakan aplikasi pencarian, Anda perlu membuat index terlebih dahulu:

```powershell
python modeling.py
```

Script ini akan:
- Memuat dataset dari `datasets/tempo_with_summaries.csv`
- Melakukan preprocessing pada teks artikel
- Membuat index Whoosh di folder `indexdir/`

### 3. Menjalankan Aplikasi Web

Setelah index dibuat, jalankan aplikasi Flask:

```powershell
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

### 4. Melakukan Pencarian

1. Buka browser dan akses `http://localhost:5000`
2. Masukkan kata kunci pencarian di form yang tersedia
3. Sistem akan menampilkan hasil pencarian berdasarkan ranking BM25 beserta ringkasan

## Dataset

Aplikasi ini menggunakan dataset artikel berita Tempo yang berisi kolom:
- `title`: Judul artikel
- `content`: Isi artikel
- `datetime`: Tanggal publikasi
- `tags`: Tag artikel
- `summary`: Ringkasan artikel

## Preprocessing

Pipeline preprocessing yang diterapkan:

1. **Pembersihan Teks**: Menghapus karakter escape, spasi berlebih, dan karakter tidak diinginkan
2. **Konversi Timestamp**: Mengubah timestamp menjadi format tanggal yang readable
3. **Segmentasi Kalimat**: Memisahkan teks menjadi kalimat-kalimat
4. **Lowercase**: Mengubah semua teks menjadi huruf kecil
5. **Penghapusan Tanda Baca**: Menghilangkan semua tanda baca
6. **Stemming**: Mengubah kata ke bentuk dasarnya menggunakan Sastrawi
7. **Penghapusan Stopwords**: Menghilangkan kata-kata umum bahasa Indonesia

## Dependencies

- **Whoosh**: Library untuk full-text search dan indexing
- **Pandas**: Untuk manipulasi data
- **Sastrawi**: Library untuk stemming dan stopword removal bahasa Indonesia
- **NLTK**: Untuk tokenisasi teks
- **Regex**: Untuk pattern matching dan text cleaning
- **Flask**: Framework web untuk interface
- **Scikit-learn**: Untuk cosine similarity dalam algoritma TextRank
- **Jupyter**: Untuk menjalankan notebook analisis (opsional)
- **KaggleHub**: Untuk download dataset (opsional)

## Catatan

- Pastikan file dataset `tempo_with_summaries.csv` tersedia di folder `datasets/`
- Index hanya perlu dibuat sekali, kecuali ada perubahan pada dataset
- Untuk dataset yang besar, proses indexing mungkin memerlukan waktu beberapa menit

## Lisensi

Aplikasi ini dibuat untuk keperluan akademik.
