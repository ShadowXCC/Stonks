# This currently only works for comparing performance between 2 "snapshots" of an account
import ingest
import dataworkers as dw
import glob

# Fix % of account in "Pub Sample Data" in the CSV (We should probably assume that % of account will add up to something near 100%)

# At some future point copy the csv files to some other directory, and when a new csv is added copy it over there to be read into the program
# At some future point, figure out how to save data so it is not always read on the fly

def perfmessage(snapshots, downloadDates):
    m = ""

    downloadDatesLength = len(snapshotsKeys)

    m += "Found " + str(downloadDatesLength) + " .csv files in the directory.\n"

    timeDifference = ingest.compareDownloadDates(downloadDates[0], downloadDates[downloadDatesLength - 1])
    m += "The time gap between uploaded all CSVs is " + str(timeDifference) + ", with an average time gap of " + str(ingest.averageDownloadDates(downloadDates)) + ".\n"
    m += "\n"
    m += "Between your two mostly recently uploaded CSVs, \"" + str(downloadDates[downloadDatesLength - 2]) + "\" and \"" + str(downloadDates[downloadDatesLength - 1]) + "\":\n"

    m += "The positions fully sold are " + str(dw.getFullySoldPositions(snapshots[downloadDates[downloadDatesLength - 2]], snapshots[downloadDates[downloadDatesLength - 1]])) + ".\n"
    m += "The wholly newly purchased positions are " + str(dw.getNewlyPurchasedPositions(snapshots[downloadDates[downloadDatesLength - 2]], snapshots[downloadDates[downloadDatesLength - 1]])) + ".\n"

    m += "\n"

    ticker = "MSFT"
    m += positionStatsMessage(ticker)

    return m

def positionStatsMessage(ticker):
    total = 0
    values = dw.listEachValueOfPosition(snapshots, ticker)
    valuesLength = len(values)
    for val in values:
        total += val
    r = "The total value of " + ticker + " is " + str('${:,.2f}'.format(total)) + ".\n"

    olderValue = values[valuesLength - 2]
    newerValue = values[valuesLength - 1]
    if newerValue > olderValue:
        r += "Your holding of " + ticker + " increased by " + '${:,.2f}'.format(int(newerValue) - int(olderValue)) + ".\n"
    elif newerValue < olderValue:
        r += "Your holding of " + ticker + " decreased by " + '${:,.2f}'.format(int(olderValue) - int(newerValue)) + ".\n"
    elif newerValue == olderValue:
        r += ticker + " stayed the same."
    
    return r





dirpath = "C:\\Users\\shado\\Desktop\\Stonks\\Fidelity Portfolio Performance\\Pub Sample Data\\*.csv"
files = glob.glob(dirpath)

snapshots = {}
for file in files:
    # snapshots[ingest.downloadDate(file)] = ingest.CSV(file)
    snapshots.update({ingest.downloadDate(file) : ingest.CSV(file)})

snapshotsKeys = sorted(snapshots)

# print(snapshots)
snapshots=dict(sorted(snapshots.items(), key=lambda p: p[0]))
# print("\n\n\n")
# print(snapshots)

# print(snapshots[snapshotsKeys[len(snapshots)-1]])

print(perfmessage(snapshots, snapshotsKeys))

# print(dw.listEachValueOfPosition(snapshots, "MSFT"))

# print(dw.listPositionPerSnap(snapshots, "MSFT"))