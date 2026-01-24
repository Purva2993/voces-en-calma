"""
Healers Directory Page
Showcases wellness practitioners serving the Latina community
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Healers - Voces en Calma",
    page_icon="🌺",
    layout="wide"
)

# Get current language
lang = st.session_state.get('language', 'en')

# Custom CSS for healer cards with side-by-side layout
st.markdown("""
<style>
    .healer-container {
        display: flex;
        gap: 30px;
        align-items: flex-start;
        background: linear-gradient(135deg, #f9f7f4 0%, #ffffff 100%);
        border-left: 4px solid #d4a574;
        padding: 30px;
        border-radius: 12px;
        margin: 30px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .healer-image {
        flex: 0 0 300px;
        border-radius: 12px;
        overflow: hidden;
    }
    .healer-image img {
        width: 100%;
        height: auto;
        border-radius: 12px;
    }
    .healer-content {
        flex: 1;
    }
    .healer-name {
        color: #8b6f47;
        font-size: 32px;
        font-weight: 600;
        margin-bottom: 5px;
    }
    .healer-title {
        color: #a0826d;
        font-size: 16px;
        font-style: italic;
        margin-bottom: 20px;
    }
    .healer-bio {
        color: #333;
        line-height: 1.8;
        margin: 15px 0;
        font-size: 15px;
    }
    .healer-specialty {
        background: #8b6f47;
        color: white;
        padding: 8px 15px;
        border-radius: 20px;
        display: inline-block;
        margin: 5px 5px 5px 0;
        font-size: 13px;
    }
    .contact-info {
        background: #f0ebe5;
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
    }
    .contact-link {
        color: #8b6f47;
        text-decoration: none;
        font-weight: 500;
    }
    .contact-link:hover {
        color: #6b5537;
        text-decoration: underline;
    }
    @media (max-width: 768px) {
        .healer-container {
            flex-direction: column;
        }
        .healer-image {
            flex: 0 0 auto;
            width: 100%;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🌺 Meet Our Wellness Practitioners")
st.markdown("*Honoring both ancestral wisdom and modern healing practices*")
st.markdown("---")

# Introduction
st.markdown("""
<div style='background: linear-gradient(135deg, #f9f7f4 0%, #ffffff 100%); 
            padding: 25px; border-radius: 12px; border-left: 4px solid #d4a574; margin-bottom: 40px;'>
    <p style='font-size: 18px; line-height: 1.8; color: #333; margin: 0;'>
        Our practitioners integrate traditional healing wisdom with contemporary therapeutic approaches, 
        creating spaces where Latinas can explore wellness practices that honor both their cultural roots 
        and modern needs. Each practitioner brings unique gifts while centering cultural competency, 
        community care, and holistic healing.
    </p>
</div>
""", unsafe_allow_html=True)

# Jackie Bravo
col1, col2 = st.columns([1, 2])

with col1:
    # Placeholder for Jackie's image
    st.image("/Users/purvamugdiya/Desktop/VEC/images/Jackie_image.png", use_column_width=True)

with col2:
    st.markdown("""
    <div class='healer-name'>Jackie Bravo</div>
    <div class='healer-title'>Mom, Registered Yoga Teacher 200, Photographer, Co-Founder</div>
    
    <div class='healer-bio'>
        <p>Jackie Bravo is a multifaceted wellness practitioner who brings together her roles as a mother, 
        certified yoga teacher, photographer, and co-founder of Sol Space Chicago. Her approach to healing 
        integrates movement, mindfulness, and creative expression.</p>
        <p>As a 200-hour Registered Yoga Teacher, Jackie creates accessible, heart-centered classes that 
        honor both traditional yogic wisdom and contemporary wellness practices. Her work emphasizes the 
        connection between body, mind, and spirit, making yoga accessible to practitioners of all levels.</p>
        <p>Through Sol Space Chicago, Jackie co-creates a welcoming community space where Latinas can explore 
        holistic wellness practices in an environment that honors their cultural identity and lived experiences.</p>
    </div>
    
    <div style='margin: 20px 0;'>
        <span class='healer-specialty'>🧘‍♀️ Yoga Instruction</span>
        <span class='healer-specialty'>📸 Photography</span>
        <span class='healer-specialty'>🌟 Community Building</span>
        <span class='healer-specialty'>💚 Mindfulness Practices</span>
    </div>
    
    <div class='contact-info'>
        <p style='margin: 5px 0;'><strong>📞 Phone:</strong> <a href='tel:773-633-9294' class='contact-link'>773-633-9294</a></p>
        <p style='margin: 5px 0;'><strong>📧 Email:</strong> <a href='mailto:jackie@solspacechicago.org' class='contact-link'>jackie@solspacechicago.org</a></p>
        <p style='margin: 5px 0;'><strong>🌐 Website:</strong> <a href='https://solspacechicago.org' target='_blank' class='contact-link'>solspacechicago.org</a></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Luz Alondra
col1, col2 = st.columns([1, 2])

with col1:
    # Placeholder for Luz's image
    st.image("/Users/purvamugdiya/Desktop/VEC/images/Luz_image.png", use_column_width=True)

with col2:
    st.markdown("""
    <div class='healer-name'>Luz Alondra</div>
    <div class='healer-title'>She/Her/Ella • Founder & CEO, Grounded Goddess</div>
    
    <div class='healer-bio'>
        <p>Luz is a 200-hour certified yoga teacher, sound healing practitioner, and cycle syncing educator 
        devoted to holding grounded, intuitive spaces for embodied healing. As the Founder and CEO of 
        Grounded Goddess, she believes movement, rest, and ritual are for every body, and that reconnecting 
        with our natural rhythms is a powerful act of care and resistance.</p>
        <p>Her philosophy centers on the belief that reconnecting with our natural rhythms—our breath, our 
        cycles, the moon—is a powerful act of self-care and resistance. Through her work, Luz creates spaces 
        where individuals can slow down, listen to their bodies, and honor their innate wisdom.</p>
        <p>Through sound baths, moon circles, cycle syncing workshops, and yoga classes, Luz offers 
        beginner-friendly experiences that blend structure with softness. Her teachings honor both ancient 
        wisdom and modern understanding, creating a bridge between traditional practices and contemporary needs.</p>
    </div>
    
    <div style='margin: 20px 0;'>
        <span class='healer-specialty'>🧘‍♀️ Yoga (200-Hour Certified)</span>
        <span class='healer-specialty'>🔮 Sound Healing</span>
        <span class='healer-specialty'>🌙 Moon Circles</span>
        <span class='healer-specialty'>🌸 Cycle Syncing</span>
        <span class='healer-specialty'>🎵 Sound Baths</span>
        <span class='healer-specialty'>💫 Embodied Healing</span>
    </div>
    
    <div class='contact-info'>
        <p style='margin: 5px 0;'><strong>🌐 Instagram:</strong> <a href='https://instagram.com/thegroundedgoddess' target='_blank' class='contact-link'>@thegroundedgoddess</a></p>
        <p style='margin: 5px 0;'><strong>📍 Location:</strong> Available for sessions and workshops</p>
    </div>
    """, unsafe_allow_html=True)

# Philosophy Section
st.markdown("---")
st.markdown("### 🌿 Our Healing Philosophy")

st.markdown("""
<div style='background: #f9f7f4; padding: 25px; border-radius: 12px; margin: 20px 0;'>
    <p style='font-size: 16px; line-height: 1.8; color: #333;'>
        We believe healing happens at the intersection of ancestral wisdom and modern practices. 
        Our practitioners honor traditional healing methods—curanderismo, herbal medicine, prayer, 
        and indigenous practices—while integrating evidence-based approaches like trauma-informed care, 
        mindfulness, and somatic therapies.
    </p>
    <p style='font-size: 16px; line-height: 1.8; color: #333; margin-top: 15px;'>
        This integration creates a holistic approach that respects cultural identity while offering 
        contemporary tools for healing. We center community care, recognizing that individual wellness 
        is deeply connected to collective wellbeing.
    </p>
</div>
""", unsafe_allow_html=True)

# Call to Action
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 40px 30px; background: linear-gradient(135deg, #8b6f47 0%, #a0826d 100%); 
            border-radius: 12px; color: white; margin: 30px 0;'>
    <h3 style='margin-bottom: 15px; font-size: 28px;'>✨ Ready to Begin Your Healing Journey?</h3>
    <p style='font-size: 18px; margin-bottom: 25px;'>
        Share your story anonymously and discover support options that resonate with your needs. 
        Your voice matters, and you deserve culturally-grounded care.
    </p>
</div>
""", unsafe_allow_html=True)

# Link to Share Story
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("✍️ Share Your Story", use_container_width=True, type="primary"):
        st.switch_page("pages/1_Share_Story.py")