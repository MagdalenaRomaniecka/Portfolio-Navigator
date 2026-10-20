import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Magdalena Romaniecka ✦ Portfolio",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- HELPER FUNCTION ---
def find_file(filename):
    for root, _, files in os.walk("."):
        if filename and filename in files:
            return os.path.join(root, filename)
    return filename

# --- DESIGN SYSTEM (DARK LUXURY) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Lato:wght@300;400;700&display=swap');
    
    .stApp {
        background-color: #0E0E0E;
        color: #E0E0E0;
        font-family: 'Lato', sans-serif !important;
    }
    .hero-container {
        text-align: center;
        padding: 60px 20px 40px 20px;
    }
    .hero-title {
        font-family: 'Tenor Sans', sans-serif;
        color: #D4AF37;
        font-size: 3.5rem;
        letter-spacing: 8px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        color: #888888;
        font-size: 1.2rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 30px;
    }
    .hero-pitch {
        color: #E0E0E0;
        max-width: 700px;
        margin: 0 auto 50px auto;
        line-height: 1.8;
        font-size: 1.1rem;
    }
    .section-title {
        font-family: 'Tenor Sans', sans-serif;
        color: #D4AF37;
        font-size: 1.5rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin: 50px 0 20px 0;
        text-align: center;
        border-bottom: 1px solid rgba(212,175,55,0.3);
        padding-bottom: 10px;
    }
    .giant-cta-container {
        text-align: center;
        margin-top: 60px;
        margin-bottom: 80px;
    }
    .giant-cta-btn {
        display: inline-block;
        background: linear-gradient(145deg, #D4AF37 0%, #B8962D 100%);
        color: #0E0E0E !important;
        font-family: 'Tenor Sans', sans-serif;
        font-size: 1.5rem;
        font-weight: bold;
        letter-spacing: 4px;
        text-transform: uppercase;
        padding: 25px 60px;
        text-decoration: none !important;
        border-radius: 3px;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.2);
    }
    .giant-cta-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(212, 175, 55, 0.35);
        background: linear-gradient(145deg, #E5C354 0%, #D4AF37 100%);
    }
    .footer { text-align: center; color: #555555; font-size: 0.75rem; letter-spacing: 3px; border-top: 1px solid #1F1F1F; padding-top: 30px; margin-top: 40px; }
    </style>
""", unsafe_allow_html=True)

def main():
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">Magdalena Romaniecka</div>
            <div class="hero-subtitle">Data Architect ✦ Web Analytics ✦ CRO</div>
            <div class="hero-pitch">
                Bridging Data Engineering with Conversion Rate Optimization. 
                Deploying Python, NLP, and Streamlit architectures to transform raw macroeconomic 
                and behavioral data into scalable enterprise solutions.
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # --- MULTIMEDIA SECTION ---
    st.markdown('<div class="section-title">Executive Portfolio Audit</div>', unsafe_allow_html=True)
    
    video_path = find_file("Auditing_Magdalena_Romaniecka_Fragrance_Data_Architecture.mp4")
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.warning("Video file not found. Please ensure 'Auditing_Magdalena_Romaniecka_Fragrance_Data_Architecture.mp4' is in the directory.")

    st.markdown('<div class="section-title">The Phygital Architecture</div>', unsafe_allow_html=True)
    
    img_path = find_file("Data_Architecture_Anti_Crisis_Shield (1).png")
    if os.path.exists(img_path):
        st.image(img_path, use_column_width=True)
    else:
        st.warning("Infographic not found. Please ensure 'Data_Architecture_Anti_Crisis_Shield (1).png' is in the directory.")

    # --- CALL TO ACTION ---
    st.markdown("""
        <div class="giant-cta-container">
            <a href="https://global-fragrance-intelligence-app-fqjkvd9syohbhfpczxgnph.streamlit.app/" target="_blank" class="giant-cta-btn">
                ENTER MASTER DASHBOARD
            </a>
            <div style="color:#888; font-size:0.85rem; margin-top:20px; letter-spacing:2px; text-transform:uppercase;">
                Explore The Full Phygital Ecosystem Inside
            </div>
        </div>
        <div class="footer">ARCHITECTURAL DESIGN BY MAGDALENA ROMANIECKA ✦ 2026</div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()