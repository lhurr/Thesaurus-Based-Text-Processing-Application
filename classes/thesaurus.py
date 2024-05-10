'''
Name: Lim Hur
Class: DAAA/FT/2B/02
Admin: 2112589
'''
import re
from utils import Utils
from classes.keyOrderedDict import KeyOrderedDict
from .word import Word

class Thesaurus(KeyOrderedDict):
    def __init__(self, dictionary: KeyOrderedDict, tracker):
        super().__init__(**dictionary)
        self.tracker = tracker
        if self:
            self.custom_sort()
        # Tracker to see if the thesaurus was loaded via user input (manually keyed in) or via text file.
        # 1 is for thesaurus loaded via user input, <filename> is for thesaurus loaded via .txt file
    #Creates new thesaurus (returns a class method)
    @classmethod
    def new_thesaurus(cls):
        key_ordered_dict = KeyOrderedDict()
        add_keyword = 'y'
        while add_keyword == 'y':
            keyword, synonym, add_keyword = cls.__get_thesaurus_entry(key_ordered_dict)
            if keyword == '':
                return cls(key_ordered_dict,1)
            else:
                key_ordered_dict[keyword] = synonym
        return cls(key_ordered_dict, 1)

    @staticmethod
    def __get_thesaurus_entry(key_ordered_dict:KeyOrderedDict):
        while True:
            synonyms = list()
            user_inp = True
            try:
                keyword = input('Enter keyword: ').strip().lower()
                if keyword == '':
                    return keyword, None,'n'
                keyword_cond = Utils.simple_validator([
                    (keyword in key_ordered_dict.keys() , 'Error! Keyword already exists'),
                    (any( [keyword in lst for lst in key_ordered_dict.values()] ),'Keyword has already been recorded as a synonym!' ),
                    (Utils.entry_validator(keyword), 'Keyword should only contain alphabets and length of ONE word')
                ])
                if not keyword_cond:
                    continue
                
                print(f'\nYou may enter one or more synonyms for "{keyword}"\n(please press "Enter" once done).')

                while user_inp != '':

                    user_inp = input(f'Enter synonym for "{keyword}": ').strip().lower()
                    if user_inp == '':
                        break
                    syn_condition = Utils.simple_validator([
                        (bool(user_inp == keyword), 'Do not repeat keyword for synonym'), 
                        (bool(user_inp in synonyms), f'Synonym {user_inp} for {keyword} keyword only allowed once! Failed to add synonym'),
                        (any( [((key == user_inp) or (user_inp in v)) for key,v in key_ordered_dict.items()] ), 'Error! Make sure synonym is not an existing keyword or repeated across different keywords' ),
                        (Utils.entry_validator(user_inp, synonym=True), 'Synonym should only contain alphabets')
                    ])

                    if syn_condition:
                        synonyms.append(Word(user_inp))

                assert len(synonyms) >= 1, 'No recorded synonyms'

                more_kw = ''
                while more_kw not in ['y', 'n']:
                    more_kw = input('Do you want to add more keywords? y/n: ').strip()
                
                return keyword,synonyms, more_kw
            except Exception as e:
                print(e)
                continue

# Read thesaurus file
    @classmethod
    def read_thesaurus_file(cls):
        while True:
            key_ordered_dict = KeyOrderedDict()
            try:
                txt, file_name = Utils.get_file_data()
                if file_name == '':
                    return
 
                data = re.sub('[,][ ]*\n' , ',', txt)
                
                # Load data from text file, makes sure that keywords do not repeat
                # Only unique & NON-KEYWORD synonyms are allowed in the thesaurus
                for keys in data.strip().split('\n'):
                    if len(keys.strip()) ==0:
                        continue
                    keyword, value = cls.__get_thesaurus_file_entry(keys)

                    # Assertions for faulty files (to ensure file is in good format)
                    assert not any( map(lambda x: Utils.entry_validator(x, synonym=True), value ) ), 'Synonym cannot contain values'
                    assert keyword != '', 'Empty Keyword detected'
                    assert not Utils.entry_validator(keyword), f'Error! Keyword {keyword} contains non alphabet characters/2 words'
                    assert keyword not in key_ordered_dict.keys(), 'Error! Keyword is repeated'
                    assert not any([ ( (keyword in v) or (k in value) or (bool(set(value) & set(v)) ) )    for k,v in key_ordered_dict.items()]) , \
                    'Error! Synonym is an existing keyword/repeated across different keywords OR keyword appeared in a synonym' 
                    assert not any(map(lambda y : y == keyword, value)), f'Synonym {keyword} cannot be equal to key value'

                    key_ordered_dict[keyword] = value
                print()
                print(f'Thesaurus "{file_name}" has been loaded and is printed here...')
                
                return cls(key_ordered_dict, file_name)
            except AssertionError as err:
                print(err)
                continue
            except Exception:
                print('Error loading, please make sure it is in the thesaurus format')
                continue
            
    # Gets each keyword: synonym entry
    @staticmethod
    def __get_thesaurus_file_entry(keys):
        key = keys.split(':')[0].lower()
        syn_value = list({Word(  word.strip().lower()  ) for word in keys.split(':')[1].split(',') if word.strip() != key and word != '' and not word.isspace() })
        return key,syn_value

    def custom_sort(self, sort_func= None):
        Word.sort_func = sort_func
        # Set the sort function for word; Default is None 
        for val in self:
            self[val] = Utils.quick_sort(self[val], sort_func)
        return self


    def __str__(self):
        output_str = ''
        for val in self:
            output_str += f'{val}: {", ".join(self[val])}' + '\n'
        return output_str[:-1]
