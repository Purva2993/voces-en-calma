"""
Share Story Page - Anonymous story submission form
"""

import streamlit as st
from utils.database import save_story, update_story_emotion
from utils.privacy import (
    sanitize_text, 
    check_for_names, 
    validate_story_length, 
    get_privacy_notice,
    get_consent_text
)
from utils.nlp_model import detect_emotion
from utils.translations import get_text, get_language_toggle, set_language
from utils.ui_helpers import add_custom_css, show_loading

# Page configuration - MUST be first
st.set_page_config(
    page_title="Share Your Story - Voces en Calma",
    page_icon="📝",
    layout="centered"
)

# Add custom CSS
add_custom_css()

# Get current language (set globally in Home.py)
lang = get_language_toggle()

# Header
st.title(get_text('share_story_title', lang))
st.markdown(f"### {get_text('share_story_subtitle', lang)}")

# Privacy notice - prominent display
with st.expander(get_text('privacy_header', lang), expanded=True):
    st.markdown(get_privacy_notice(lang))

# Support type options - translated
SUPPORT_OPTIONS = [
    get_text('journaling', lang),
    get_text('group_circles', lang),
    get_text('one_on_one', lang),
    get_text('art_therapy', lang),
    get_text('bodywork', lang),
    get_text('spiritual', lang),
    get_text('self_study', lang),
    get_text('somatic', lang),
    get_text('herbal', lang)
]

# Initialize session state for form
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# Main form
if not st.session_state.form_submitted:
    
    st.markdown(f"### {get_text('tell_us_story', lang)}")
    st.markdown(get_text('story_prompt', lang))
    
    # Story text input
    story_text = st.text_area(
        get_text('tell_us_story', lang) + " (anonymous):",
        placeholder=get_text('story_placeholder', lang),
        height=200,
        max_chars=700,
        help="Share what feels right for you. No pressure to be perfect—just honest."
    )
    
    # Character counter
    char_count = len(story_text)
    if char_count < 20:
        st.caption(get_text('character_count_min', lang, count=char_count))
    elif char_count > 600:
        st.caption(get_text('character_count_close', lang, count=char_count))
    else:
        st.caption(get_text('character_count_ok', lang, count=char_count))
     
    # Support preferences
    st.markdown(f"### {get_text('support_types', lang)}")
    st.markdown(get_text('support_desc', lang))
    
    support_choices = st.multiselect(
        get_text('support_types', lang) + ":",
        options=SUPPORT_OPTIONS,
        help="These help practitioners understand what the community is seeking."
    )
     
    # Optional practitioner note
    st.markdown(f"### {get_text('anything_else', lang)}")
    practitioner_note = st.text_input(
        get_text('practitioner_note', lang),
        placeholder=get_text('practitioner_placeholder', lang),
        max_chars=300
    )
    
    # Consent
    consent = st.checkbox(get_text('consent_text', lang))
    
    # Submit button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submit_button = st.button(get_text('submit_button', lang), type="primary", use_container_width=True)
    
    # Process submission
    if submit_button:
        # Validation
        errors = []
        
        if not story_text.strip():
            errors.append("Please share your story before submitting.")
        
        if not support_choices:
            errors.append("Please select at least one type of support you're open to.")
        
        if not consent:
            errors.append("Please acknowledge the consent statement.")
        
        # Validate story length
        is_valid_length, length_message = validate_story_length(story_text)
        if not is_valid_length:
            errors.append(length_message)
        
        # Check for names (warning only)
        has_name, name_warnings = check_for_names(story_text)
        
        if errors:
            for error in errors:
                st.error(error)
        else:
            # Sanitize text
            cleaned_story, sanitize_warnings = sanitize_text(story_text)
            cleaned_note, note_warnings = sanitize_text(practitioner_note)
            
            # Show warnings if any personal info was removed
            if sanitize_warnings or note_warnings:
                st.warning("⚠️ We detected and removed some personal information to protect your privacy:")
                for warning in sanitize_warnings + note_warnings:
                    st.write(f"- {warning}")
            
            # Show name warning if detected
            if has_name:
                for warning in name_warnings:
                    st.warning(f"⚠️ {warning}")
                st.info("Your story will still be submitted, but consider if you've shared more than you intended.")
            
            # Save to database
            with show_loading("💫 Processing your story..."):
                story_id = save_story(
                    story_text=cleaned_story,
                    support_choices=support_choices,
                    practitioner_note=cleaned_note
                )
                
                if story_id:
                    # Detect emotion using NLP
                    emotion, confidence, all_emotions = detect_emotion(cleaned_story)
                    
                    # Update story with emotion label
                    update_story_emotion(story_id, emotion, confidence)
                    
                    # Store emotion info in session state for confirmation page
                    st.session_state.detected_emotion = emotion
                    st.session_state.emotion_confidence = confidence
                    
                    st.session_state.form_submitted = True
                    st.rerun()
                else:
                    st.error("Something went wrong. Please try again or contact support.")

else:
    # Success message after submission
    st.success(f"### {get_text('story_heard', lang)}")
    
    # Show detected emotion if available
    if 'detected_emotion' in st.session_state:
        emotion = st.session_state.detected_emotion
        confidence = st.session_state.emotion_confidence
        
        emotion_display = get_text(emotion, lang)
        
        st.info(get_text('detected_emotion', lang, emotion=emotion_display))
    
    st.markdown(get_text('thank_you', lang))

    
    col1, col2 = st.columns(2)
    with col1:
        if st.button(get_text('back_home', lang), use_container_width=True):
            st.session_state.form_submitted = False
            # Clear emotion data
            if 'detected_emotion' in st.session_state:
                del st.session_state.detected_emotion
            if 'emotion_confidence' in st.session_state:
                del st.session_state.emotion_confidence
    
    with col2:
        if st.button(get_text('share_another', lang), use_container_width=True):
            st.session_state.form_submitted = False
            # Clear emotion data
            if 'detected_emotion' in st.session_state:
                del st.session_state.detected_emotion
            if 'emotion_confidence' in st.session_state:
                del st.session_state.emotion_confidence
            st.rerun()