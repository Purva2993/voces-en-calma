"""
Privacy protection module for Voces en Calma
Sanitizes text to prevent accidental personal information sharing
"""

import re

def sanitize_text(text):
    """
    Remove potential personal identifiers from text
    Returns: (cleaned_text, warnings_list)
    """
    warnings = []
    cleaned = text
    
    # Detect and remove email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.search(email_pattern, cleaned):
        cleaned = re.sub(email_pattern, '[EMAIL REMOVED]', cleaned)
        warnings.append("Email address detected and removed")
    
    # Detect and remove phone numbers (various formats)
    phone_patterns = [
        r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',  # 123-456-7890 or 1234567890
        r'\b\(\d{3}\)\s*\d{3}[-.]?\d{4}\b',  # (123) 456-7890
        r'\b\d{3}\s\d{3}\s\d{4}\b'  # 123 456 7890
    ]
    for pattern in phone_patterns:
        if re.search(pattern, cleaned):
            cleaned = re.sub(pattern, '[PHONE REMOVED]', cleaned)
            warnings.append("Phone number detected and removed")
    
    # Detect potential street addresses (basic)
    address_pattern = r'\b\d+\s+[A-Za-z]+\s+(Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct)\b'
    if re.search(address_pattern, cleaned, re.IGNORECASE):
        cleaned = re.sub(address_pattern, '[ADDRESS REMOVED]', cleaned, flags=re.IGNORECASE)
        warnings.append("Street address detected and removed")
    
    # Detect social security numbers
    ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
    if re.search(ssn_pattern, cleaned):
        cleaned = re.sub(ssn_pattern, '[SSN REMOVED]', cleaned)
        warnings.append("Social security number detected and removed")
    
    return cleaned, warnings


def check_for_names(text):
    """
    Check if text might contain common names (warning, not removal)
    Returns: boolean and list of potential issues
    """
    warnings = []
    
    # Common name patterns - very basic check
    # In production, you'd use a name entity recognition model
    common_patterns = [
        r'\bmy name is\b',
        r'\bi am\s+[A-Z][a-z]+\b',
        r'\bcall me\s+[A-Z][a-z]+\b',
    ]
    
    for pattern in common_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            warnings.append("Text may contain a name. Consider rephrasing without identifying information.")
            return True, warnings
    
    return False, warnings


def validate_story_length(text, min_length=20, max_length=700):
    """
    Validate that story is within acceptable length
    Returns: (is_valid, message)
    """
    text_length = len(text.strip())
    
    if text_length < min_length:
        return False, f"Story is too short. Please write at least {min_length} characters."
    
    if text_length > max_length:
        return False, f"Story is too long. Please keep it under {max_length} characters."
    
    return True, "Story length is valid"


def get_privacy_notice(lang='en'):
    """Return the privacy notice text for display"""
    if lang == 'es':
        return """
        🔒 **Tu Privacidad es Sagrada**
        
        - No se recopilan nombres, correos electrónicos ni identificadores personales
        - No se rastrean direcciones IP ni datos de ubicación
        - Tu historia es completamente anónima
        - Solo almacenamos tus palabras y el apoyo que buscas
        
        Por favor evita incluir:
        - Tu nombre completo o el nombre de otra persona
        - Direcciones de correo electrónico o números de teléfono
        - Direcciones específicas de calles
        - Cualquier otra información identificable
        """
    else:
        return """
        🔒 **Your Privacy is Sacred**
        
        - No names, emails, or personal identifiers are collected
        - No IP addresses or location data are tracked
        - Your story is completely anonymous
        - We only store your words and the support you seek
        
        Please avoid including:
        - Your full name or anyone else's name
        - Email addresses or phone numbers
        - Specific street addresses
        - Any other identifying information
        """


def get_consent_text():
    """Return consent acknowledgment text"""
    return """
    By sharing your story, you acknowledge that:
    - Your anonymous story may be read by Latina wellness practitioners
    - Aggregated (not individual) insights will help shape community support offerings
    - Your story helps us understand what our community needs
    """