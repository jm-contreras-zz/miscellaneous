# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:45:17 2014
@author: Juan Manuel Contreras (juan.manuel.contreras.87@gmailcom)

Monty Hall problem (http://en.wikipedia.org/wiki/Monty_Hall_problem) simulator.
Inspired by Harvard Universiy's CS109 Data Science (http://bit.ly/1agO1GB).

Once imported, monty_hall's method 'simulate' is called with three variables.
    n_doors = number of doors in the game
    switch  = guess strategy after goat reveal (0 = don't switch, 1 = switch)
    n_sim   = number of simulations to run
"""

def simulate(n_doors, switch, n_sim):

    # Import modules
    from numpy import array, mean, random

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
        # If only one door, choose it
        if len(can_host_goat) == 1:
            goat_doors[i] = can_host_goat[0]
        # Otherwise, choose between the two options
        else:
            goat_doors[i] = random.choice(can_host_goat, 1)[0]
            goat_doors = array(goat_doors)
    
    # Switch guesses, if it is part of the strategy
    if switch:
        for i in range(n_sim):
            guesses[i] = list(set(doors) - set([guesses[i], goat_doors[i]]))[0]
        with_without = 'With'
    else:
        with_without = 'Without'

    # Calculate the percentage of correct guesses
    percentage = int(round(100 * mean(prize_doors == guesses)))    
    
    # Report results
    print with_without + ' a switching strtegy, a player wins ' + \
          str(percentage) + '% of simulations.'