class CashMachine:

    def __init__(self):
        self.banknotes = []

    @property
    def is_avaliable(self):
        return len(self.banknotes) >0

    def put_money(self,list_of_banknotes):
        for money in list_of_banknotes:
            self.banknotes.append(money)

    def withdraw_money(self, amount):
        to_withdraw = []
        for bill in sorted(self.banknotes, reverse = True):
            if sum(to_withdraw) + bill <= amount:
                to_withdraw.append(bill)
        if sum(to_withdraw) != amount:
            to_withdraw = []

        for bill in to_withdraw:
            self.banknotes.remove(bill)
        return to_withdraw



class TestClassMachine:

    def test_initialization(self):
        cash_machine = CashMachine()
        assert cash_machine

    def test_is_avaliable(self):
        cash_machine = CashMachine()
        assert cash_machine.is_avaliable is False
        cash_machine.put_money ([200,100,100,50])
        assert cash_machine.is_avaliable is True


    def test_withdraw_money(self):
        cash_machine = CashMachine()
        cash_machine.put_money ([200,100,100,50])
        assert cash_machine.withdraw_money(150) == [100,50]

        cash_machine = CashMachine()
        cash_machine.put_money ([200,100,100,50])
        assert cash_machine.withdraw_money(200) == [200]

        cash_machine = CashMachine()
        cash_machine.put_money ([200,100,100,50])
        assert cash_machine.withdraw_money(500) == []

        cash_machine = CashMachine()
        cash_machine.put_money ([200,100,100,50])
        assert cash_machine.withdraw_money(450) == [200,100,100,50]

        cash_machine = CashMachine()
        cash_machine.put_money ([50,50,20,20,20])
        assert cash_machine.withdraw_money(110) == [50,20,20,20]