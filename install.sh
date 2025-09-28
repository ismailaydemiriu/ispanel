#!/bin/bash

# isPanel Kurulum Script'i
# Bu script isPanel'i sisteminize kurulumunu sağlar

set -e

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

# Mevcut dizinden dosyaları kopyala
echo -e "${YELLOW}Dosyalar kopyalanıyor...${NC}"
cp -r * $ISPANEL_HOME/ 2>/dev/null || true
cp -r .* $ISPANEL_HOME/ 2>/dev/null || true

# Templates dizinini kontrol et
if [ ! -d "$ISPANEL_HOME/templates" ]; then
    echo -e "${RED}Templates dizini bulunamadı!${NC}"
    exit 1
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