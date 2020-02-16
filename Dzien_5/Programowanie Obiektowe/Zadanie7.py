class Employee:
    def __init__(self, f_name, l_name, rph):
        self.first_name = f_name
        self.last_name = l_name
        self.rate_per_hour = rph
        self._worked_normal_hours = 0
        self._worked_overhours = 0

    def register_time(self, hours):
        if hours > 8:
            self._worked_normal_hours += 8
            self._worked_overhours += hours - 8
        else:
            self._worked_normal_hours += hours

    def pay_salary(self):
        to_pay = (
                self._worked_normal_hours * self.rate_per_hour +
                self._worked_overhours * 2 * self.rate_per_hour
        )
        self._worked_normal_hours = 0
        self._worked_overhours = 0
        return to_pay


class PremiumEmployee(Employee):
    def __init__(self, f_name, l_name, rph, bonus):
        super().__init__(f_name, l_name, rph)
        self.bonus = bonus

    def give_bonus(self, amount):
        self.bonus += amount

    # def pay_salary(self):
    #     to_pay = (
    #             self._worked_normal_hours * self.rate_per_hour +
    #             self._worked_overhours * 2 * self.rate_per_hour +
    #             self.bonus
    #     )
    #     self._worked_normal_hours = 0
    #     self._worked_overhours = 0
    #     self.bonus = 0
    #     return to_pay

    def pay_salary(self):
        to_pay = super().pay_salary()
        to_pay += self.bonus
        self.bonus = 0
        return to_pay


class TestEmployee:

    def test_bonus(self):
        pe = PremiumEmployee('Jan', 'Nowak', 100.0, 0)
        pe.register_time(5)
        pe.give_bonus(1000)
        # assert pe.pay_salary() == 1500
        assert pe.pay_salary() == 1500
