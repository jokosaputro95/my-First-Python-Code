"""'''
Ini adalah demo project pertama saya dengan python
'''"""
print("Hello world")
print("My name is Joko Saputro")

# Sekuensial
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan ditoko?"')
print('Ibu menjawab. "Beli satu botol susu, jika ada telur beli 6 butir"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlahBotolSusu = 120
jumlahTelur = 1200

print(f'Jumlah botol susu {jumlahBotolSusu} botol')
print(f'Jumlah telur {jumlahTelur} butuir')

if jumlahBotolSusu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlahTelur != 0:
        print("Budi membeli 1 botol susu, dan 6 butir telur")
else:
    print("Budi tidak jadi membeli 1 botol susu, dan 6 butir telur")

print("Budi pulang kerumah")
print("Menyampaikan hasilnya kepada ibu")