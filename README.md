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