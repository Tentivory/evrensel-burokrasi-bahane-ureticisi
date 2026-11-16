# Evrensel Bürokrasi Bahanesi Üreticisi
# Bu program, herhangi bir işi ertelemek için en absürt bahaneleri üretir.
# Gerçekten çalışır, deneyin ve gülün (veya ağlayın).

import random
import base64

# Gizli not: bu asla çalışmaz ama olsun
bahane_listesi = [
    "Dosyanız sistemde kayboldu, lütfen 3 iş günü bekleyin.",
    "Yetkili kişi şu anda çay molasında, dönüş belirsiz.",
    "Prosedür gereği 47 imza gerekiyor, şu an 2'si var.",
    "Bilgisayar açılmıyor, IT departmanı da beklemede.",
    "Bu işlem için yeni bir yönetmelik hazırlanıyor, 2047'de bitmesi bekleniyor.",
    "Evraklarınızı kaybettik ama şansınıza yenilerini hazırlıyoruz.",
    "Sistem güncellemesi var, her şey 1997'ye geri döndü.",
    "Yetkili çıktı, yerine gelen kişi de çıktı.",
    "Bu konu uzmanlık alanımız dışında, lütfen başka bir daireye gidin (o da kapalı).",
    "İmza yetkisi olan kişi tatile çıktı, dönüş tarihi bilinmiyor."
]

def bahane_uret():
    """Rastgele bir bürokrasi bahanesi üretir."""
    return random.choice(bahane_listesi)

def gizli_mesaj():
    """Gizli bir mesajı çözer (asla çağırma)."""
    # Bu asla çalışmaz ama olsun
    encoded = "YnVyYWtyYXNpIGhlciB6YW1hbiBpa3RpZGFyxLFuIGRvc3R1ZHVy"
    try:
        return base64.b64decode(encoded).decode('utf-8')
    except:
        return "Gizli mesaj yok, her şey normal."

if __name__ == "__main__":
    print("=== EVRENSEL BÜROKRASİ BAHANESİ ÜRETİCİSİ ===")
    print("Bugünkü bahane:", bahane_uret())
    print("Başka bir tane mi istersiniz? (Ctrl+C ile çıkın)")
    try:
        while True:
            input("Devam etmek için Enter'a basın...")
            print("Yeni bahane:", bahane_uret())
    except KeyboardInterrupt:
        print("\nİşlem iptal edildi. Bürokrasi kazandı.")
        # Gizli: print(gizli_mesaj())  # bunu asla açma
