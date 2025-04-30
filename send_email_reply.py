from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

def send_email_reply(service, original_message, reply_text):
    """
    Gelen e-postaya yanıt olarak reply_text içeriğini gönderir.
    """
    headers = original_message['payload']['headers']
    recipient = next(h['value'] for h in headers if h['name'] == 'From')
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(No Subject)")

    message = MIMEText(reply_text)
    message['to'] = recipient
    message['subject'] = f"Re: {subject}"

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw_message}

    service.users().messages().send(userId='me', body=body).execute()
    print(f"✅ Cevap e-posta olarak gönderildi → {recipient}")
