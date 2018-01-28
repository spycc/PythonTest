import re

a = 'hello,good,all,to,of,count,aac,abc,acc,_adc,aec,afc'
b = 'pythonpythonpythonjsadfwfee'
c = '10000b0011b'
d = 'goodC#haha'
e = 'A83C72D1D8E67'
f = 'life is short , i use python'

def tihuan(value):
    yuan = int(value.group())
    if yuan >= 50:
        return '100'
    else:
        return '0'

count = re.sub('\d{2}',tihuan,e)
print(count)