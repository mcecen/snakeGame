# Yılan Oyunu (Snake Game)

Bu proje, **Python** ve **Pygame** kullanılarak geliştirilmiş gelişmiş bir yılan oyunudur.
Modern görsel efektler, animasyonlar ve kullanıcı dostu menü sistemi ile klasik Snake oyununa farklı bir deneyim kazandırır.

---

## Özellikler

* 3 farklı zorluk seviyesi:

  * Kolay
  * Normal
  * Zor
* Yılanın hareket yönüne göre dinamik göz animasyonu
* Parlama efektli yem (sinüs dalgası ile animasyon)
* Skora bağlı hız artışı
* Modern ve sade arayüz
* Kendine çarpma ve duvar çarpışma kontrolü
* Oyun sonu ekranı (overlay efektli)

---

## Kullanılan Teknolojiler

* Python 3
* Pygame
* Math (animasyon efektleri için)

---

## Kurulum

### 1. Python yüklü değilse:

Python'u indir:
https://www.python.org/downloads/

### 2. Gerekli kütüphaneyi yükle:

```bash
pip install pygame
```

---

## Çalıştırma

```bash
python snakeGame.py
```

---

## Kontroller

| Tuş     | İşlev              |
| ------- | ------------------ |
| ↑ ↓ ← → | Hareket            |
| W A S D | Alternatif hareket |
| ENTER   | Menü seçimi        |

---

## Oyun Mekanikleri

* Yılan yem yedikçe büyür.
* Her 3 skor artışında hız yükselir.
* Duvara veya kendine çarparsan oyun biter.
* Yılanın başı çarptığında kırmızı yanıp söner.

---

## Görsel Detaylar

* Yılanın başında yönüne göre konumlanan gözler
* Yem için sinüs fonksiyonu ile oluşturulmuş büyüyüp küçülme efekti:

  * Daha canlı bir oyun hissi sağlar
* Yumuşak geçişli menü sistemi

---