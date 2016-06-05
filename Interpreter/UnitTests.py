import unittest
from Model import Model
from Person import Person

# remove useless method in model for get unwashed data only used by tests before
# smell 1 make a people class for model primitive obsession
# smell 2 large class model
# smell 3 move graph making to its own class


class UnitTest(unittest.TestCase):

    def test_file_input(self):
        self.myModel = Model()
        self.myModel.data_handler.read_in("TestData.csv")
        self.expected = Person('D003', 'M', 12, 312, 'Normal', 123)
        self.assertEquals(self.myModel.data_handler.get_data()[0].get_id(), self.expected.get_id())
        self.assertEquals(self.myModel.data_handler.get_data()[0].get_weight(), self.expected.get_weight())
        self.assertEquals(self.myModel.data_handler.get_data()[0].get_age(), self.expected.get_age())
        self.assertEquals(self.myModel.data_handler.get_data()[0].get_sales(), self.expected.get_sales())
        self.assertEquals(self.myModel.data_handler.get_data()[0].get_income(), self.expected.get_income())

    def test_csv_file_input(self):
        self.myModel = Model()
        self.myModel.data_handler.read_in("TestData.csv")
        self.expected = 12
        self.failUnlessEqual(len(self.myModel.data_handler.unwashed_data_set), self.expected)

    def test_washing_data(self):
        self.myModel = Model()
        # There are 5 errors so length should be cut down to 7 after washing
        self.myModel.data_handler.read_in("TestData.csv")
        self.expected = 7
        self.failUnlessEqual(len(self.myModel.data_handler.get_data()), self.expected)

    def test_get_weight(self):
        self.myModel = Model()
        self.myModel.data_handler.read_in("TestData.csv")
        self.expected = 4
        self.failUnlessEqual(len(self.myModel.get_weight()), self.expected)
        self.failUnlessEqual(self.myModel.get_weight()[0], 2)
        self.failUnlessEqual(self.myModel.get_weight()[3], 4)
        self.failUnlessEqual(self.myModel.get_weight()[2], 1)

    def test_get_gender(self):
        self.myModel = Model()
        self.myModel.data_handler.read_in("TestData.csv")
        self.expected = 2
        self.failUnlessEqual(len(self.myModel.get_gender()), self.expected)
        self.failUnlessEqual(self.myModel.get_gender()[0], 2)
        self.failUnlessEqual(self.myModel.get_gender()[1], 5)

    def test_get_sales(self):
        self.myModel = Model()
        self.myModel.data_handler.read_in("TestData.csv")
        self.expected = 7
        self.failUnlessEqual(len(self.myModel.get_sales()), self.expected)
        self.failUnlessEqual(self.myModel.get_sales()[0], 312)
        self.failUnlessEqual(self.myModel.get_sales()[3], 636)
        self.failUnlessEqual(self.myModel.get_sales()[-1], 345)

    def test_del_data(self):
        self.myModel = Model()
        self.myModel.data_handler.read_in("TestData.csv")
        self.expected = 7
        self.failUnlessEqual(len(self.myModel.data_handler.get_data()), self.expected)
        self.myModel.data_handler.del_data()
        self.expected = 0
        self.failUnlessEqual(len(self.myModel.data_handler.get_data()), self.expected)

    def test_pickle_methods(self):
        self.myModel = Model()
        self.myModel.data_handler.read_in("TestData.csv")
        self.myModel.data_handler.save_pickle_data()
        self.myModel.data_handler.del_data()
        self.myModel.data_handler.load_pickle_data()
        self.expected = 7
        self.failUnlessEqual(len(self.myModel.data_handler.get_data()), self.expected)
