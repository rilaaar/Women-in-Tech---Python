# # class kucing sebagai "definisi"
# class Kucing:
#   nama = None
#   warna = None

# # membuat instance/variabel sebagai "objek nyata"
# kucing1 = Kucing()
# kucing1.nama = "leo"
# kucing1.warna = "hitam"

# kucing2 = Kucing()
# kucing2.nama = "kitty"
# kucing2.warna = "putih"

# print(kucing1.nama) # Output: 'leo'
# print(kucing1.warna) # Output: 'hitam'
# print(kucing2.nama) # Output: 'kitty'
# print(kucing2.warna) # Output: 'putih'


class Kucing:
  nama = None
  warna = None

  def ciri(self):
    print(f'Kucing bernama {self.nama} memiliki warna {self.warna}')

kucing1 = Kucing()
kucing1.nama = "leo"
kucing1.warna = "hitam"

kucing2 = Kucing()
kucing2.nama = "kitty"
kucing2.warna = "putih"

# panggil fungsi ciri
kucing1.ciri() # Output: Kucing bernama leo memiliki warna hitam 
kucing2.ciri() # Output: Kucing bernama kitty memiliki warna putih

print()

# --> Polymorphism
#A simple Python function to demonstrate Polymorphism
def add(a, b, c = 0):
   return a + b + c
# Driver code
print(add(2, 3))
print(add(2, 3, 4))

print()

#Polymorphism in Class Methods
class Indonesia():
   def capital(self):
     print("Jakarta is the capital of Indonesia")
   def language(self):
     print("Bahasa Indonesia the primary language of Indonesia")
class Peru():
   def capital(self):
     print("Lima is the capital of Peru")
   def language(self):
     print("Peru has many languages in use, with its official languages being Spanish, Quechua and Aymara")
obj_ina = Indonesia()
obj_peru = Peru()
for country in (obj_ina, obj_peru):
   country.capital()
   country.language()

print()


# --> Inheritance
class Hewan: # superclass (Parent)
    def bersuara(self): 
        print("Some sound")
    def aksi(self):
        print("Melakukan sesuatu")

class Anjing(Hewan): # subclass (Child) 
    def bersuara(self): # pewarisan sifat
        super().bersuara() # memanggil fungsi Parent 
    def mengejar(self):
        print("mengejar")

class Kucing(Hewan):
    def bersuara(self): # overriding
        print("Meow")
    def memanjat(self):
        print("Memanjat")

anjing = Anjing()
anjing.bersuara()
anjing.mengejar()