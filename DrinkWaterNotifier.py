import time
from datetime import datetime
from plyer import notification

dt = datetime.now()
current_time = dt.strftime("%H:%M:%S")

notification.notify(
title = "Drink Water Reminder",
message = "This is a Reminder for you to Drink 2 Glasses of Water\nTime: "+current_time+"\nNote: Next Reminder will be after 1 hr.",

app_icon = "water.ico",

timeout = 50
)
time.sleep(60*60)#1 hr
