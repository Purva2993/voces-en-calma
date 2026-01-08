"""
UI Helper Functions
Loading animations, error handling, and UI improvements
"""

import streamlit as st
import time
from functools import wraps


def show_loading(message="Loading..."):
    """
    Show professional loading spinner with custom message and animation
    """
    return st.spinner(message)


def show_page_loader():
    """
    Show full-page loader animation
    """
    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
            <div class="skeleton" style="width: 100%; height: 100px; border-radius: 10px;"></div>
        </div>
    """, unsafe_allow_html=True)


def animate_metric(label, value, delta=None, icon="📊"):
    """
    Create an animated metric card with icon
    """
    st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #FAF6F1 0%, #F5EFE7 100%);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid rgba(212, 132, 110, 0.1);
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            animation: scaleIn 0.5s ease-out;
            transition: all 0.3s ease;
        " onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 16px rgba(0,0,0,0.12)';" 
           onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.04)';">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
            <div style="font-size: 0.9rem; font-weight: 600; color: #6B5B95; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">
                {label}
            </div>
            <div style="font-size: 2.2rem; font-weight: 700; color: #D4846E;">
                {value}
            </div>
            {f'<div style="font-size: 0.9rem; color: #8B9D83; margin-top: 0.5rem;">{delta}</div>' if delta else ''}
        </div>
    """, unsafe_allow_html=True)


def safe_execute(func, error_message="An error occurred", show_error=True):
    """
    Safely execute a function with error handling
    """
    try:
        return func()
    except Exception as e:
        if show_error:
            st.error(f"{error_message}: {str(e)}")
        print(f"Error in {func.__name__}: {e}")
        return None


def with_loading(message="Processing..."):
    """
    Decorator to add loading spinner to functions
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with st.spinner(message):
                return func(*args, **kwargs)
        return wrapper
    return decorator


def show_success_message(message, duration=3):
    """
    Show temporary success message
    """
    success_placeholder = st.empty()
    success_placeholder.success(message)
    time.sleep(duration)
    success_placeholder.empty()


def show_error_message(message, details=None):
    """
    Show error message with optional details
    """
    st.error(message)
    if details:
        with st.expander("Show details"):
            st.code(details)


def validate_required_fields(fields_dict):
    """
    Validate required fields
    Returns: (is_valid, error_messages)
    """
    errors = []
    for field_name, field_value in fields_dict.items():
        if not field_value or (isinstance(field_value, str) and not field_value.strip()):
            errors.append(f"{field_name} is required")
    
    return len(errors) == 0, errors


def create_metric_card(label, value, delta=None, help_text=None):
    """
    Create a styled metric card
    """
    return st.metric(
        label=label,
        value=value,
        delta=delta,
        help=help_text
    )


def add_custom_css():
    """
    Add custom CSS for better mobile responsiveness, animations, and professional polish
    """
    st.markdown("""
        <style>
        /* Import Google Fonts for better typography */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        /* Global Styles */
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Smooth page transitions */
        .main {
            animation: fadeIn 0.5s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Better mobile responsiveness */
        @media (max-width: 768px) {
            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 2rem;
            }
            
            h1 {
                font-size: 1.8rem !important;
            }
            
            h2 {
                font-size: 1.4rem !important;
            }
            
            h3 {
                font-size: 1.2rem !important;
            }
        }
        
        /* Header animations */
        h1, h2, h3 {
            animation: slideInLeft 0.6s ease-out;
        }
        
        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        /* Card hover effects with elevation */
        .element-container {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .element-container:hover {
            transform: translateY(-2px);
        }
        
        /* Loading animation improvements */
        .stSpinner > div {
            border-color: #D4846E !important;
            border-width: 3px !important;
        }
        
        /* Button enhancements with ripple effect */
        .stButton > button {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border-radius: 8px;
            font-weight: 500;
            letter-spacing: 0.5px;
            position: relative;
            overflow: hidden;
        }
        
        .stButton > button:before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }
        
        .stButton > button:hover:before {
            width: 300px;
            height: 300px;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        }
        
        .stButton > button:active {
            transform: translateY(0);
        }
        
        /* Primary button styling */
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #D4846E 0%, #C17860 100%);
            border: none;
            color: white;
        }
        
        /* Download button styling */
        .stDownloadButton > button {
            background: linear-gradient(135deg, #8B9D83 0%, #7A8A75 100%);
            color: white;
            border: none;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        
        .stDownloadButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 16px rgba(139, 157, 131, 0.3);
        }
        
        /* Metric cards enhancement with gradient backgrounds */
        [data-testid="stMetric"] {
            background: linear-gradient(135deg, #FAF6F1 0%, #F5EFE7 100%);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid rgba(212, 132, 110, 0.1);
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            transition: all 0.3s ease;
            animation: scaleIn 0.5s ease-out;
        }
        
        [data-testid="stMetric"]:hover {
            box-shadow: 0 4px 16px rgba(0,0,0,0.08);
            transform: translateY(-2px);
        }
        
        @keyframes scaleIn {
            from {
                opacity: 0;
                transform: scale(0.9);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        
        [data-testid="stMetricValue"] {
            font-size: 2.2rem;
            font-weight: 700;
            color: #D4846E;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 0.9rem;
            font-weight: 600;
            color: #6B5B95;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Expander styling with smooth animations */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #F5EFE7 0%, #FAF6F1 100%);
            border-radius: 10px;
            padding: 1rem;
            border: 1px solid rgba(212, 132, 110, 0.2);
            transition: all 0.3s ease;
            font-weight: 600;
        }
        
        .streamlit-expanderHeader:hover {
            background: linear-gradient(135deg, #F5EFE7 0%, #EFE5D7 100%);
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            transform: translateX(4px);
        }
        
        /* Text input and text area enhancements */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            border-radius: 8px;
            border: 2px solid #F5EFE7;
            transition: all 0.3s ease;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: #D4846E;
            box-shadow: 0 0 0 3px rgba(212, 132, 110, 0.1);
        }
        
        /* Selectbox and multiselect styling */
        .stSelectbox > div > div,
        .stMultiSelect > div > div {
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        
        /* Info, success, warning, error boxes */
        .stAlert {
            border-radius: 10px;
            border: none;
            animation: slideInRight 0.5s ease-out;
        }
        
        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        /* Plotly chart container enhancements */
        .js-plotly-plot {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }
        
        .js-plotly-plot:hover {
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        }
        
        /* Dataframe styling */
        .stDataFrame {
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }
        
        /* Sidebar enhancements */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #FAF6F1 0%, #F5EFE7 100%);
        }
        
        [data-testid="stSidebar"] .stButton > button {
            width: 100%;
            border-radius: 8px;
        }
        
        /* Horizontal rule styling */
        hr {
            margin: 2rem 0;
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, #D4846E, transparent);
            opacity: 0.3;
        }
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px 8px 0 0;
            padding: 12px 24px;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(212, 132, 110, 0.1);
        }
        
        /* Progress bar styling */
        .stProgress > div > div > div {
            background: linear-gradient(90deg, #D4846E, #C17860);
            border-radius: 10px;
        }
        
        /* Checkbox and radio styling */
        .stCheckbox, .stRadio {
            transition: all 0.3s ease;
        }
        
        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #F5EFE7;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #D4846E, #C17860);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(180deg, #C17860, #B06852);
        }
        
        /* Fade in animation for charts */
        .plot-container {
            animation: fadeInUp 0.6s ease-out;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Pulse animation for important elements */
        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.8;
            }
        }
        
        .pulse {
            animation: pulse 2s ease-in-out infinite;
        }
        
        /* Loading skeleton animation */
        @keyframes shimmer {
            0% {
                background-position: -1000px 0;
            }
            100% {
                background-position: 1000px 0;
            }
        }
        
        .skeleton {
            animation: shimmer 2s infinite;
            background: linear-gradient(
                to right,
                #F5EFE7 0%,
                #EFE5D7 20%,
                #F5EFE7 40%,
                #F5EFE7 100%
            );
            background-size: 1000px 100%;
        }
        </style>
    """, unsafe_allow_html=True)


def show_empty_state(title, message, icon="📭"):
    """
    Show empty state with icon and message
    """
    st.markdown(f"""
        <div style="text-align: center; padding: 3rem; color: #8B9D83;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">{icon}</div>
            <h3>{title}</h3>
            <p>{message}</p>
        </div>
    """, unsafe_allow_html=True)


def progress_bar(current, total, label="Progress"):
    """
    Show progress bar
    """
    progress = current / total if total > 0 else 0
    st.progress(progress, text=f"{label}: {current}/{total}")


def confirmation_dialog(message, key="confirm"):
    """
    Show confirmation dialog
    Returns: True if confirmed
    """
    st.warning(message)
    col1, col2 = st.columns(2)
    
    with col1:
        confirm = st.button("✅ Confirm", key=f"{key}_yes", use_container_width=True)
    with col2:
        cancel = st.button("❌ Cancel", key=f"{key}_no", use_container_width=True)
    
    return confirm


def format_number(num, precision=0):
    """
    Format number with commas
    """
    if precision == 0:
        return f"{int(num):,}"
    else:
        return f"{num:,.{precision}f}"


def truncate_text(text, max_length=100, suffix="..."):
    """
    Truncate text to max length
    """
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(' ', 1)[0] + suffix