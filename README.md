# ATD Muhasebe — Cari ve Stok Takip Uygulaması

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyQt6](https://img.shields.io/badge/UI-PyQt6-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

ATD Muhasebe, küçük ve orta ölçekli işletmeler için tasarlanmış, kullanımı kolay, modern arayüzlü bir **Cari ve Stok Takip** uygulamasıdır. Python ve PyQt6 kullanılarak geliştirilen bu uygulama, verileri güvenli bir şekilde JSON formatında yerel olarak saklar.

## 🚀 Öne Çıkan Özellikler

### 📦 Stok Yönetimi
- **Ürün Kartları:** Barkod, birim, çarpan ve KDV oranlarıyla detaylı ürün kaydı.
- **Kritik Stok Takibi:** Stok seviyesi kritik eşiğin altına düştüğünde otomatik uyarı (kırmızı vurgu).
- **Excel Entegrasyonu:** Excel'den toplu ürün aktarımı ve mevcut stoğu Excel'e ihraç etme.

### 👥 Cari Hesap Takibi
- **Müşteri ve Tedarikçi Yönetimi:** Borç/alacak takibi, iletişim bilgileri ve vergi detayları.
- **Cari Hareketler:** Her cari için detaylı ekstre ve işlem geçmişi.
- **Bakiye Durumu:** Anlık net bakiye görüntüleme (Borçlu/Alacaklı).

### 📄 Fatura ve Fiş İşlemleri
- **Satış & Alış:** Satış faturası, alış faturası ve iade fişleri oluşturma.
- **Sipariş Fişi:** Stok ve bakiyeyi etkilemeyen teklif/sipariş kayıtları.
- **Yazdıra:** Profesyonel görünümlü fatura ve fiş çıktıları alma.

### 🔍 Gelişmiş Sorgulama ve Raporlama
- **Detaylı Filtreleme:** Tarih aralığı, cari ve işlem türüne göre akıllı sorgulama.
- **PDF Raporlar:** Satış ve cari hareket raporlarını PDF olarak dışa aktarma.
- **Kasa Takibi:** Tüm nakit akışını ve tahsilat/ödeme işlemlerini tek ekrandan izleme.

## 🛠️ Teknik Altyapı
- **Dil:** Python 3
- **Arayüz:** PyQt6 (Modern ve Duyarlı Tasarım)
- **Veritabanı:** JSON tabanlı dosya sistemi (SQL kurulumu gerektirmez)
- **Raporlama:** pandas, openpyxl, fpdf2

## 📦 Kurulum

1.  Bu depoyu klonlayın:
    ```bash
    git clone https://github.com/kullanici_adinız/atd-muhasebe.git
    cd atd-muhasebe
    ```
2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
3.  Uygulamayı başlatın:
    ```bash
    python main.py
    ```

## 🏗️ Build (EXE Oluşturma)

Windows üzerinde taşınabilir bir `.exe` dosyası oluşturmak için PyInstaller kullanılır. Hazır scripti çalıştırabilirsiniz:

```bash
build.bat
```
Çıktı `dist/ATD_Muhasebe/` dizininde oluşturulacaktır. **Not:** `data/` klasörünün exe dosyasıyla aynı dizinde olduğundan emin olun.

## 📁 Proje Yapısı

-   `src/core/`: Veritabanı (db) singleton ve veri modelleri.
-   `src/ui/`: PyQt6 arayüz dosyaları ve sekme yönetimleri.
-   `src/utils/`: Excel, PDF, Yazdırma ve Yedekleme yardımcıları.
-   `data/`: Verilerin saklandığı yerel JSON dosyaları.

## 📝 Lisans
Bu proje **MIT Lisansı** ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.

---
*Geliştiren: [Sizin Adınız / Şirket Adınız]*
