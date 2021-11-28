import smtplib;
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login("mmanzicder@gmail.com", "Muman123@!")

    subject = "Email send testing!!!"
    body = "Hi this is mail transferring with Python"
    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail("mmanzicder@gmail.com", "mmanzicder@gmail.com", msg)
