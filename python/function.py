x = 4 

if x > 7 : 
    print("grade A")
elif x > 5 and x <= 7 : 
    print("grade B")
else : 
    print("grade C") 


print()

sayuran = ["kangkung", "bayam", "brokoli", "kol", "sawi", "kacang panjang"]
for sayur in sayuran :
    if sayur == "kol" :
        print("ini kol")
    else : 
        print(sayur)

print()

i = 0
while i < 5:               # perulangan tidak terbatas
  print("Perulangan ke:"+str(i))
  i = i+1                 # untuk batas perulangan (nilai i ditambah 1 terus)

for i in range(0,5) :     # perulangan terbatas 
    print("Diulang ke - " +str(i))


print()

try:
    # potensi kode yang menghasilkan exception
    y = 5 / 0
except:
    # kode yang akan dieksekusi jika exception terjadi 
    print("Terjadi kesalahan!")
    pass


print()

dict_kendaraan = {
   "mobil": {
       "nama": "honda brio",
       "tahun": 2015,
       "harga": 200000000
   },
   "motor": {
       "nama": "yamaha xsr155",
       "tahun": 2020,
       "harga": 35000000
   }
}

# for kendaraan in dict_kendaraan.keys() : 
#     print(kendaraan)
#     for k in dict_kendaraan[kendaraan].values() :
#         print(k)

for k,v in dict_kendaraan.items() : 
    print(k)
    for i,j in v.items() : 
        print(i + " : " +str(j))



print()

def sapa(nama) : 
    for n in nama:
        print("Halo,", n)

name = ["Rila", "Afhrila"]
sapa(name)

sapa("Rila")


def tambah(a,b) : 
    c = a + b 
    return c

t = tambah(2, 4)
print(t)


def perkalian2(a): 
    z = a * 2 
    return z 
print(perkalian2(2))

kali2 = lambda a : a * 2        # fungsi lamda pengganti def (hanya untuk 1 ekpresi)
print(kali2(2))