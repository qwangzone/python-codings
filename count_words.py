import sys

class CountWords:

    def __init__(self, filename, word):
        self.filename = filename
        self.word = word
        self.times = 0
        self.dic = {}

    def open_file(self):
        with open(self.filename, 'r') as f:
            content = f.read()
            ls = content.split()

            #print (ls)
            for i in range(0, len(ls)):
                #去除单词中的逗号，点以及空格
                ls[i] = ls[i].strip(",")
                ls[i] = ls[i].strip(".")
                ls[i] = ls[i].strip(" ")
            #print (ls)
            for i in ls:
                if self.word.lower() == i.lower():
                    self.times = self.times+1
            # for i in ls:
            #     if i not in self.dic:
            #         self.dic[i] = 1
            #     else:
            #         self.dic[i] = self.dic[i] + 1
            #     return self.dic

            #print (self.ls)
            return self.times

if __name__ == '__main__':
    filename = sys.argv[1]
    word = sys.argv[2]
    #print (filename)
    print (word)
    print (CountWords(filename, word).open_file())

