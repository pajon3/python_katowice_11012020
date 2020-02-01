

# napisz funkcję, która jako argument przyjmie jako argument słownik ze statusami oraz status i zwróci liczbe ludzi o podanym statusie
def status_count(statusy, status):
    # x = 0
    # for i in statusy:
    #     if statusy[i] == status:
    #         x += 1
    # return x
    return list(statusy.values()).count(status)  # rozwiązanie z metodami


def test_status_count_with_existing_status():
    statusy = {
        "Alicja": "online",
        "Rafał": "offline",
        "Anna": "online"
    }
    assert status_count(statusy, "online") ==2
    assert status_count(statusy, "offline") ==1



