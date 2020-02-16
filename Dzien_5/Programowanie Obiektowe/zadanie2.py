class Employee:
    def __init__(self, imie: str, nazwisko: str, stawka: float):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.worked_normal_hours = 0
        self.worked_over_hours = 0



    def register_time(self, hours):
        if hours >= 8:
            self.worked_normal_hours += hours
            self.worked_over_hours += hours - 8
        else:
            self.worked_normal_hours = hours

    def pay_salary(self):
        to_pay = self.worked_normal_hours * self.stawka + self.worked_over_hours * self.stawka * 2
        self.worked_normal_hours = 0
        self.worked_over_hours = 0
        return to_pay


employee = Employee("Jan", "Nowak", 100.0)
employee.register_time(10)
print(employee.pay_salary())
