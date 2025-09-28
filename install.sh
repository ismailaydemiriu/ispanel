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
apt-get install -y python3 python3-pip git curl wget

# isPanel dizinini oluştur
ISPANEL_HOME="/usr/local/ispanel"
echo -e "${YELLOW}isPanel dizini oluşturuluyor: $ISPANEL_HOME${NC}"
mkdir -p $ISPANEL_HOME

# Geçici dizin oluştur
TMP_DIR=$(mktemp -d)
cd $TMP_DIR

# GitHub'dan repo'yu klonla
echo -e "${YELLOW}isPanel GitHub'dan indiriliyor...${NC}"
git clone https://github.com/ismailaydemiriu/ispanel.git
cd ispanel

# Dosyaları kopyala
echo -e "${YELLOW}Dosyalar kopyalanıyor...${NC}"

# Ana dosyaları kopyala
cp -f ispanel "$ISPANEL_HOME/"
cp -f README.md "$ISPANEL_HOME/"
cp -f install.sh "$ISPANEL_HOME/"

# Git repository'sini kopyala (güncelleme için gerekli)
if [ -d ".git" ]; then
    cp -r .git "$ISPANEL_HOME/"
    echo -e "${GREEN}Git repository kopyalandı${NC}"
fi

# Templates dizinini kopyala
if [ -d "templates" ]; then
    cp -r templates "$ISPANEL_HOME/"
    echo -e "${GREEN}Templates dizini kopyalandı${NC}"
else
    echo -e "${RED}Templates dizini bulunamadı!${NC}"
    exit 1
fi

# Tests dizinini kopyala (varsa)
if [ -d "tests" ]; then
    cp -r tests "$ISPANEL_HOME/"
    echo -e "${GREEN}Tests dizini kopyalandı${NC}"
fi

# Geçici dizini temizle
cd /
rm -rf $TMP_DIR

# Python script'ini çalıştırılabilir yap
chmod +x $ISPANEL_HOME/ispanel

# Symlink kurulumu için Python script'ini çağır
echo -e "${YELLOW}isPanel komutu kuruluyor...${NC}"
python3 $ISPANEL_HOME/ispanel install-symlink

# Test et
if command -v ispanel &> /dev/null; then
    echo -e "${GREEN}✅ isPanel successfully installed!${NC}"
    echo ""
    echo -e "${CYAN}📋 Available Installation Options:${NC}"
    echo -e "${YELLOW}  1) Full Installation (OpenLiteSpeed + PHP 8.2/8.3 + MariaDB)${NC}"
    echo -e "${YELLOW}  2) Install OpenLiteSpeed Only (Web Server + PHP)${NC}"
    echo -e "${YELLOW}  3) Install MariaDB Only (Database Server)${NC}"
    echo ""
    echo -e "${CYAN}🚀 Quick Start:${NC}"
    echo -e "${GREEN}  • Run: ${YELLOW}ispanel${NC} ${GREEN}to open the interactive menu${NC}"
    echo -e "${GREEN}  • Language: English (default) / Türkçe${NC}"
    echo -e "${GREEN}  • Installation directory: /usr/local/ispanel${NC}"
    echo -e "${GREEN}  • Command: /usr/local/bin/ispanel${NC}"
    echo ""
    echo -e "${CYAN}📖 Next Steps:${NC}"
    echo -e "${WHITE}  1. Run 'ispanel' to start the installation wizard${NC}"
    echo -e "${WHITE}  2. Choose your installation type (Full/OpenLiteSpeed/MariaDB)${NC}"
    echo -e "${WHITE}  3. Follow the on-screen instructions${NC}"
    echo ""
else
    echo -e "${RED}❌ isPanel installation failed!${NC}"
    exit 1
fi

echo -e "${GREEN}🎉 Installation completed successfully!${NC}"
echo -e "${YELLOW}💡 To open isPanel menu: ${CYAN}ispanel${NC}"