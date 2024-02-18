class JobSeeker:
    def find_employee(self, data_module):
        employees_list = data_module.get_employees()
        print("Доступные работники для аренды:")
        for index, employee in enumerate(employees_list, start=1):
            print(f"{index}. {employee}")

        choice = int(input("Введите номер работника, которого вы хотите арендовать: "))
        if 1 <= choice <= len(employees_list):
            selected_employee = employees_list[choice - 1]
            print(f"Вы выбрали {selected_employee} для аренды.")
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

