import streamlit as st
import pandas as pd
from data_fetcher import get_market_data
from visualization import create_treemap, create_price_chart, create_market_summary
from analysis import StockAnalyzer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    st.set_page_config(
        page_title="BIST Görünümü", 
        layout="wide", 
        initial_sidebar_state="collapsed",
        page_icon="📈"
    )
    
    # Tab'ları oluştur
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Genel Görünüm", "🌟 Yıldız Pazar", "📈 Ana Pazar", "🔍 Hisse Analizi"])
    
    with st.spinner("Rapor oluşturuluyor..."):
        # Verileri getir (yerel veya canlı)
        yildiz_df, ana_df = get_market_data()
        
        # Tüm verileri birleştir
        tum_df = pd.concat([yildiz_df, ana_df])
        
        if len(tum_df) > 0:
            # Genel Görünüm Tab'ı
            with tab1:
                st.title("BIST Genel Görünümü")
                
                # Tüm piyasa treemap'i (pazar gösterimi olmadan)
                st.plotly_chart(create_treemap(tum_df, "Tüm Piyasa"), use_container_width=True)
                
                # Piyasa özeti
                create_market_summary(tum_df)
                
                # Genel istatistikler
                st.subheader("Piyasa İstatistikleri")
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Toplam Şirket Sayısı", len(tum_df))
                col2.metric("Yükselen Hisse Sayısı", len(tum_df[tum_df["Değişim (%)"] > 0]))
                col3.metric("Düşen Hisse Sayısı", len(tum_df[tum_df["Değişim (%)"] < 0]))
                col4.metric("Değişmeyen Hisse Sayısı", len(tum_df[tum_df["Değişim (%)"] == 0]))
            
            # Yıldız Pazar Tab'ı
            with tab2:
                st.title("BIST Yıldız Pazar")
                
                # Yıldız Pazar özeti
                create_market_summary(yildiz_df)
                
                # Yıldız Pazar Treemap (pazar gösterimi ile)
                st.plotly_chart(create_treemap(yildiz_df, "Yıldız Pazar", show_market=True), use_container_width=True)
            
            # Ana Pazar Tab'ı
            with tab3:
                st.title("BIST Ana Pazar")

                # Ana Pazar özeti
                create_market_summary(ana_df)
                
                # Ana Pazar Treemap (pazar gösterimi ile)
                st.plotly_chart(create_treemap(ana_df, "Ana Pazar", show_market=True), use_container_width=True)
            
            # Hisse Analizi Tab'ı
            with tab4:
                st.title("Hisse Senedi Analizi")
                
                # Üst kısım için stil ekleyin
                st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    font-weight: bold;
                }
                .analysis-card {
                    padding: 20px;
                    border-radius: 10px;
                    background-color: #f9f9f9;
                    margin-bottom: 20px;
                }
                </style>
                """, unsafe_allow_html=True)
                
                # Açıklama metni ekleyin
                st.markdown("""
                <div class="analysis-card">
                <p class="big-font">📈 Hisse Senedi Detaylı Analizi</p>
                <p>Aşağıdan bir hisse seçerek teknik analiz, finansal durum ve güncel piyasa verilerini içeren detaylı bir rapor oluşturabilirsiniz.</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Tüm hisseleri birleştir
                all_stocks = sorted(tum_df["Hisse"].tolist())
                
                # Hisse seçimi için tek sütun kullan
                selected_stock = st.selectbox(
                    "Analiz edilecek hisseyi seçin:",
                    all_stocks,
                    index=0 if "THYAO" in all_stocks else 0
                )
                
                # Seçilen hisse hakkında ön bilgiler
                if selected_stock:
                    # Hisse bilgilerini seç
                    stock_info = tum_df[tum_df["Hisse"] == selected_stock].iloc[0]
                    
                    # Kart içinde sadece son fiyat ve değişim bilgilerini göster
                    st.markdown(f"""
                    <div style="
                        background-color: {'#d4f7d4' if stock_info['Değişim (%)'] > 0 else '#f7d4d4'};
                        padding: 15px;
                        border-radius: 5px;
                        margin: 10px 0px;
                        text-align: center;
                    ">
                        <h3>{selected_stock}</h3>
                        <p>Sektör: {stock_info['Sektör']}</p>
                        <table style="width: 100%; text-align: center;">
                            <tr>
                                <td><b>Son Fiyat:</b> {stock_info['Son Kapanış']:.2f} ₺</td>
                                <td><b>Değişim:</b> {stock_info['Değişim (%)']:.2f}%</td>
                            </tr>
                        </table>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Büyük, çekici bir analiz butonu
                if st.button("🔍 Detaylı Analiz Oluştur", type="primary", use_container_width=True):
                    try:
                        # Analizör oluştur
                        analyzer = StockAnalyzer()
                        
                        # Analizi yap - progress bar olmadan
                        result = analyzer.analyze_stock(selected_stock)
                        
                        if result['success']:                            
                            # Grafik ve piyasa verilerini doğrudan göster - tam genişlikte
                            st.subheader(f"{selected_stock} Fiyat Grafiği")
                            if 'stock_data' in result and 'history' in result['stock_data']:
                                df = result['stock_data']['history']
                                fig = create_price_chart(df, f'{selected_stock} Fiyat Grafiği')
                                st.plotly_chart(fig, use_container_width=True)
                            
                            # Analiz içeriğini ekrana yazdır
                            st.markdown("---")
                            st.subheader(f"{selected_stock} Analiz Raporu")
                            st.markdown(result['analysis'])
                            
                            # İndir butonu - tam genişlikte
                            st.markdown("---")
                            if st.download_button(
                                label="📥 Raporu İndir",
                                data=result['analysis'],
                                file_name=f"{selected_stock}_analiz_raporu.md",
                                mime="text/markdown",
                                use_container_width=True
                            ):
                                st.success("Rapor başarıyla indirildi!")
                                
                        else:
                            st.error(f"❌ Hata oluştu: {result['error']}")

                    except Exception as e:
                        st.error(f"❌ Beklenmeyen bir hata oluştu: {str(e)}")
                        st.exception(e)
        else:
            st.error("Veri bulunamadı!")

if __name__ == "__main__":
    main()