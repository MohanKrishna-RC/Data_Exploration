import re

#Email indetify
text = '"mkg3456-dfg.lj@gmail.com","hjdsfshgfhwj@gmail.com"'
print(re.findall(r'[a-zA-Z0-9_\-\.]+[@][a-z]+[\.][a-z]{2,3}',text))

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

#find the string of length 10>5, min 5, <5
text = 'Python exercises, PHP exercises, C# exercises'

sent_min5 = re.findall(r'[a-zA-Z]{5,}',text)
sent_max5 = re.findall(r'[a-zA-Z]{1,5}',text)
sent_limit = re.findall(r'[a-zA-Z]{5,10}',text)
print(sent_min5,sent_max5,sent_limit)

#convert camel-case(PythonExercises) to snake case(python_exercises)

camel_text = "PythonExercisesAreGood"
def camel_to_snake(text):
     str1 = re.sub('(.)([A-Z][a-z]+)',r'\1_\2',text)
     print(str1)
     return re.sub('([a-z0-9])([A-Z])',r'\1_\2',str1).lower()

print(camel_to_snake(camel_text))

#Covert snake case string to camel case string
snake_text = "python_exercises_are_good"
def snake_to_camel(text):
     return "".join(x.capitalize() or '_' for x in snake_text.split('_'))
print(snake_to_camel(snake_text))

#find text between quotation marks ("")
text = '"Python","JAVA","Lovaf"'
print(re.findall(r'"(.*?)"',text))

#remove mutlispace in a string and whitespaces
text = "Python   Exercises   are   good"
print(re.sub(r' +','_',text))
print(re.sub(r' +',' ',text))
print(re.sub(r' +','',text)) #remove whitespaces
print(re.sub(r'\s+','',text)) #remove whitespaces

#remove all characters except alphanumeric characters

text1 = '**//Python Exercises// - 12. '
pattern = re.compile('[\W_]+')
print(pattern.sub('',text1))
print(re.sub(r'[\W_]+','',text1))

#split string at uppercase letters
text = "Python Exercises Are Good"
print(re.findall(r'[A-Z][^A-Z]*',text))

#find all adverbs and their positions
text = "Clearly, he has no excuse for such behavior, fairly fup."
for m in re.finditer(r"\w+ly", text):
     print(m)
     print('%d-%d: %s' % (m.start(), m.end(), m.group(0)))

#split a string with multiple delimiters
text = 'The quick brown\nfox jumps*over the lazy dog.'
print(re.split('; |, |\*|\n',text))

#check a decimal with a precision of 2.
text = '123.1412'
print(bool(re.search(r"^[0-9]+(\.[0-9]{1,2})?$",text)))