import sys

class CountWords:

    def __init__(self, filename, word):
        self.filename = filename
        self.word = word
        self.times = 0

    def open_file(self):
        with open(self.filename, 'r') as f:
            content = f.read()
            ls = content.split()
            #ls = ['some', 'that', 'some', 'wq', 'sjsaj', 'smsma', 'wangqi,']
            print (ls)
            for i in range(0,len(ls)):
                #print(ls[i])
                #print (content.split()[i])
                ls[i]=ls[i].strip(",")
            print (ls)
            for i in ls:
                #print (i)
                if self.word.lower() == i:
                    self.times = self.times+1
            #print (self.ls)
            return self.times
"""
    def count_times(self):
        for i in self.ls:
            if self.word == i:
                self.times += 1
        return self.times
"""
if __name__ == '__main__':
    #filename = sys.argv[1]
    #word = sys.argv[2]
    #print (filename)
    #print (word)
    #print (type(CountWords(filename).open_file()))
    print (CountWords("test.txt","wangqi").open_file())
