import re

# S = "asdfg12345!@#$%dsfjjhf"

# res = re.findall(r'\w+', S)  #To find words in a string
#clean_data = re.sub(r'[^a-zA-Z0-9]','',S)
# a = re.findall(r'[0-9]+',S)
# b = re.findall(r'[a-z]+',S)
# c = re.findall(r'[A-Z]+',S)
# d = re.findall(r'[@_!#$%^&*()<>?/\|}{~:]+',S)

# comp = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
# e = comp.search(S)
# print(a,b,c,d,e)

S = 'abb'
pattern = '^a(b*)$'
pattern1 = 'ab+'
pattern2 = 'a.*?b$'
f1 = re.search(pattern1,S)
print(f1)

#Write Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

import re
results = re.finditer(r"([0-9]{1,6})", "Exercises number 1, 12, 13, and 435654 are important")
print("Number of length 1 to 3")
print(results)
for n in results:
     print(n.group(0))


string = "asdfg12345!@#$%dsfjjhf"


type = list(map(lambda i: isinstance(i,int),string))

type = list(map(lambda i: isinstance(i,str),string))

num = re.findall(r'[0-9]',string)
alp = re.findall(r'[a-z]',string)
spc = re.findall(r'[^a-z0-9A-Z]',string)
# spc = re.findall(r'[^a-z]+[^0-9]+',string)
print(num)
print(spc)


"""
#Indetify the substring matches with locations
import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))
"""
