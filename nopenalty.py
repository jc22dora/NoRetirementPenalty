import pandas as pd
import math
class NoPenalty:

    def __init__(self, buyDate, sellDate, value):
        self.SPXU = pd.read_excel("SPXU.xlsx")
        self.SPXL = pd.read_excel("SPXL.xlsx")
        self.ira = value
        self.stockaccount = value
        self.bankaccount = 0
        self.netequities = self.setNetEquities()
        self.spxuBuyPrice = getSPXUPrice(buyDate)
        self.spxuSellPrice = getSPXUPrice(sellDate)
        self.spxlBuyPrice = getSPXLPrice(buyDate)
        self.spxlSellPrice = getSPXLPrice(sellDate)


    def setNetEquities(self, ):
        self.netequities = self.ira + self.stockaccount + self.bankaccount

    def getSPXUPrice(self, buyDate):
        #parse through SPXU for price at date buyDate
        return price

    def getSPXLPrice(self, sellDate):
        #parse through SPXL for price at date sellDate
        return price

    def transactionAlgorithm(self):
        spxuShares = math.floor(self.ira/self.spxuBuyPrice)
        spxlShares = math.floor(self.stockaccount/self.spxuBuyPrice)