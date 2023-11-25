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

    # m += "Between your two mostly recently uploaded CSVs, \"" + str(downloadDates[downloadDatesLength - 2]) + "\" and \"" + str(downloadDates[downloadDatesLength - 1]) + "\":\n"
    # m += "The positions fully sold are " + str(dw.getFullySoldPositions(snapshots[downloadDates[downloadDatesLength - 2]], snapshots[downloadDates[downloadDatesLength - 1]])) + ".\n"
    # m += "The fully newly purchased positions are " + str(dw.getNewlyPurchasedPositions(snapshots[downloadDates[downloadDatesLength - 2]], snapshots[downloadDates[downloadDatesLength - 1]])) + ".\n"
    # m += "\n"

    m += "Across all snapshots, your holdings have changed in these ways:"
    m += fullHoldingsQuantityChangeMessage(snapshots, snapshotsKeys) + "\n"
    m += fullHoldingsNewlyPurchasedPositionsMessage(snapshots, snapshotsKeys)
    m += fullHoldingsFullySoldPositionsMessage(snapshots, snapshotsKeys)



    # m += "\n" + positionStatsMessage("MSFT")

    return m

def positionStatsMessage(ticker):
    total = 0
    values = dw.listEachValueOfPosition(snapshots, ticker)
    valuesLength = len(values)
    for val in values:
        total += val
    r = "The total value of " + ticker + " is " + str('${:,.2f}'.format(total)) + ", split across " + str(valuesLength) +" purchases.\n"

    olderValue = values[valuesLength - 2]
    newerValue = values[valuesLength - 1]
    if newerValue > olderValue:
        r += "Your holding of " + ticker + " increased by " + '${:,.2f}'.format(int(newerValue) - int(olderValue)) + ".\n"
    elif newerValue < olderValue:
        r += "Your holding of " + ticker + " decreased by " + '${:,.2f}'.format(int(olderValue) - int(newerValue)) + ".\n"
    elif newerValue == olderValue:
        r += ticker + " stayed the same."
    
    return r

def fullHoldingsQuantityChangeMessage(snapshots, snapshotsKeys):
    r = ""

    # r += "Your first snapshot had "

    differences = dw.checkForChangesInQuantityAcrossAllSnapshots(snapshots)

    for diffSnap in differences:
        keys = differences[diffSnap].keys()
        r += "\nIn between the " + snapshotsKeys[diffSnap] + " - " + snapshotsKeys[diffSnap + 1] + " snapshots, your holdings of:"
        for key in keys:
            qChange = differences[diffSnap][key]

            r += "\n\t" + key
            if qChange > 0:
                r += " increased by " + str(qChange) + " shares."
            elif qChange < 0:
                r += " decreased by " + str(qChange) + " shares."
            elif qChange == 0:
                r += " stayed the same."

    return r

def fullHoldingsNewlyPurchasedPositionsMessage(snapshots, snapshotsKeys):
    r = ""

    for i in range(0, len(snapshotsKeys) - 1):
        newPositions = dw.getNewlyPurchasedPositions(snapshots[snapshotsKeys[i]], snapshots[snapshotsKeys[i + 1]])
        
        if len(newPositions) == 0:
            r +=  "Nothing was newly purchased in the " + str(i + 1) + " period.\n"
        else:
            r += str(newPositions) + " are newly purchased in the " + str(i + 1) + " period.\n"
        

    return r

def fullHoldingsFullySoldPositionsMessage(snapshots, snapshotsKeys):
    r = ""

    for i in range(0, len(snapshotsKeys) - 1):
        fullySoldPositions = dw.getFullySoldPositions(snapshots[snapshotsKeys[i]], snapshots[snapshotsKeys[i + 1]])
        
        if len(fullySoldPositions) == 0:
            r +=  "Nothing was fully sold in the " + str(i + 1) + " period.\n"
        else:
            r += str(fullySoldPositions) + " were fully sold in the " + str(i + 1) + " period.\n"


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
snapshotsLength = len(snapshots)
# print("\n\n\n")
# print(snapshots)

# print(snapshots[snapshotsKeys[len(snapshots)-3]])
# print(snapshots[snapshotsKeys[len(snapshots)-2]])
# print(snapshots[snapshotsKeys[len(snapshots)-1]])

print(perfmessage(snapshots, snapshotsKeys))

