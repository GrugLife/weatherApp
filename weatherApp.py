#! python 3
# umbrellaReminder - check and see if it is raining.  If so, send a text to bring umbrella

import requests, bs4, time
from twilio.rest import TwilioRestClient
from selenium import webdriver

# Twilio info
accountSID = '################################' #Enter Twilio accountSID
authToken = '#################################' #Enter authToken
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+##########' #Enter Twilio Number
myCellNumber = '+##########' #Enter Phone Number to recieve text message


# Get website
url = 'http://forecast.weather.gov/MapClick.php?lat=37.80038839031306&lon=-122.4361020549652#.V2i3Nnqo7Ht'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Download the weather for today
time = soup.select('.period-name')
time = time[0].getText()

foreCast = soup.select('.short-desc')
foreCast = foreCast[0].getText()

temp = soup.select('.temp')
temp = temp[0].getText()

time1 = soup.select('.period-name')
time1 = time1[1].getText()

foreCast1 = soup.select('.short-desc')
foreCast1 = foreCast1[1].getText()

temp1 = soup.select('.temp')
temp1 = temp1[1].getText()

# send SMS
message = twilioCli.messages.create(body = '{} will be {} with a {}\n{} will be {} with a {}'.format(time, foreCast, temp, time1, foreCast1, temp1),from_=myTwilioNumber, to = myCellNumber)
