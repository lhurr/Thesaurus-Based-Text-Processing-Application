'''
Name: Lim Hur
Class: DAAA/FT/2B/02
Admin: 2112589
'''
from .trie import Trie
import re, random
from functools import cached_property
from utils import Utils

# class to perform text processing using regex (Trie regex structure)
class TextProcessor:
    def __init__(self, thesaurus, word_ls ):
        # Takes in thesaurus (if any) and creates a trie from the word list provided
        self.__thesaurus = thesaurus
        self.__regex_gen = Trie()
        self.__regex_gen.add(word_ls= word_ls)

    # Replace synonyms with keyword: make sure capitalization is retained
    def __replace_with_keyword(self, regex_obj):
        word :str = regex_obj.group(0)

        return self.__thesaurus[word.lower()].capitalize() if word[0].isupper() else self.__thesaurus[word.lower()]
    # Replace key words with synonyms: make sure that the capitalization is retained
    def __replace_with_synonym(self, regex_obj):
        word:str = regex_obj.group(0)

        replaced = random.choice(self.__thesaurus[word.lower()])   
        #Select randomly from the synonym list

        return replaced.capitalize() if word[0].isupper() else replaced

    # Compiles the pattern, make sure the matches are case insensitive
    # \b \b ensures that we dont match the substring (e.g dont replace cataaaa with kittyaaaa)
    @cached_property
    def compile(self):
        return re.compile(fr"\b{self.__regex_gen.pattern()}\b", re.IGNORECASE)

    # Perform text replacement for elegant writing and simplified writing
    def replace(self, text):
        return self.compile.sub(self.__replace_with_synonym if isinstance(list(self.__thesaurus.values())[0] , list) else self.__replace_with_keyword , text  )

    # Perform searching on text, return the sentences the string was found in (OPTION 6)
    def search(self,text):
        try:
            rtn_str = ''
            regex_inst = self.compile.pattern
            for sentence in re.split('[?.!]', text):
                for idx,x in enumerate(re.finditer(fr'{regex_inst}', sentence, flags=re.IGNORECASE)):
                    rtn_str += f'{x.group()} : {sentence[:x.start()] + f"[{x.group()}]" + sentence[x.start()+ len(x.group()):] }' + '\n'
        except Exception as e:
            print(e)
            return
        return rtn_str if rtn_str != '' else None
        

        