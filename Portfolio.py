import yfinance
import csv
import random
import pandas
import matplotlib.pyplot as plt
import os


        

# runs n trials with sample size s from the last y years of data
def runTrials(n:int, s:int, y:int):
    experiment = Experiment()
    for i in range(n):
        experiment.runTrial(5, 5)
        



class Experiment():
    def __init__(self) -> None:
        self.index = []
        self.buildIndex()

    def buildIndex(self):  #lx
        with open("EQUITY_L.csv", mode= 'r') as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                self.index.append(line[9])
        
    
    def downloadNSE(self):
        for stockName in self.buildIndex():
            str = "data/" + stockName + ".csv"
            yfinance.download(stockName, period="10y").to_csv(str)
            check = pandas.read_csv(str)


    def wrangle(self, sd : list[pandas.DataFrame]):
        #correct objects as column names
        for data in sd:
            data.drop([0, 1], inplace= True)
            data.rename(columns= {"Price" : "Date"}, inplace= True)
        return sd

    def clean_data(self):
        for stockName in self.index:
            try:
                str = "data/" + stockName+ ".csv"
                if (len(pandas.read_csv(str)) <= 10):
                    os.remove(str)
            except FileNotFoundError:
                continue
            

   
    #runs trial with sample size s and for data since year y without replacement
    def runTrial(self, s:int, y:int):
        myIndex = self.index.copy()
        sampleNames = []
        sampleData: list[pandas.DataFrame] = []
        for i in range(s):
            j = random.randint(0, len(myIndex))
            sampleNames.append(myIndex.pop(j))

        for stockName in sampleNames:
            str = "data/" + stockName + ".csv" 
            csvFile = pandas.read_csv(str)
            sampleData.append(csvFile)

        self.wrangle(sampleData)
        
        
