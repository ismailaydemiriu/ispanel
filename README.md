# ispanel - SSH tabanlı mini panel (Ubuntu 22+)

## Kurulum (Ubuntu 22+)

### 🚀 Tek Tıkla Kurulum

```bash
curl -sSL https://raw.githubusercontent.com/ismailaydemiriu/ispanel/main/install.sh | sudo bash
```

veya

```bash
wget -qO- https://raw.githubusercontent.com/ismailaydemiriu/ispanel/main/install.sh | sudo bash
```

### 📋 Manuel Kurulum

1) Python scripti kopyalayın ve çalıştırılabilir yapın

```bash
sudo chmod +x ispanel
```

2) Kurulum sihirbazını çalıştırın (OpenLiteSpeed + PHP 8.2 + MariaDB):

```bash
sudo python3 ispanel install
```

Kurulum sonunda `/usr/local/bin/ispanel` komutu oluşturulur.

### Komut bulunamazsa / kurulum yarıda kalırsa

Eğer `sudo ispanel` komutu çalışmazsa veya kurulum sırasında symlink oluşumu yarıda kalırsa:

```bash
# 1) Symlink'i yeniden oluştur
sudo rm -f /usr/local/bin/ispanel
sudo ln -s $(pwd)/ispanel /usr/local/bin/ispanel

# 2) Menüden de onarabilirsiniz
sudo ispanel  # açılırsa
# 25) isPanel güncelle → 1) ispanel komutunu onar
```

Not: Python komutu `python3` olmalıdır. `python` yoksa şu şekilde çalıştırın:

```bash
sudo python3 ispanel install
```

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
2) Kurulum (OpenLiteSpeed + PHP 8.3 + MariaDB)
3) Domain ekle
4) Domain Listesi
5) Domain sil
6) DB Listesi
7) Virtual Host Root düzelt
8) Vhost Konfigürasyon düzelt
9) DB oluştur
10) DB sil
11) MySQL root şifre sıfırla
12) OpenLiteSpeed admin şifre sıfırla
13) Port kontrolü ve Firewall yönetimi
14) SSL/HTTPS desteği kur
15) MariaDB güvenlik ayarları
16) OpenLiteSpeed performans optimizasyonu
17) Dosya yedekleme menüsü
18) Veritabanı yedekleme menüsü
19) Yedekleri listele
20) Cron backup ayarları
21) Onarım araçları
22) Cache sistemleri (Redis/Memcached)
23) Sistem yönetimi
24) OLS/PHP ayarları
25) isPanel güncelle
0) Çıkış
```

## Notlar

- **Domain docroot:** `/home/<domain>/public_html`
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
- ✅ Fail2Ban ile brute-force koruması

### Yedekleme Sistemi
- ✅ Domain yedekleme (tar.gz)
- ✅ Veritabanı yedekleme (mysqldump)
- ✅ Yedek geri yükleme
- ✅ Yedek listeleme
- ✅ Otomatik yedek dizinleri
- ✅ SHA256 doğrulamalı yedekleme çıktıları

### SSL/HTTPS Özellikleri
- ✅ Let's Encrypt otomatik sertifika
- ✅ HTTPS listener konfigürasyonu
- ✅ SSL güvenlik ayarları
- ✅ HTTP/HTTPS yönlendirme
- ✅ Fail2Ban kurulumu (temel brute-force koruması)

## Test ve Geliştirme

- Pytest tabanlı temel testler `tests/` dizininde yer alır.
- Yeni geliştirmeler için `python -m pytest` ile testleri çalıştırabilirsiniz.
- Testler, OpenLiteSpeed yapılandırmasını sahte bir dizine yönlendirecek şekilde izole edilmiştir.

## Loglama

- Tüm komut çağrıları `/var/log/ispanel.log` dosyasına kaydedilir (uzaktan konum `ISPANEL_LOG_FILE` ile değiştirilebilir).
- Detay seviyesini `ISPANEL_LOG_LEVEL` ortam değişkeni (`INFO`, `DEBUG` vb.) ile ayarlayabilirsiniz.

## Şablonlar

- OpenLiteSpeed vhost yapılandırması `templates/vhost.conf.j2` şablonundan üretilir.
- `ISPANEL_TEMPLATE_DIR` ortam değişkeni ile farklı bir şablon dizini kullanılabilir.