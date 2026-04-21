
# Praktikum Python - Aliasing dan Memori

## 4.1 Analisis Objek
Menjelaskan fenomena aliasing pada list di Python.

## 4.2 Eksplorasi Tipe Data
Perbandingan penggunaan memori antara integer dan list.

## Hasil
- Aliasing menyebabkan dua variabel berbagi memori yang sama
- List menggunakan memori lebih besar dibanding integer


## PENJELASAN

Ya, list a ikut berubah ketika b diubah. Hal ini terjadi karena b = a tidak membuat salinan baru, tetapi hanya membuat b menunjuk ke lokasi memori yang sama dengan a.

Dalam konsep memori komputer, kedua variabel tersebut mengacu pada objek yang sama (aliasing). Oleh karena itu, perubahan pada salah satu variabel akan mempengaruhi variabel lainnya.
