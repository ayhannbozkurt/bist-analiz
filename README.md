# BIST Piyasa Analiz Uygulaması

## Proje Hakkında

Bu uygulama, Borsa İstanbul (BIST) piyasasındaki hisse senetlerinin gerçek zamanlı analizini yapan, görselleştiren ve detaylı raporlar sunan bir web uygulamasıdır. Streamlit kullanılarak geliştirilmiş olup, kullanıcı dostu arayüzü sayesinde piyasa verilerini kolayca incelemenizi sağlar.

## Özellikler

- **Genel Piyasa Görünümü**: Tüm BIST piyasasının treemap görselleştirmesi ve özet istatistikleri
- **Yıldız Pazar Analizi**: BIST Yıldız Pazar'daki hisselerin detaylı analizi ve görselleştirmesi
- **Ana Pazar Analizi**: BIST Ana Pazar'daki hisselerin detaylı analizi ve görselleştirmesi
- **Hisse Senedi Detaylı Analizi**: Seçilen hisse senedi için:
  - Fiyat grafiği
  - Teknik analiz
  - Finansal durum raporu
  - İndirilebilir detaylı analiz raporu

## Kurulum

### Gereksinimler

```
streamlit
pandas
plotly
yfinance
python-dotenv
```

### Kurulum Adımları

1. Projeyi klonlayın:
   ```
   git clone <repo-url>
   cd <repo-directory>
   ```

2. Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```

3. `.env` dosyasını oluşturun (gerekiyorsa):
   ```
   touch .env
   ```

## Kullanım

### Uygulamayı Çalıştırma

```
streamlit run app.py
```

Bu komut, uygulamayı yerel bir web sunucusunda başlatacak ve tarayıcınızda otomatik olarak açılacaktır.

### Veri Güncelleme

Uygulamayı yerel olarak çalıştırırken verileri güncellemek için:

```
python python_data.py
```

Bu komut, BIST piyasasından en güncel verileri çekecek ve yerel veri dosyalarını güncelleyecektir.

## Uygulama Yapısı

- **app.py**: Ana uygulama dosyası ve kullanıcı arayüzü
- **data_fetcher.py**: BIST verilerini çeken modül
- **visualization.py**: Görselleştirme fonksiyonlarını içeren modül
- **analysis.py**: Hisse senedi analiz fonksiyonlarını içeren modül
- **python_data.py**: Verileri güncellemek için kullanılan script

## Ekran Görüntüleri

[Buraya uygulamanın ekran görüntülerini ekleyebilirsiniz]

## Katkıda Bulunma

1. Bu repo'yu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inize push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## Lisans

[Lisans bilgisi eklenecek]

## İletişim

[İletişim bilgilerinizi ekleyebilirsiniz] # bist-analiz

# Environment variables
.env

# Python cache
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
dist/
build/
*.egg-info/

# Jupyter Notebook
.ipynb_checkpoints

# Virtual Environment
venv/
env/
ENV/

# IDE specific files
.idea/
.vscode/
*.swp
*.swo
