# Tekrarlanan Poligon Noktalarını Bulmak

#### Python ile:

```py
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
```

### Görüntü

![image](https://github.com/Neodevils/koordinatlar/assets/71941576/352cc33a-ac05-4dc8-96a4-e07c3ae3e481)

<hr>

#### JavaScript ile:

```js
// Verileri al fonksiyonunu tanımlıyoruz
const verileriAl = async () => {
    try {
        // "poligon.txt" dosyasını alıyoruz
        const cevap = await fetch("poligon.txt");
        // Dosya içeriğini metin olarak alıyoruz
        const veri = await cevap.text();

        // Metni satırlara bölüp, arada ki boşlukları temizliyoruz
        const poligonSatirlari = veri.trim().split("\n");
        // Bulunan isimleri takip etmek için bir küme oluşturuyoruz
        const bulunanIsimler = new Set();
        // Tekrar eden isimleri saklamak için bir dizi oluşturuyoruz
        const tekrarEdenIsimler = [];

        // Her satıra bakıyoruz
        for (const satir of poligonSatirlari) {
            // Satırı boşluklara göre bölüyoruz
            const elemanlar = satir.split(/\s+/);
            if (elemanlar.length > 0) {
                const isim = elemanlar[0];
                // Eğer isim zaten bulunuyorsa tekrarEdenIsimler dizisine ekle, değilse bulunanIsimler kümesine ekliyoruz
                if (bulunanIsimler.has(isim)) {
                    tekrarEdenIsimler.push(isim);
                } else {
                    bulunanIsimler.add(isim);
                }
            }
        }

        // Tekrar eden isimler varsa yazdır, yoksa mesaj verdirtiyoruz
        if (tekrarEdenIsimler.length > 0) {
            console.log("Tekrar eden poligon isimleri:");
            for (const isim of tekrarEdenIsimler) {
                console.log(isim);
            }
        } else {
            console.log("Tekrar eden poligon ismi bulunamadı.");
        }
    } catch (hata) {
        // Hata durumunda hatayı konsola yazdırıyoruz
        console.error(hata);
    }
};

// Verileri al fonksiyonunu çağırıyoruz
verileriAl();
```

![image](https://github.com/Neodevils/koordinatlar/assets/71941576/5da6e804-142f-4f73-bca6-aa813511e944)


# Poligon Noktalarını Sıralamak

Bu işlem iki dosya gerektiriyor.

### HTML
```html
<!DOCTYPE html>
<html lang="tr">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Belge</title>
    </head>
    <body>
        <!-- Dosya seçebilmesi için dosya giriş alanı -->
        <input type="file" id="fileInput" />

        <!-- Dosyayı sıralamak için kullanılacak düğme -->
        <button type="button" onclick="dosyayiSirala()">Dosyayı Sırala</button>
        <br />

        <script src="sort_content.js" defer></script>
        <script src="checking_duplicated.js" defer></script>
    </body>
</html>
```

### JavaScript

```js
// Dosyayı sıralamak için kullanılan JavaScript fonksiyonu
function dosyayiSirala() {
    // HTML sayfasındaki "dosyaGirdisi" öğesini al
    const dosyaGirdisi = document.getElementById("dosyaGirdisi");

    // Kullanıcının seçtiği dosyayı al
    const dosya = dosyaGirdisi.files[0];

    // Eğer bir dosya seçildiyse devam et
    if (dosya) {
        // Dosyayı okumak için bir FileReader oluştur
        const okuyucu = new FileReader();

        // Dosya okuma işlemi tamamlandığında yapılacak işlem
        okuyucu.onload = (e) => {
            // Dosya içeriğini al
            const dosyaIcerigi = e.target.result;

            // Dosyadaki satırları ayır
            const satirlar = dosyaIcerigi.split("\n");

            // Satırları sırala
            satirlar.sort();

            // Sıralanmış satırları tekrar birleştir
            const siralanmisIcerik = satirlar.join("\n");

            // Sıralanmış içeriği konsola yazdır
            console.log(siralanmisIcerik);
        };

        // Dosyayı metin olarak oku
        okuyucu.readAsText(dosya);
    }
}
```




