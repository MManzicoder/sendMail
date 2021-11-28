import smtplib;
import os;
EMAIL_ADRESS_CONFIG = os.environ.get("EMAIL_User_Name")
password = os.environ.get("Email_Pass")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADRESS_CONFIG, password)

    subject = "Networking SMTP Assignment"
    body = """Hello sir this is mail transferring with Python using smtplib. 
    \nHere is the link of codes on github https://github.com/MManzicoder/sendMail \n 
    Have a good day!."""
    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADRESS_CONFIG, "gbaziramwabo@gmail.com", msg)
