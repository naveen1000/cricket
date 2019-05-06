import requests
import time
mid='0'
tnotify=0
inotify=0
mid=input('Enter mid\n')
bow='NO'

while True:
    tnotify=int(input('Do you want notification for every over?(1/0)\n'))
    if(tnotify==0 or tnotify==1):
        break
while True:
    inotify=int(input('Do you want to send data to IFTTT?(1/0)\n'))
    if(inotify==0 or inotify==1):
        break
ti=0
t50=0
t100=0
wicket=0
over=0
score=0
s1='';s2='';s3=''
s=["1","2","3","4","5","6","7","8","9","10"]
ur='http://mapps.cricbuzz.com/cbzios/match/'+mid+'/leanback.json'


try:
    source=requests.get(ur)
    data = source.json()
except:
    print("An exception occurred prefetching")
    exit()
    
try:
    twicket=int(data["comm_lines"][0]["wkts"])
    twicket=twicket+1
except:
    print("An exception occurred fetching twkt")
    
try:
    tover=int(float(data['bat_team']['innings'][0]['overs']))
    tover=tover+1
except:
    print("An exception occurred fetching tover")
    


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
                batname0=data['batsman'][0]['name'][0:6]
                batname1=data['batsman'][1]['name'][0:6]
                bat0score=data['batsman'][0]['r']
                bat1score=data['batsman'][1]['r']
                bat0ball=data['batsman'][0]['b']
                bat1ball=data['batsman'][1]['b']
                bowler=data['bowler'][0]['name']
                s3=batname0+"("+bat0score+"-"+bat0ball+")"+batname1+"("+bat1score+"-"+bat1ball+")"
            except:
                print("An exception occurred fetching batters")
            if inotify==1:
                s1=data["comm_lines"][0]["score"]+'/'+data["comm_lines"][0]["wkts"]
                s2=data['bat_team']['innings'][0]['overs']
                iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s3
                requests.get(iurl)
            try:
                print(data["comm_lines"][0]["score"]+"/"+data["comm_lines"][0]["wkts"]+" "+data['bat_team']['innings'][0]['overs']+" "+bowler)
                print(s3)
                if (over==(tover-1.0+0.5)):
                    bow=bowler
            except:
                print("An exception occurred fetching bowlwer")
        except:
            print("An exception occurred fetching score")
            
        if over==tover:
            print("notified")
            if tnotify==1:
                print("notified")
                str=data["comm_lines"][0]["score"]+" "+data['bat_team']['innings'][0]['overs']+" "+bow+" \n"+data['prev_overs']
                url='https://api.telegram.org/bot879982304:AAHG7ZRyEMWoQB-ToaiJBv_gMvkW-ekJcSg/sendMessage?chat_id=582942300&text=hey'+str
                requests.get(url)
            if inotify==1:    
                s1=data["comm_lines"][0]["score"]+'/'+data["comm_lines"][0]["wkts"]
                s2=data['bat_team']['innings'][0]['overs']
                s3=data['prev_overs']
                iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s3
                requests.get(iurl)
            tover=tover+1
            time.sleep(15)
            
        if wicket==twicket:
            print(wicket)
            str="wicket "+s[twicket-1]+" "+data['last_wkt_name']+" "+data['last_wkt_score']+" B: "+data['bowler'][0]['name']
            url='https://api.telegram.org/bot831624998:AAFUKPiuCHJkO4kf75UHPbgMpN8M9yDo9ns/sendMessage?chat_id=582942300&text=hey'+str
            source=requests.get(url)
            if inotify==1:
                s1=str
                s2=''
                s3=''
                iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s3
                requests.get(iurl)
            twicket=twicket+1
            time.sleep(15)
            
        if ((score>50 and score<56) and t50==0):
            str="half_century:50"
            url='https://api.telegram.org/bot879982304:AAHG7ZRyEMWoQB-ToaiJBv_gMvkW-ekJcSg/sendMessage?chat_id=582942300&text=hey'+str
            source=requests.get(url)
            if inotify==1:
                s1=str
                s2=data['bat_team']['innings'][0]['overs']
                s3=''
                iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s3
                requests.get(iurl)
            t50=t50+1
            time.sleep(12)
            
        if ((score>99 and score<106) and t100==0):
            str="century:100"
            url='https://api.telegram.org/bot879982304:AAHG7ZRyEMWoQB-ToaiJBv_gMvkW-ekJcSg/sendMessage?chat_id=582942300&text=hey'+str
            source=requests.get(url)
            if inotify==1:
                s1=str
                s2=data['bat_team']['innings'][0]['overs']
                s3=''
                iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2+'&value3='+s3
                requests.get(iurl)
            t100=t100+1
            time.sleep(12)   
            
        if (over==20 or wicket==10):
            exit()
      
    except:
        print("An exception occurred requesting") 
    time.sleep(10)

