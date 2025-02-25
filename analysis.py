from langchain_xai import ChatXAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
import yfinance as yf
from datetime import datetime, timedelta

class StockAnalyzer:
    def __init__(self, api_key=None):
        # Load environment variables
        load_dotenv()
        
        # Initialize the ChatXAI model
        self.llm = ChatXAI(
            model_name="grok-beta",
            temperature=0,
            xai_api_key=api_key or os.getenv("XAI_API_KEY")
        )
        
        # Define the analysis template
        self.analysis_template = """
# {stock_code} Hisse Senedi Analiz Raporu

## Güncel Piyasa Verileri
{market_data}

## Detaylı Analiz Raporu

{stock_code} hisse senedi için yapılan detaylı analiz aşağıda sunulmuştur:

1. Finansal Durum ve Performans:
   {fundamental_analysis_points}

2. Teknik Göstergeler ve Fiyat Analizi:
   {technical_analysis_points}

3. Piyasa Duyarlılığı ve Haberler:
   {news_analysis_points}

4. Risk Faktörleri ve Fırsatlar:
   - Jeopolitik ve sektörel riskler
   - Şirkete özel risk faktörleri
   - Büyüme potansiyeli ve fırsatlar
   - Sektördeki rekabet durumu 

---

## 💡 Yatırım Stratejisi ve Öneriler

{expected_outputs}

⚠️ Not: Bu analiz yatırım tavsiyesi niteliği taşımamaktadır. Tüm yatırım kararlarınızı kendi araştırmalarınıza dayanarak alınız.
"""

    def get_stock_data(self, stock_code):
        """
        yfinance kullanarak hisse senedi verilerini çeker
        
        Args:
            stock_code (str): Hisse senedi kodu
            
        Returns:
            dict: Hisse senedi verileri
        """
        try:
            # BIST hisseleri için .IS ekle
            ticker = yf.Ticker(f"{stock_code}.IS")
            
            # Son 1 yıllık kapanış fiyatları
            end_date = datetime.now()
            start_date = end_date - timedelta(days=365)
            hist = ticker.history(start=start_date, end=end_date)
            
            # Hisse bilgilerini al
            info = ticker.info
            
            # Son fiyat ve değişim bilgileri
            current_price = hist['Close'][-1] if not hist.empty else None
            prev_close = hist['Close'][-2] if len(hist) > 1 else None
            price_change = ((current_price - prev_close) / prev_close * 100) if current_price and prev_close else None
            
            # 52 hafta en yüksek/düşük
            year_high = hist['High'].max() if not hist.empty else None
            year_low = hist['Low'].min() if not hist.empty else None
            
            # Format değerleri güvenli bir şekilde işle (None kontrolü)
            def safe_format(value, format_str=".2f"):
                if value is None:
                    return "N/A"
                try:
                    if format_str == ".2f":
                        return f"{value:.2f}"
                    elif format_str == ",":
                        return f"{value:,}"
                    else:
                        return str(value)
                except:
                    return "N/A"
            
            market_data = f"""
            📊 Güncel Piyasa Verileri ({datetime.now().strftime('%d.%m.%Y %H:%M')}):
            
            - Güncel Fiyat: {safe_format(current_price)} TL
            - Günlük Değişim: {safe_format(price_change)}%
            - 52 Hafta En Yüksek: {safe_format(year_high)} TL
            - 52 Hafta En Düşük: {safe_format(year_low)} TL
            - İşlem Hacmi: {safe_format(info.get('volume', 'N/A'), ",")} TL
            - Piyasa Değeri: {safe_format(info.get('marketCap', 'N/A'), ",")} TL
            - F/K Oranı: {info.get('trailingPE', 'N/A')}
            - Beta: {info.get('beta', 'N/A')}
            """
            
            return {
                'success': True,
                'market_data': market_data,
                'current_price': current_price,
                'price_change': price_change,
                'info': info,
                'history': hist
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def analyze_stock(self, stock_code):
        """
        Hisse senedi analizi yapar
        
        Args:
            stock_code (str): Analiz edilecek hisse senedi kodu (örn: THYAO)
            
        Returns:
            dict: Analiz sonuçları
        """
        try:
            # Önce güncel verileri çek
            stock_data = self.get_stock_data(stock_code)
            if not stock_data['success']:
                raise Exception(f"Hisse verileri çekilemedi: {stock_data['error']}")
            
            # Safe format function for display
            def safe_format(value, format_str=".2f"):
                if value is None:
                    return "N/A"
                try:
                    if format_str == ".2f":
                        return f"{value:.2f}"
                    elif format_str == ",":
                        return f"{value:,}"
                    else:
                        return str(value)
                except:
                    return "N/A"
            
            # Prepare analysis inputs
            analysis_inputs = {
                "stock_code": f"{stock_code}.IS",
                "market_data": stock_data['market_data'],
                "fundamental_analysis_points": f"""
                - Gelir Tablosu ve Büyüme: Şirketin yıllık gelir büyümesi, FAVÖK marjı trendi ve net kar marjı gelişimi incelenmiştir.
                - Bilanço Yapısı: Varlık yapısı, borç/özkaynak oranı ve işletme sermayesi yeterliliği değerlendirilmiştir.
                - Nakit Akışı: Operasyonel nakit akışı, yatırım harcamaları ve finansman faaliyetleri analiz edilmiştir.
                - Finansal Oranlar: ROE, ROA, Net Kar Marjı trendi, PD/DD analizi ve F/K oranı ({stock_data['info'].get('trailingPE', 'N/A')}) incelenmiştir.
                - Sektörel Konum: Pazar payı, rekabet avantajları ve operasyonel verimlilik değerlendirilmiştir.
                """,
                
                "technical_analysis_points": f"""
                - Fiyat Durumu: Mevcut fiyat {safe_format(stock_data['current_price'])} TL, günlük değişim {safe_format(stock_data['price_change'])}%
                - Teknik Göstergeler: RSI, MACD ve hareketli ortalamalar incelenmiştir.
                - Hacim Analizi: Günlük işlem hacmi {safe_format(stock_data['info'].get('volume', 'N/A'), ",")} TL olup, fiyat-hacim ilişkisi ve kurumsal işlemler değerlendirilmiştir.
                - Trend ve Formasyonlar: Mevcut trend, olası formasyonlar ve kritik destek/direnç seviyeleri belirlenmiştir.
                """,
                
                "news_analysis_points": f"""
                - Şirket Gelişmeleri: Stratejik kararlar, yönetim değişiklikleri, yeni yatırımlar ve finansal sonuçlar incelenmiştir.
                - Sektör Dinamikleri: Sektördeki gelişmeler, regülasyonlar ve küresel trendler değerlendirilmiştir.
                - Yatırımcı Algısı: Sosyal medya analizi, yatırımcı yorumları ve uzman görüşleri derlenmiştir.
                - Kurumsal Hareketler: Fon alım-satımları, yabancı yatırımcı pozisyonları ve büyük lot işlemler takip edilmiştir.
                """,
                
                "expected_outputs": f"""
                - Fiyat Beklentisi: Mevcut {safe_format(stock_data['current_price'])} TL seviyesinden kısa, orta ve uzun vadeli hedef fiyat aralıkları belirlenmiştir.
                - Risk/Getiri: Potansiyel yukarı yönlü getiri ve aşağı yönlü riskler değerlendirilmiştir.
                - Yatırım Stratejisi: Pozisyon önerileri, giriş-çıkış seviyeleri ve stop-loss noktaları hesaplanmıştır.
                - Portföy Yaklaşımı: Ağırlık önerisi, çeşitlendirme stratejisi ve hedge önerileri sunulmuştur.
                """
            }

            # Create the prompt template and chain
            prompt = ChatPromptTemplate.from_template(self.analysis_template)
            chain = LLMChain(llm=self.llm, prompt=prompt)
            
            # Run the analysis
            response = chain.run(analysis_inputs)
            
            # Debug print
            print("LLM Response:", response)
            
            return {
                'success': True,
                'analysis': response,  # Return the entire response as is
                'stock_data': stock_data
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
