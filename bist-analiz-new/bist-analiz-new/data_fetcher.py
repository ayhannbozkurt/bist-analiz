import pandas as pd
import yfinance as yf
import os
import streamlit as st
from bist_data import get_yildiz_pazar_stocks, get_ana_pazar_stocks, SECTOR_MAPPING
from typing import Dict, Optional, Tuple

# Çekilen verileri önbelleğe alarak performansı iyileştir
@st.cache_data(ttl=3600)  # 1 saat süreyle önbellekte tut
def get_market_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Borsa İstanbul pazar verilerini getirir.
    Yerel CSV'ler varsa onları, yoksa canlı veri kullanır.
    
    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: Yıldız Pazar ve Ana Pazar verileri
    """
    if is_local():
        # Yerel CSV dosyalarından oku
        try:
            yildiz_df = pd.read_csv("data/yildiz_pazar.csv")
            yildiz_df["Pazar"] = "Yıldız Pazar"
            
            ana_df = pd.read_csv("data/ana_pazar.csv")
            ana_df["Pazar"] = "Ana Pazar"
            
            return yildiz_df, ana_df
        except Exception as e:
            st.error(f"CSV dosyaları okunamadı: {str(e)}")
            return pd.DataFrame(), pd.DataFrame()
    else:
        # Canlı veri çek
        yildiz_df_list = []
        for hisse in get_yildiz_pazar_stocks():
            result = get_stock_info(hisse)
            if result is not None:
                result["Pazar"] = "Yıldız Pazar"
                yildiz_df_list.append(result)
        yildiz_df = pd.DataFrame(yildiz_df_list)
        
        ana_df_list = []
        for hisse in get_ana_pazar_stocks():
            result = get_stock_info(hisse)
            if result is not None:
                result["Pazar"] = "Ana Pazar"
                ana_df_list.append(result)
        ana_df = pd.DataFrame(ana_df_list)
        
        return yildiz_df, ana_df

def is_local() -> bool:
    """
    Uygulamanın yerel ortamda mı çalıştığını kontrol eder
    
    Returns:
        bool: Yerel CSV dosyaları varsa True, yoksa False
    """
    return os.path.exists("data/yildiz_pazar.csv") and os.path.exists("data/ana_pazar.csv")

def get_stock_info(hisse: str) -> Optional[Dict]:
    """
    Bir hisse için gerekli bilgileri çeker
    
    Args:
        hisse (str): Hisse kodu (örn. THYAO.IS)
        
    Returns:
        Optional[Dict]: Hisse bilgileri veya None
    """
    try:
        stock = yf.Ticker(hisse)
        
        try:
            # Son 5 günün kapanış fiyatlarını al
            hist = stock.history(period="5d") 
            
            if len(hist) < 2:  # Yeterli veri yoksa
                st.warning(f"{hisse}: Yeterli fiyat verisi bulunamadı. Hisse delistelenmiş olabilir ya da veri sağlayıcıda sorun yaşanıyor.")
                return None
                
            son_kapanis = hist['Close'].iloc[-1]  # Son kapanış
            onceki_kapanis = hist['Close'].iloc[-2]  # Önceki kapanış
            
            değişim = ((son_kapanis - onceki_kapanis) / onceki_kapanis) * 100
            
            info = stock.info
            
            # info boş bir sözlük olarak gelmiş olabilir veya gerekli alanları içermeyebilir
            if not info or len(info) < 3:  # Temel birkaç bilgi bile yoksa
                st.warning(f"{hisse}: Hisse bilgileri alınamadı. Veri sağlayıcıda sorun olabilir.")
                return None
                
            market_cap = info.get('marketCap', 0) / 37 / 1000000  # TL'den USD'ye çevrim
            
            # F/K oranı hesapla
            pe_ratio = info.get('trailingPE', None)
            if pe_ratio is None or pe_ratio <= 0 or pe_ratio > 1000:
                pe_ratio = None
            
            # 52 hafta yüksek/düşük bilgisi
            high_52week = info.get('fiftyTwoWeekHigh', 0)
            low_52week = info.get('fiftyTwoWeekLow', 0)
            
            # Yüzdelik pozisyon hesapla (şimdiki fiyatın 52 hafta aralığındaki yeri)
            if high_52week > low_52week and high_52week > 0 and low_52week > 0:
                position_52week = ((son_kapanis - low_52week) / (high_52week - low_52week)) * 100
            else:
                position_52week = None
                
            # Günlük hacim (adet)
            volume = info.get('volume', 0)
            avg_volume = info.get('averageVolume', 0)
            
            # Sektör bilgisini daha sağlam bir şekilde al
            sector = info.get('sector', None)
            if sector is None or sector == '':
                sector = 'Diğer'
            sector = SECTOR_MAPPING.get(sector, sector)
            if sector is None or sector == '':
                sector = 'Diğer'
            
            if market_cap > 0:
                return {
                    "Hisse": hisse.replace(".IS", ""),
                    "Değişim (%)": değişim,
                    "Piyasa Değeri (mn $)": market_cap,
                    "Sektör": sector,
                    "Son Kapanış": son_kapanis,
                    "Önceki Kapanış": onceki_kapanis,
                    "F/K": pe_ratio,
                    "52H Yüksek": high_52week,
                    "52H Düşük": low_52week,
                    "52H Pozisyon (%)": position_52week,
                    "Günlük Hacim": volume,
                    "Ortalama Hacim": avg_volume
                }
                
            st.warning(f"{hisse}: Piyasa değeri bilgisi alınamadı.")
            return None
                
        except Exception as hist_error:
            # Daha fazla bilgi sağla
            st.warning(f"{hisse}: Veri çekilirken hata oluştu: {str(hist_error)}")
            return None
            
    except Exception as e:
        # Daha fazla bilgi sağla
        st.warning(f"{hisse}: İşlem sırasında hata: {str(e)}")
        return None
        
    return None 