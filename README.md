"# datePicker" 

This script will help you to extract the date strings from a text field and return as an array of python datetime object.

It supports on following date formats:

* ' 12/12/2016'
* ' 21-12-2016'
* ' 21.12.2016'
* ' 2016-07-20'
* ' 2016/07/20'
* ' 2016.07.20'
* ' 16.12.01’
* ' 6th of november, 2016'
* ' 6th of nov, 2016'
* ' 6th,november, 2016'
* ' 6th,nov, 2016'
* ' nov 4,16'
* ' november 4,2016'
* ' 6th of November in 2016'

How to use:

print(analyzer("I want to go somewhere on 12th of nov, 2016 and I will be returning back on 2017.7.20"))

result:

[datetime.datetime(2016, 11, 12, 0, 0), datetime.datetime(2017, 7, 20, 0, 0)]

