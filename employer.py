from employee import Employee

class Employer:
    def __init__(self, name):
        self.name = name

    def add_employee(self, data_module):
        name = input("Введите имя работника: ")
        position = input("Введите должность работника: ")
        hourly_rate = float(input("Введите почасовую ставку работника: "))
        availability = input("Введите доступность работника: ")
        employee = Employee(name, position, hourly_rate, availability)
        data_module.add_employee(employee)
        print(f"{self.name}, вы успешно добавили {employee} для аренды.")
