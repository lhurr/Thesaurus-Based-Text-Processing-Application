'''
Name: Lim Hur
Class: DAAA/FT/2B/02
Admin: 2112589
'''
import os,random,re
from os.path import exists,isfile
from typing import List, Tuple

# Utilities class to support our main program. Contains functions for general purpose.
class Utils:
    @staticmethod
    def press_anywhere(): 
        # Allows users to press key to continue
        if os.name == 'nt':
            print('\nPress Any key, to continue....', end=' ')
            os.system('pause >nul')
            print('\n')
        else:
            os.system("""bash -c 'read -s -n 1 -p "Press Any Key, to continue..."'""")
            print('\n')

    # Method for 'SAVE' & 'SAVE AS'
    # Gets a valid output filename from user. If user does not properly enter, prompts error to obtain a valid filename
    # Allows users to specify an empty input, to exit the prompt
    # 
    @staticmethod
    def save_as_file(message, medium = 'Your file "{}" has been saved.', mode='x', saved_existing_file=False):
        while True:
            try:
                save_file = input('Please enter new filename: ').strip() if not saved_existing_file else saved_existing_file
                if save_file == '':
                    return
                assert save_file.endswith('.txt'), 'Specify text file (.txt)'
                assert not bool(re.match(r'[\\/*?:"<>|]', save_file)), 'Filename with illegal special characters!'
                # check special characters
                
                with open(save_file, mode=mode) as f:
                    f.write(str(message) + '\n')
                print(medium.format(save_file))
                # print()
                return save_file
            except (FileExistsError, AssertionError) as e:
                print(e)
                continue

    # Opens a file, and return file data and file name
    @staticmethod
    def get_file_data(msg = 'We will be opening an existing thesaurus'):
        while True:
            print()
            if msg:
                print(msg)
            try:
                io_file = input('Please enter input file: ').strip()
                if io_file == '':
                    return False , io_file
                assert exists(io_file), 'Invalid file (doesnt exist)'
                assert isfile(io_file), 'Not a file'
                assert io_file.endswith('.txt'), 'Make sure it ends with .txt!'
                with open(io_file, 'r') as f:
                    data = f.read()
                return data, io_file
            except (OSError, Exception) as e:
                print(e)
                continue

    # Obtains numerical choice from user.
    @staticmethod
    def get_number_choice(arr_choices):
        # Forces user to enter numerical integer within the required range, else prompts user to re enter
        while True:
            min,max = 1,len(arr_choices)
            choices = list(f'\t{idx+1}: {words}' for idx, words in enumerate(arr_choices))
            message = f"Please select your choice: {str(tuple(range(1,len(arr_choices)+1))).replace(' ', '') }\n" + '\n'.join(choices) + '\nEnter choice: '
            try:
                user_inp = int(input(message).strip())
                if user_inp >=min and user_inp<=max:
                    return user_inp
                else:
                    print(f'Not an Integer between {min} to {max}')
                    continue
            except Exception:
                print(f'Not an Integer between {min} to {max}')
                continue

    # Simple validator to validate and print out errors
    @staticmethod
    def simple_validator(arr: List[Tuple[bool,str]]  ):
        # Simple validator that returns true/false
        for condition in arr:
            if condition[0]:
                print(condition[1])
                # Print errors
                print()
                return False
        else:
            return True       

    # Quick sort function (Divide and conquer algorithm), recursively sorts O nlogn
    @staticmethod
    def quick_sort(array, sort_func = None):
        if callable(sort_func) and sort_func.__name__ == 'shuffle':
            random.shuffle(array)
            return array
        
        less = []
        pv_list = []
        greater = []
        # Return arr if less than equal to 1 element
        if len(array) <=1:
            return array
        else:
            pivot = array[0]
            for x in array:
                if x < pivot:
                    less.append(x)
                elif x > pivot:
                    greater.append(x)
                else:
                    pv_list.append(x)
            lesser = Utils.quick_sort(less, sort_func)
            bigger = Utils.quick_sort(greater, sort_func)
            
            return lesser + pv_list + bigger

    # method to validate keywords and synonyms of a thesaurus
    # Only allows for alphabets and single word for KEYWORD. Only allows alphabets for synonyms
    @staticmethod
    def entry_validator(data:str, synonym = False):
        if synonym: return (not bool(re.match('^[a-zA-Z -]*$', data)))
        return (not bool(re.match('^[A-Za-z]+[-]*[A-za-z]*$', data)))

    
    # Get words that user wishes to search (Advance Feature 5)
    @staticmethod
    def get_word_ls():
        user_inp, word_ls = False, []
        while user_inp != '':
            user_inp = input('Please enter the word you wish to find! (Enter to finish): ').strip()
            if user_inp == '':
                break
            word_ls.append(user_inp)
        return word_ls
