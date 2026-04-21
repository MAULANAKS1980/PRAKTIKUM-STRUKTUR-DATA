
# Praktikum 1 Python - Aliasing dan Memori

## 4.1 Analisis Objek
Menjelaskan fenomena aliasing pada list di Python.

## 4.2 Eksplorasi Tipe Data
Perbandingan penggunaan memori antara integer dan list.

## Hasil
- Aliasing menyebabkan dua variabel berbagi memori yang sama
- List menggunakan memori lebih besar dibanding integer

# PRAKTIKUM 2 PYTHON

## PENJELASAN

Ya, list a ikut berubah ketika b diubah. Hal ini terjadi karena b = a tidak membuat salinan baru, tetapi hanya membuat b menunjuk ke lokasi memori yang sama dengan a.

Dalam konsep memori komputer, kedua variabel tersebut mengacu pada objek yang sama (aliasing). Oleh karena itu, perubahan pada salah satu variabel akan mempengaruhi variabel lainnya.


| Jumlah Data | Nested Loop (O(n²)) | Set (O(n)) |
|------------|-------------------|-----------|
| 100        | 0.001 detik       | 0.0001 detik |
| 1.000      | 0.05 detik        | 0.0005 detik |
| 10.000     | 5 detik           | 0.002 detik |




Fungsi B (menggunakan set) jauh lebih cepat dibandingkan fungsi A (nested loop), terutama ketika jumlah data semakin besar.

Hal ini terjadi karena:
- Fungsi A memiliki kompleksitas O(n²), sehingga waktu eksekusi meningkat sangat cepat seiring bertambahnya data.
- Fungsi B hanya O(n), karena pengecekan pada set dilakukan dalam waktu konstan (O(1)).

Kesimpulan:
Untuk data besar, penggunaan set jauh lebih efisien dibandingkan nested loop.


## Praktikum 3 Python - Manual Delete & String Reverse

## Manual Delete
Menghapus elemen list tanpa menggunakan fungsi bawaan.

## String Reverse
Membalik string tanpa slicing atau reverse().

## Analisis Kompleksitas
- Hapus awal: O(n)
- Hapus akhir: O(1)

## Kesimpulan
Operasi pada list lebih mahal jika melibatkan pergeseran elemen.