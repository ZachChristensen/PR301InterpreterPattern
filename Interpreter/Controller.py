"""
    # Failed file Load
    >>> myController = Controller()
    >>> myController.load_data("fakeFile.txt")

"""

from Model import Model
from View import View


class Controller:
    def __init__(self, path):
        self.myModel = Model()
        if path != "" or path is not None:
            self.load_data(path)
        self.myView = View(self)
        self.myModel.data_handler.load_pickle_data()
        self.myView.cmdloop()

    def delete_data(self):
        self.myModel.data_handler.del_data()

    def wash_data(self):
        self.myModel.wash_data()

    def get_data(self):
        return self.myModel.data_handler.get_data()

    def get_weight_data(self):
        return self.myModel.get_weight()

    def get_sales_data(self):
        return self.myModel.get_sales()

    def get_gender_data(self):
        return self.myModel.get_gender()

    def load_data(self, path):
        try:
            file = open(path)
            file.read()
        except FileNotFoundError:
            print("File Does Not Exist")
            return
        self.myModel.data_handler.read_in(path)

    def save_data(self):
        self.myModel.data_handler.save_pickle_data()
