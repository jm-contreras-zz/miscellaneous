# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:45:17 2014
Monty Hall problem (http://en.wikipedia.org/wiki/Monty_Hall_problem) simulator.
Inspired by Harvard Universiy's CS109 Data Science (http://bit.ly/1agO1GB).
@author: Juan Manuel Contreras (juan.manuel.contreras.87@gmailcom)
"""

# Import modules
from numpy import array, mean, random

# Declarations
n_doors = 3   # Number of doors
switch  = 1   # Switch doors after goat reveal? 0 = No, 1 = Yes
n_sim   = 100 # Number of simulations

# Create array of doors
doors = range(n_doors)

# Assign prize doors
prize_doors = random.choice(doors, n_sim)

# Simulate guesses
guesses = random.choice(doors, n_sim)

# Open goat doors    
goat_doors = [None] * n_sim
for i in range(n_sim):
    can_host_goat = list(set(doors) - set([prize_doors[i], guesses[i]]))
    if len(can_host_goat) == 1:
        goat_doors[i] = can_host_goat[0]
    else:
        goat_doors[i] = random.choice(can_host_goat, 1)[0]
goat_doors = array(goat_doors)

# Switch guesses, if part of strategy
if switch:
    for i in range(n_sim):
        guesses[i] = list(set(doors) - set([guesses[i], goat_doors[i]]))[0]

# Calculate percentage of correct guesses
percentage = mean(prize_doors == guesses)
