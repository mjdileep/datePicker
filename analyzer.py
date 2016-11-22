__author__ = 'ASUS-PC'
import re
from dateutil.parser import *
def analyzer(text):
    regex=re.compile('( (0?[1-9]|1[0-9]|2[0-9]|3[01])[tTNSns][DTHdth]( of | OF | ?, ?).{3,10}(, ?)?( in | IN )?(\d\d)?(\d\d))|( (0?[1-9]|1[0-9]|2[0-9]|3[01])[.\/-](0?[1-9]|1[12])[.\/-](\d\d)?(\d\d))|( (\d\d)?(\d\d)[.\/-](0?[1-9]|1[12])[.\/-](0?[1-9]|1[0-9]|2[0-9]|3[01]).)|( \w{3,10} (0?[1-9]|1[0-9]|2[0-9]|3[01]) ?, ?(\d\d)?(\d\d))')
    itr=regex.finditer(text)
    time_entities=[]
    for each in itr:
        time_entities.append(parse(each.group(),fuzzy=True))
    return time_entities
print(analyzer("Hi, I would like to book a ticket from London to Singapore on 13-12-2016 and return on 20-12-2016. What are the cheap options you have?Thank you.Dinal"))