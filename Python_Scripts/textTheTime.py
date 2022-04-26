from SMSScript import *
from datetime import datetime
import time


timeOfDay = datetime.today().strftime("%I:%M %p")
message = "Hey Lucas its "+ timeOfDay
1
email_alert("Time Reminder", message,"6068754768@vtext.com")
print("sent 1 text")

amountSent = 1
while(True):
    time.sleep(1800)
    timeOfDay = datetime.today().strftime("%I:%M %p")
    message = "Hello again Lucas. Its been 30 min. Its now "+timeOfDay

    email_alert("Time Reminder", message,"6068754768@vtext.com")

    amountSent+=1
    print("sent " + str(amountSent)+ " texts")
    
    

    
    
