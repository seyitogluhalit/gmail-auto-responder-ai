from datetime import datetime

def save_to_file(email_text: str, reply_text: str):
    """
    E-posta ve AI cevabını yerel dosyaya kaydeder.
    """
    with open("mail_log.txt", "a", encoding="utf-8") as file:
        file.write(f"\n===== {datetime.now()} =====\n")
        file.write("Email:\n")
        file.write(email_text + "\n\n")
        file.write("AI Reply:\n")
        file.write(reply_text + "\n")
        file.write("==============================\n")
    print("🗃️ Mail ve cevap kaydedildi.")
