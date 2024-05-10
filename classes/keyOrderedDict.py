'''
Name: Lim Hur
Class: DAAA/FT/2B/02
Admin: 2112589
'''
from utils import Utils

# Custom Data structure for key ordered dictionary.
# We have a list that keeps track of the keys, and because of the fact (dictionary keys are immutable)
class KeyOrderedDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self._keys_ls = list(kwargs)
        self.__isSorted = False
    def __setitem__(self,k,v):
        if not k in self:
            self._keys_ls.append(k)
            self.__isSorted = False
        super().__setitem__(k,v)
    def __getitem__(self,k):
        return super().__getitem__(k)
    def __contains__(self, k):
        return super().__contains__(k)
    # Clears the list and the dictionary
    def clear(self):
        super().clear()
        del self._keys_ls 
        self._keys_ls = []
    def __iter__(self):
    # Overload __iter__ magic method (Default sort the keys)
        if not self.__isSorted:
            self._keys_ls = Utils.quick_sort(self._keys_ls, sort_func=None)
            self.__isSorted = True
        return iter(self._keys_ls)