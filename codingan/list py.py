# Akses list
## Menampilkan elemen ke-3
Makanan = ['Bakso', 'Mie Ayam', 'Seblak', 'Nasi goreng', 'Pecel Lele']
print()
print("Makanan :", Makanan)
print()
print('Elemen ke-3', Makanan[2])
print()

## Ambil nilai elemen ke-2 sampai ke-4
print('Elemen ke-2 sampai ke-4', Makanan[1:5])
print()

## Ambil elemen terakhir
print ('Elemen terakhir', Makanan[-1])
print()



# Ubah elemen list
## Ubah elemen ke-4 dengan nilai lainnya
Mobil = ['Avanza', 'Terios', 'Rush', 'Ferrari', 'Kijang']
print()
print("Mobil sebelum di ubah:", Mobil)
print()
Mobil[3] = 'Xenia'
print("Mobil sesudah di ubah:", Mobil)
print()

## Ubah elemen ke-4 sampai dengan elemen terakhir
Mobil[3:] = ["Agya", "Ayla"]
print("ubah elemen ke-4 hingga akhir :", Mobil)
print()



# Tambah elemen list
## Ambil 2 bagian dari list pertama (A) dan jadikan list kedua (B)
a = [20, 21, 22, 23, 24]
b = [30, 31, 32, 33, 34]

b.append(a[0:2])
print(b)

## Tambah list B dengan nilai string
print()
b.append("59")
print(b)

## Tambah list B dengan 3 nilai
print()
print(b + [40, 41, 42])

## Gabungkan list B dengan list A
print()
print(a + b)
