import json


lista =[1,2,3]
slownik = {'ala':'kot', 'lista': lista}
print(json.dumps(slownik))

with open("dane.json", 'w') as f:
    json.dump(slownik, f)