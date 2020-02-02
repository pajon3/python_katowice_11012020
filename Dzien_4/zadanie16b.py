import re
# def consecutive(text, znak):
#     seria = 0
#     seria_max = 0
#     for i in range(0,len(text)-1):
#         if text[i] == znak:
#             seria +=1
#             seria_max = max(seria, seria_max)
#         else:
#             seria = 0
#     return seria_max

def consecutive(text, znak):
    pattern = re.compile(f"{znak}*")
    data = pattern.findall(text)
    # data = [len(x) for x in data]
    data = map(lambda x: len(x), data)
    return max(data)



def test_consecutive():
    assert consecutive("aabbbbaabbbbbababba","b") == 5
    assert consecutive("ddddiddd","d") == 4
    assert consecutive("rrrtrrrtrrr","r") == 3
    assert consecutive("eererewwerewww","w") == 3
    assert consecutive("eeeeer","e") == 5