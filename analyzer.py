__author__ = 'ASUS-PC'
import re
import datetime
from dateutil.parser import *
def analyzer(text):
    regex=re.compile('( (0?[1-9]|1[0-9]|2[0-9]|3[01])[tTNSns][DTHdth]( of | OF | ?, ?).{3,10}(, ?)?( in | IN )?(\d\d)?(\d\d))|( (0?[1-9]|1[0-9]|2[0-9]|3[01])[.\/-](0?[1-9]|1[12])[.\/-](\d\d)?(\d\d))|( (\d\d)?(\d\d)[.\/-](0?[1-9]|1[12])[.\/-](0?[1-9]|1[0-9]|2[0-9]|3[01]).)|( \w{3,10} (0?[1-9]|1[0-9]|2[0-9]|3[01]) ?, ?(\d\d)?(\d\d))')
    itr=regex.finditer(text)
    time_entities=[]
    for each in itr:
        time_entities.append(time_parser(each.group()))
        #time_entities.append(parse(each.group(),fuzzy=True))
    return time_entities

def time_parser(text):
    date=None
    try:
        date=datetime.datetime.strptime(text,' %d/%m/%Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %d/%m/%y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %d-%m-%Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %d-%m-%y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %d.%m.%Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %d.%m.%y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %Y-%m-%d')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %y-%m-%d')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %Y/%m/%d')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %y/%m/%d')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %Y.%m.%d')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %y.%m.%d')
        return date
    except:
        pass

    #***************************************************************************************
    try:
        date=datetime.datetime.strptime(text, ' %dth of %B in %Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text, ' %dth of %b in %Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text, ' %dth of %B in %y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text, ' %dth of %B, %Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text, ' %dth of %B,%Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text, ' %dth of %B, %y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text, ' %dth of %B,%y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %dth of %b, %Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %dth of %b,%Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %dth of %b, %y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %dth of %b,%y')
        return date
    except:
        pass

    #******************************************************

    try:
        date=datetime.datetime.strptime(text, ' %dth,%B, %Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text, ' %dth,%B,%Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text, ' %dth,%B, %y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text, ' %dth,%B,%y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %dth,%b, %Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %dth,%b,%Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %dth,%b, %y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %dth,%b,%y')
        return date
    except:
        pass


    #****************************************************************************

    try:
        date=datetime.datetime.strptime(text,' %B %d,%Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %b %d,%Y')
        return date
    except:
        pass


    try:
        date=datetime.datetime.strptime(text,' %B %d,%y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %b %d,%y')
        return date
    except:
        pass



    try:
        date=datetime.datetime.strptime(text,' %B %d, %Y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %b %d, %Y')
        return date
    except:
        pass


    try:
        date=datetime.datetime.strptime(text,' %B %d, %y')
        return date
    except:
        pass
    try:
        date=datetime.datetime.strptime(text,' %b %d, %y')
        return date
    except:
        pass
    return date
print(analyzer("I want to go somewhere on 12th of nov, 2016 and I will be returning back on 2016.7.20"))

[datetime.datetime(2016, 11, 12, 0, 0), datetime.datetime(2016, 7, 20, 0, 0)]