import requests
from bs4 import BeautifulSoup as bs
import time
mid='21537'
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
    ur='http://mapps.cricbuzz.com/cbzios/match/'+mid+'/leanback.json'
    try:
        source=requests.get(ur)
        data = source.json() 
        score=int(data["comm_lines"][0]["score"])
        wicket=int(data["comm_lines"][0]["wkts"])
        over=float(data['bat_team']['innings'][0]['overs'])
        s1=data["comm_lines"][0]["score"]+'/'+data["comm_lines"][0]["wkts"]
        s2=data['bat_team']['innings'][0]['overs']
        s3=''
        iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s3
        requests.get(iurl)
        print(over)
        print(score)
        if over==tover:
            str=data["comm_lines"][0]["score"]+" "+data['bat_team']['innings'][0]['overs']+" \n"+data['prev_overs']
            url='https://api.telegram.org/bot452373832:AAGauK8mHnS_H401kn5887JwCTGZo_MhM80/sendMessage?chat_id=582942300&text=hey'+str
            requests.get(url)
            s1=data["comm_lines"][0]["score"]+'/'+data["comm_lines"][0]["wkts"]
            s2=data['bat_team']['innings'][0]['overs']
            s3=data['prev_overs']
            iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s3
            requests.get(iurl)
            tover=tover+1
            time.sleep(10)
            
        if wicket==twicket:
            print(wicket)
            str="wicket "+s[twicket-1]+" "+data['last_wkt_name']+" "+data['last_wkt_score']+" B: "+data['bowler'][0]['name']
            url='https://api.telegram.org/bot452373832:AAGauK8mHnS_H401kn5887JwCTGZo_MhM80/sendMessage?chat_id=582942300&text=hey'+str
            source=requests.get(url)
            s1=str
            s2=''
            s3=''
            iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s3
            requests.get(iurl)
            twicket=twicket+1
            time.sleep(10)
            
        if score==50:
            str="half_century:50"
            url='https://api.telegram.org/bot452373832:AAGauK8mHnS_H401kn5887JwCTGZo_MhM80/sendMessage?chat_id=582942300&text=hey'+str
            source=requests.get(url)
            s1=str
            s2=data['bat_team']['innings'][0]['overs']
            s3=''
            iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s3
            requests.get(iurl)
            time.sleep(10)
            
        if score==100:
            str="century:100"
            url='https://api.telegram.org/bot452373832:AAGauK8mHnS_H401kn5887JwCTGZo_MhM80/sendMessage?chat_id=582942300&text=hey'+str
            source=requests.get(url)
            s1=str
            s2=data['bat_team']['innings'][0]['overs']
            s3=''
            iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s3
            requests.get(iurl)
            time.sleep(10)            
        
    except:
        print("An exception occurred") 
    time.sleep(10)

