'''
An A* search based solution for the E15 puzzle.
'''
import random

'''
NOTE FROM -> Yusuf Ziya Dilek
Beware that 10 scrambles does not scramble very much, especially top left
does not change much since the empty tile starts from the bottom right
'''


class Node:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.estimatedDistanceToGoal = self.h1Heuristic()

    # Override EQUALS (==)
    def __eq__(self, other):
        rows = len(self.puzzle)
        columns = len(self.puzzle[0])
        for i in range(0, rows):
            for j in range(0, columns):
                if self.puzzle[i][j] != other.puzzle[i][j]:
                    return False
        return True

    # Override LESS THAN (<)
    def __lt__(self, other):
        if self.estimatedDistanceToGoal < other.estimatedDistanceToGoal:
            return True
        else:
            return False

    # Override GREATER THAN (>)
    def __gt__(self, other):
        if self.estimatedDistanceToGoal > other.estimatedDistanceToGoal:
            return True
        else:
            return False

    # GET possible Nodes that we can go from this Node
    def getAllNextPossibleNodes():
        print("DO this next")

    # Find the admissable heuristic of this puzzle
    def h1Heuristic(self):
        h1 = 0
        rows = len(self.puzzle)
        columns = len(self.puzzle[0])
        finalState = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, -1]]
        for i in range(0, rows):
            for j in range(0, columns):
                if (self.puzzle[i][j]-finalState[i][j]) != 0:
                    h1 = h1 + 1
        return h1

    # Get the position of the empty tile [row, column]
    def getEmptyTilePosition(self):
        rows = len(self.puzzle)
        columns = len(self.puzzle[0])
        for i in range(0, rows):
            for j in range(0, columns):
                if self.puzzle[i][j] == -1:
                    index = [i, j]
                    return index
        print("There is a problem, no empty tile in this puzzle!!!")

    #  Display the Puzzle in a neat way
    def display(self):
        rows = len(self.puzzle)
        columns = len(self.puzzle[0])
        print("-----------------")
        for i in range(0, rows):
            print("| ", end="")
            for j in range(0, columns):
                if self.puzzle[i][j] == -1:
                    if j == 0:
                        print(f"  | ", end="")
                    else:
                        print(f"  | ", end="")
                else:
                    if j == 0:
                        print(f"{self.puzzle[i][j]} | ", end="")
                    else:
                        print(f"{self.puzzle[i][j]} | ", end="")
            print()
        print("-----------------")


# Just call this function and it returns distinct Puzzle
def createPuzzle():
    # Note -1 is the empty tile
    nd = Node([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, -1]])
    initState = nd.puzzle
    for i in range(10):  # The empty tile moves 10 times randomly
        index = nd.getEmptyTilePosition()
        emptyTileRow = index[0]
        emtyTileCol = index[1]

        randomTileShift = random.randint(0, 1)  # 0 is vertical, 1 is horizontal
        if randomTileShift == 0:  # vertical
            randomTileShiftUporDown = random.randint(0, 1)  # Random 0 is UP, 1 is DOWN
            if randomTileShiftUporDown == 0:  # VERTICAL UP
                if index[0] == 0:  # Top line can't shift up one more times
                    temp = initState[emptyTileRow+1][emtyTileCol]
                    initState[emptyTileRow+1][emtyTileCol] = -1
                    initState[emptyTileRow][emtyTileCol] = temp
                else:
                    temp = initState[emptyTileRow-1][emtyTileCol]
                    initState[emptyTileRow-1][emtyTileCol] = -1
                    initState[emptyTileRow][emtyTileCol] = temp
            elif randomTileShiftUporDown == 1:  # VERTICAL DOWN
                if index[0] == 3:  # this line can't go DOWN
                    temp = initState[emptyTileRow-1][emtyTileCol]
                    initState[emptyTileRow][emtyTileCol-1] = -1
                    initState[emptyTileRow][emtyTileCol] = temp
                else:
                    temp = initState[emptyTileRow+1][emtyTileCol]
                    initState[emptyTileRow+1][emtyTileCol] = -1
                    initState[emptyTileRow][emtyTileCol] = temp
        elif randomTileShift == 1:  # horizontal
            randomTileShiftRightorLeft = random.randint(0, 1)  # Random RIGHT is 0, LEFT is 1
            if randomTileShiftRightorLeft == 0:  # HORIZONTAL RIGHT
                if index[1] == 3:
                    temp = initState[emptyTileRow][emtyTileCol-1]
                    initState[emptyTileRow][emtyTileCol-1] = -1
                    initState[emptyTileRow][emtyTileCol] = temp
                else:
                    temp = initState[emptyTileRow][emtyTileCol+1]
                    initState[emptyTileRow][emtyTileCol+1] = -1
                    initState[emptyTileRow][emtyTileCol] = temp
            elif randomTileShiftRightorLeft == 1:  # HORIZONTAL LEFT
                if index[1] == 0:
                    temp = initState[emptyTileRow][emtyTileCol+1]
                    initState[emptyTileRow][emtyTileCol+1] = -1
                    initState[emptyTileRow][emtyTileCol] = temp
                else:
                    temp = initState[emptyTileRow][emtyTileCol-1]
                    initState[emptyTileRow][emtyTileCol-1] = -1
                    initState[emptyTileRow][emtyTileCol] = temp

    #print(initState)
    return initState


def main():
    '''
    Just Testing the functions and classes
    '''
    '''
    for i in range(10):
        newPuzzle = createPuzzle()
        display(newPuzzle)
        print()
    '''
    '''
    nd = Node([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, -1]], 3)
    print(nd.puzzle)
    nd2 = Node([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, -1]], 5)
    if nd < nd2:
        print("Less than")
    else:
        print("Not less")
    '''
    '''
    puzzle = createPuzzle()
    print(puzzle)
    print(h1Heuristic(puzzle))
    '''
    nd = Node(createPuzzle())
    nd.display()
    print(f"h1 heuristic = {nd.estimatedDistanceToGoal}")


if __name__ == "__main__":
    main()
