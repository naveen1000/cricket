import requests
from bs4 import BeautifulSoup as bs
import time
mid='22402'

mid=input('Enter mid')
ur='http://mapps.cricbuzz.com/cbzios/match/'+mid+'/leanback.json'
try:
    source=requests.get(ur)
    data = source.json()
except:
    print("An exception occurred requesting")
ti=0

twicket=1
try:
    twicket=int(data["comm_lines"][0]["wkts"])
    twicket=twicket+1
except:
    print("An exception occurred fetching twkt")

tover=1
try:
    tover=int(float(data['bat_team']['innings'][0]['overs']))
    tover=tover+1
except:
    print("An exception occurred fetching tover")

wicket=0
over=0
score=0
s1='';s2='';s3='';
s=["1","2","3","4","5","6","7","8","9","10"]
while 1:
    ur='http://mapps.cricbuzz.com/cbzios/match/'+mid+'/leanback.json'
    try:
        source=requests.get(ur)
        data = source.json()
        try:
            score=int(data["comm_lines"][0]["score"])
            wicket=int(data["comm_lines"][0]["wkts"])
            over=float(data['bat_team']['innings'][0]['overs'])
            try:
                batname0=data['batsman'][0]['name'][0:5]
                batname1=data['batsman'][1]['name'][0:5]
                bat0score=data['batsman'][0]['r']
                bat1score=data['batsman'][1]['r']
                bat0strike=data['batsman'][0]['strike']
                bat1strike=data['batsman'][1]['strike']
                bat0ball=data['batsman'][0]['b']
                bat1ball=data['batsman'][1]['b']
                s3=batname0+bat0strike+"("+bat0score+"-"+bat0ball+")"+batname1+bat1strike+"("+bat1score+"-"+bat1ball+")"
            except:
                print("An exception occurred fetching batters")
            s1=data["comm_lines"][0]["score"]+'/'+data["comm_lines"][0]["wkts"]
            s2=data['bat_team']['innings'][0]['overs']
            iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s3
            requests.get(iurl)
            print(over)
            print(score)
            print(s3)
        except:
            print("An exception occurred fetching score")

        if over==tover:
            str=data["comm_lines"][0]["score"]+" "+data['bat_team']['innings'][0]['overs']+" \n"+data['prev_overs'].split("|")[2]+" \n"+data['bowler'][0]['name']
            url='https://api.telegram.org/bot879982304:AAHG7ZRyEMWoQB-ToaiJBv_gMvkW-ekJcSg/sendMessage?chat_id=582942300&text=hey'+str
            requests.get(url)
            s1=data["comm_lines"][0]["score"]+'/'+data["comm_lines"][0]["wkts"]
            s2=data['bat_team']['innings'][0]['overs']
            s3=data['prev_overs']
            s4=s3.split("|")[2]+" "+data['bowler'][0]['name']
            iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s4
            requests.get(iurl)
            tover=tover+1
            time.sleep(10)
            
        if wicket==twicket:
            print(wicket)
            str="wicket "+s[twicket-1]+" "+data['last_wkt_name']+" "+data['last_wkt_score']+" B: "+data['bowler'][0]['name']
            url='https://api.telegram.org/bot831624998:AAFUKPiuCHJkO4kf75UHPbgMpN8M9yDo9ns/sendMessage?chat_id=582942300&text=hey'+str
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
        print("An exception occurred requesting") 
    time.sleep(8)

