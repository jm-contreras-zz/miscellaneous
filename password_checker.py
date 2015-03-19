# -*- coding: utf-8 -*-
"""
Created on Wed May 07 16:16:42 2014

password_checker.py receives command-line input as a comma-delimited list of
passwords and checks if each is valid according to these criteria:

1) between 6 and 12 characters
2) at least 2 letters (1 lowercase, 1 uppercase)
3) at least 1 number
4) at least 1 symbol from this list [$, #, @]

For each password, password_checker.py prints a message indicating that it is
valid or, alternatively, the reason why it is invalid.

SAMPLE INPUT
'ABd1234@1,a F1#,2We3345'

SAMPLE OUTPUT
Password ABd1234@1 is acceptable!
Password a F1# is shorter than 6 characters.
Password 2We3345 does not include a required symbol [$, #, @].

@author: juan.manuel.contreras.87@gmail.com
"""

# Import modules
from sys import argv
from re import search

def main(passwords):
    
    # Declare an empty text key
    text = None
    
    # Iterate through all passwords
    for p in passwords:
        
        # Check length
        n_char = len(p)   
        if n_char < 6:
            text = 'is shorter than 6 characters.'
        elif n_char > 12:
            text = 'is longer than 12 characters.'
        
        # Check characters
        if not search('[^0-9]+', p):
            text = 'does not include a number (0-9).'
        elif not search('[^a-z]+', p):
            text = 'does not include a lowercase letter (a-z).'
        elif not search('[^A-Z]+', p):
            text = 'does not include an uppercase letter (A-Z).'
        elif not search('\$|\#|\@', p):
            text = 'does not include a required symbol [$, #, @].'
        
        # Assess validity
        if not text:
            text = 'is acceptable!'
        
        # Print assessment
        print 'Password %s %s' % (p, text)
        
        # Reset the text key
        text = None
        
if __name__ == '__main__':

    main(argv[1].split(','))
