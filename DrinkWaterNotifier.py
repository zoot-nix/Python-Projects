import time
from datetime import datetime
from plyer import notification #for notifications on pc

dt = datetime.now()
current_time = dt.strftime("%H:%M:%S")

notification.notify(
#title of notification
title = "Drink Water Reminder",
#message of the notification
message = "This is a Reminder for you to Drink 2 Glasses of Water\nTime: "+current_time+"\nNote: Next Reminder will be after 1 hr.",

#icon for notification
#download water.ico from repo
app_icon = "water.ico",

#notification stays for 50 secs
timeout = 50
)
#repeats in 1 hr
time.sleep(60*60)
