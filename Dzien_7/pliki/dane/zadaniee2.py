import sys
from collections import defaultdict

if len(sys.argv) > 1:
    plik = sys.argv[1]
else:
    plik = "logs.txt"

last_login_time = {}
user_system_time = defaultdict(int)

with open(plik) as l:
    for line in l:
        name, action, time = (line.split(";"))
        time = int(time)
        if action == "LOGIN":
            last_login_time[name] = time
        elif action == "LOGOUT":
            user_system_time[name] += time - last_login_time[name]

for name, time in sorted(user_system_time.items(), key=lambda x: int(x[0].split("-")[1])):
    print(f"- {name}: {time} s")
