import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "madhavmenon2006@gmail.com"
receiver_email = "madhavmenon2006@gmail.com" 
app_password = "REDACTED" 

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "HELLOES"
body = "wsg gang"

msg.attach(MIMEText(body, "plain"))

try:
    print("[+] Connecting to SMTP server...")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print("[+] Email sent successfully!")
except Exception as e:
    print("[-] Error:", e)
