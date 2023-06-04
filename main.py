from datetime import datetime
import backtrader as bt
import pandas as pd
import numpy as np

class SmaCross(bt.Strategy): # bt.Strategy를 상속한 class로 생성해야 함.
    params = dict(
        pfast = 5,
        pslow = 30
    )
    
    def log(self, txt, dt=None):
        #' Logging function fot this strategy'
        dt = dt or self.data.datetime[0]
        if isinstance(dt, float):
            dt = bt.num2date(dt)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        sma1 = bt.ind.SMA(period = self.p.pfast)
        sma2 = bt.ind.SMA(period = self.p.pslow)
        self.crossover = bt.ind.CrossOver(sma1,sma2)

        self.holding = 0
        
    
    def next(self):
        global size
        global count
        current_price= self.data.close[0]
        if not self.position: # not in the market
            if self.crossover > 0:
                available_stocks = int(self.broker.getcash()/current_price)
                self.buy(price=current_price, size=100) # 매수 size = 구매 개수 설정 
                self.log('BUY CREATE, %.2f' % (current_price))
                 
                print(100, 'EA')

        else:
            if self.crossover<0:
                self.close()
                self.log('SELL CREATE, %.2f' % (current_price))
                print(, 'EA')
        
data = bt.feeds.GenericCSVData(
    dataname="amc_ohlcv.csv",

    fromdate = datetime(2017,1,1),
    todate = datetime(2017,12,31),

    nullvalue = 0.0,
    dtformat=('%Y-%m-%d'),

    datetime=0,
    high=2,
    low=3,
    open=1,
    close=4,
    volume=6,

                headers = True,
                separator = ','
)
                



def main(data):
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(54640) #2021년도 개인투자자 평균 투자액
    cerebro.broker.setcommission(0.0015)
    cerebro.adddata(data)
    cerebro.addstrategy(SmaCross)
    cerebro.run()
    cerebro.plot(style='candlestick',barup='red',bardown='blue',xtight=True,ytight=True, grid=True)  # and plot it with a single command'''

if __name__ == "__main__":
    main(data)

