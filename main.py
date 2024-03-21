import pandas as pd
import time 
from textSender import texter
#reads data strores it into 2 single linked list 

def main():    
    #username and password
    sender_credentials = ("nyupideltapsi@gmail.com", "irpx bpmu ozne fybr")
    
    #sheet id 
    sheet_id = '14G4rlx1aTXdQ--nQ4Ltbpc8XDQu6RUVs71xvOHYdP5Q'
    df = pd.read_csv( f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

    #change the message and subject of email 
    amount=0
    while(amount!=(len(df['name']))):
        message="Hi "+str(df['name'][amount])
        message=message+", Active house is hosting GIM on Tuesday 2/13 from 7-9pm and would love for you all to come out. If you will not be in the city during this time, we would still love to have you come as we also have an option to zoom in with the link to be provided later. Looking forward to hearing from you soon!"
        phone=str(df['phone'][amount])
        texter(f'{phone}',f'{message}')
        time.sleep(2)
        amount=amount+1
if __name__=='__main__':
    main()
    print("done")

    #for the size of phonenumber it will send them a message
   # for phone in df['phonenumber']:13 frND n848-
    # for career in providers:
    #  print(career)
    #  send_sms_via_email(phone, message, career, sender_credentials)
    #  time.sleep(0.5)
