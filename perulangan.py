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
jumlahBukuBaca_dan_yangSudahdipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami sebanyak {jumlahBukuBaca_dan_yangSudahdipahami}')
totalJumlahBaca = 0

while totalJumlahBaca < jumlahBuku * 2:
    totalJumlahBaca += 1
    if jumlahBukuBaca_dan_yangSudahdipahami == 9:
        print(f'Buku ke {jumlahBukuBaca_dan_yangSudahdipahami + 1} belum paham')
    else:
        jumlahBukuBaca_dan_yangSudahdipahami += 1
        print(f'Buku ke {jumlahBukuBaca_dan_yangSudahdipahami} sudah dibaca dan dipahami')

print(f'Jumlah buku yang sudah dibaca dan di pahami {jumlahBukuBaca_dan_yangSudahdipahami}')

if jumlahBukuBaca_dan_yangSudahdipahami == totalJumlahBaca:
    print('"Bu, semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa dipahami, Budi hanya bisa memahami {jumlahBukuBaca_dan_yangSudahdipahami} buku"')
