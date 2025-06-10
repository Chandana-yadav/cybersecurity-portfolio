# 🛡️ Phishing & Vishing Defense Capstone – Human-Centric Cybersecurity Simulation

**Capstone Project** | Yeshiva University | Aug–Dec 2024  

---

## 🎯 Objective

This project focuses on combating social engineering through a multi-layered framework of **phishing and vishing simulations**, **behavioral risk scoring**, and **awareness training tools**. We replicated real-world attack vectors to assess and improve human defense mechanisms.

---

## 🧩 Components

### 📧 Phishing Simulation (`/phishing_simulator`)
- Python-based email sender mimicking Google, Facebook, Amazon
- Tracks open, click-through, and submission behavior
- Used for training and risk profiling

### 📞 Vishing Bot (`/vishing_bot`)
- Voice phishing simulation using **Twilio API**
- Scripted urgent call scenarios (“Your bank account is locked”)
- Collected user response metrics (e.g., panic triggers)

### 🌐 Awareness Portal (`/awareness_portal`)
- HTML/CSS site with phishing quizzes, modules, and a reporting tool
- Interactive learning experience to boost detection skills

### 🔍 Risk Scoring (`/risk_scoring_model`)
- Persona-based behavioral analysis using Excel and survey data
- Risk scoring framework to prioritize follow-up training

### 🧩 Chrome Extension (`/browser_extension`)
- Warns users when they visit known phishing sites
- Manual “check this site” button for real-time awareness

---

## 📊 Key Results

- 📉 improved participant detection rates from 55% to 85% post-training.
- 🎯 Created vishing simulations that generated 70+ unique data points
- 🧠 Developed risk scores for user personas across departments
- 🔁 Designed scalable SOC workflows for phishing detection and triage

---

## 🛠️ Tech Stack

- Python · Flask · JavaScript · HTML/CSS
- Twilio API · Excel · Matplotlib · Chrome Extensions (Manifest V3)

---

## 🚀 How to Use

1. Clone repo and explore folders by use case
2. Run phishing simulator via Python SMTP setup (see README in `/phishing_simulator`)
3. Deploy vishing bot via Twilio (setup instructions in `/vishing_bot`)
4. Open awareness portal locally or host on a web server
5. Load Chrome extension from `/browser_extension` using `chrome://extensions`

---

## 📁 Project Artifacts

- 📽️ [Demo Video](https://1drv.ms/v/c/754c82fbaed9c76f/EU3AcTGy-CJGgJU2eL2NTlIBJiWMNtdi1AwEmG2Eh6duGg?e=khwZVY)  
- 📑 Final Report + Presentation (`/docs/`)  
- 📊 Risk Persona Models (Excel)

---

## 👥 Authors

- Chandana Yadav Datti  
- Ravi Charan Teja Boddeti  
- Vinay Kumar
- Komali Ala
- Vamsi Krishna 

---

## 🔐 Why This Matters

Human error is the #1 cyber vulnerability. This project demonstrates a scalable, behavioral-first approach to training users against social engineering tactics like phishing and vishing.

