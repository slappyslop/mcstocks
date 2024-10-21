class Portfolio():
    dateStarted = 0
    listOfStocks = []
    dailyReturns = 0

    def __init__(self, listofStocks, dateStarted):
        self.listOfStocks = listofStocks
        self.dateStarted = dateStarted


