def kembalian(bayar, harga):
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    kembalian = bayar - harga
    hasil = {}
    for uang in pecahan:
        if kembalian >= uang:
            jumlah = kembalian // uang
            hasil[str(uang)] = jumlah
            kembalian -= jumlah * uang
    return hasil

print("======= Sistem Kasir =========")
harga = int(input("\nMasukkan total belanja: "))
bayar = int(input("Masukkan nominal pembayaran: "))

if bayar < harga:
    print("Uang yang dibayarkan kurang dari total belanja.")
else:
    print("Kembalian:", kembalian(bayar, harga))