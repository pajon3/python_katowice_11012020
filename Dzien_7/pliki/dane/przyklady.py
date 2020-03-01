#
#
# fh =open('logs.txt')
# print(dir(fh))
#
#
# fh.close()

with open('logs.txt') as loghi, open('emails.txt') as emaile:
    print(logi.read())
    print(emaile.read())