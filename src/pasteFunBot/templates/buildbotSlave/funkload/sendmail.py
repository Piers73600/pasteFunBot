import sys
import smtplib
from email.MIMEText import MIMEText

def sendTextMail(to,subject,text):
    sender = "stpda-server@makina-corpus.com"
    mail = MIMEText(text)
    mail['From'] = sender
    mail['Subject'] = subject
    mail['To'] = to
    smtp = smtplib.SMTP()
    smtp.connect()
    smtp.sendmail(sender, [to], mail.as_string())
    smtp.close()
 
if __name__ == "__main__":
    l = sys.argv[1:]
    sendTextMail(l[0],l[1], l[2])
