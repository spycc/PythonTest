import re

a = 'hello,good,all,to,of,count,aac,abc,acc,_adc,aec,afc'
b = 'pythonpythonpythonjsadfwfee'
c = '10000b0011b'
d = 'goodC#haha'

count = re.findall('c#',d,re.I)
print(count)