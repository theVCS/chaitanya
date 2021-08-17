import smtplib as s
import pandas as pd

def send_mail(subject, body, emailList):
    ob=s.SMTP("smtp.gmail.com", 587)
    ob.starttls()
    dt = pd.read_csv("accounts/credentials.csv")
    email = dt.email[0]
    password = dt.password[0]
    ob.login(email, password)
    message = "Subject:{}\n\n{}".format(subject,body)
    ob.sendmail(email, emailList, message)
