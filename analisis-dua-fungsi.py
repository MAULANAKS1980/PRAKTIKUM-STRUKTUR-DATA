import time
import random


def cari_duplikat_nested(data):
    duplikat = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j] and data[i] not in duplikat:
                duplikat.append(data[i])
    return duplikat

def cari_duplikat_set(data):
    sudah_ada = set()
    duplikat = set()

    for item in data:
        if item in sudah_ada:
            duplikat.add(item)
        else:
            sudah_ada.add(item)

    return list(duplikat)

def generate_data(n):
    return [random.randint(1, n//2) for _ in range(n)]

ukuran_data = [100, 1000, 10000]

for n in ukuran_data:
    data = generate_data(n)

    # Fungsi A
    start = time.time()
    cari_duplikat_nested(data)
    waktu_a = time.time() - start

    # Fungsi B
    start = time.time()
    cari_duplikat_set(data)
    waktu_b = time.time() - start

    print(f"\nData size: {n}")
    print(f"Nested Loop: {waktu_a:.6f} detik")
    print(f"Set Method: {waktu_b:.6f} detik")