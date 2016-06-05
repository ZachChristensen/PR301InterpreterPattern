from DataHandler import DataHandler
from LoadFileCSV import LoadFileCSV


class Model:
    def __init__(self):
        self.data_handler = DataHandler(self, LoadFileCSV())

    def get_sales(self):
        result = []
        for i in self.data_handler.display_data:
            result.append(i.get_sales())
        return result

    def get_weight(self):
        normal = 0
        over = 0
        obese = 0
        under = 0
        for i in self.data_handler.display_data:
            if i.get_weight() == 'Normal':
                normal += 1
            elif i.get_weight() == 'Overweight':
                over += 1
            elif i.get_weight() == 'Obesity':
                obese += 1
            elif i.get_weight() == 'Underweight':
                under += 1
        return [normal, over, obese, under]

    def get_gender(self):
        m = 0
        f = 0
        for i in self.data_handler.display_data:
            if i.get_gender() == 'M':
                m += 1
            elif i.get_gender() == 'F':
                f += 1
        return [m, f]
