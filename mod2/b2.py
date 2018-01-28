import re
a = 'hello,good,all,to,of,count,aac,abc,acc,_adc,aec,afc'
b = 'pythonpythonpythonjsadfwfee'
c = '10000b0011b'
d = 'goodC#haha'
e = 'A83C72D1D8E67'
f = 'life is short , i use python, i love python'
count = re.search('life (.*) python(.*)python',f)
print(count.group(0,1,2))
