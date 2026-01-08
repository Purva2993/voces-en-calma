# 🚀 Deployment Guide - Voces en Calma

## Pre-Deployment Checklist

### ✅ Files to Create/Verify

- [ ] `README.md` - Project documentation
- [ ] `.gitignore` - Exclude unnecessary files
- [ ] `requirements.txt` - All dependencies listed
- [ ] `.streamlit/config.toml` - Streamlit configuration
- [ ] All Python files in proper structure

### ✅ Testing Checklist

- [ ] Test all pages work locally
- [ ] Test language toggle (English/Spanish)
- [ ] Test story submission flow
- [ ] Test admin login
- [ ] Test data export features
- [ ] Test on mobile device (responsive)
- [ ] Test emotion detection
- [ ] Test trend analysis charts

---

## Step-by-Step Deployment

### Step 1: Prepare GitHub Repository

1. **Create a new repository on GitHub**
   - Go to https://github.com/new
   - Name: `voces-en-calma`
   - Description: "Privacy-first storytelling platform for Latina wellness"
   - Public or Private (your choice)
   - Don't initialize with README (we have one)

2. **Initialize Git locally** (if not already done)
```bash
cd /path/to/voces-en-calma
git init
git add .
git commit -m "Initial commit: Voces en Calma v1.0"
```

3. **Connect to GitHub**
```bash
git remote add origin https://github.com/YOUR_USERNAME/voces-en-calma.git
git branch -M main
git push -u origin main
```

---

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io
   - Sign in with GitHub

2. **Create New App**
   - Click "New app" button
   - Select your repository: `YOUR_USERNAME/voces-en-calma`
   - Branch: `main`
   - Main file path: `Home.py`
   - App URL: Choose a custom subdomain (e.g., `voces-en-calma`)

3. **Configure Advanced Settings** (Optional)
   - Python version: 3.11
   - Click "Deploy!"

4. **Wait for Deployment**
   - Usually takes 2-5 minutes
   - Watch the logs for any errors

5. **Test Your Deployed App**
   - Visit your app URL
   - Test all features
   - Try both languages
   - Test admin login

---

### Step 3: Post-Deployment

1. **Update README.md**
   - Add your live app URL
   - Update screenshots if needed

2. **Test Everything**
   - [ ] Home page loads
   - [ ] Language toggle works
   - [ ] Story submission works
   - [ ] Healers page displays
   - [ ] Admin login works
   - [ ] Dashboard loads with data
   - [ ] Charts render correctly
   - [ ] Data export works
   - [ ] Mobile responsive

3. **Share Your App**
   - Copy the URL
   - Share with stakeholders
   - Add to your portfolio
   - Update resume/LinkedIn

---

## Troubleshooting Common Issues

### Issue: "Module not found"
**Solution:** Check `requirements.txt` has all dependencies
```bash
pip freeze > requirements.txt
```

### Issue: "Database not found"
**Solution:** Database is created automatically on first run. Make sure `data/` folder exists.

### Issue: "Page not loading"
**Solution:** Check Streamlit Cloud logs for errors. Ensure `Home.py` is in root directory.

### Issue: "Charts not rendering"
**Solution:** Verify Plotly is in requirements.txt: `plotly==5.18.0`

### Issue: "Admin login not working"
**Solution:** Check `utils/auth.py` credentials are correct.

---

## Environment Variables (if needed)

If you want to use secrets (for production):

1. **Create `.streamlit/secrets.toml`** (locally, don't commit)
```toml
[admin]
password = "your_secure_password"

[contact]
email = "support@yourdomain.com"
phone = "+1-555-123-4567"
```

2. **In Streamlit Cloud:**
   - Go to App Settings → Secrets
   - Paste your secrets

3. **Update code to use secrets:**
```python
import streamlit as st
admin_password = st.secrets["admin"]["password"]
```

---

## Performance Optimization

### For Large Datasets
- Consider PostgreSQL instead of SQLite
- Add caching with `@st.cache_data`
- Implement pagination for large tables

### For Faster Load Times
- Optimize images
- Minimize CSS
- Use lazy loading for charts

---

## Monitoring & Maintenance

### After Deployment:
- [ ] Monitor app analytics in Streamlit Cloud
- [ ] Check error logs regularly
- [ ] Update dependencies periodically
- [ ] Backup database regularly
- [ ] Monitor user feedback

### Updating Your App:
```bash
# Make changes locally
git add .
git commit -m "Update: description of changes"
git push origin main

# Streamlit Cloud auto-deploys on push!
```

---

## Custom Domain (Optional)

To use your own domain:

1. **In Streamlit Cloud:**
   - Go to App Settings → General
   - Add custom domain

2. **In your DNS provider:**
   - Add CNAME record pointing to Streamlit

---

## Backup Strategy

### Database Backup
```bash
# Create backup
cp data/voces.db data/voces_backup_$(date +%Y%m%d).db

# Schedule automatic backups (Linux/Mac)
crontab -e
# Add: 0 2 * * * cp /path/to/voces.db /path/to/backup/
```

---

## Support & Resources

- **Streamlit Docs:** https://docs.streamlit.io
- **Streamlit Community:** https://discuss.streamlit.io
- **GitHub Issues:** Create issues in your repo
- **Contact:** Your email/support channel

---

**🎉 Congratulations on deploying Voces en Calma!**