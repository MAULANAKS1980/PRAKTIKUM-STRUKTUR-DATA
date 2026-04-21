def manual_delete(arr, index):
    if index < 0 or index >= len(arr):
        return "Index tidak valid"

    # Geser elemen ke kiri
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]

    # Hapus elemen terakhir (duplikat)
    arr = arr[:-1]

    return arr


# Contoh penggunaan
data = [10, 20, 30, 40, 50]
print("Sebelum:", data)

hasil = manual_delete(data, 2)
print("Sesudah:", hasil)