print('-----------------------------------------')
print('Nama     : Aliyah Azzah Sekedang         ')
print('Program  : Mini Projek Dasar Pemograman 1')
print('NIM      : 2409116021                    ')
print('Kelas    : A                             ')
print('-----------------------------------------')

#Menampilkan nama lengkap dan password
nama_lengkap = "Aliyah Azzah"
password = 12345

#Login
anama_lengkap = str(input("\nMasukkan Nama Lengkap: "))
bpassword = int(input("Masukkan Password: "))

while True:
    if anama_lengkap == nama_lengkap and bpassword == password:
        print("\n ໒꒱ ‧₊˚ Selamat datang, Aliyah Azzah! ˚₊‧ ꒰ა")
        break
    else:
        print("Password salah, silahkan login kembali")
        anama_lengkap = input("\nMasukkan Nama Lengkap: ")
        bpassword = int(input("Masukkan Password: "))

#Menghitung gaji karyawan 
while True:
    jam_kerja = float(input("\nMasukkan jumlah jam kerja: "))
    tarif_kerja = float(input("Masukkan tarif kerja per jam: "))

    gaji = jam_kerja * tarif_kerja

    if jam_kerja > 160:
        bonus = 0.1 * gaji
        jumlah_gaji = gaji + bonus
        print("Anda mendapatkan bonus. Jumlah gaji anda " + str(jumlah_gaji))
    else:
        print("Nominal gaji anda = " + str(jumlah_gaji))

    option = input("\nApakah anda ingin menghitung ulang gaji anda? \n(Iya/Tidak): ").lower()
    if option == "tidak":
        print("Terima Kasih, selamat bekerja kembali!")
        break
    else:
        continue




