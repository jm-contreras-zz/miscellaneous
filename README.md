miscellaneous
==========
**Repository of various standalone scripts.**

- **helpers.R** contains functions that I use regularly so I source them automatically when I open an R session.
  - **clearws** clears the workspace of the current environment
  - **clock** counts how much time elapses between two lines of code (a la MATLAB's [*tic*](http://www.mathworks.com/help/matlab/ref/tic.html) and [*toc*](http://www.mathworks.com/help/matlab/ref/toc.html))
  - **countUnique** counts the number of unique values in each variable of a matrix or data frame
  - **sourceBatch** sources a batch of .R files in a given directory
  - **stat.mode** and **se** compute the mode and the standard error of the mean, respectively

- **monty_hall.py** runs simulations of the [Monty Hall Problem](http://en.wikipedia.org/wiki/Monty_Hall_problem), allowing the user to specify the number of simulations to run and the game strategy to adopt (switch guesses or not). The user can also change the number of doors in the game and the number of doors opened by the host.

- **num2log.R** contains a function that takes as input a data frame with numeric or mixed variables. It identifies the variables that can be converted to logical type (i.e., only values 0, 1, and NA) and converts them accordingly.

- **password_checker.py** receives command-line input as a comma-delimited list of passwords and checks if each is valid according to specific criteria. For each password, it prints a message indicating that it is valid or, alternatively, the reason why it is invalid.

- **project_euler.py** contains solutions to 20 problems from [Project Euler](http://projecteuler.net/), a website dedicated to computational problems that involve logic and mathematics.
