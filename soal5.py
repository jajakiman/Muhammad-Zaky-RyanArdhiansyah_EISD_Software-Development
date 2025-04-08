def kombinasi(nama):
    nama = nama.replace(" ", "").lower()
    cek_kombinasi = {nama[i:i+r] for r in range(1, 7) for i in range(len(nama) - r + 1)}
    return len(cek_kombinasi)

print("========= Cek kombinasi username ===========")
nama = input("Masukkan username: ")
kombinasi_unik = kombinasi(nama)

print(f"Total kemungkinan username unik: {kombinasi_unik}")
