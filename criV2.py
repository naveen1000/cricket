import requests
import time

def finotify():
    s1=data["comm_lines"][0]["score"]+'/'+data["comm_lines"][0]["wkts"]
    s2=data['bat_team']['innings'][0]['overs']
    iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+s1+'&value2='+s2
    requests.get(iurl)

def century(t):
    url='https://api.telegram.org/bot879982304:AAHG7ZRyEMWoQB-ToaiJBv_gMvkW-ekJcSg/sendMessage?chat_id=582942300&text=hey'+str2
    requests.get(url)
    if inotify==1:
        iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+str2
        requests.get(iurl)
    time.sleep(12)

def wick():
    str1="wicket "+" "+" "+data['last_wkt_name']+" "+data['last_wkt_score']+" B: "+data['bowler'][0]['name']
    url='https://api.telegram.org/bot831624998:AAFUKPiuCHJkO4kf75UHPbgMpN8M9yDo9ns/sendMessage?chat_id=582942300&text=hey'+str1
    requests.get(url)
    if inotify==1:
        iurl='https://maker.ifttt.com/trigger/CricketScore/with/key/H9qCqfSIfI2WiwXhF2zZz?value1='+str1
        requests.get(iurl)
    global twicket
    twicket=twicket+1
    time.sleep(15)
        

def main():
# try:
    global t50
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
    print(data["comm_lines"][0]["score"]+"/"+data["comm_lines"][0]["wkts"]+" "+data['bat_team']['innings'][0]['overs']+" "+bowler)
    print(s3)
    if inotify==1:
        finotify()
    try:
        if (over==(tover-1.0+0.5)):
            bow=bowler
    except:
        print("An exception occurred fetching bowlwer")

    if wicket==twicket:
        wick()
    score=52
    if ((score>50 and score<56) and t50==50):
        century(t50)
        t50=t50+1
    if ((score>99 and score<106) and t100==100):
        #t100=t100+1
        century(t100)
    if (over==20 or wicket==10):
        exit()
    #except:
    #    print("An exception occurred fetching score")

mid=input('Enter mid\n')
ur='http://mapps.cricbuzz.com/cbzios/match/'+mid+'/leanback.json'
inotify=0
twicket=0
t50=50
t100=100
str2=""
try:
    source=requests.get(ur)
    data = source.json()
    twicket=int(data["comm_lines"][0]["wkts"])
    twicket=twicket+1
    tover=int(float(data['bat_team']['innings'][0]['overs']))
    tover=tover+1
except:
    print("An exception occurred prefetching")
    exit()
while 1:
    source=requests.get(ur)
    data = source.json()
    main()
    time.sleep(8)
