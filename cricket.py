import requests
from bs4 import BeautifulSoup as bs
import time
i=1
ti=1
twicket=3
tover=12
s=["1","2","3","4","5","6","7","8","9","10"]
'''ur='http://mapps.cricbuzz.com/cbzios/match/21648/watch-mini-commentary.json'
#ur='http://mapps.cricbuzz.com/cbzios/match/21537/leanback.json'
source=requests.get(ur)
data = source.json()
#print(type(data))
#print(data) 
score=data["comm_lines"][0]["score"]
wicket=data["comm_lines"][0]["wkts"]
print(wicket)
'''
while 1:
    ur='http://mapps.cricbuzz.com/cbzios/match/21537/leanback.json'
    source=requests.get(ur)
    data = source.json()
    #print(type(data))
    #print(data) 
    score=int(data["comm_lines"][0]["score"])
    wicket=int(data["comm_lines"][0]["wkts"])
    over=float(data['bat_team']['innings'][0]['overs'])
    #https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1=Alex&value2=Helen
    print(over)
    print(score)
    if over==tover:
        str=data["comm_lines"][0]["score"]+" "+data['bat_team']['innings'][0]['overs']+" \n"+data['prev_overs']
        url='https://api.telegram.org/bot452373832:AAGauK8mHnS_H401kn5887JwCTGZo_MhM80/sendMessage?chat_id=582942300&text=hey'+str
        source=requests.get(url)
        tover=tover+1
        
    if wicket==twicket:
        print(wicket)
        str="wicket "+s[twicket-1]+" "+data['last_wkt_name']+" "+data['last_wkt_score']+" B: "+data['bowler'][0]['name']
        url='https://api.telegram.org/bot452373832:AAGauK8mHnS_H401kn5887JwCTGZo_MhM80/sendMessage?chat_id=582942300&text=hey'+str
        source=requests.get(url)
        twicket=twicket+1

    if score==50:
        str="half_century:50"
        url='https://api.telegram.org/bot452373832:AAGauK8mHnS_H401kn5887JwCTGZo_MhM80/sendMessage?chat_id=582942300&text=hey'+str
        source=requests.get(url)
    if score==100:
        str="century:100"
        url='https://api.telegram.org/bot452373832:AAGauK8mHnS_H401kn5887JwCTGZo_MhM80/sendMessage?chat_id=582942300&text=hey'+str
        source=requests.get(url)
    i=i+1
    time.sleep(10)

