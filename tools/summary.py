'''
Name: Lim Hur
Class: DAAA/FT/2B/02
Admin: 2112589
'''
from .word import Word
from .frequencyWord import FrequencyWord
from utils import Utils
import re
# Text summarization class to return top N words
class TextSummarization:
    def __init__(self, text, top_n = 5) -> None:
        self.text = text
        self.top_n = top_n
    def get_freq_list(self):
        word_dict = {}
        for line_idx, line in enumerate(self.text.splitlines()):
            for word_index, word in enumerate(line.strip().split(sep=' ')):
                if word in word_dict.keys():
                    word_dict[word].increment_frequency()
                else:
                    word_dict[word] = FrequencyWord(word=re.sub('[^A-Za-z0-9]+','',word) )
        self.word_ls = word_dict.values()
    # Prints out the occurances of the words
    def get_main_message(self):
        msg_out = ''
        sorted_ls = Utils.quick_sort(list(self.word_ls), sort_func=None)
        for word in sorted_ls[-self.top_n:]:
            msg_out += f'{word} : {str(word.get_frequency())} Occurences \n' 
        return msg_out






