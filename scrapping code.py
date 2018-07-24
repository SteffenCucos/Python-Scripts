import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time



class exchange:
    def __init__(self,name):
        self.name = name
        self.coins = []




    def fill_coins(self):
        return
        



class coin:

    def __init__(self,name,url):
        self.name=name
        self.url=url
        print("--------------",self.name,"--------------")
        start_time = time.time()
        req = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        print ("urllib.request.Request", time.time() - start_time, "to run")

        
        start_time = time.time()
        #html = requests.urlopen(req).read()
        html = req.text
        print ("urllib.request.urlopen", time.time() - start_time, "to run")

        
        start_time = time.time()
        self.data = BeautifulSoup(html,'html.parser')
        print ("BeautifulSoup", time.time() - start_time, "to run","\n")
        self.table = self.getTable()
        
    def update(self):
        req = requests.Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        start_time = time.time()
        html = requests.urlopen(req).read()
        start_time = time.time()
        self.data = BeautifulSoup(html,'html.parser')
        self.table = self.getTable()
    def get_price(self):
        pass
        
    def getTable(self):
        data = self.data.findAll('table')[5].getText().split("\n")
        while(u'' in data or u'\xa0' in data):
            for item in data:
                if item ==(u'') or item == u'\xa0':
                    data.remove(item)
        table = []
        for col in range(8):
            Crow = []
            for row in range(len(data)//8):
                Crow.append((data[8*row+col]).encode('utf-8'))
            table.append(Crow)
        return table         

    def printTable(self):
        
        PTable = ""
        longest = 0
        for row in self.table:
            for item in row:
                if len(item)>longest:
                    longest = len(item) #find longest item
        for i in range(len(self.table[0])):
            row = ""
            for w in range(len(self.table)):
                item = self.table[w][i]
                padding = longest - len(str(item))
                
                row+="|"+self.table[w][i]+ " "*padding
            print(row)                
        return






btc = coin("btc","https://www.investing.com/currencies/btc-usd")
eth = coin("eth","https://www.investing.com/currencies/eth-usd")
ltc = coin("ltc","https://www.investing.com/currencies/ltc-usd")
neo = coin("ans","https://www.investing.com/currencies/ans-usd")


if __name__ =="__main__":
    btc.printTable()
    eth.printTable()
    ltc.printTable()
    neo.printTable()
        #btc.update()
        #time.sleep(20)






