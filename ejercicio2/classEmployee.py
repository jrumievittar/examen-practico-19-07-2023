class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def change_salary(self, salary):
        new_salary = int(input("Cuál es tu nuevo salario?: "))
        if new_salary != 'false':
            self.salary = new_salary


if __name__ == '__main__':
    # instancio la clase
    employee = Employee('Jesus', 2000)
    employee.get_salary()
    employee.change_salary(salary='2500')
