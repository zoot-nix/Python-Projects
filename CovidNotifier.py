import time
import datetime
import requests#retriving covid data from web
from plyer import notification#for notifications on pc

covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    #Data is not fetched due to lack of internet connection
    print("Please Check your Internet Connection.")

if (covidData != None):
    #convert data to json
    data = covidData.json()["Success"]

    while(True):
        notification.notify(
        #title of the notification
        title = "COVID19 Stats of India on {}".format(datetime.date.today()),
        #message of the notification
        message = "Total Cases: {totalcases}\nToday Cases: {todaycases}\nToday Deaths: {todaydeaths}\nTotal Active: {active}".format( totalcases = data['cases'], todaycases = data['todayCases'], todaydeaths = data['todayDeaths'], active = data['active']),
        #app icon
        app_icon = "covid.ico",
        #stays for 50 sec in notifications
        timeout = 50

        )
        #to repeat after 4 hrs
        time.sleep(60*60*4)
