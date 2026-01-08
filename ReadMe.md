# 🕊️ Voces en Calma

**A privacy-first storytelling platform where community members anonymously share stress experiences and connect with Latina wellness practitioners who blend ancestral healing with modern therapeutic approaches.**

![Voces en Calma](https://img.shields.io/badge/Status-Live-success)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29-red)

## 🌟 Features

### For Community Members
- **Anonymous Storytelling** - Share stress experiences without personal identifiers
- **Support Matching** - Connect with appropriate wellness resources
- **Bilingual Interface** - Full English/Spanish support
- **Privacy-First Design** - No IP tracking, no personal data collection

### For Wellness Practitioners
- **Insights Dashboard** - Emotion analytics and trends
- **Community Patterns** - Understand what support is needed most
- **External Sentiment Analysis** - Compare with broader Latina wellness conversations
- **Data Export** - Download reports and insights

### Technical Features
- **NLP Emotion Detection** - Automatic emotional theme tagging using VADER + keyword analysis
- **Real-time Analytics** - Interactive visualizations with Plotly
- **Trend Analysis** - Track emotion patterns over time
- **Secure Authentication** - Role-based access for practitioners
- **Responsive Design** - Mobile-friendly with smooth animations

## 🚀 Live Demo

[View Live Application](#) *(Add your Streamlit Cloud URL here)*

**Demo Credentials:**
- Username: `admin`
- Password: `voces2024`

## 📸 Screenshots

### Community Portal
![Home Page](screenshots/home.png)
![Share Story](screenshots/share_story.png)

### Practitioner Dashboard
![Insights Dashboard](screenshots/insights.png)
![Emotion Trends](screenshots/trends.png)

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.11
- **Database**: SQLite
- **NLP**: VADER Sentiment + Custom Emotion Classification
- **Visualizations**: Plotly, Plotly Express
- **Styling**: Custom CSS with animations
- **Deployment**: Streamlit Cloud

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip
- virtualenv (recommended)

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/voces-en-calma.git
cd voces-en-calma
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run Home.py
```

5. **Access the app**
```
http://localhost:8501
```

## 📁 Project Structure

```
voces-en-calma/
├── Home.py                      # Main application entry
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── .streamlit/
│   └── config.toml             # Streamlit configuration
├── pages/
│   ├── 1_Share_Story.py        # Story submission page
│   ├── 2_Healers.py            # Practitioner directory
│   └── 3_Insights.py           # Analytics dashboard (admin)
├── utils/
│   ├── __init__.py
│   ├── database.py             # Database operations
│   ├── nlp_model.py            # Emotion detection
│   ├── privacy.py              # Privacy & sanitization
│   ├── web_scraper.py          # External sentiment collection
│   ├── export_data.py          # Data export functions
│   ├── translations.py         # Bilingual support
│   ├── ui_helpers.py           # UI components & animations
│   └── auth.py                 # Authentication
├── data/
│   └── voces.db                # SQLite database (auto-created)
└── screenshots/                # Application screenshots
```

## 🔧 Configuration

### Admin Credentials
Edit `utils/auth.py` to add/modify admin accounts:

```python
ADMIN_CREDENTIALS = {
    "admin": "voces2024",
    "practitioner1": "wellness123"
}
```

### Contact Information
Update contact details in `utils/auth.py`:

```python
CONTACT_INFO = {
    "email": "support@vocesencalma.org",
    "phone": "+1 (555) 123-4567",
    "hours": "Monday - Friday, 9 AM - 5 PM PST"
}
```

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. **Push to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Click "New app"**

4. **Configure deployment:**
   - Repository: `yourusername/voces-en-calma`
   - Branch: `main`
   - Main file: `Home.py`

5. **Deploy!**

## 📊 Key Metrics

- **22 Stories** shared by community members
- **10 External Sources** analyzed
- **9 Emotion Categories** detected
- **9 Support Types** available
- **2 Languages** supported

## 🔐 Privacy & Security

- ✅ No personal identifiers stored
- ✅ No IP address tracking
- ✅ Anonymous story submission
- ✅ Privacy-first data sanitization
- ✅ Secure practitioner authentication
- ✅ GDPR-compliant design

## 🎨 Design Philosophy

This platform honors **ancestral wisdom** (curanderismo, prayer, herbal remedies) while embracing **modern therapeutic approaches** (trauma-informed care, mindfulness, evidence-based practices).

**Core Values:**
- Community healing
- Cultural authenticity
- Privacy & dignity
- Accessibility
- Bilingual support

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributors

**Purva Mugdiya** - *Lead Developer*
- [LinkedIn](https://linkedin.com/in/yourprofile)
- [Portfolio](https://yourportfolio.com)

## 🙏 Acknowledgments

- Latina wellness practitioners who inspired this work
- The community members who share their stories
- Anthropic's Claude for development assistance

## 📧 Contact

For questions, feedback, or support:
- Email: support@vocesencalma.org
- Phone: +1 (555) 123-4567
