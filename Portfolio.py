import yfinance
import csv
import random
import pandas


        

# runs n trials with sample size s from the last y years of data
def runTrials(n:int, s:int, y:int):
    experiment = Experiment()
    experiment.buildIndex()
    for i in range(n):
        experiment.runTrial
        



class Experiment():
    def __init__(self) -> None:
        self.index = []

    def buildIndex(self):
        with open("EQUITY_L.csv", mode= 'r') as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                self.index.append(line[9])
        return self.index
    
    def downloadNSE(self):
        for stockName in self.buildIndex():
            str = "data/" + stockName + ".csv"
            yfinance.download(stockName, period="10y").to_csv(str)

    
    #runs trial with sample size s and last y years of data
    def runTrial(self, s:int, y:int):
        myIndex = self.index.copy()
        sampleNames = []
        sampleData = []
        for i in range(s):
            random.randint(0, len(self.index))
            sampleNames.append(myIndex.pop(i))
   

experiment = Experiment()
experiment.downloadNSE()