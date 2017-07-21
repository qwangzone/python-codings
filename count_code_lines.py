import sys
import os
class CountCodeLines:
    def __init__(self, directory):
        self.directory = directory

    def count_code(self):
        start = 1
        line_null = 0
        dirs = os.listdir(self.directory)
        for file in dirs:
            if file.split('.')[-1] == "txt":
                print (file)
                with open(file, 'r') as f:
                    for l in f.readlines():
                        print (str(start) + "、" + l)
                        start = start + 1
                        if l.strip() == "":
                            line_null = line_null + 1

        print (u"代码行数为：" + str(start-1))
        print (u"其中空行为：" + str(line_null))





if __name__ == '__main__':
    file = sys.argv[1:][0]
    print (file)
    CountCodeLines(file).count_code()



