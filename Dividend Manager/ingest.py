import pandas as pd

columnsToDrop = ["Account Number", "Description", "Last Price", "Last Price Change", "Percent Of Account", "Type", "Est. Annual Income"]
def dividendCSV(filepath):
    import pandas as pd

    data = pd.read_csv(filepath)
    dataLastRowNum = data.index.stop
    data = data.drop(data.index[dataLastRowNum - 3:dataLastRowNum])

    data = data.drop(columns=columnsToDrop)

    return data