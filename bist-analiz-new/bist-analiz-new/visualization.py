import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def create_market_summary(df: pd.DataFrame):
    """
    Piyasa özeti oluşturma fonksiyonu
    
    Args:
        df (pd.DataFrame): Piyasa verileri içeren DataFrame
    """
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Sektör Dağılımı")
        sektor_df = df.groupby('Sektör').agg({
            'Piyasa Değeri (mn $)': 'sum',
            'Hisse': 'count'
        }).sort_values('Piyasa Değeri (mn $)', ascending=False)
        sektor_df.columns = ['Toplam Değer (mn $)', 'Şirket Sayısı']
        st.dataframe(sektor_df)
    
    with col2:
        st.subheader("En Çok Yükselenler")
        rising_df = df.nlargest(10, "Değişim (%)")[
            ["Hisse", "Değişim (%)", "Önceki Kapanış", "Son Kapanış"]
        ]
        # "Değişim (%)" formatlama - % işareti olmadan
        st.dataframe(rising_df.style.format({
            'Değişim (%)': '{:.2f}',  # % işareti olmadan
            'Önceki Kapanış': '{:.2f} ₺',
            'Son Kapanış': '{:.2f} ₺'
        }))
    
    with col3:
        st.subheader("En Çok Düşenler")
        falling_df = df.nsmallest(10, "Değişim (%)")[
            ["Hisse", "Değişim (%)", "Önceki Kapanış", "Son Kapanış"]
        ]
        # "Değişim (%)" formatlama - % işareti olmadan
        st.dataframe(falling_df.style.format({
            'Değişim (%)': '{:.2f}',  # % işareti olmadan
            'Önceki Kapanış': '{:.2f} ₺',
            'Son Kapanış': '{:.2f} ₺'
        }))

def create_treemap(df: pd.DataFrame, title: str = "", show_market: bool = False) -> go.Figure:
    """
    Treemap oluşturma fonksiyonu
    
    Args:
        df (pd.DataFrame): Treemap'te gösterilecek veriler
        title (str, optional): Treemap başlığı. Default ""
        show_market (bool, optional): Pazar bilgisinin gösterilip gösterilmeyeceği. Default False
        
    Returns:
        go.Figure: Oluşturulan treemap figürü
    """
    # Değişim yüzdesine göre renk aralıkları
    renkaralık = [-10, -5, -2, 0, 2, 5, 10]
    df["Renk"] = pd.cut(df["Değişim (%)"], bins=renkaralık,
                      labels=["darkred", "red", "lightpink", "lightgreen", "lime", "darkgreen"])
    
    # Veri kopyası oluştur (orijinal değişmesin)
    plot_df = df.copy()
    
    # Plotly'nin otomatik göstereceği gereksiz sütunları kaldır
    if "id" in plot_df.columns:
        plot_df = plot_df.drop(columns=["id"])
    if "parent" in plot_df.columns:
        plot_df = plot_df.drop(columns=["parent"])
    
    # Hiyerarşik path oluştur
    if show_market and "Pazar" in plot_df.columns:
        path = ["Pazar", "Sektör", "Hisse"]
    else:
        path = ["Sektör", "Hisse"]
    
    # Figür oluştur
    fig = px.treemap(
        plot_df,
        path=path,
        values="Piyasa Değeri (mn $)",
        color="Renk",
        custom_data=["Değişim (%)", "Sektör", "Piyasa Değeri (mn $)", 
                    "Son Kapanış", "Önceki Kapanış"],
        color_discrete_map={
            "(?)": "#262931",
            "darkred": "#8B0000", 
            "red": "#FF0000",
            "lightpink": "#FFB6C1",
            "lightgreen": "#90EE90",
            "lime": "#32CD32",
            "darkgreen": "#006400"
        },
        hover_data=None  # False yerine None kullan
    )
    
    # Layout özelliklerini güncelle
    fig.update_layout(
        title={
            'text': title,
            'y':0.98,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24}
        },
        height=800, 
        font=dict(size=14),
        uniformtext=dict(minsize=10),
        margin=dict(t=50, l=10, r=10, b=10),
        template="plotly_dark"
    )
    
    # Hover template'i tamamen yeniden tanımla
    custom_hover = '<b>%{label}</b><br>' + \
                  'Sektör: %{customdata[1]}<br>' + \
                  'Piyasa Değeri: %{customdata[2]:,.0f} mn $<br>' + \
                  'Son Kapanış: %{customdata[3]:.2f} ₺<br>' + \
                  'Önceki Kapanış: %{customdata[4]:.2f} ₺<br>' + \
                  'Günlük Değişim: %{customdata[0]:.2f}%<extra></extra>'
    
    # Trace'leri güncelle
    fig.update_traces(
        textfont=dict(size=14),
        hovertemplate=custom_hover,
        hoverinfo="text",
        textposition="middle center",
        textinfo="label+text",
        insidetextfont=dict(size=12)
    )
    
    # Text template ayarla
    fig.data[0].texttemplate = "<b>%{label}</b><br>%{customdata[0]:.1f}%"
    
    return fig

def create_price_chart(df: pd.DataFrame, title: str) -> go.Figure:
    """
    Hisse fiyat grafiği oluşturur
    
    Args:
        df (pd.DataFrame): Fiyat verileri
        title (str): Grafik başlığı
        
    Returns:
        go.Figure: Mum grafiği figürü
    """
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name="Fiyat"  # İsim vererek trace0 yerine "Fiyat" gösterilir
    )])
    
    # Grafik ayarları
    fig.update_layout(
        title={
            'text': title,
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 18}
        },
        yaxis_title='Fiyat (TL)',
        xaxis_title='Tarih',
        template='plotly_dark',
        height=500,
        xaxis_rangeslider_visible=False,  # Rangeslider'ı kaldır
        margin=dict(l=50, r=50, t=80, b=50),
        showlegend=False  # Tamamen legend'ı kaldır
    )
    
    # Hareketli ortalama ekleme
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['Close'].rolling(window=20).mean(),
        mode='lines',
        name='20 Günlük Ortalama',
        line=dict(color='orange', width=1)
    ))
    
    return fig 