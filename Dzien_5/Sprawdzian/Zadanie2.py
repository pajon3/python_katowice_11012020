
def online_status(statuses, status):
    counter = 0
    for x in statuses:
        if statuses[x] == status:
            counter += 1

    return counter



statuses = {
    'Alice':  'online',
    'Bob': 'online',
    'Eve': 'offline',
}

def test_online_status():
    assert online_status(statuses,"xxx") == 0
    assert online_status(statuses, "online") == 2
    assert online_status(statuses, "offline") == 1