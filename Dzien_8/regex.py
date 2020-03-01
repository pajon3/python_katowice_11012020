import re

# pattern = re.compile(" \d{2}-\d{3} ") #kody
# pattern = re.compile(" \d{2} \w{3} \d{4} ")  #daty
pattern = re.compile("user-\d{0,}@\w{0,}.\w{2,3,4}")  #maile

with open('input.txt', encoding="utf8") as text:
    wyniki  = pattern.findall(text.read())
print(wyniki)
print(len(wyniki))