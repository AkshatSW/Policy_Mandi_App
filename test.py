import smtplib
from email.mime.text import MIMEText

# Email credentials and config
smtp_server = "policymandi.in"
smtp_port = 465
sender_email = "contact@policymandi.in"
sender_password = "PolicyMandi@123"
recipient_email = "akshatsrivastava200213@gmail.com"

# Email content
subject = "Test Email from GoDaddy SMTP"
body = "This is a test email sent via GoDaddy SMTP using Python."

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_email

try:
    print("Connecting to SMTP server...")
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)
        print("Login successful.")
        server.send_message(msg)
        print(f"Email sent successfully to {recipient_email}")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
