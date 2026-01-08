"""
Healers Directory Page - Meet our Latina wellness practitioners
"""

import streamlit as st
from utils.translations import get_text, get_language_toggle, set_language
from utils.ui_helpers import add_custom_css

# Page configuration
st.set_page_config(
    page_title="Our Circle of Healers - Voces en Calma",
    page_icon="🌺",
    layout="centered"
)

# Add custom CSS
add_custom_css()

# Get current language (set globally in Home.py)
lang = get_language_toggle()

# Custom CSS for healer cards
st.markdown("""
    <style>
    .healer-card {
        background-color: #F5EFE7;
        padding: 1.5em;
        border-radius: 15px;
        margin: 1.5em 0;
        border-left: 5px solid #D4846E;
    }
    .healer-name {
        color: #D4846E;
        font-size: 1.5em;
        font-weight: 700;
        margin-bottom: 0.3em;
    }
    .healer-title {
        color: #6B5B95;
        font-style: italic;
        margin-bottom: 1em;
    }
    .healer-bio {
        color: #2C3E50;
        line-height: 1.6;
    }
    .practice-tag {
        background-color: #8B9D83;
        color: white;
        padding: 0.3em 0.8em;
        border-radius: 15px;
        font-size: 0.85em;
        margin-right: 0.5em;
        display: inline-block;
        margin-top: 0.5em;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title(get_text('healers_title', lang))
st.markdown(f"### {get_text('healers_subtitle', lang)}")

# Introduction
st.markdown(get_text('healers_intro', lang))

# Healer profiles (you can customize these with real practitioners later)
healers = [
    {
        "name": "Ana María Reyes",
        "title": "Curandera & Trauma-Informed Coach",
        "bio": "Ana María bridges generations of healing wisdom passed down from her abuela with contemporary trauma therapy. She specializes in helping people navigate family expectations and cultural identity while honoring ancestral practices of *limpias* (spiritual cleansing) and herbal medicine.",
        "practices": ["Curanderismo", "Trauma Therapy", "Herbal Medicine", "Energy Healing"]
    },
    {
        "name": "Marisol Delgado, LMFT",
        "title": "Licensed Therapist & Herbalist",
        "bio": "As a licensed marriage and family therapist and certified herbalist, Marisol creates a unique healing space where talk therapy meets traditional plant medicine. She understands the specific stressors facing Latina women balancing multiple roles and cultural expectations.",
        "practices": ["Talk Therapy", "Herbal Remedies", "Family Systems", "CBT"]
    },
    {
        "name": "Yaneli Torres",
        "title": "Somatic Movement Facilitator & Yoga Instructor",
        "bio": "Yaneli helps people release stress and trauma held in the body through gentle movement, breathwork, and somatic practices. She weaves traditional Mexican dance and music into her sessions, creating healing experiences that honor our cultural roots while addressing modern burnout.",
        "practices": ["Somatic Healing", "Yoga", "Breathwork", "Dance Therapy"]
    },
    {
        "name": "Esperanza Medina",
        "title": "Spiritual Guide & Prayer Circle Leader",
        "bio": "Esperanza leads prayer circles, meditation groups, and spiritual guidance sessions rooted in *fe* (faith) and community gathering traditions. She creates sacred spaces where people can find peace, connection, and spiritual support during difficult times.",
        "practices": ["Prayer Circles", "Meditation", "Spiritual Counseling", "Group Rituals"]
    },
    {
        "name": "Dr. Carmen Flores, PsyD",
        "title": "Clinical Psychologist & Art Therapist",
        "bio": "Dr. Flores combines clinical psychology with creative expression therapy. She believes healing happens through storytelling, art, music, and creative practices that connect us to our emotions and our culture. Her work is especially powerful for those processing grief and loss.",
        "practices": ["Clinical Psychology", "Art Therapy", "EMDR", "Creative Expression"]
    }
]

# Display healer cards
for healer in healers:
    st.markdown(f"""
        <div class="healer-card">
            <div class="healer-name">{healer['name']}</div>
            <div class="healer-title">{healer['title']}</div>
            <div class="healer-bio">{healer['bio']}</div>
            <div style="margin-top: 1em;">
                {''.join([f'<span class="practice-tag">{practice}</span>' for practice in healer['practices']])}
            </div>
        </div>
    """, unsafe_allow_html=True)

# Philosophy section
st.markdown(f"## {get_text('healing_philosophy', lang)}")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### {get_text('ancestral_wisdom', lang)}")
    if lang == 'es':
        st.markdown("""
        - *Curanderismo* y sanación tradicional
        - Remedios herbales y medicina de plantas
        - Oración y prácticas espirituales
        - Música, danza y rituales culturales
        - Tradiciones de reunión comunitaria
        """)
    else:
        st.markdown("""
        - *Curanderismo* & traditional healing
        - Herbal remedies & plant medicine
        - Prayer & spiritual practices
        - Music, dance & cultural rituals
        - Community gathering traditions
        """)

with col2:
    st.markdown(f"### {get_text('modern_approaches', lang)}")
    if lang == 'es':
        st.markdown("""
        - Terapia informada en trauma
        - Sanación somática y basada en el cuerpo
        - Atención plena y meditación
        - Técnicas basadas en evidencia (CBT, EMDR)
        - Psicoeducación y herramientas de salud mental
        """)
    else:
        st.markdown("""
        - Trauma-informed therapy
        - Somatic & body-based healing
        - Mindfulness & meditation
        - Evidence-based techniques (CBT, EMDR)
        - Psychoeducation & mental health tools
        """)

st.info(get_text('how_this_works_text', lang))

# Call to action
st.markdown(f"### {get_text('ready_share_story', lang)}")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button(get_text('submit_button', lang), type="primary", use_container_width=True):
        st.switch_page("pages/1_Share_Story.py") if hasattr(st, 'switch_page') else None

# Footer
st.markdown("""
    <div style="text-align: center; color: #8B9D83; font-size: 0.9em; margin-top: 2em;">
    💚 This is a community-led healing space<br>
    We honor all paths to wellness and healing
    </div>
""", unsafe_allow_html=True)