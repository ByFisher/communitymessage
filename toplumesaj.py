import datetime
import pywhatkit
import time 

with open("phone.txt", "r") as f:
    lines = f.readlines()

# Telefon numaralarının başındaki ve sonundaki boşlukları ve satır sonu karakterlerini temizle
lines = [number.strip() for number in lines]

while datetime.datetime.now().day != 0.50:
    time.sleep(60*60)

while datetime.datetime.now().day != 2:
    time.sleep(60*5)

mesaj = "deneme amacıyla mesaj iceriği"
for number in lines:
    t = datetime.datetime.now()
    pywhatkit.sendwhatmsg(number, mesaj, t.hour, t.minute + 1)  # Dakikayı bir arttır
