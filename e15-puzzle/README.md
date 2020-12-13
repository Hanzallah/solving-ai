# AI-461 Homework 02

`solution.py` contains the solution we have come up with for the E15 puzzle problem.

-> An A* search based solution for the E15 puzzle.

-> We used h1: number of misplaced tiles as the admissible heuristic. Proof:
h1 is an admissible heuristic for the 15-puzzle, since every tile that is out
of position must be moved at least once

-> We used generator(createPuzzle())  to obtain a dozen distinct initial states
of the E15-puzzle.

Just run the code and 12 E15 puzzles will be created and solved. The Initial
puzzle and the solution path will be outputted on the console.

**Note:** The specific run we used in the .pdf can be found in the Juptyr Notebook
file. Since puzzles are generated randomly, you will get different set of
dozen puzzles when you run the code.
