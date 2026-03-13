@echo off
echo Proje bagimliliklari kuruluyor...
pip install -r requirements.txt
pip install pyinstaller

echo.
echo Executable (.exe) insa ediliyor...
pyinstaller --noconfirm ATD_Muhasebe.spec

echo.
echo Islem tamamlandi. Uygulama "dist/Stok_Cari_Takip/Stok_Cari_Takip.exe" dizininde bulunabilir.
pause
