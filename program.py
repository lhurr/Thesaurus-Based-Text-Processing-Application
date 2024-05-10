'''
Name: Lim Hur
Class: DAAA/FT/2B/02
Admin: 2112589
'''

# Imports
from utils import Utils
from classes.thesaurus import Thesaurus
from random import shuffle, choice
from classes.summary import TextSummarization
from classes.text_process import TextProcessor

class Program:
    def __init__(self, config):
        # Load config regarding assignment details
        # thesaurus is None when program starts
        self.__name, self.__admin, self.__class = config['author']['name'], config['author']['adminNo'], config['author']['class']
        self.__module = config['application_welcome']
        self.__module_code = config['module_code']
        self.__thesaurus = None

    # Run the main loop/menu of the program. Allows users to move between the options.
    def run(self):
        self.__print_start()
        while True:
            Utils.press_anywhere()
            starting_choices = ['New', 'Open', 'Sort', 'Process Text', 'Text Summarization', 'Text Searching','Print', 'Save', 'Save as', 'Exit']
            user_choice = Utils.get_number_choice(arr_choices=starting_choices)
            if user_choice == 1:
                self.__choice1()
            elif user_choice == 2:
                self.__choice2()
            elif user_choice == 3:
                self.__choice3()
            elif user_choice == 4:
                self.__choice4()
            elif user_choice ==5:
                self.__choice5()
            elif user_choice == 6:
                self.__choice6()
            elif user_choice == 7:
                self.__choice7()
            elif user_choice == 8:
                self.__choice8()
            elif user_choice == 9:
                self.__choice9()
            elif user_choice == 10:
                self.__choice10()
                return
    # Print initial banner and assignment details
    def __print_start(self):
        print('*' * 57)
        print(f'''* {self.__module}\t*''')
        print('*' + '-' * 55 + '*')

        print('*',' '*53 ,'*')
        print("""*  -""", 'Done by:', f'{self.__name}({self.__admin})', ' '*24, '*')
        print("""*  -""", 'Class:', f'{self.__class}', ' '*32, '*')
        print('*' * 57)
    
    # Option 1: Allows user to set up NEW thesaurus 
    def __choice1(self):
        print('\nWe will be starting a new Thesaurus.\nYou may now enter a series of keywords and their synonyms.\n')
        self.__thesaurus = Thesaurus.new_thesaurus()
        # Check if thesaurus exists, else return to option menu
        if not self.__thesaurus:
            return  
        print()
        print('Your new thesaurus is ready and printed here....')
        print(self.__thesaurus)
        
    # Option 2: Allow user to set up new thesaurus from .txt file
    def __choice2(self):
        thesaurus_file = Thesaurus.read_thesaurus_file()
        # Check if thesaurus file exists
        if thesaurus_file:
            self.__thesaurus = thesaurus_file
            print(self.__thesaurus)
            print()
        
    # Option 3: Different sorting conditions
    def __choice3(self):
        # Check if thesaurus exists
        if not self.__thesaurus:
            print('You dont have any thesaurus')
            return
        sort_ls = ['Alphabetically (Default)', 'Length/Alphabetically', 'Length/Random Alphabetically', 'Randomly', 'Back to main menu']
        sort_choice = Utils.get_number_choice(sort_ls)
        if sort_choice == 1:
            self.__thesaurus = self.__thesaurus.custom_sort()
            # Default sorting (Alphabetically)
        elif sort_choice == 2:
            self.__thesaurus = self.__thesaurus.custom_sort( [len, 'alphabet'] )
            # Sorting by length/alphabetically
        elif sort_choice == 3:
            self.__thesaurus = self.__thesaurus.custom_sort( choice )
            # Sort by length/random alphabetically
        elif sort_choice == 4:
            self.__thesaurus = self.__thesaurus.custom_sort( shuffle )
            # Sort randodmly
        else:
            return
        print('Sorting Synonyms: {}'.format(sort_ls[sort_choice-1]))
        print(self.__thesaurus)
    # Choice 4: Text processing, for simplified and elegant writing
    def __choice4(self):
        if not self.__thesaurus:
            print('You dont have any thesaurus')
            return  
        data ,input_file = Utils.get_file_data(msg='Select the file you want to process')
        if input_file == '':
            return
        
        print('The text before processing:')
        print(data, '\n')

        Utils.press_anywhere()
        print('Next choose a text processing option.\n')
        writing_choice = Utils.get_number_choice(['Simplified Writing', 'Elegant writing', 'Back to Main Menu'])
        if writing_choice in {1,2}:
            thesaurus_variant = self.__thesaurus if writing_choice == 2 else {item: key for key ,ls in self.__thesaurus.items() for item in ls}
            self.__processor = TextProcessor(thesaurus= thesaurus_variant, word_ls= thesaurus_variant.keys() )
            print('Processing Text for: {}\n'.format('Elegant writing' if writing_choice==2 else 'Simplified Writing'))
            try:
                final_text = self.__processor.replace(text=data)
            except:
                return
        else:
            return
        print('The text after processing:\n{}\n'.format(final_text))
        Utils.press_anywhere()

        save_to_file = ''
        while save_to_file not in ['y', 'n']:
            save_to_file = input('Do you want to save the text into a file? y/n: ').strip()
        if save_to_file == 'y':
            _ = Utils.save_as_file(final_text, medium = 'The text has been saved in "{}"')

    # Choice5 : Advance feature: Text Summarization
    def __choice5(self):
        data ,input_file = Utils.get_file_data(msg='Select the file you wish to summarize')
        if input_file == '':
            return
        print('Your file {} you wish to summarize is printed here:'.format(input_file))
        print(data)
        Utils.press_anywhere()
        
        summary = TextSummarization(data, top_n=5)
        summary.get_freq_list()
        print('Your file after summarization:\n')
        print(summary.get_main_message())
        

    # Choice 6: Text Searching
    def __choice6(self):
        print('We will be performing text searching')
        data ,input_file = Utils.get_file_data(msg='Select the file you wish to perform text searching on')
        if input_file == '':
            return
        word_ls = Utils.get_word_ls()
        if len(word_ls) <1:
            return
        searcher = TextProcessor(thesaurus=None, word_ls= word_ls)
        final_text = searcher.search(text=data)
        if final_text is None:
            final_text = 'No search matches'
        print('\nPrinting out search summary now (**Printing out sentences that contains searched (words searched printed in [ ])**):\n')
        print(final_text)

    # Choice 7: printing of thesaurus (self.__thesaurus.tracker is used to track if user opened thesaurus from file or set up from user validation)
    def __choice7(self):
        if not self.__thesaurus:
            print('You dont have any thesaurus')
            return  
        print('The thesaurus {} is printed here....'.format('that you created' if self.__thesaurus.tracker == 1 else self.__thesaurus.tracker))
        print(self.__thesaurus)

    # Option 8: Save option for existing thesaurus that has file
    def __choice8(self):
        try:
            if self.__thesaurus.tracker ==1:
                print('The thesaurus doesnt have an existing file. Please save as instead')
                return
        except:
            print('Please make sure thesaurus is available')
            return
        # Set mode to 'w' to overwrite the file.
        _ = Utils.save_as_file(self.__thesaurus, mode='w', saved_existing_file=self.__thesaurus.tracker) 

        
    # Option 9: Allow user to save into new text file
    def __choice9(self):
        if not self.__thesaurus:
            print('You dont have any thesaurus! Please choose New or Open to load a thesaurus')
            return            
        print('Save As')
        saved_file = Utils.save_as_file(self.__thesaurus) # Save thesaurus into text file.
        # Sets the tracker to the newly saved as file
        if saved_file is not None:
            self.__thesaurus.tracker = saved_file 

    # Friendly goodbye message for user
    def __choice10(self):
        print()
        print(f'Bye, thanks for using {self.__module_code} DSAA: Thesaurus Based Text Processor')