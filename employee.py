class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def gross_monthly_pay(self):
        return self._salary * (1/12)


class SeniorEmployee(Employee):

    def gross_monthly_pay(self):
        return super().gross_monthly_pay() + 500



emp = SeniorEmployee("Val Jean", 12000.00)
print(emp.gross_monthly_pay())