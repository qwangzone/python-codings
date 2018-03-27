'''
写一个函数is_isogram来判断单词是否是isogram。

isogram的逻辑是

单词里没有重复的字符
空格和中划线-可以重复
下面的单词都是isogram的

lumberjacks
background
downstream
six-year-old
'''
def is_isogram_old(word):
    dic1 = {}
    for i in word.lower():
        if i == ' ':
            continue
        elif i == '-':
            continue
        elif i not in dic1:
            dic1[i] = 1
        else:
            dic1[i] = dic1[i] + 1

    for key, value in dic1.items():
        #print(key, value)
        if value > 1:
            yield False
        else:
            yield True
def is_isogram(word):
    lis = []
    for a in is_isogram_old(word):
        lis.append(a)
    if False in lis:
        return False
    else:
        return True

import unittest




# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class TestIsogram(unittest.TestCase):

    def test_empty_string(self):
        self.assertIs(is_isogram(""), True)

    def test_isogram_with_only_lower_case_characters(self):
        self.assertIs(is_isogram("isogram"), True)

    def test_word_with_one_duplicated_character(self):
        self.assertIs(is_isogram("eleven"), False)

    def test_longest_reported_english_isogram(self):
        self.assertIs(is_isogram("subdermatoglyphic"), True)

    def test_word_with_duplicated_character_in_mixed_case(self):
        self.assertIs(is_isogram("Alphabet"), False)

    def test_hypothetical_isogrammic_word_with_hyphen(self):
        self.assertIs(is_isogram("thumbscrew-japingly"), True)

    def test_isogram_with_duplicated_hyphen(self):
        self.assertIs(is_isogram("six-year-old"), True)

    def test_made_up_name_that_is_an_isogram(self):
        self.assertIs(is_isogram("Emily Jung Schwartzkopf"), True)

    def test_duplicated_character_in_the_middle(self):
        self.assertIs(is_isogram("accentor"), False)

    # Additional tests for this track

    def test_isogram_with_duplicated_letter_and_nonletter_character(self):
        self.assertIs(is_isogram("Aleph Bot Chap"), False)


if __name__ == '__main__':
    unittest.main()







