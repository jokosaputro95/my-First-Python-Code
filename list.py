bookList = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
print('Tampil variable bookList')
print(bookList)

print('\nProses semua dengan for in')
for newBook in bookList:
    print(newBook)

print('\nTampilkan isi bookList pada indeks tertentu')
print(bookList[0])
print(bookList[2])

print('\nProses semua dengan for in range')
for i in range(0, len(bookList)):
    print(bookList[i])

print('\nProses semua dengan for in range, dimana tipe data tiap elemen berbeda2')
bookList = [1, 'One Piece', -505, 3.14]
for i in range(0, len(bookList)):
    print(bookList[i])

print('\nKembalikan nilai awal booklist')
bookList = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
print('Tambahkan 1 buku baru')
bookList.append('Dunia Biologi')
for i in range(0, len(bookList)):
    print(bookList[i])

print('\nClear list')
bookList.clear()

print('\nMerubah/Mengganti nilai booklist')
print('Ganti element ke-2')
bookList = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
bookList[2] = 'Python for Beginner'
x = bookList.pop(1)
y = bookList.pop(-1)
for i in range(0, len(bookList)):
    print(bookList[i])

print('\nHasil pop')
print(x)
print(y)

print('\nPerintah Delete')
bookList = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del bookList[0]
for i in range(0, len(bookList)):
    print(bookList[i])

print('\nPerintah Delete dengan list comprehension')
bookList = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del bookList[:2]
print(bookList)
bookList = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del bookList[:-1]
print(bookList)
bookList = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del bookList[0::2]
print(bookList)
bookList = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del bookList[:]
print(bookList)
for i in range(0, len(bookList)):
    print(bookList[i])

print('\nMembuat List baru dengan copy list')
bookList = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
newBookList = bookList.copy()
for i in range(0, len(newBookList)):
    print(newBookList[i])

print('\nMembuat List baru comprehension: ganjil')
bookList = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
newBookList = bookList[0::2]
for i in range(0, len(newBookList)):
    print(newBookList[i])

print('\nMembuat List baru comprehension: genap')
bookList = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
newBookList = bookList[1::2] #start stop end
for i in range(0, len(newBookList)):
    print(newBookList[i])

print('\nMembuat List baru comprehension: buang paling akhir')
bookList = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
newBookList = bookList[0:-1] #start stop end
for i in range(0, len(newBookList)):
    print(newBookList[i])

print('\nMembuat List baru comprehension: buang paling akhir lompat 2')
bookList = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
newBookList = bookList[0:-1:2] #start stop end
for i in range(0, len(newBookList)):
    print(newBookList[i])
