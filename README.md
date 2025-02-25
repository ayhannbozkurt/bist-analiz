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

```
DEMO
```

https://github.com/user-attachments/assets/ce23329d-090d-43e2-82d9-f942669fdda3


## Kurulum

### Gereksinimler

```
streamlit
pandas
plotly
yfinance
langchain
```

### Kurulum Adımları

1. Projeyi klonlayın:
   ```
   git clone https://github.com/ayhannbozkurt/bist-analiz
   cd <bist-analiz>
   ```

2. Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```

3. `.env` dosyasını oluşturun:
   ```
   touch .env
   ```
## API KEYS

Uygulama için GROK api key almanız gerekecektir. .env dosyasının içine aldığınız api key'i bu şekilde girin;

XAI_API_KEY=your_api_key

## Kullanım

### Uygulamayı Çalıştırma

```
streamlit run app.py
```

Bu komut, uygulamayı yerel bir web sunucusunda başlatacak ve tarayıcınızda otomatik olarak açılacaktır.

### Veri Güncelleme

Uygulamayı yerel olarak çalıştırırken verileri güncellemek için:

```
python download_data.py
```

Bu komut, BIST piyasasından en güncel verileri çekecek ve yerel veri dosyalarını güncelleyecektir.

## Uygulama Yapısı

- **app.py**: Ana uygulama dosyası ve kullanıcı arayüzü
- **data_fetcher.py**: BIST verilerini çeken modül
- **visualization.py**: Görselleştirme fonksiyonlarını içeren modül
- **analysis.py**: Hisse senedi analiz fonksiyonlarını içeren modül
- **python_data.py**: Verileri güncellemek için kullanılan script

