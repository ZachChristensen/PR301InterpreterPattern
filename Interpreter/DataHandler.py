import pickle
import re
from Person import Person


class DataHandler:
    def __init__(self, model, new_load_file):
        self.myModel = model
        self.load_file = new_load_file
        self.unwashed_data_set = list()
        self.display_data = list()
        self.wrong_data = list()

    def setLoadFile(self, new_load_file):
        self.load_file = new_load_file

    def save_pickle_data(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.display_data, f)

    def load_pickle_data(self):
        try:
            with open('data.pickle', 'rb') as f:
                self.display_data = pickle.load(f)
        except FileNotFoundError:
            print("Existing data not found.")
            return

    def read_in(self, path):
        self.load_file.load_data(self, path)

    def add_new_data(self, new_array):
        self.unwashed_data_set += new_array

    def del_data(self):
        self.unwashed_data_set = list()
        self.display_data = list()

    def get_data(self):
        return self.display_data

    @staticmethod
    def is_valid_data(person):
        if len(person) is not 6:
            return False
        rules = ["^[A-Z][0-9]{3}$",
                 "(M|F)",
                 "[0-9]{1,2}$",
                 "[0-9]{3}$",
                 "(Normal|Overweight|Obesity|Underweight)",
                 "[0-9]{2,3}$"]
        num = 0
        for data in person:
            if num == 0:
                matching = re.match(rules[num], data, flags=re.IGNORECASE)
            else:
                matching = re.match(rules[num], data)
            num += 1
            if matching is None:
                return False
        return True

