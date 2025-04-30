from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import os

SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.send'
]



def get_emails(max_count=5):
    """
    Gelen kutusundan en fazla max_count kadar e-posta çeker ve içerik + metadata döner.
    """
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', maxResults=max_count).execute()
    messages = results.get('messages', [])

    if not messages:
        print("Gelen kutusunda e-posta yok.")
        return []

    email_data = []
    for msg in messages:
        full_msg = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = full_msg['payload']

        try:
            body = payload['parts'][0]['body']['data']
        except:
            body = payload.get('body', {}).get('data', '')

        decoded_msg = base64.urlsafe_b64decode(body).decode('utf-8')
        email_data.append((decoded_msg, service, full_msg))

    return email_data
