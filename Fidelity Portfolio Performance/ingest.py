from datetime import timedelta

columnsToDrop = ["Today's Gain/Loss Dollar", "Today's Gain/Loss Percent", "Cost Basis Total", "Average Cost Basis", "Type"]
def CSV(filepath):
    import pandas as pd
    import numpy as np

    data = pd.read_csv(filepath)
    dataLastRowNum = data.index.stop
    data = data.drop(data.index[dataLastRowNum - 3:dataLastRowNum])

    data = data.drop(columns=columnsToDrop)

    data = data.replace(np.nan, "--")

    # data['Ex-Date']= pd.to_datetime(data['Ex-Date'], errors='ignore')
    # data['Pay Date']= pd.to_datetime(data['Pay Date'], errors='ignore')

    return data

def downloadDate(filepath):
    # read file
    # search for something starting with {"Date downloaded } and ending with {"} with regex

    import re

    r = ""
    
    f = open(filepath, "r", encoding="utf-8")
    r = re.findall("\"Date downloaded .*\"", f.read())
    r = r[0]

    timezone = r[len(r) - 3:len(r) - 1]

    r = r[17:len(r) - 4]

    return r

def compareDownloadDates(oldDate, newDate):
    from datetime import datetime

    oldDate = datetime.strptime(oldDate, "%m/%d/%Y %I:%M %p")
    newDate = datetime.strptime(newDate, "%m/%d/%Y %I:%M %p")

    return newDate - oldDate

def averageDownloadDates(downloadDates):
    downloadDatesLength = len(downloadDates)

    gaps = []
    for i in range(0, downloadDatesLength - 1):
        gaps.append(compareDownloadDates(downloadDates[i], downloadDates[i + 1]))


    bigGap = timedelta(seconds=0)
    for gap in gaps:
        bigGap = bigGap + gap

    
    return bigGap/downloadDatesLength