import numpy as np

def erika(uang_sekarang, bunga_pertahun,target_minimal):
    # rumus mencari waktu : waktu= log(target_minimal/uang_sekarang) / log(1+bunga)
    
    persenan_bunga = bunga_pertahun/100 # mengubah 10 menjadi 0.10 agar menjadi 10%
    waktu = np.log(target_minimal/uang_sekarang) / np.log(1+persenan_bunga) #kalkulasi waktu menggunakan rumus
    return waktu
        

print ("jawaban: ","%.2f" % erika(200,10,400),"Tahun")