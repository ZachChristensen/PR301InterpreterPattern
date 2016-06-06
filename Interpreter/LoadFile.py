from abc import ABCMeta, abstractmethod


class LoadFile(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.data = ""

    @abstractmethod
    def load_data(data_handler, path):
        pass
