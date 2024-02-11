def harga(jumlah_gram_emas, harga_pergram, harga_pergram_sekarang):
    #mencari harga 25gram emas saat gerrard membelinya
    harga_emas_awal = jumlah_gram_emas * harga_pergram
    #mencari harga 25gram emas saat ini
    harga_emas_sekarang = jumlah_gram_emas * harga_pergram_sekarang
    #mencari keuntungan gerrard ketika menjualnya saat ini
    keuntungan = harga_emas_sekarang- harga_emas_awal
    #mengubah keuntungan ke persen
    persen = (keuntungan/harga_emas_sekarang)*100
    
    return keuntungan, persen

# keuntungan awal
keuntungan, persen = harga(25, 650000, 685000)
print("Pertama, Keuntungan: Rp.", keuntungan, ", Persen:", round(persen),"%")

# keuntungan baru
keuntungan, persen = harga(40, 685000, 715000)
print("Kedua, Keuntungan: Rp.", keuntungan, ", Persen:", round(persen),"%")