def reverse_string_manual(kalimat):
    hasil = ""
    
    for i in range(len(kalimat) - 1, -1, -1):
        hasil += kalimat[i]
    
    return hasil


# Contoh
teks = "Halo Dunia"
print("Asli:", teks)
print("Balik:", reverse_string_manual(teks))