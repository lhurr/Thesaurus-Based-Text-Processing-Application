'''
Name: Lim Hur
Class: DAAA/FT/2B/02
Admin: 2112589
'''

from program import Program

# Application configuration in dictionary format that can be changed.
APP_CONFIG = {'author':
    {'name': 'Lim Hur', 
    'class': 'DAAA/2B/02', 
    'adminNo': '2112589'}, 
    'application_welcome': """ST1507 DSAA: Welcome to:\t\t\t\t*\n*\t\t\t\t\t\t\t*\n*  ~ Thesaurus Based Text Processing Application ~""",
    'module_code': 'ST1507', 
    'print': 'h'}

# Runs the main program
program = Program(APP_CONFIG)
program.run()
