"""
Voces en Calma - Main Application
A safe space for anonymous storytelling and wellness matching
"""

import streamlit as st
from utils.database import get_story_count
from utils.translations import get_text, get_language_toggle, set_language
from utils.ui_helpers import add_custom_css
from utils.auth import get_contact_info, is_authenticated

# Page configuration - MUST be first
st.set_page_config(
    page_title="Voces en Calma",
    page_icon="🕊️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Add custom CSS for polish - AFTER page config
add_custom_css()

# Sidebar customization
with st.sidebar:

    # Global Language toggle - will persist across all pages
    st.markdown("### 🌐 Language / Idioma")
    
    current_lang = get_language_toggle()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🇺🇸 English", 
                    use_container_width=True,
                    type="primary" if current_lang == 'en' else "secondary"):
            set_language('en')
            st.rerun()
    with col2:
        if st.button("🇲🇽 Español", 
                    use_container_width=True,
                    type="primary" if current_lang == 'es' else "secondary"):
            set_language('es')
            st.rerun()
    
    st.markdown("---")
    
    # Show admin info if authenticated
    if is_authenticated():
        st.success("🔓 Admin Access Active")
        st.caption("You have access to the Insights Dashboard")

# Get current language
lang = get_language_toggle()

# Custom CSS for beautiful styling
st.markdown("""
    <style>
    /* Reduce excessive spacing */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1000px;
    }
    
    /* Tighter spacing between sections */
    .element-container {
        margin-bottom: 0.5rem;
    }
    
    /* Remove extra padding from markdown */
    .stMarkdown {
        margin-bottom: 0.5rem;
    }
    
    /* Main header styling */
    .main-header {
        text-align: center;
        color: #D4846E;
        font-size: 3em;
        font-weight: 700;
        margin-bottom: 0.3em;
        margin-top: 0;
    }
    
    .subtitle {
        text-align: center;
        color: #6B5B95;
        font-size: 1.3em;
        font-style: italic;
        margin-bottom: 1.5em;
        margin-top: 0;
    }
    
    .welcome-text {
        font-size: 1.1em;
        line-height: 1.6;
        color: #2C3E50;
        text-align: center;
        margin: 1.5em 0;
        padding: 0 1rem;
    }
    
    .stats-box {
        background-color: #F5EFE7;
        padding: 1.5em;
        border-radius: 10px;
        text-align: center;
        margin: 1.5em 0;
    }
    
    .cta-button {
        text-align: center;
        margin: 1.5em 0;
    }
    
    /* Consistent section spacing */
    h2 {
        margin-top: 1.5rem !important;
        margin-bottom: 1rem !important;
    }
    
    h3 {
        margin-top: 1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Horizontal rules with less space */
    hr {
        margin: 1.5rem 0 !important;
    }
    
    /* Remove extra space from info boxes */
    .stAlert {
        margin: 1rem 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown(f'<h1 class="main-header">{get_text("main_header", lang)}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="subtitle">{get_text("subtitle", lang)}</p>', unsafe_allow_html=True)

# Welcome message - with tighter spacing
welcome_text = get_text("welcome_text", lang)
st.markdown(f'<div class="welcome-text">{welcome_text}</div>', unsafe_allow_html=True)

# Community impact stats
story_count = get_story_count()
st.markdown(f"""
    <div class="stats-box">
        <h3 style="color: #D4846E; margin-bottom: 0.5em;">{get_text("community_impact", lang)}</h3>
        <p style="font-size: 2em; font-weight: 700; color: #6B5B95; margin: 0;">{story_count}</p>
        <p style="color: #2C3E50;">{get_text("stories_shared", lang)}</p>
    </div>
""", unsafe_allow_html=True)

# Three-column layout for features
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"### 🔒 {get_text('private', lang)}")
    st.write(get_text('private_desc', lang))

with col2:
    st.markdown(f"### 🤝 {get_text('supported', lang)}")
    st.write(get_text('supported_desc', lang))

with col3:
    st.markdown(f"### 🌱 {get_text('community_led', lang)}")
    st.write(get_text('community_led_desc', lang))

# Call to action
st.markdown('<div class="cta-button">', unsafe_allow_html=True)
st.info(get_text('ready_to_share', lang))
st.markdown('</div>', unsafe_allow_html=True)

# About section
st.markdown(f"## {get_text('about', lang)}")

# Split text into paragraphs and format consistently
about_text_content = get_text('about_text', lang)
paragraphs = about_text_content.split('\n\n')

for para in paragraphs:
    if para.strip():
        # Check if it's the emphasized line
        if 'matter' in para.lower() and len(para) < 100:
            st.markdown(f"""
            <p style="
                font-size: 1.1em;
                line-height: 1.7;
                color: #2C3E50;
                text-align: left;
                margin: 1rem 0;
                font-weight: 600;
            ">
            <strong>{para.strip()}</strong>
            </p>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <p style="
                font-size: 1.05em;
                line-height: 1.7;
                color: #2C3E50;
                text-align: left;
                margin: 1rem 0;
            ">
            {para.strip()}
            </p>
            """, unsafe_allow_html=True)

# Contact section
contact_info = get_contact_info()

# Community Guidelines
st.markdown(f"## {get_text('community_guidelines', lang)}")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    ### {get_text('be_respectful', lang)}
    {get_text('be_respectful_text', lang)}
    """)

with col2:
    st.markdown(f"""
    ### {get_text('stay_anonymous', lang)}
    {get_text('stay_anonymous_text', lang)}
    """)

with col3:
    st.markdown(f"""
    ### {get_text('seek_support', lang)}
    {get_text('seek_support_text', lang)}
    """)

# Footer
st.markdown("---")
st.markdown(f"""
    <div style="text-align: center; color: #8B9D83; font-size: 0.9em; margin-top: 2em;">
    {get_text('footer', lang)}<br><br>
    📧 {contact_info['email']} | 📞 {contact_info['phone']}
    </div>
""", unsafe_allow_html=True)