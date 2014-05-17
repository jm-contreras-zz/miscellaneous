# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:45:17 2014
Monty Hall problem (http://en.wikipedia.org/wiki/Monty_Hall_problem) simulator.
Inspired by Harvard University's CS109 Data Science (http://bit.ly/1agO1GB).
@author: Juan Manuel Contreras (juan.manuel.contreras.87@gmailcom)

The user must specify 4 variables.
n_doors  = the number of doors in the game
n_open   = the number of doors opened by the host
switch   = should the door be switched after the goat reveal? 0 = no, 1 = yes
n_sim    = the number of simulations to run 
"""

def simulator(n_doors, n_open, switch, n_sim):

    # Import modules
    from numpy import mean, random

    # Create array of doors
    doors = range(n_doors)
    
    # Assign prize doors
    prize_doors = random.choice(doors, n_sim)
    
    # Simulate guesses
    guesses = random.choice(doors, n_sim)
    
    # Open goat doors    
    goat_doors = [None] * n_sim
    for i in range(n_sim):
        # Determine which doors can host the goats (no prize, not guessed)
        can_host_goat = list(set(doors) - set([prize_doors[i], guesses[i]]))
        # If the guessed door has the prize, choose which goat door to open
        goat_doors[i] = random.choice(can_host_goat, n_open, replace=False)
    # Switch guesses, if part of strategy
    if switch:
        for i in range(n_sim):
            this_goat_list = list(goat_doors[i])
            this_goat_list.append(guesses[i])
            possible_guesses = list(set(doors) - set(this_goat_list))
            guesses[i] = random.choice(possible_guesses, 1)[0]
        word_report = 'With'
    else:
        word_report = 'Without'
    # Calculate percentage of correct guesses
    percentage = mean(prize_doors == guesses) * 100
    
    # Report results
    print '%s a switching strategy, you win %s of simulations.' % \
    (word_report, int(percentage))
