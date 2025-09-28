#!/bin/bash

# ispanel - SSH tabanlı mini panel (Ubuntu 22+)
# Tek tıkla kurulum scripti

set -e

echo "=== ispanel Kurulum Scripti ==="
echo "Ubuntu 22+ için SSH tabanlı mini panel kurulumu"
echo ""

# Root kontrolü
if [ "$EUID" -ne 0 ]; then
    echo "Bu script root olarak çalıştırılmalıdır."
    echo "Kullanım: sudo bash install.sh"
    exit 1
fi

# OS kontrolü
if [ ! -f /etc/os-release ]; then
    echo "Desteklenmeyen işletim sistemi."
    exit 1
fi

. /etc/os-release
if [[ "$ID" != "ubuntu" ]] || [[ "$VERSION_ID" < "22.04" ]]; then
    echo "Bu script Ubuntu 22.04+ için tasarlanmıştır."
    echo "Mevcut sistem: $PRETTY_NAME"
    exit 1
fi

echo "Sistem kontrolü: ✅ Ubuntu $VERSION_ID"

# Gerekli paketleri güncelle
echo "Sistem paketleri güncelleniyor..."
apt-get update -y

# Gerekli paketleri kur
echo "Gerekli paketler kuruluyor..."
apt-get install -y curl wget python3 python3-pip git

# ispanel'i klonla
echo "ispanel indiriliyor..."
if [ -d "/tmp/ispanel" ]; then
    rm -rf /tmp/ispanel
fi

git clone https://github.com/ismailaydemiriu/ispanel.git /tmp/ispanel

# ispanel'i /usr/local/bin/ dizinine kopyala
echo "ispanel kuruluyor..."
cp /tmp/ispanel/ispanel /usr/local/bin/
chmod +x /usr/local/bin/ispanel

# Temizlik
rm -rf /tmp/ispanel

echo ""
echo "=== Kurulum Tamamlandı ==="
echo "✅ ispanel başarıyla kuruldu"
echo ""
echo "Kullanım:"
echo "  sudo ispanel"
echo ""
echo "İlk kurulum için:"
echo "  sudo ispanel"
echo "  Menüden '1' seçeneğini seçin"
echo ""
echo "Detaylı bilgi: https://github.com/ismailaydemiriu/ispanel"
