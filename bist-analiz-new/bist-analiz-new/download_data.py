#!/usr/bin/env python3
"""
BIST Veri İndirme Modülü
Bu script BIST verisini indirip yerel CSV dosyalarına kaydeder
"""

import pandas as pd
import os
from data_fetcher import get_stock_info
from bist_data import get_yildiz_pazar_stocks, get_ana_pazar_stocks

def download_market_data():
    """
    BIST verilerini indirir ve CSV olarak kaydeder
    """
    print("Yıldız Pazar verileri indiriliyor...")
    yildiz_df_list = []
    for hisse in get_yildiz_pazar_stocks():
        print(f"İşleniyor: {hisse}", end="\r")
        result = get_stock_info(hisse)
        if result is not None:
            result["Pazar"] = "Yıldız Pazar"
            yildiz_df_list.append(result)
    
    print("\nAna Pazar verileri indiriliyor...")
    ana_df_list = []
    for hisse in get_ana_pazar_stocks():
        print(f"İşleniyor: {hisse}", end="\r")
        result = get_stock_info(hisse)
        if result is not None:
            result["Pazar"] = "Ana Pazar"
            ana_df_list.append(result)
    
    # DataFrame'leri oluştur
    yildiz_df = pd.DataFrame(yildiz_df_list)
    ana_df = pd.DataFrame(ana_df_list)
    
    # Klasörü kontrol et ve oluştur
    if not os.path.exists("data"):
        os.makedirs("data")
        
    # CSV'lere kaydet
    yildiz_df.to_csv("data/yildiz_pazar.csv", index=False)
    ana_df.to_csv("data/ana_pazar.csv", index=False)
    
    print(f"\nVeriler kaydedildi:")
    print(f"- Yıldız Pazar: {len(yildiz_df)} hisse")
    print(f"- Ana Pazar: {len(ana_df)} hisse")
    
    return yildiz_df, ana_df

if __name__ == "__main__":
    download_market_data() 