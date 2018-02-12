import smtplib, os 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
def email2me(subject,msg,attach=None):
    
    server = smtplib.SMTP('smtp.naver.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("endeavor4_a1@naver.com", 'kutkd1954201767')
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From']= "endeavor4_a1@naver.com"
    message['To'] = "endeavor4_a1@naver.com"
    part1 = MIMEText(msg,_charset = 'utf-8')
    message.attach(part1)
    if attach != None:
        part = MIMEBase('application','octet-stream')
        part.set_payload(open(attach,'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=%s'%os.path.basename(attach))
        message.attach(part)
    server.sendmail(message['From'], message['To'], message.as_string())
    server.quit()

def email2u(subject,msg,attach=None):
    
    server = smtplib.SMTP('smtp.naver.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("endeavor4_a1@naver.com", 'kutkd1954201767')
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From']= "endeavor4_a1@naver.com"
    message['To'] = "mobbom@naver.com"
    part1 = MIMEText(msg,_charset = 'utf-8')
    message.attach(part1)
    if attach != None:
        part = MIMEBase('application','octet-stream')
        part.set_payload(open(attach,'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=%s'%os.path.basename(attach))
        message.attach(part)
    server.sendmail(message['From'], message['To'], message.as_string())
    server.quit()
