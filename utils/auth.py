"""
Authentication and Authorization Module
Handles admin login and role-based access control
"""

import streamlit as st

# Admin credentials (in production, use environment variables or database)
ADMIN_CREDENTIALS = {
    "admin": "voces2024",  # Change this to a secure password
    "practitioner1": "wellness123",
    "practitioner2": "healing456"
}

# Contact information
CONTACT_INFO = {
    "email": "support@vocesencalma.org",
    "phone": "+1 (555) 123-4567",
    "hours": "Monday - Friday, 9 AM - 5 PM PST"
}


def check_admin_access():
    """
    Check if user has admin/practitioner access
    Returns True if authenticated, False otherwise
    """
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        username = st.session_state.get("username", "")
        password = st.session_state.get("password", "")
        
        if username in ADMIN_CREDENTIALS and ADMIN_CREDENTIALS[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["user_role"] = "admin"
            st.session_state["current_user"] = username
            # Don't store password
            if "password" in st.session_state:
                del st.session_state["password"]
        else:
            st.session_state["authenticated"] = False
            st.session_state["login_error"] = True

    # Check if already authenticated
    if st.session_state.get("authenticated", False):
        return True
    
    # Show login form
    st.markdown("## 🔐 Practitioner Login")
    st.markdown("*This dashboard is for Latina wellness practitioners only.*")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.text_input(
            "Username", 
            key="username",
            placeholder="Enter your username"
        )
        
        st.text_input(
            "Password", 
            type="password", 
            key="password",
            placeholder="Enter your password"
        )
        
        if st.session_state.get("login_error", False):
            st.error("😕 Invalid username or password. Please try again.")
            st.session_state["login_error"] = False
        
        st.markdown("---")
        
        if st.button("🔓 Login", type="primary", use_container_width=True):
            password_entered()
            st.rerun()
        
        st.markdown("---")
        
        # Help section
        with st.expander("💡 Need Help?"):
            st.markdown(f"""
            **Forgot your credentials?**
            
            Contact us:
            - 📧 Email: {CONTACT_INFO['email']}
            - 📞 Phone: {CONTACT_INFO['phone']}
            - 🕐 Hours: {CONTACT_INFO['hours']}
            """)
    
    return False


def logout():
    """
    Logout current user
    """
    st.session_state["authenticated"] = False
    st.session_state["user_role"] = None
    st.session_state["current_user"] = None


def get_current_user():
    """
    Get current logged in user
    """
    return st.session_state.get("current_user", None)


def is_authenticated():
    """
    Check if user is authenticated
    """
    return st.session_state.get("authenticated", False)


def get_contact_info():
    """
    Get contact information
    """
    return CONTACT_INFO