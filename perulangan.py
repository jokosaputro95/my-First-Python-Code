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
jumlahBuku = 10
print('Ibu berkata, "Baca semua buku"')
jumlahBukuBaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlahBukuBaca}')

while jumlahBukuBaca < jumlahBuku:
    jumlahBukuBaca += 1
    print(f"Baca ke {jumlahBukuBaca} buku")

print(f'Jumlah buku yang sudah dibaca {jumlahBukuBaca}')