class BangunDatar():
  def Luas(self):
    print("Menghitung Luas bangun datar")

  def Keliling(self):
    print("Menghitung Keliling bangun datar")

class Persegi(BangunDatar):
  def _init_(self, sisi=0):
    self.sisi = sisi

  def Luas(self):
    print("Luas Bangun Datar Persegi: ", self.sisi * self.sisi)

  def Keliling(self):
    print("Keliling Bangun Datar Persegi: ", 4 * self.sisi)

class Lingkaran(BangunDatar):
  
  def _init_(self, r=0):
    self.r = r

  def Luas(self):
    print("Luas Bangun Datar Lingkaran: ", 3.14 * self.r ** 2)

  def Keliling(self): 
    print("Keliling Bangun Datar Lingkaran: ", 2 * 3.14 * self.r)

class PersegiPanjang(BangunDatar):
  def _init_(self, panjang=0, lebar=0):
    self.panjang = panjang
    self.lebar = lebar

  def Luas(self):
    print("Luas Bangun Datar Persegi Panjang: ", self.panjang * self.lebar)

  def Keliling(self):
    print("Keliling Bangun Datar Persegi Panjang: ", 2 * self.panjang + 2 * self.lebar)

class Segitiga(BangunDatar):
  def _init_(self, alas=0, tinggi=0):
    self.alas = alas
    self.tinggi = tinggi

  def Luas(self):
    print("Luas Bangun Datar Segitiga: ", 1/2 * self.alas * self.tinggi)

class Main():
  
  def menu(): 
    print("\n\nMenu Program Overridding")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Persegi Panjang")
    print("4. Segitiga")
    print("5. Keluar Program")

  menu()
  pilihan = int(input("\nPilih Menu:(Tulis Angka)"))

  while pilihan != 5:
    if pilihan == 1:
     persegi = Persegi()
     print("Menghitung Luas dan Keliling Bangun Datar Persegi")
     persegi.sisi = int(input("Masukkan Sisi Persegi : ")) 
     persegi.Luas()
     persegi.Keliling()
    
    elif pilihan == 2:
     lingkaran = Lingkaran()
     print("Menghitung Luas dan Keliling Bangun Datar Lingkaran")
     lingkaran.r = int(input("Masukkan Jari-jari Lingkaran : "))
     lingkaran.Luas()
     lingkaran.Keliling()

    elif pilihan == 3:
     persegiPanjang = PersegiPanjang()
     print("Menghitung Luas dan Keliling Bangun Datar Persegi Panjang")
     persegiPanjang.panjang = int(input("Masukkan Panjang Persegi Panjang : "))
     persegiPanjang.lebar = int(input("Masukkan Lebar Persegi Panjang : "))
     persegiPanjang.Luas()
     persegiPanjang.Keliling()

    
    elif pilihan == 4:
     segitiga = Segitiga()
     print("Menghitung Luas Bangun Datar Segitiga")
     segitiga.alas = int(input("Masukkan Alas Segitiga : "))
     segitiga.tinggi = int(input("Masukkan Tinggi Segitiga : "))
     segitiga.Luas()

    else:
      print("Menu tidak tersedia")

    menu()
    pilihan = int(input("\nPilih Menu:(Tulis Angka) "))

  print("Terima Kasih!")