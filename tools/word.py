'''
Name: Lim Hur
Class: DAAA/FT/2B/02
Admin: 2112589
'''
from random import choice
# Word class for sorting of synonyms
class Word(str):

    sort_func = None

    def __hash__(self):
        return super().__hash__()
    def __gt__(self, other):
        if Word.sort_func is not None:
            if isinstance(Word.sort_func, list):
                return super().__gt__(other) if len(self) == len(other) else len(self) > len(other)
            
            elif Word.sort_func.__name__ == 'choice':
                # If sort by length/randomly then we return randomly true or false
                return Word.sort_func([True,False]) if len(self) == len(other) else len(self) > len(other)

            return Word.sort_func(self) > Word.sort_func(other)
        else:
            return super().__gt__(other)
    def __lt__(self, other):
        if Word.sort_func is not None:
            # If sort by length/randomly then we return randomly true or false
            if isinstance(Word.sort_func, list):
                return super().__lt__(other) if len(self) == len(other) else len(self) < len(other)
            
            elif Word.sort_func.__name__ == 'choice':
                return Word.sort_func([True,False]) if len(self) == len(other) else len(self) < len(other)

            return Word.sort_func(self) < Word.sort_func(other)
        else:
            return super().__lt__(other)
            
        