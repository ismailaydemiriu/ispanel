# ispanel - SSH tabanlı mini panel (Ubuntu 22+)

## Kurulum (Ubuntu 22+)

1) Python scripti kopyalayın ve çalıştırılabilir yapın

```bash
sudo chmod +x ispanel
```

2) Kurulum sihirbazını çalıştırın (OpenLiteSpeed + PHP 8.2 + MariaDB):

```bash
sudo python3 ispanel install
```

Kurulum sonunda `/usr/local/bin/ispanel` komutu oluşturulur.

## Menülü kullanım

```bash
sudo ispanel
```

## Komutlar

- **Kurulum:** `sudo python3 ispanel install`
- **Domain ekle:** `sudo python3 ispanel domain-add example.com`
- **Domain sil:** `sudo python3 ispanel domain-rm example.com`
- **DB oluştur:** `sudo python3 ispanel db-create dbname dbuser strongpass`
- **DB sil:** `sudo python3 ispanel db-delete dbname dbuser`

## Menü Seçenekleri

```
=== ispanel (Ubuntu 22+) ===
1) Kurulum (OpenLiteSpeed + PHP 8.2 + MariaDB)
2) Domain ekle
3) Domain sil
4) DB oluştur
5) DB sil
6) MySQL root şifre sıfırla
7) OpenLiteSpeed admin şifre sıfırla
8) Port kontrolü ve Firewall yönetimi
9) SSL/HTTPS desteği kur
10) MariaDB güvenlik ayarları
11) OpenLiteSpeed performans optimizasyonu
12) Domain yedeği al
13) Veritabanı yedeği al
14) Domain yedeği geri yükle
15) Veritabanı yedeği geri yükle
16) Yedekleri listele
0) Çıkış
```

## Notlar

- **Domain docroot:** `/var/www/<domain>/public_html`
- **OpenLiteSpeed listener** `Default` içine `map <domain>:80 <domain>` satırı eklenir.
- **MariaDB root parolası** yok varsayılmıştır; farklı ise `mysql -uroot -p` ile erişim gerektirir.
- **OpenLiteSpeed admin panel:** `https://SERVER_IP:7080` (kullanıcı: admin)

## Özellikler

### Temel Özellikler
- ✅ OpenLiteSpeed + PHP 8.2 kurulumu
- ✅ MariaDB kurulumu
- ✅ Domain ekleme/silme
- ✅ Veritabanı oluşturma/silme
- ✅ MySQL root şifre sıfırlama
- ✅ OpenLiteSpeed admin şifre sıfırlama
- ✅ Etkileşimli menü arayüzü

### Güvenlik ve Performans
- ✅ Firewall yönetimi (UFW/iptables)
- ✅ SSL/HTTPS desteği (Let's Encrypt)
- ✅ MariaDB güvenlik ayarları
- ✅ OpenLiteSpeed performans optimizasyonu
- ✅ Port kontrolü

### Yedekleme Sistemi
- ✅ Domain yedekleme (tar.gz)
- ✅ Veritabanı yedekleme (mysqldump)
- ✅ Yedek geri yükleme
- ✅ Yedek listeleme
- ✅ Otomatik yedek dizinleri

### SSL/HTTPS Özellikleri
- ✅ Let's Encrypt otomatik sertifika
- ✅ HTTPS listener konfigürasyonu
- ✅ SSL güvenlik ayarları
- ✅ HTTP/HTTPS yönlendirme