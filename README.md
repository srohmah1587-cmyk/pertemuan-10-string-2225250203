# Pertemuan 10 - String dan Pengolahan Teks

**Nama:** Siti Rohmah  
**NIM:** 2225250203  
**Kelas:** 3A

## Tujuan

Mengolah dan menormalisasi data teks menggunakan string Python, meliputi normalisasi nama mahasiswa, pembuatan inisial nama, dan normalisasi kode kelas agar data memiliki format yang konsisten dan mudah dibaca.

## Cara Menjalankan

Jalankan program melalui terminal menggunakan perintah berikut:

```bash
python3 tugas/normalisasi_data_mahasiswa.py
```

Pastikan terminal berada di direktori utama repository dan file program tersedia pada folder `tugas`.

## Algoritma

Proses normalisasi data teks dilakukan melalui langkah-langkah berikut:

1. Program meminta pengguna memasukkan nama mahasiswa dan kode kelas.
2. Nama mahasiswa dinormalisasi dengan menghapus spasi berlebih di awal dan akhir, merapikan spasi antar kata, serta mengubah huruf awal setiap kata menjadi huruf kapital.
3. Inisial nama dibuat dengan mengambil huruf pertama dari setiap kata pada nama yang sudah dinormalisasi, kemudian menggabungkannya menjadi huruf kapital.
4. Kode kelas dinormalisasi dengan menghapus spasi berlebih, mengubah semua huruf menjadi huruf kapital, dan mengganti spasi antarbagian kode dengan tanda hubung (`-`).
5. Program menampilkan nama yang sudah dinormalisasi, kode yang sudah distandarkan, dan inisial nama.

## Test Case Wajib

Pengujian dilakukan untuk memastikan program dapat menormalisasi nama, kode, dan inisial sesuai dengan hasil yang ditentukan.

| No. | Input Nama | Input Kode | Hasil Utama yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | `aan hendrayana` | `pmat a 2026` | `Aan Hendrayana \| PMAT-A-2026 \| AH` | `Aan Hendrayana \| PMAT-A-2026 \| AH` | Berhasil |
| 2 | `fATHIYYAH mUTHMAINNAH` | `kelas b` | `Fathiyyah Muthmainnah \| KELAS-B \| FM` | `Fathiyyah Muthmainnah \| KELAS-B \| FM` | Berhasil |
| 3 | `BUDI` | `pmtk 01` | `Budi \| pmtk 01 \| B` | `Budi \| PMTK-01 \| B` | Berhasil |
| 4 | `siti nur aisyah` | `kelas c` | `Siti Nur Aisyah \| KELAS-C \| SNA` | `Siti Nur Aisyah \| KELAS-C \| SNA` | Berhasil |

## Refleksi

Melalui praktikum ini, saya memahami bahwa string Python dapat digunakan untuk mengolah dan menormalisasi data teks agar lebih rapi dan konsisten. Saya mempelajari penggunaan `strip()` untuk menghapus spasi di awal dan akhir teks, `split()` dan `join()` untuk merapikan spasi antar kata, `title()` untuk mengatur kapitalisasi nama, serta `upper()` untuk mengubah kode menjadi huruf kapital.

Salah satu masalah teks yang ditemukan adalah penulisan nama dengan huruf kapital yang tidak konsisten dan adanya spasi berlebih. Masalah tersebut dapat diperbaiki menggunakan fungsi normalisasi nama. Selain itu, kode kelas yang memiliki beberapa bagian dipisahkan dengan tanda hubung agar formatnya seragam. Dengan menerapkan fungsi-fungsi tersebut, program dapat menghasilkan nama, kode, dan inisial yang lebih konsisten.
