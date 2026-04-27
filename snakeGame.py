import pygame
import sys
import random
import time
import math  # YENİ: Parlama efekti için matematik kütüphanesi eklendi

# Pygame'i başlat
pygame.init()

# --- Oyun Ayarları ve Sabitler ---
GENISLIK, YUKSEKLIK = 800, 600
BLOK_BOYUTU = 20

# Renkler (RGB)
SIYAH = (15, 15, 15)
BEYAZ = (255, 255, 255)
YESIL = (40, 180, 99)
ACIK_YESIL = (120, 220, 150)
KIRMIZI = (220, 30, 30)
MAVI = (50, 153, 213)
SARI_VURGU = (241, 196, 15)
GOZ_RENGI = (5, 5, 5)  # YENİ: Gözler için renk
YARI_SAYDAM_SIYAH = (0, 0, 0, 180)

# Ekranı ve saati oluştur
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption('Python Yılan Oyunu')
saat = pygame.time.Clock()

# Fontlar
font_baslik = pygame.font.SysFont('impact', 70)
font_menu = pygame.font.SysFont('corbel', 40)
font_talimat = pygame.font.SysFont('calibri', 22, italic=True)
skor_font = pygame.font.SysFont('comicsansms', 35)

def skoru_goster(skor, hiz):
    skor_metni = skor_font.render(f"Skor: {skor}", True, BEYAZ)
    hiz_metni = skor_font.render(f"Hız: {hiz}", True, BEYAZ)
    ekran.blit(skor_metni, [10, 10])
    ekran.blit(hiz_metni, [GENISLIK - 150, 10])

def yilan_ciz(yilan_listesi, yon, yilan_rengi=YESIL, kafa_rengi=None):
    if not kafa_rengi:
        kafa_rengi = yilan_rengi

    for parca in yilan_listesi[:-1]:
        pygame.draw.rect(ekran, yilan_rengi, [parca[0], parca[1], BLOK_BOYUTU, BLOK_BOYUTU])

    if yilan_listesi:
        kafa = yilan_listesi[-1]
        pygame.draw.rect(ekran, kafa_rengi, [kafa[0], kafa[1], BLOK_BOYUTU, BLOK_BOYUTU])

        # YENİ: Yılanın başına göz çizme
        merkez = BLOK_BOYUTU // 2
        goz_yari_cap = 3
        sol_goz_pos, sag_goz_pos = None, None

        if yon == (BLOK_BOYUTU, 0):  # Sağa gidiyor
            sol_goz_pos = (kafa[0] + merkez, kafa[1] + merkez - goz_yari_cap * 2)
            sag_goz_pos = (kafa[0] + merkez, kafa[1] + merkez + goz_yari_cap * 2)
        elif yon == (-BLOK_BOYUTU, 0):  # Sola gidiyor
            sol_goz_pos = (kafa[0] + merkez, kafa[1] + merkez - goz_yari_cap * 2)
            sag_goz_pos = (kafa[0] + merkez, kafa[1] + merkez + goz_yari_cap * 2)
        elif yon == (0, -BLOK_BOYUTU):  # Yukarı gidiyor
            sol_goz_pos = (kafa[0] + merkez - goz_yari_cap * 2, kafa[1] + merkez)
            sag_goz_pos = (kafa[0] + merkez + goz_yari_cap * 2, kafa[1] + merkez)
        elif yon == (0, BLOK_BOYUTU):  # Aşağı gidiyor
            sol_goz_pos = (kafa[0] + merkez - goz_yari_cap * 2, kafa[1] + merkez)
            sag_goz_pos = (kafa[0] + merkez + goz_yari_cap * 2, kafa[1] + merkez)

        if sol_goz_pos and sag_goz_pos:
            pygame.draw.circle(ekran, GOZ_RENGI, sol_goz_pos, goz_yari_cap)
            pygame.draw.circle(ekran, GOZ_RENGI, sag_goz_pos, goz_yari_cap)

def metin_nesnesi(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def baslangic_ekrani():
    menu_aktif = True
    secili_opsiyon = 0
    opsiyonlar = ["Kolay", "Normal", "Zor"]
    hiz_degerleri = [10, 15, 25]
    demo_yilan = [[100, 100], [80, 100], [60, 100]]
    demo_yon = [BLOK_BOYUTU, 0]

    while menu_aktif:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    secili_opsiyon = (secili_opsiyon - 1) % len(opsiyonlar)
                elif event.key == pygame.K_DOWN:
                    secili_opsiyon = (secili_opsiyon + 1) % len(opsiyonlar)
                elif event.key == pygame.K_RETURN:
                    return hiz_degerleri[secili_opsiyon]

        yeni_bas = [demo_yilan[0][0] + demo_yon[0], demo_yilan[0][1] + demo_yon[1]]
        if yeni_bas[0] >= GENISLIK or yeni_bas[0] < 0:
            demo_yon[0] *= -1
            if random.choice([True, False]): demo_yon = [0, BLOK_BOYUTU * random.choice([-1, 1])]
        if yeni_bas[1] >= YUKSEKLIK or yeni_bas[1] < 0:
            demo_yon[1] *= -1
            if random.choice([True, False]): demo_yon = [BLOK_BOYUTU * random.choice([-1, 1]), 0]

        yeni_bas = [demo_yilan[0][0] + demo_yon[0], demo_yilan[0][1] + demo_yon[1]]
        demo_yilan.insert(0, yeni_bas)
        demo_yilan.pop()

        ekran.fill(SIYAH)
        yilan_ciz(demo_yilan, (0, 0), ACIK_YESIL)  # Demo yılanın gözü olmasına gerek yok

        baslik_surf, baslik_rect = metin_nesnesi("YILAN OYUNU", font_baslik, SARI_VURGU)
        baslik_rect.center = (GENISLIK / 2, YUKSEKLIK / 4)
        ekran.blit(baslik_surf, baslik_rect)

        for i, opsiyon_metni in enumerate(opsiyonlar):
            y_pozisyonu = YUKSEKLIK / 2 + i * 60
            renk = YESIL if i == secili_opsiyon else BEYAZ
            if i == secili_opsiyon:
                secim_isareti, _ = metin_nesnesi(">", font_menu, renk)
                ekran.blit(secim_isareti, (GENISLIK / 2 - 120, y_pozisyonu - 25))

            opsiyon_surf, opsiyon_rect = metin_nesnesi(opsiyon_metni, font_menu, renk)
            opsiyon_rect.center = (GENISLIK / 2, y_pozisyonu)
            ekran.blit(opsiyon_surf, opsiyon_rect)

        talimat_surf, talimat_rect = metin_nesnesi("Seçmek için YÖN TUŞLARI, onaylamak için ENTER", font_talimat, MAVI)
        talimat_rect.center = (GENISLIK / 2, YUKSEKLIK - 50)
        ekran.blit(talimat_surf, talimat_rect)

        pygame.display.update()
        saat.tick(15)

def oyun_dongusu(baslangic_hizi):
    oyun_bitti = False
    oyun_kapandi = False
    x1, y1 = GENISLIK / 2, YUKSEKLIK / 2
    x1_degisim, y1_degisim = 0, 0
    yilan_listesi = []
    yilan_uzunlugu = 1
    hiz = baslangic_hizi
    yem_x = round(random.randrange(0, GENISLIK - BLOK_BOYUTU) / BLOK_BOYUTU) * BLOK_BOYUTU
    yem_y = round(random.randrange(0, YUKSEKLIK - BLOK_BOYUTU) / BLOK_BOYUTU) * BLOK_BOYUTU

    while not oyun_bitti:
        while oyun_kapandi:
            overlay = pygame.Surface((GENISLIK, YUKSEKLIK), pygame.SRCALPHA)
            overlay.fill(YARI_SAYDAM_SIYAH)
            ekran.blit(overlay, (0, 0))

            game_over_surf, game_over_rect = metin_nesnesi("Oyun Bitti!", font_baslik, KIRMIZI)
            game_over_rect.center = (GENISLIK / 2, YUKSEKLIK / 4)
            ekran.blit(game_over_surf, game_over_rect)

            final_skor_surf, final_skor_rect = metin_nesnesi(f"Final Skor: {yilan_uzunlugu - 1}", font_menu, SARI_VURGU)
            final_skor_rect.center = (GENISLIK / 2, YUKSEKLIK / 2)
            ekran.blit(final_skor_surf, final_skor_rect)

            restart_surf, restart_rect = metin_nesnesi("Ana Menüye Dönmek İçin Bir Tuşa Basın", font_talimat, BEYAZ)
            restart_rect.center = (GENISLIK / 2, YUKSEKLIK * 0.75)
            ekran.blit(restart_surf, restart_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    return

        yon = (x1_degisim, y1_degisim)  # YENİ: Gözler için yönü sakla

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyun_bitti = True
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a) and x1_degisim == 0:
                    x1_degisim, y1_degisim = -BLOK_BOYUTU, 0
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and x1_degisim == 0:
                    x1_degisim, y1_degisim = BLOK_BOYUTU, 0
                elif event.key in (pygame.K_UP, pygame.K_w) and y1_degisim == 0:
                    x1_degisim, y1_degisim = 0, -BLOK_BOYUTU
                elif event.key in (pygame.K_DOWN, pygame.K_s) and y1_degisim == 0:
                    x1_degisim, y1_degisim = 0, BLOK_BOYUTU

        x1 += x1_degisim
        y1 += y1_degisim

        if x1 >= GENISLIK or x1 < 0 or y1 >= YUKSEKLIK or y1 < 0 or [x1, y1] in yilan_listesi[:-1]:
            oyun_kapandi = True
            pygame.time.wait(500)

        ekran.fill(SIYAH)

        # YENİ: Yemi daire olarak çiz ve parlama efekti ekle
        parlama_degeri = abs(math.sin(pygame.time.get_ticks() * 0.005))  # 0 ile 1 arasında yumuşak salınım
        yem_yari_cap = int((BLOK_BOYUTU // 2 - 3) + parlama_degeri * 5)  # Yarıçapı 2-7 arasında değiştir
        yem_merkez = (yem_x + BLOK_BOYUTU // 2, yem_y + BLOK_BOYUTU // 2)
        pygame.draw.circle(ekran, KIRMIZI, yem_merkez, yem_yari_cap)

        yilan_basi = [x1, y1]
        yilan_listesi.append(yilan_basi)
        if len(yilan_listesi) > yilan_uzunlugu:
            del yilan_listesi[0]

        kafa_rengi = YESIL
        if oyun_kapandi:
            if int(time.time() * 2) % 2 == 0:
                kafa_rengi = KIRMIZI
        yilan_ciz(yilan_listesi, yon, YESIL, kafa_rengi)

        skoru_goster(yilan_uzunlugu - 1, hiz)
        pygame.display.update()

        if x1 == yem_x and y1 == yem_y:
            yem_x = round(random.randrange(0, GENISLIK - BLOK_BOYUTU) / BLOK_BOYUTU) * BLOK_BOYUTU
            yem_y = round(random.randrange(0, YUKSEKLIK - BLOK_BOYUTU) / BLOK_BOYUTU) * BLOK_BOYUTU
            yilan_uzunlugu += 1
            if (yilan_uzunlugu - 1) % 3 == 0 and yilan_uzunlugu > 1:
                hiz += 1

        saat.tick(hiz)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    while True:
        secilen_hiz = baslangic_ekrani()
        oyun_dongusu(secilen_hiz)