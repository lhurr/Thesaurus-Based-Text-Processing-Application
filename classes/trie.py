'''
Name: Lim Hur
Class: DAAA/FT/2B/02
Admin: 2112589
'''
import re
from typing import Union, Text, Dict

# Trie data structure ( used to build regex patterns )  creates a Trie out of word list. The trie can be exported to Regex pattern.
class Trie:
    def __init__(self):
        self.__trieData : Dict[Text, Union[int, Dict]] = dict()


    def add(self, word_ls):
        for word in word_ls:
            ref = self.__trieData
            for char in word:
                ref[char] = char in ref and ref[char] or {}
                ref = ref[char]
            ref[''] = 1
    
    def pattern(self):
        return self.__get_regex(self.__trieData)

    # generate regex from trie
    def __get_regex(self, data):
        if "" in data and len(data.keys()) == 1:
            return None
            # recursion terminal stop is reached the function returns none 
        
        alt = []
        cc = []
        leaf_reached = 0
        for char in data.keys():
            if isinstance(data[char], dict):
        # to check if one layer below is a dict, if is a dict is not the end of the word, if is not a dict it is the end of the word

                try:
                    recurse = self.__get_regex(data[char])
                    #when recursion terminal stop is reached the function returns none 

                    alt.append(re.escape(char) + recurse)
                except Exception as e:
                    # print(e)
                    cc.append(re.escape(char))
            else:
                leaf_reached = 1

        empty = not len(alt) > 0
        if len(cc) > 0:
            if len(cc) == 1:
                alt.append(cc[0])
            else:
                alt.append('[' + ''.join(cc) + ']')
                # join all the keyword on the same level together

        if len(alt) == 1:
            result = alt[0]
        else:
            result = "(?:" + "|".join(alt) + ")"
            # add a non capturing group  and "|" to seperate the different word 

        if leaf_reached:
            if empty:
                result += "?"
            else:
                result = "(?:" + result + ")?"
        return result
