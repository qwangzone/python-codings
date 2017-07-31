import sys
import os
class CountCodeLines:
    def __init__(self, directory):
        self.directory = directory
        self.start = 1
        self.line_null = 0

    def list_all_file(self):
        #file_list = []
        dirs = os.listdir(self.directory)
        #for file in dirs:
        #    file_list.append(file)
        #return file_list
        file_list = [f for f in dirs if f.split(".")[-1] == 'py']
        return file_list

    def count_code(self):
        for file in self.list_all_file():
            with open(file, 'rb') as f:
                for l in f.readlines():
                    print (str(self.start) + "、" + l.decode('utf8'))
                    self.start = self.start + 1
                    if l.decode('utf8').strip() == "":
                        self.line_null = self.line_null + 1
        return self

    def display(self):
        print (u"代码行数为：" + str(self.start-1))
        print (u"其中空行为：" + str(self.line_null))





if __name__ == '__main__':
    directory = sys.argv[1:][0]
    print (directory)
    CountCodeLines(directory).count_code().display()
