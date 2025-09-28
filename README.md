# isPanel - SSH-based Web Hosting Management Panel (Ubuntu 22+)

[![Language Support](https://img.shields.io/badge/Language-EN%20%7C%20TR-blue)](https://github.com/ismailaydemiriu/ispanel)
[![OpenLiteSpeed](https://img.shields.io/badge/OpenLiteSpeed-1.7.18-green)](https://openlitespeed.org/)
[![PHP](https://img.shields.io/badge/PHP-8.2%20%7C%208.3-purple)](https://php.net/)
[![MariaDB](https://img.shields.io/badge/MariaDB-10.6+-orange)](https://mariadb.org/)

## 🌍 Multi-Language Support / Çok Dilli Destek

**English** | [Türkçe](#türkçe)

---

## Installation (Ubuntu 22+)

### 🚀 One-Click Installation

```bash
curl -sSL https://raw.githubusercontent.com/ismailaydemiriu/ispanel/main/install.sh | sudo bash
```

or

```bash
wget -qO- https://raw.githubusercontent.com/ismailaydemiriu/ispanel/main/install.sh | sudo bash
```

### 📋 Manual Installation

1) Copy Python script and make it executable

```bash
sudo chmod +x ispanel
```

2) Run installation wizard (OpenLiteSpeed + PHP 8.2/8.3 + MariaDB):

```bash
sudo python3 ispanel install
```

After installation, the `/usr/local/bin/ispanel` command is created.

### Installation Directory
isPanel is installed in `/usr/local/ispanel/`:
- Main script: `/usr/local/ispanel/ispanel`
- Templates: `/usr/local/ispanel/templates/`
- Command: `/usr/local/bin/ispanel` (wrapper)

### If command not found / installation interrupted

If `sudo ispanel` command doesn't work or symlink creation is interrupted during installation:

```bash
# 1) Recreate symlink
sudo rm -f /usr/local/bin/ispanel
sudo ln -s $(pwd)/ispanel /usr/local/bin/ispanel

# 2) You can also repair from menu
sudo ispanel  # if it opens
# 25) Update isPanel → 1) Repair ispanel command
```

Note: Python command must be `python3`. If `python` doesn't exist, run like this:

```bash
sudo python3 ispanel install
```

## Menu Usage

```bash
sudo ispanel
```

## Commands

- **Install:** `sudo python3 ispanel install`
- **Add Domain:** `sudo python3 ispanel domain-add example.com`
- **Remove Domain:** `sudo python3 ispanel domain-rm example.com`
- **Create DB:** `sudo python3 ispanel db-create dbname dbuser strongpass`
- **Delete DB:** `sudo python3 ispanel db-delete dbname dbuser`

## Menu Options

```
=== isPanel - Web Hosting Management Panel ===
1) Installation (OpenLiteSpeed + PHP 8.2/8.3 + MariaDB)
2) Add Domain
3) Change Domain PHP Version
4) Domain List
5) Remove Domain
6) Create Database
7) Database List
8) Delete Database
9) Fix Virtual Host Root
10) Fix Vhost Configuration
11) Reset MySQL Root Password
12) Reset OpenLiteSpeed Admin Password
13) Port Control and Firewall Management
14) Install SSL/HTTPS Support
15) MariaDB Security Settings
16) OpenLiteSpeed Performance Optimization
17) File Backup Menu
18) Database Backup Menu
19) List Backups
20) Cron Backup Settings
21) Repair Tools
22) Cache Systems (Redis/Memcached)
23) System Management
24) OLS/PHP Settings
25) Update isPanel
0) Exit
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

## Templates

- OpenLiteSpeed vhost configuration is generated from `templates/vhost.conf.j2` template.
- Different template directory can be used with `ISPANEL_TEMPLATE_DIR` environment variable.

---

# Türkçe

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

2) Kurulum sihirbazını çalıştırın (OpenLiteSpeed + PHP 8.2/8.3 + MariaDB):

```bash
sudo python3 ispanel install
```

Kurulum sonunda `/usr/local/bin/ispanel` komutu oluşturulur.

### Kurulum Dizini
isPanel `/usr/local/ispanel/` dizinine kurulur:
- Ana script: `/usr/local/ispanel/ispanel`
- Templates: `/usr/local/ispanel/templates/`
- Komut: `/usr/local/bin/ispanel` (wrapper)

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
=== isPanel - Web Hosting Yönetim Paneli ===
1) Kurulum (OpenLiteSpeed + PHP 8.2/8.3 + MariaDB)
2) Domain Ekle
3) Domain PHP Sürümü Değiştir
4) Domain Listesi
5) Domain Sil
6) Veritabanı Oluştur
7) Veritabanı Listesi
8) Veritabanı Sil
9) Virtual Host Root Düzelt
10) Vhost Konfigürasyon Düzelt
11) MySQL Root Şifre Sıfırla
12) OpenLiteSpeed Admin Şifre Sıfırla
13) Port Kontrolü ve Firewall Yönetimi
14) SSL/HTTPS Desteği Kur
15) MariaDB Güvenlik Ayarları
16) OpenLiteSpeed Performans Optimizasyonu
17) Dosya Yedekleme Menüsü
18) Veritabanı Yedekleme Menüsü
19) Yedekleri Listele
20) Cron Backup Ayarları
21) Onarım Araçları
22) Cache Sistemleri (Redis/Memcached)
23) Sistem Yönetimi
24) OLS/PHP Ayarları
25) isPanel Güncelle
0) Çıkış
```

## Özellikler

### 🌐 Çok Dilli Destek
- **İngilizce** (varsayılan)
- **Türkçe**
- SSH'da `ispanel` yazınca ilk olarak dil seçimi yapılır

### 🚀 Web Hosting Özellikleri
- ✅ OpenLiteSpeed 1.7.18+ (yüksek performanslı web sunucusu)
- ✅ PHP 8.2 ve 8.3 desteği (domain bazında seçilebilir)
- ✅ MariaDB 10.6+ (MySQL uyumlu veritabanı)
- ✅ Let's Encrypt SSL sertifikaları
- ✅ HTTP/3 QUIC desteği
- ✅ Gzip sıkıştırma
- ✅ Cache optimizasyonu

### 🔧 Yönetim Özellikleri
- ✅ SSH tabanlı komut satırı arayüzü
- ✅ Domain ekleme/silme
- ✅ Veritabanı oluşturma/silme
- ✅ PHP sürüm yönetimi (domain bazında)
- ✅ Otomatik yedekleme sistemi
- ✅ Firewall yönetimi (UFW)
- ✅ Port kontrolü ve yönetimi
- ✅ Sistem optimizasyonu

### 🔒 Güvenlik Özellikleri
- ✅ SSL/HTTPS otomatik kurulum
- ✅ Let's Encrypt sertifika yenileme
- ✅ Fail2Ban kurulumu (brute-force koruması)
- ✅ MariaDB güvenlik ayarları
- ✅ Firewall kuralları
- ✅ Dosya izin yönetimi

### 📦 Yedekleme ve Onarım
- ✅ Domain yedekleme (tar.gz)
- ✅ Veritabanı yedekleme (mysqldump)
- ✅ Otomatik yedekleme (cron)
- ✅ Yedek listesi ve yönetimi
- ✅ Onarım araçları
- ✅ Sistem durumu kontrolü

### 🎨 Modern Arayüz
- ✅ Profesyonel default index.php
- ✅ Kurumsal tasarım
- ✅ Responsive web arayüzü
- ✅ Teknoloji yığını gösterimi
- ✅ Sistem istatistikleri

## SSL/HTTPS Özellikleri
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