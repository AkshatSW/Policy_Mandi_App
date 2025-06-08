from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
import csv
import os
from dotenv import load_dotenv

# Load .env only if exists, useful for local dev
if os.path.exists('.env'):
    load_dotenv('.env')

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html', page_title="Home")

@app.route('/about')
def about():
    return render_template('aboutus.html', page_title="About Us")

@app.route('/Contact')
def Contact():
    return render_template('Contact.html', page_title="Contact Us")

@app.route('/careers')
def careers():
    return render_template('careers.html', page_title="Careers")

@app.route('/webmail')
def login():
    return redirect(
        "https://p3plzcpnl505166.prod.phx3.secureserver.net:2096/cpsess2752899820/3rdparty/roundcube/?_task=mail&_mbox=INBOX", 
        code=302
    )

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')

    # Read from environment variables (configured in cPanel > Setup Python App)
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = int(os.environ.get('SMTP_PORT', 465))
    sender_email = os.environ.get('SENDER_EMAIL')
    sender_password = os.environ.get('SENDER_PASSWORD')
    recipient_email = os.environ.get('RECIPIENT_EMAIL')

    subject = "New Contact Form Submission"
    body = f"Name: {name}\nPhone: {phone}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        # Save to CSV
        with open('contacts.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if os.stat('contacts.csv').st_size == 0:
                writer.writerow(['Name', 'Phone'])
            writer.writerow([name, phone])

        print("Connecting to SMTP server...")
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.set_debuglevel(1)
            server.login(sender_email, sender_password)
            print("Login successful. Sending email...")
            server.send_message(msg)
            print("Email sent successfully.")

        return {"status": "success", "message": "Form submitted and email sent!"}
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"status": "error", "message": f"Failed to send: {str(e)}"}
    
@app.context_processor
def inject_request():
    return dict(request=request)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
