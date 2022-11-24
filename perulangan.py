"""
Program perulangan membaca buku
"""
# Perulangan dengan for
"""
jumlahBuku = 10
print('Ibu berkata, "Baca semua buku"')
jumlahBukuBaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlahBukuBaca}')

for jumlahBukuBaca in range(1, jumlahBuku+1):
    print(f'buku ke {jumlahBukuBaca} sudah dibaca')

print(f'Jumlah buku yang sudah dibaca {jumlahBukuBaca}')
"""

# Perulangan dengan while
"""
jumlahBuku = 10
print('Ibu berkata, "Baca semua buku"')
jumlahBukuBaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlahBukuBaca}')

while jumlahBukuBaca < jumlahBuku:
    jumlahBukuBaca += 1
    print(f"Baca ke {jumlahBukuBaca} buku")

print(f'Jumlah buku yang sudah dibaca {jumlahBukuBaca}')
"""

# Perulangan dengan while with undefined
"""
Baca semua buku sampai faham
"""
jumlahBuku = 10
print('Ibu berkata, "Baca semua buku sampai faham"')
jumlahBacaDanPaham = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami sebanyak {jumlahBacaDanPaham}')
jumlahBaca = 0

while jumlahBaca < jumlahBuku * 2:
    jumlahBaca += 1
    if jumlahBacaDanPaham == 9:
        print(f'Buku ke {jumlahBacaDanPaham + 1} belum paham')
    else:
        jumlahBacaDanPaham += 1
        print(f'Buku ke {jumlahBacaDanPaham} sudah dibaca dan dipahami')

print(f'Jumlah buku yang sudah dibaca dan di pahami {jumlahBacaDanPaham}')

if jumlahBacaDanPaham == jumlahBaca:
    print('"Bu, semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa dipahami, Budi hanya bisa memahami {jumlahBacaDanPaham} buku"')
