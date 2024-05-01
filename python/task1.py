# barang = [
#     {
#         "nama": "gelang",
#         "diskon": 23/100 * 123000,
#         "harga": 123000
#     },
# ]

# def hitung_total(barang):           # cara 1 pakai def 
#     total_harga = 0

#     for type in barang: 
#         total_harga = type["harga"] - type["diskon"]

#     return total_harga 

# print(hitung_total(barang))


# hargaasli = float(input('Masukan harga asli: '))
# persendiskon = float(input('Masukan persentase diskon (%): '))

# diskon = hargaasli * (persendiskon/100)
# setelahdiskon = hargaasli - diskon

# print("Diskon: Rp {:,}".format(float(diskon)))
# print("Harga setelah diskon: Rp {:,}".format(float(setelahdiskon)))



harga_asli = int (123000)
diskon = float (23/100)
harga_diskon = int (harga_asli * diskon)
total_harga = int (harga_asli - harga_diskon) 

print("Harga asli = Rp." + str(harga_asli) +",-")
print("Diskon = " + str(int(diskon * 100)) +"%")
print("Harga barang setelah didiskon = Rp." + str(total_harga) +",-")

