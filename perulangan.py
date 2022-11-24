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
bookCount = 10
print('Ibu berkata, "Baca semua buku sampai faham"')
understoodCount = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami sebanyak {understoodCount}')
readCount = 0

while readCount < bookCount * 2:
    readCount += 1
    if understoodCount == 9:
        print(f'Buku ke {understoodCount + 1} belum paham')
    else:
        understoodCount += 1
        print(f'Buku ke {understoodCount} sudah dibaca dan dipahami')

print(f'Jumlah buku yang sudah dibaca dan di pahami {understoodCount}')

if understoodCount == readCount:
    print('"Bu, semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa dipahami, Budi hanya bisa memahami {understoodCount} buku"')
