#!/bin/bash

# isPanel Kurulum Script'i
# Bu script isPanel'i sisteminize kurulumunu sağlar

set -e
set -x  # Debug mode - tüm komutları göster

# Renk tanımlamaları
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Root kontrolü
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}Lütfen bu script'i root olarak çalıştırın${NC}"
    exit 1
fi

echo -e "${GREEN}isPanel Kurulumu Başlıyor...${NC}"

# Gerekli paketleri kur
echo -e "${YELLOW}Gerekli paketler kontrol ediliyor...${NC}"
apt-get update -y
apt-get install -y python3 python3-pip git

# isPanel dizinini oluştur
ISPANEL_HOME="/usr/local/ispanel"
echo -e "${YELLOW}isPanel dizini oluşturuluyor: $ISPANEL_HOME${NC}"
mkdir -p $ISPANEL_HOME

# Script'in bulunduğu dizini al
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Mevcut dizinden dosyaları kopyala
echo -e "${YELLOW}Dosyalar kopyalanıyor...${NC}"

# Ana dosyaları kopyala
cp -f "$SCRIPT_DIR/ispanel" "$ISPANEL_HOME/" 2>/dev/null || true
cp -f "$SCRIPT_DIR/README.md" "$ISPANEL_HOME/" 2>/dev/null || true
cp -f "$SCRIPT_DIR/install.sh" "$ISPANEL_HOME/" 2>/dev/null || true

# Templates dizinini kopyala
if [ -d "$SCRIPT_DIR/templates" ]; then
    cp -r "$SCRIPT_DIR/templates" "$ISPANEL_HOME/"
    echo -e "${GREEN}Templates dizini kopyalandı${NC}"
else
    echo -e "${RED}Templates dizini bulunamadı: $SCRIPT_DIR/templates${NC}"
    exit 1
fi

# Tests dizinini kopyala (varsa)
if [ -d "$SCRIPT_DIR/tests" ]; then
    cp -r "$SCRIPT_DIR/tests" "$ISPANEL_HOME/"
    echo -e "${GREEN}Tests dizini kopyalandı${NC}"
fi

# Python script'ini çalıştırılabilir yap
chmod +x $ISPANEL_HOME/ispanel

# Symlink kurulumu için Python script'ini çağır
echo -e "${YELLOW}isPanel komutu kuruluyor...${NC}"
python3 $ISPANEL_HOME/ispanel install-symlink

# Test et
if command -v ispanel &> /dev/null; then
    echo -e "${GREEN}isPanel başarıyla kuruldu!${NC}"
    echo -e "${GREEN}Kullanım: ispanel${NC}"
else
    echo -e "${RED}isPanel kurulumu başarısız!${NC}"
    exit 1
fi

echo -e "${GREEN}Kurulum tamamlandı!${NC}"
echo -e "${YELLOW}isPanel menüsünü açmak için: ispanel${NC}"