
# Pertemuan 13 - Debugging dan Testing

Nama: Nindia Najihatuz Zahro
NIM: 2225250150
Kelas: 3E

## Kasus
Program memproses data nilai mahasiswa untuk menghitung rata-rata, menentukan status kelulusan, dan mencari nilai tertinggi.

## Test Case

| ID | Input | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|---|
| T1 | `[80, 60, 90, 70]` untuk rata-rata | 75.0 | 75.0 | PASS |
| T2 | `[100, 80]` untuk rata-rata | 90.0 | 90.0 | PASS |
| T3 | Nilai 60 untuk status | Lulus | Lulus | PASS |
| T4 | Nilai 59 untuk status | Tidak lulus | Tidak lulus | PASS |
| T5 | `[80, 60, 90, 70]` untuk nilai tertinggi | 90 | 90 | PASS |

## Retest

Setelah program diperbaiki, seluruh lima test case dijalankan kembali. Hasil pengujian menunjukkan bahwa semua test case berstatus PASS karena hasil aktual sesuai dengan hasil yang diharapkan.

Ketiga bug berhasil diperbaiki:
1. Perhitungan rata-rata menggunakan jumlah data sebenarnya.
2. Nilai 60 dinyatakan lulus dengan operator `>=`.
3. Nilai tertinggi ditentukan dengan perbandingan `>` yang benar.

## Bug Report

Bug B01: Rata-rata salah karena jumlah data selalu dibagi 5.

Bug B02: Nilai 60 dinyatakan tidak lulus karena program menggunakan operator >.

Bug B03: Nilai tertinggi salah karena kondisi perbandingan menggunakan <.

## Retest
Akan diisi setelah program diperbaiki dan seluruh test case dijalankan kembali.

## Cara Menjalankan
python praktik/praktik_4_debugging.py

## Refleksi
Debugging membantu menemukan penyebab kesalahan program. Test case digunakan untuk membandingkan hasil yang diharapkan dengan hasil aktual.
