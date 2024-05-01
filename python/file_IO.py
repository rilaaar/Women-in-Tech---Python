f = open("referensi.txt")
# print(f.read()) # mencetak isi file 

# # f = open("D:\Ra\Women in Tech - Python\referensi.txt")    #blm bisa dibuka

# print(f.read(4)) # mencetak beberapa character saja 
# print(f.readline()) # read 1 line 


f = open("referensi.txt")
for x in f:
   print(x) # mencetak setiap baris yang ada di dalam file.


f.close()


# Mode akses 
# r = membaca file, error jika tidak ada 
# a = menambah data pada file 
# w = menulis file baru 
# x = membuat file baru 

