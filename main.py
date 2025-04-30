from get_emails import get_emails
from generate_reply import generate_reply
from send_email_reply import send_email_reply
from save_to_file import save_to_file

def main():
    emails = get_emails(max_count=5)

    if not emails:
        print("İşlenecek e-posta bulunamadı.")
        return

    for index, (email_text, service, original_message) in enumerate(emails):
        print(f"\n E-Posta #{index + 1}")
        print("Gelen içerik:\n", email_text[:200], "...") 
        reply = generate_reply(email_text)
        send_email_reply(service, original_message, reply)
        save_to_file(email_text, reply)
        print("Üretilen Cevap:\n", reply)

if __name__ == "__main__":
    main()
