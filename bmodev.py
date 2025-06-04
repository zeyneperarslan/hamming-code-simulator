import tkinter as tk
from tkinter import messagebox

def veri_giris(data, bit_uzunlugu):
    return len(data) == bit_uzunlugu and all(bit in '01' for bit in data)

def hammingkodhesapla(data, bit_uzunlugu):
    if len(data) != bit_uzunlugu or not all(bit in '01' for bit in data):     # Veri doğruluğunu kontrol edildi.
        raise ValueError("Hatalı giriş!!! Lütfen uygun bir veri girin.")

   
    parity_bit_sayisi = 0
    while 2 ** parity_bit_sayisi - 1 < bit_uzunlugu + parity_bit_sayisi:    # Parite bit sayısını hesaplandı.
        parity_bit_sayisi += 1

  
    hamming_kod_uzunlugu = bit_uzunlugu + parity_bit_sayisi                 # Hamming kodunu hesaplandı.
    hamming_kod = ['0'] * hamming_kod_uzunlugu
    data_indeks = 0

    
    for i in range(1, hamming_kod_uzunlugu + 1):
        if i & (i - 1) == 0:                               # Parite bitleri için yer açıldı.
            continue
        else:
            hamming_kod[i - 1] = data[data_indeks]        # Veriyi ve parite bitlerini yerleştirildi.
            data_indeks += 1

    
    for i in range(parity_bit_sayisi):
        pozisyon = 2 ** i
        deger = 0
        for j in range(1, hamming_kod_uzunlugu + 1):
            if j & pozisyon:
                deger ^= int(hamming_kod[j - 1])            # xor işlemi yapıldı.
        hamming_kod[pozisyon - 1] = str(deger)              # Parite bitleri hesaplandı ve yerleştirildi.

    return ''.join(hamming_kod)

def hata_ekleme(hamming_kod, hatali_indeks):
    if hatali_indeks >= len(hamming_kod):
        return hamming_kod

    degisen_bit = '0' if hamming_kod[hatali_indeks] == '1' else '1'                      #biti 0sa 1 1se 0 olarak değiştirildi.
    return hamming_kod[:hatali_indeks] + degisen_bit + hamming_kod[hatali_indeks + 1:]   #yeni hamming kod yazdırıldı.

def hata_tespit(hamming_kod):
    sendrom = 0
    for i, bit in enumerate(hamming_kod, start=1):
        if bit == '1':
            sendrom ^= i
    return sendrom

def hata_duzeltme(hamming_kod, sendrom):
    if sendrom == 0:                         #sendrom 0'a eşitse kod hatalı değilidir ve aynı kodu döndürür.
        return hamming_kod

    hatali_indeks = sendrom - 1
    degisen_bit = '0' if hamming_kod[hatali_indeks] == '1' else '1'                      #biti 0sa 1 1se 0 olarak değiştirildi.
    return hamming_kod[:hatali_indeks] + degisen_bit + hamming_kod[hatali_indeks + 1:]   #yeni hamming kod yazdırıldı.

def on_hesaplama_button():
    data =data_entry.get()
    bit_uzunlugu = int(bit_uzunlugu_entry.get())
    sonuc = hammingkodhesapla(data, bit_uzunlugu)
    if sonuc:
        hamming_kod_label.config(text=f"Hamming Kodu: {sonuc}")

def on_hata_ekleme_button():
    hatali_indeks = int(hatali_indeks_entry.get())
    if hatali_indeks < 0 or hatali_indeks >= len(hamming_kod_label.cget("text")):
        messagebox.showerror("Hata", "Geçersiz hata indeksi.")
        return

    hata = hata_ekleme(hamming_kod_label.cget("text").split(": ")[1], hatali_indeks)
    hamming_kod_label.config(text=f"Yeni Hamming Kodu: {hata}")

def on_hata_tespit_button():
    sendrom = hata_tespit(hamming_kod_label.cget("text").split(": ")[1])
    if sendrom!= 0:
        dogrukod = hata_duzeltme(hamming_kod_label.cget("text").split(": ")[1], sendrom)
        hamming_kod_label.config(text=f" -> Hata Tespit Edildi!! \n Sendrom: {sendrom} \n Düzeltilmiş Hamming Kodu: {dogrukod}")
    else:
        hamming_kod_label.config(text=f"Hamming Kodu: {hamming_kod_label.cget('text').split(': ')[1]}\nHata Tespit Edilemedi.")


root = tk.Tk()                                    # Tkinter arayüzü oluşturuldu.
root.title("Hamming Kodu Simülasyonu")


data_label = tk.Label(root, text="Veri:")           #Girişler oluşturuldu.
data_label.grid(row=0, column=0, padx=5, pady=5)
data_entry = tk.Entry(root)
data_entry.grid(row=0, column=1, padx=5, pady=5)

bit_uzunlugu_label = tk.Label(root, text="Bit Uzunluğu (4 / 8 / 16):")
bit_uzunlugu_label.grid(row=1, column=0, padx=5, pady=5)
bit_uzunlugu_entry = tk.Entry(root)
bit_uzunlugu_entry.grid(row=1, column=1, padx=5, pady=5)

hesaplama_button = tk.Button(root, text="Hamming Kodu Hesapla", command=on_hesaplama_button)
hesaplama_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5) 

hamming_kod_label = tk.Label(root, text="")
hamming_kod_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

hatali_indeks_label = tk.Label(root, text="Hatalı Bit İndeksi:")
hatali_indeks_label.grid(row=4, column=0, padx=5, pady=5)
hatali_indeks_entry = tk.Entry(root)
hatali_indeks_entry.grid(row=4, column=1, padx=5, pady=5)

hata_ekleme_button = tk.Button(root, text="Hata Oluştur", command=on_hata_ekleme_button)
hata_ekleme_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

hata_tespit_button = tk.Button(root, text="Hata Tespit Et ve Düzelt", command=on_hata_tespit_button)
hata_tespit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()