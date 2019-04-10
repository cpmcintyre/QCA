import pandas as pd
import os
import datetime

class contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number


newcon = contact('Rick Rick', 7493233523)


data = open('0_WhatsApp Chat with Thomas Lee.txt', encoding="ANSI")
stun = []
for i in data:
    base= i.replace('\n','').split('-')
    try:
        record = {'date':base[0].split(',')[0].strip(),
                  'time':base[0].split(',')[1].strip(),
                  'sender':base[1].split(':')[0],#update to contact object?
                  'message':base[1].split(':')[1]}
        stun.append(record)
    except:
        print('Rejected Message')
        print(i)

data.close()

res = pd.DataFrame(stun)

res.to_csv('Outputconvodata.csv')
