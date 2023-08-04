# Metin dosyasından poligon isimlerini okuyup ve bir listeye bölüyoruz
with open('poligon_dosyası.txt', 'r') as file:
    poligon_verisi = file.read()

poligon_satırı = poligon_verisi.strip().split('\n')

# Karşılaşılan poligon isimlerini takip etmek için bir küme (set) başlatıyoruz
bulunan_noktalar = set()

# Yinelenen poligon isimlerini depolamak için bir liste oluşturuyoruz
tekrar_edilen_noktalar = []

# Yinelemeleri kontrol edip ve küme ve listeyi güncelliyoruz
for satır in poligon_satırı:
    eleman = satır.split()
    if len(eleman) > 0:
        isim = eleman[0]
        if isim in bulunan_noktalar:
            tekrar_edilen_noktalar.append(isim)
        else:
            bulunan_noktalar.add(isim)

# Yinelenen poligon isimlerini listeliyoruz
if tekrar_edilen_noktalar:
    print("Yinelenen poligon isimleri:")
    for isim in tekrar_edilen_noktalar:
        print(isim)
else:
    print("Yinelenen poligon ismi bulunamadı.")
