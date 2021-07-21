import datatime
import pywhatkit
import time 
with open("phone.txt", "r") as f:
	lines = f.readlines()

for i in range (len(lines)):
	lines[i] = lines[i].reaplace(" ", "").strip()
while datatime.datatime.now().day != 20:
	time.sleep(60*60)
while datatime.datatime.now().day != 5:
	time.sleep(60*5)
mesaj = "denmeme amaclı mesaj icerıgi"
for number in lines:
	t = datatime.datatime.now()
	pywhatkit.sendwhatmsg(number, mesaj, t.hour, t.time,+ 1)
 #pywhatkıt.sendwhatmsg_to_group(group_id, message, time_hour, time_min)