data_snr = [5, 8, 11, 14, 18, 
22, 27, 9, 16, 24, 
12, 30, 7, 20, 15, # 15 data inti sampai sini
4, 10, 13, 19, 26] # 5 data tambahan

# hitung rata-rata snr
# status snr
# hitung jumlah kategori

def rata_rata(data):
    total = 0
    for nilai in data:
        total += nilai
    return total / len(data)

def kualitas_sinyal(snr):
    if snr < 10: 
        return "RENDAH"
    elif snr < 20: 
        return "BAIK"
    else:
        return "SANGAT BAIK"

def hitung_kategori(data):
    rendah = 0
    baik = 0
    sangat_baik = 0
    for snr in data:
        status = kualitas_sinyal(snr)
        if status == "RENDAH":
            rendah += 1
        elif status == "BAIK":
            baik += 1
        else:
            sangat_baik += 1
    return rendah, baik, sangat_baik


print("----- MONITORING SNR -----")

for i in range(len(data_snr)):
    snr = data_snr[i]
    status = kualitas_sinyal(snr)
    print(i + 1, ". SNR =", snr, "dB ->", status)

rendah, baik, sangat_baik = hitung_kategori(data_snr)
rata = rata_rata(data_snr)

print()
print("=== RINGKASAN ===")
print("Total data    :", len(data_snr))
print("RENDAH        :", rendah)
print("BAIK          :", baik)
print("SANGAT BAIK   :", sangat_baik)
print("Rata-rata SNR :", round(rata, 2), "dB")
print("Maksimum SNR  :", max(data_snr), "dB")
print("Minimum SNR   :", min(data_snr), "dB")
