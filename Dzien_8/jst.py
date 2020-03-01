import csv
# with open("Baza_teleadresowa_jst_stan_na_28.02.2020.csv") as f:
#     reader = csv.reader(f, delimiter = ";")
#     with open("baza_jst.csv", "w", newline="") as fs:
#         writer = csv.writer(fs, delimiter = ";")
#         for row in reader:
#             writer.writerow(row)


with open("Baza_teleadresowa_jst_stan_na_28.02.2020.csv") as f:
    reader = csv.DictReader(f, delimiter = ";")
    dane = []
    for row in reader:
        dane.append((row['Kod_TERYT'], row['telefon kierunkowy'] + row['telefon'].replace(" ", "").replace("\n","")))


with open("baza_jst.csv", "w", newline="") as fs:
    writer = csv.writer(fs, delimiter = ";")
    writer.writerow(["TERYT", "telefon"])
    writer.writerows(dane)