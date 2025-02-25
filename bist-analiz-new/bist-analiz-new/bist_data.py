"""
BIST hisse senetleri ve ilgili veri yapıları
"""
def get_yildiz_pazar_stocks():
    """BIST Yıldız Pazar hisse listesini döndürür (228 şirket)"""
    return [
        # Yıldız Pazar (KAP verilerine göre güncel liste)
        "BINHO.IS", "ADEL.IS", "ADGYO.IS", "AGHOL.IS", "AGESA.IS", "AGROT.IS", "AHGAZ.IS", "AKBNK.IS",
        "AKCNS.IS", "AKFGY.IS", "AKFIS.IS", "AKFYE.IS", "AKSGY.IS", "AKSA.IS", "AKSEN.IS", "AKGRT.IS",
        "ALGYO.IS", "ALARK.IS", "ALBRK.IS", "ALFAS.IS", "ALTNY.IS", "ANSGR.IS", "AEFES.IS", "ANHYT.IS",
        "ARCLK.IS", "ARDYZ.IS", "ARMGD.IS", "ASGYO.IS", "ASELS.IS", "ASTOR.IS", "ATAKP.IS", "ATATP.IS",
        "AVPGY.IS", "AYDEM.IS", "AYGAZ.IS", "AZTEK.IS", "BALSU.IS", "BASGZ.IS", "BTCIM.IS", "BSOKE.IS",
        "BERA.IS", "BJKAS.IS", "BIENY.IS", "BIMAS.IS", "BINBN.IS", "BIOEN.IS", "BOBET.IS", "BORSK.IS",
        "BORLS.IS", "BRSAN.IS", "BRYAT.IS", "BFREN.IS", "BRISA.IS", "BUCIM.IS", "CEMZY.IS", "CCOLA.IS",
        "CVKMD.IS", "CWENE.IS", "CANTE.IS", "CATES.IS", "CLEBI.IS", "CIMSA.IS", "DAPGM.IS", "DSTKF.IS",
        "DEVA.IS", "DOHOL.IS", "ARASE.IS", "DOAS.IS", "EBEBK.IS", "ECZYT.IS", "EFORC.IS", "EGEEN.IS",
        "ECILC.IS", "EKGYO.IS", "ENJSA.IS", "ENERY.IS", "ENKAI.IS", "EREGL.IS", "ESCAR.IS", "TEZOL.IS",
        "EUREN.IS", "EUPWR.IS", "FENER.IS", "FROTO.IS", "GWIND.IS", "GSRAY.IS", "GENIL.IS", "GESAN.IS",
        "GLYHO.IS", "GOKNR.IS", "GOLTS.IS", "GOZDE.IS", "GRTHO.IS", "GUBRF.IS", "GLRMK.IS", "GRSEL.IS",
        "SAHOL.IS", "HLGYO.IS", "HRKET.IS", "HEKTS.IS", "HTTBT.IS", "ENTRA.IS", "INVEO.IS", "INVES.IS",
        "IEYHO.IS", "INDES.IS", "IPEKE.IS", "ISDMR.IS", "ISFIN.IS", "ISGYO.IS", "ISMEN.IS", "IZENR.IS",
        "JANTS.IS", "KLKIM.IS", "KLSER.IS", "KLYPV.IS", "KRDMA.IS", "KRDMD.IS", "KAREL.IS", "KARSN.IS",
        "KTLEV.IS", "KAYSE.IS", "KERVT.IS", "KLGYO.IS", "KLRHO.IS", "KMPUR.IS", "KCAER.IS", "KCHOL.IS",
        "KONTR.IS", "KONYA.IS", "KORDS.IS", "KOTON.IS", "KOZAL.IS", "KOZAA.IS", "KOPOL.IS", "KUYAS.IS",
        "LIDER.IS", "LILAK.IS", "LMKDC.IS", "LINK.IS", "LOGO.IS", "LYDHO.IS", "MAGEN.IS", "MAVI.IS",
        "MIATK.IS", "MGROS.IS", "MPARK.IS", "MOGAN.IS", "MOPAS.IS", "NATEN.IS", "NTHOL.IS", "NUHCM.IS",
        "OBAMS.IS", "ODAS.IS", "ODINE.IS", "OTKAR.IS", "OYAKC.IS", "OZKGY.IS", "OZATD.IS", "PAPIL.IS",
        "PARSN.IS", "PASEU.IS", "PSGYO.IS", "PATEK.IS", "PGSUS.IS", "PEKGY.IS", "PENTA.IS", "PEHOL.IS",
        "PETKM.IS", "POLHO.IS", "POLTK.IS", "QUAGR.IS", "RALYH.IS", "RAYSG.IS", "REEDR.IS", "RYGYO.IS",
        "RYSAS.IS", "RGYAS.IS", "SARKY.IS", "SASA.IS", "SAYAS.IS", "SDTTR.IS", "SELEC.IS", "SRVGY.IS",
        "SNGYO.IS", "SMRTG.IS", "SUNTK.IS", "SURGY.IS", "SUWEN.IS", "SKBNK.IS", "SOKM.IS", "TABGD.IS",
        "TNZTP.IS", "TATEN.IS", "TAVHL.IS", "TKFEN.IS", "TKNSA.IS", "TOASO.IS", "TRGYO.IS", "TSPOR.IS",
        "TUKAS.IS", "TRCAS.IS", "TUREX.IS", "TCELL.IS", "TMSN.IS", "TUPRS.IS", "THYAO.IS", "TTKOM.IS",
        "TTRAK.IS", "GARAN.IS", "HALKB.IS", "ISCTR.IS", "TSKB.IS", "TURSG.IS", "SISE.IS", "VAKBN.IS",
        "ULKER.IS", "VAKFN.IS", "VAKKO.IS", "VERUS.IS", "VESBE.IS", "VESTL.IS", "YKBNK.IS", "YYLGD.IS",
        "YEOTK.IS", "YIGIT.IS", "ZRGYO.IS", "ZOREN.IS"
    ]

def get_ana_pazar_stocks():
    """BIST Ana Pazar hisse listesini döndürür (270 şirket)"""
    return [
        # Ana Pazar (KAP verilerine göre güncel liste)
        "AVOD.IS", "A1CAP.IS", "ACSEL.IS", "ADESE.IS", "AFYON.IS", "AHSGY.IS", "AKENR.IS", "ATEKS.IS",
        "ALCAR.IS", "ALCTL.IS", "ALKIM.IS", "ALKA.IS", "AYCES.IS", "ALKLC.IS", "ALMAD.IS", "ALVES.IS",
        "ASUZU.IS", "ANGEN.IS", "ANELE.IS", "ARENA.IS", "ARSAN.IS", "ARTMS.IS", "ARZUM.IS", "AVHOL.IS",
        "AYEN.IS", "BAGFS.IS", "BAHKM.IS", "BAKAB.IS", "BNTAS.IS", "BANVT.IS", "BARMA.IS", "BEGYO.IS",
        "BYDNR.IS", "BAYRK.IS", "BRKSN.IS", "BEYAZ.IS", "BLCYT.IS", "BRKVY.IS", "BIGEN.IS", "BRLSM.IS",
        "BIZIM.IS", "BMSTL.IS", "BOSSA.IS", "BULGS.IS", "BURCE.IS", "BVSAN.IS", "BIGCH.IS", "CRFSA.IS",
        "CEOEM.IS", "CONSE.IS", "CGCAM.IS", "CELHA.IS", "CEMAS.IS", "CEMTS.IS", "CMBTN.IS", "CUSAN.IS",
        "DAGI.IS", "DARDL.IS", "DGATE.IS", "DCTTR.IS", "DMSAS.IS", "DENGE.IS", "DZGYO.IS", "DERIM.IS",
        "DERHL.IS", "DESA.IS", "DESPC.IS", "DNISI.IS", "DITAS.IS", "DMRGD.IS", "DOCO.IS", "DOFER.IS",
        "DOBUR.IS", "DGNMO.IS", "DOKTA.IS", "DURDO.IS", "DURKN.IS", "DYOBY.IS", "EDATA.IS", "EDIP.IS",
        "EGGUB.IS", "EGPRO.IS", "EGSER.IS", "EPLAS.IS", "EGEGY.IS", "EKOS.IS", "EKSUN.IS", "ELITE.IS",
        "EMKEL.IS", "ENDAE.IS", "ENSRI.IS", "ERBOS.IS", "ERCB.IS", "KIMMR.IS", "ESCOM.IS", "ESEN.IS",
        "EYGYO.IS", "FADE.IS", "FMIZP.IS", "FLAP.IS", "FONET.IS", "FORMT.IS", "FORTE.IS", "FRIGO.IS",
        "FZLGY.IS", "GARFA.IS", "GEDIK.IS", "GEDZA.IS", "GLCVY.IS", "GENTS.IS", "GEREL.IS", "GZNMI.IS",
        "GIPTA.IS", "GMTAS.IS", "GOODY.IS", "GSDDE.IS", "GSDHO.IS", "GLRYH.IS", "GUNDG.IS", "HATSN.IS",
        "HDFGS.IS", "HEDEF.IS", "HKTM.IS", "HOROZ.IS", "HUNER.IS", "HURGZ.IS", "ICBCT.IS", "ICUGS.IS",
        "INGRM.IS", "ISKPL.IS", "IHLGM.IS", "IHGZT.IS", "IHAAS.IS", "IHLAS.IS", "IHYAY.IS", "IMASM.IS",
        "INFO.IS", "INTEM.IS", "ISGSY.IS", "ISYAT.IS", "ISSEN.IS", "IZMDC.IS", "IZFAS.IS", "KFEIN.IS",
        "KAPLM.IS", "KRDMB.IS", "KRTEK.IS", "KARYE.IS", "KARTN.IS", "KATMR.IS", "KRVGD.IS", "TCKRC.IS",
        "KZBGY.IS", "KLMSN.IS", "KOCMT.IS", "KLSYN.IS", "KNFRT.IS", "KONKA.IS", "KGYO.IS", "KRPLS.IS",
        "KRGYO.IS", "KRSTL.IS", "KRONT.IS", "KBORU.IS", "KZGYO.IS", "KUTPO.IS", "KTSKR.IS", "LIDFA.IS",
        "LKMNH.IS", "LRSHO.IS", "LUKSK.IS", "MACKO.IS", "MAKIM.IS", "MAKTK.IS", "MAALT.IS", "MRSHL.IS",
        "MRGYO.IS", "MARTI.IS", "MTRKS.IS", "MEDTR.IS", "MEGMT.IS", "MEKAG.IS", "MNDRS.IS", "MERCN.IS",
        "MERIT.IS", "MERKO.IS", "METUR.IS", "METRO.IS", "MHRGY.IS", "MSGYO.IS", "MOBTL.IS", "MNDTR.IS",
        "EGEPO.IS", "NTGAZ.IS", "NETAS.IS", "NIBAS.IS", "NUGYO.IS", "OBASE.IS", "OFSYM.IS", "ONCSM.IS",
        "ONRYT.IS", "ORGE.IS", "OSMEN.IS", "OSTIM.IS", "OYYAT.IS", "OZGYO.IS", "OZSUB.IS", "OZYSR.IS",
        "PAMEL.IS", "PNLSN.IS", "PAGYO.IS", "PRDGS.IS", "PRKME.IS", "PCILT.IS", "PENGD.IS", "PSDTC.IS",
        "PKENT.IS", "PETUN.IS", "PINSU.IS", "PNSUT.IS", "PKART.IS", "PLTUR.IS", "PRZMA.IS", "RTALB.IS",
        "RUBNS.IS", "SAFKR.IS", "SNICA.IS", "SANFM.IS", "SANKO.IS", "SAMAT.IS", "SEGMN.IS", "SELVA.IS",
        "SERNT.IS", "SKYLP.IS", "SMART.IS", "SOKE.IS", "SKTAS.IS", "SMRVA.IS", "SEGYO.IS", "SKYMD.IS",
        "TARKM.IS", "TATGD.IS", "TEKTU.IS", "TMPOL.IS", "TERA.IS", "TLMAN.IS", "TSGYO.IS", "TUCLK.IS",
        "MARBL.IS", "TRILC.IS", "PRKAB.IS", "TURGG.IS", "ULUFA.IS", "ULUSE.IS", "ULUUN.IS", "USAK.IS",
        "UNLU.IS", "VKGYO.IS", "VBTYZ.IS", "VRGYO.IS", "VERTU.IS", "VSNMD.IS", "YAPRK.IS", "YATAS.IS",
        "YGGYO.IS", "YYAPI.IS", "YESIL.IS", "YKSLN.IS", "YUNSA.IS", "ZEDUR.IS"
    ]

def get_all_stocks():
    """Tüm BIST hisselerini döndürür (Yıldız Pazar + Ana Pazar)"""
    return get_yildiz_pazar_stocks() + get_ana_pazar_stocks()

# Türkçe sektör eşleştirmeleri
SECTOR_MAPPING = {
    'Financial Services': 'Finans',
    'Industrials': 'Sanayi',
    'Technology': 'Teknoloji',
    'Consumer Cyclical': 'Tüketim',
    'Basic Materials': 'Hammadde',
    'Communication Services': 'İletişim',
    'Consumer Defensive': 'Temel Tüketim',
    'Energy': 'Enerji',
    'Healthcare': 'Sağlık',
    'Real Estate': 'Gayrimenkul',
    'Utilities': 'Kamu Hizmetleri'
} 