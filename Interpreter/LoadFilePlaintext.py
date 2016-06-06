from LoadFile import LoadFile
from Person import Person


class LoadFilePlainText(LoadFile):
    def __init__(self):
        print("loading plain text file...")

    def load_data(data_handler, path):
        print(str(data_handler.__class__) + " " + path)
        file = open(path)
        txt = file.read()
        li = txt.split('\n')
        if li[-1].strip() == '':
            del li[-1]
        data_handler.add_new_data(li)
        if data_handler.unwashed_data_set is not []:
            print("File Loaded!")

        unwashed_data = data_handler.unwashed_data_set
        for i in unwashed_data:
            tmp = i.split(' ')
            is_valid = data_handler.is_valid_data(tmp)
            if is_valid:
                data_handler.display_data.append(Person(tmp[0], tmp[1], int(tmp[2]), int(tmp[3]), tmp[4], int(tmp[5])))

