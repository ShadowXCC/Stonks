columnsToDrop = ["Account Number", "Description", "Last Price", "Last Price Change", "Percent Of Account", "Type", "Est. Annual Income"]
def dividendCSV(filepath):
    import pandas as pd
    import numpy as np

    data = pd.read_csv(filepath)
    dataLastRowNum = data.index.stop
    data = data.drop(data.index[dataLastRowNum - 3:dataLastRowNum])

    data = data.drop(columns=columnsToDrop)

    data = data.replace(np.nan, "--")

    data['Ex-Date']= pd.to_datetime(data['Ex-Date'], errors='ignore')
    data['Pay Date']= pd.to_datetime(data['Pay Date'], errors='ignore')

    return data