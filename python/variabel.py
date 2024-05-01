from datetime import date

print ("Wellcome to WIT 2024")
print ()

# Variabel 
nama = "Rila"
umur = 24
hobi = ['belajar', 'menghalu']

print (nama)
print (umur)
print (hobi)
print ()

# check data type
print (type(nama))
print (type(umur))
print (type(hobi))
print ()

# Data casting 
x = '25'
y = int(x)

print(y)
print(type(y))

int = 5
print(int)
print(type(int))

# Tipe data tanggal/date
hari_ini = date.today()
print(hari_ini)


for angka in range(1, 7):
  print("Perulangan ke:"+str(angka))