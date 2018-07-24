import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time
from send_sms import send_message
import json
import time

class coin:

    def __init__(self,name,period):
        self.name=name
        self.history=[]
        self.period=period
        #self.history[self.period]={}
        
        
    def get_price(self):
        url="https://api.cryptowat.ch/markets/poloniex/"+self.name+"usd/price"
        
        req=urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        #soup = BeautifulSoup(html, 'html.parser')
        jsonToPython = json.loads(html)
        price = jsonToPython['result']["price"]
        return(price)


    def historic_data(self):
        '''

        eth.historic_data()


        '''
        url="https://api.cryptowat.ch/markets/poloniex/"+self.name+"usd/ohlc"
        
        req=urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        #soup = BeautifulSoup(html, 'html.parser')
        
        
        jsonToPython = json.loads(html)
        for period in jsonToPython['result']:
#            self.history[period]={}
            lstOflst=jsonToPython['result'][period]
            for infolst in lstOflst:
                self.history.append((infolst[1],infolst[1]))
                #self.history[period][infolst[0]]=infolst[1]
            

            
        
    def log(self):
        with open('index'+self.name+ '.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            price=self.get_price()
            writer.writerow([price,str(datetime.now())])
        price=self.get_price()
        timestamp = int(time.time())
        self.history.append((price,timestamp))
        #print(price," "+self.name)

    

    def MA(self,numPrev):
        sums=0
        if len(self.history)>numPrev:
            for n in range(numPrev+1):
                sums+=self.history[-1-n][0]
            return sums/(numPrev+1)
        for n in range(len(self.history)):
            sums+=self.history[-1-n][0]
        return sums/(len(self.history))
                
        
        
        
        


    

    






period="5"
eth=coin("eth",period)
eth.historic_data()
btc=coin("btc",period)
btc.historic_data()
tokens=[eth,btc]

done=False

while not done:
    for coin in tokens:
        coin.log()
        print (coin.name,coin.history[-1][0],coin.MA(5),"MA \n")
        '''if len(coin.history)%10==0:
            print(coin.history[len(coin.history)-10:len(coin.history)])'''
    #send_message(lst[0]+"<=>"+lst[1],"+14166971252")
    time.sleep(int(period))






