barang = [
    {
        "nama": "gelang",
        "jumlah": 7,
        "harga": 20000
    },
    {
        "nama": "cincin",
        "jumlah": 2,
        "harga": 200000
    },
]

def hitung_total(barang):           # cara 1 pakai def 
    total_harga = 0

    for type in barang:
        total_harga += type["jumlah"] * type["harga"]

    return total_harga 
    

hitung_total2 = lambda barang : sum ([type["harga"] * type["jumlah"] for type in barang])        # cara 2 pakai lamda

print(hitung_total(barang))
print(hitung_total2(barang))