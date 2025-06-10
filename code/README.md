# 🎯 Phishing & Vishing Simulation Scripts

This folder contains automation scripts used in our cybersecurity capstone to simulate real-world **social engineering attacks**:

- 📧 Phishing Email Simulator (Python-based email sender)
- 📞 Vishing Bot (Voice call simulation using Twilio)

These tools were designed to test user awareness and response behavior in a controlled training environment.

---

## 📧 Phishing Email Simulator

### ➤ File: `send_phishing_emails.py`

Simulates targeted phishing emails by spoofing well-known services (e.g., Google, Amazon, Facebook) and sending them via SMTP.

#### ✅ Features
- Spoofed sender name and fake domain links
- HTML email body with click-through tracking via redirect links
- Supports multiple recipients

#### 🛠 Technologies
- Python
- `smtplib`, `ssl`, `email.mime`
- HTML templates (optional)

#### 🧪 Setup Instructions
1. Use a Gmail or SMTP email account for testing.
2. Enable [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) or allow less secure apps.
3. Edit the script to include:
   - Your sender email + app password
   - Recipient email list
   - Custom phishing message or HTML
4. Run the script:
```bash
python send_phishing_emails.py
