import sys
class Cat:
    def __init__(self, file):
        self.file = file

    def open(self):
        for path in self.file:
            with open(path, 'r') as f:
                print (f.read())

    def open_lines(self):
        for path in self.file:
            with open(path, 'r') as f:
                start = 1
                for line in f.readlines():
                    print ("%s %s" %(start, line))
                    start = start + 1

if __name__ == '__main__':
    file = sys.argv[1:]
    print (sys.argv)
    if "-n" in file:
        file.remove("-n")
        Cat(file).open_lines()
    else:
        Cat(file).open()