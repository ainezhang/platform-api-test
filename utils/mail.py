"""发送邮件等通知"""
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# def send_mail(subject, body, receiver: list, attachments=None):
#     msg = MIMEMultipart()
#     msg.attach(MIMEText(body, 'html', 'utf-8'))
#     if attachments:
#         for file_path in attachments: