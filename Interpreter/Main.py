"""
Interpreter Project
Author: Zach Christensen and Jacob McPhail
Date: 4 March 2016
Version: 1.1
"""
from Controller import Controller


class Main:
    def __init__(self, path):
        self.myController = Controller(path)

if __name__ == '__main__':
    Main("TestData.csv")
