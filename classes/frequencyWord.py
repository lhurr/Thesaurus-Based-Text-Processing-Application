'''
Name: Lim Hur
Class: DAAA/FT/2B/02
Admin: 2112589
'''
from .word import Word

# Word object that keeps track of frequency of occurences
class FrequencyWord(Word):
    def __new__(self, word):
        self.__freq = 1
        return super().__new__(FrequencyWord,word)
    def increment_frequency(self):
        self.__freq +=1
    def get_frequency(self):
        return self.__freq
    def __lt__(self, other):
        return self.__freq < other.__freq
    def __gt__(self, other):
        return self.__freq > other.__freq
