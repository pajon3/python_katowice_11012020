


odczyt = "emails.txt"
zapis = "new_emails.txt"


def emails_clean(odczyt, zapis):
    x = 0
    new_emails = []

    with open(odczyt) as fo:
        with open(zapis, "w") as fz:

            for line in fo:
                for el in line:
                    if el == "@":
                        x += 1

                if x == 1:
                    correct = line.lower()
                    correct = correct.strip() + "\n"
                    if correct not in new_emails:
                        new_emails.append(correct)
                x = 0

            for email in new_emails:
                fz.write(email)


emails_clean(odczyt,zapis)