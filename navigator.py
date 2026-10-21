import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Magdalena Romaniecka ✦ Portfolio",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DESIGN SYSTEM (DARK LUXURY) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');
    
    .stApp {
        background-color: #0E0E0E;
        color: #E0E0E0;
        font-family: 'Lato', sans-serif !important;
    }
    .hero-title {
        font-family: 'Tenor Sans', sans-serif;
        color: #D4AF37;
        font-size: 3rem;
        letter-spacing: 6px;
        text-transform: uppercase;
        margin-bottom: 10px;
        margin-top: 20px;
    }
    .hero-subtitle {
        color: #888888;
        font-size: 1.1rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 30px;
    }
    .hero-pitch {
        color: #E0E0E0;
        line-height: 1.8;
        font-size: 1.1rem;
        margin-bottom: 40px;
    }
    .giant-cta-btn {
        display: inline-block;
        background: linear-gradient(145deg, #D4AF37 0%, #B8962D 100%);
        color: #0E0E0E !important;
        font-family: 'Tenor Sans', sans-serif;
        font-size: 1.3rem;
        font-weight: bold;
        letter-spacing: 3px;
        text-transform: uppercase;
        padding: 20px 40px;
        text-decoration: none !important;
        border-radius: 3px;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.2);
        width: 100%;
        text-align: center;
    }
    .giant-cta-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(212, 175, 55, 0.35);
        background: linear-gradient(145deg, #E5C354 0%, #D4AF37 100%);
    }
    .footer { 
        text-align: center; color: #555555; font-size: 0.75rem; 
        letter-spacing: 3px; border-top: 1px solid #1F1F1F; 
        padding-top: 30px; margin-top: 60px; margin-bottom: 20px;
    }
    
    /* Responsive video wrapper */
    [data-testid="stVideo"] {
        max-width: 320px !important;
        margin: 0 auto !important;
        display: block;
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 8px;
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # --- SPLIT SCREEN HERO SECTION ---
    col_text, col_video = st.columns([1, 1.2], gap="large")
    
    with col_text:
        st.markdown("""
            <div class="hero-title">Magdalena Romaniecka</div>
            <div class="hero-subtitle">Data Architect ✦ Web Analytics ✦ CRO</div>
            <div class="hero-pitch">
                Bridging Data Engineering with Conversion Rate Optimization (CRO). 
                I specialize in Python, NLP (SBERT), and Streamlit architectures to transform raw macroeconomic 
                and behavioral data into scalable enterprise solutions. 
                <br><br>
                Welcome to the Phygital Architecture.
            </div>
            
            <a href="https://global-fragrance-intelligence-app-fqjkvd9syohbhfpczxgnph.streamlit.app/" target="_blank" class="giant-cta-btn">
                ENTER MASTER DASHBOARD
            </a>
            <div style="text-align: center; color:#888; font-size:0.85rem; margin-top:15px; letter-spacing:2px; text-transform:uppercase;">
                Explore The Full Phygital Ecosystem Inside
            </div>
        """, unsafe_allow_html=True)

    with col_video:
        # BEZPOŚREDNIE WSKAZANIE PLIKU (Rozwiązuje problem z zawieszaniem!)
        video_filename = "Auditing_Magdalena_Romaniecka_Fragrance_Data_Architecture.mp4"
        
        if os.path.isfile(video_filename):
            st.video(video_filename)
        else:
            st.markdown(f"""
            <div style="border: 1px dashed rgba(212,175,55,0.4); padding: 80px 20px; text-align: center; color: #888888; background-color: #121212;">
                [ EXECUTIVE AUDIT VIDEO NOT FOUND ]<br>Please place '{video_filename}' in the root directory.
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="footer">ARCHITECTURAL DESIGN BY MAGDALENA ROMANIECKA ✦ 2026</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()