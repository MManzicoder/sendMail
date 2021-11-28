import smtplib;
import os;
userName = os.environ.get("EMAIL_User_Name")
password = os.environ.get("Email_Pass")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(userName, password)

    subject = "Email send testing!!!"
    body = "Hi this is mail transferring with Python"
    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(userName, "mmanzicder@gmail.com", msg)
