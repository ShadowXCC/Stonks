def getAccounts(data):
    r = list(set(list(data["Account Name"])))
    
    return r

def getPositionsByAccount(data, account):
    r = data.query('`Account Name` == @account')

    return r

def getallpositions(data):
    r = sorted(list(set(list(data["Symbol"]))))

    return r

def listAllPositionsSeparatedByAccount(data, accounts):
    r = []

    for account in accounts:
        r.append(str(getPositionsByAccount(data, account)))

    return r

def listAllPositionsInAccount(data, account):
    return data.loc[data['Account Name'] == account, 'Symbol']

def returnAllNonBlankByColumn(data, column):
    # subframe = fooframe.query("`{0}` == 'Large'".format(myvar))

    return data.query('`{0}` != "--" & not `{0}`.isnull()'.format(column))

def returnPositionsThatHaveExDatesSoon(data, ds):
    from datetime import datetime, date, timedelta

    date_format = '%m/%d/%Y'
    today = date.today().strftime("%m/%d/%Y")
    todayDT = datetime.strptime(today, date_format)

    exdates = list(data.loc[data['Ex-Date'].str.contains('/'), 'Ex-Date'])

    return [d for d in exdates if todayDT <= datetime.strptime(d, date_format) <= todayDT + timedelta(days = ds)]

def returnAllInstancesOfSymbol(data, sym):
    return data.query('`Symbol` == @sym')

def tallyUp(data, sym):
    r = data.query('`Symbol` == @sym')
    r = list(r["Current Value"])

    total = 0
    for i in r:
        total = total + stringMoneyToMoney(i)

    return total

def tallyUpAll(data, syms):
    r = {}
    for sym in syms:
        r.update({sym: tallyUp(data, sym)})
    
    return dict(r)

def stringMoneyToMoney(toConvert):
    from re import sub
    from decimal import Decimal

    if toConvert == "--": return stringMoneyToMoney("0.00")

    return Decimal(sub(r'[^\d.]', '', toConvert))

def returnExdateBasedOnMonth(data, month):
    if len(month) == 1: month = "0" + month

    r = data.query('`Ex-Date`.str.contains(@month + "/")', engine='python')

    toRemove = r[r['Ex-Date'].str.contains("/" + month + "/")].index
    r.drop(toRemove, inplace=True)

    return r

def returnAllExdatesBasedOnMonth(data):
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

    r = {}
    for month in months:
        r.update({month: returnExdateBasedOnMonth(data, month)})

    return r