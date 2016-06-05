
class Person:
    def __init__(self, new_id, new_sex, new_age, new_sales, new_weight, new_income):
        self.id = new_id
        self.sex = new_sex
        self.age = new_age
        self.sales = new_sales
        self.weight = new_weight
        self.income = new_income

    def get_id(self):
        return self.id

    def get_gender(self):
        return self.sex

    def get_age(self):
        return self.age

    def get_sales(self):
        return self.sales

    def get_weight(self):
        return self.weight

    def get_income(self):
        return self.income
