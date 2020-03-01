"""
$ longest_word.py text.txt
abrkabadabra

"""
import string

file_name = "PT.txt"
tabela = []


def clean(text):
    znaki = string.ascii_lowercase + "ąćęłóńśźż- "
    for znak in text:
        if znak not in znaki:
            text = text.replace(znak, "")
    return text


def short(text):
    for slowo in text:
        if len(slowo) < 4:
            text = text.replace(slowo, "")
    return text


with open(file_name, encoding="utf-8") as f:
    text = f.read().lower()
    for el in "\n\\:/":
        text = text.replace(el, " ")
    text = clean(text)
    text = short(text)

    for slowo in text:
        if slowo in tabela:
            tabela.append(slowo, 1)
        else:
            tabela[slowo] = tabela[slowo] + 1

    print(tabela)
