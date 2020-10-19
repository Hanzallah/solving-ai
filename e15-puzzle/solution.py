'''
An A* search based solution for the E15 puzzle.
'''
import random

'''
NOTE FROM -> Yusuf Ziya Dilek
Beware that 10 scrambles does not scramble very much, especially top left
does not change much since the empty tile starts from the bottom right
'''
def createPuzzle():
    # Note -1 is the empty tile
    initState = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, -1]]
    for i in range(10):  # The empty tile moves 10 times randomly
        index = getEmptyTilePosition(initState)
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


def getEmptyTilePosition(puzzle):
    rows = len(puzzle)
    columns = len(puzzle[0])
    for i in range(0, rows):
        for j in range(0, columns):
            if puzzle[i][j] == -1:
                index = [i, j]
                return index
    print("There is a problem, no empty tile in this puzzle!!!")


def display(puzzle):
    rows = len(puzzle)
    columns = len(puzzle[0])
    print("-----------------")
    for i in range(0, rows):
        print("| ", end="")
        for j in range(0, columns):
            if puzzle[i][j] == -1:
                if j == 0:
                    print(f"  | ", end="")
                else:
                    print(f"  | ", end="")
            else:
                if j == 0:
                    print(f"{puzzle[i][j]} | ", end="")
                else:
                    print(f"{puzzle[i][j]} | ", end="")
        print()
    print("-----------------")


def main():
    for i in range(10):
        newPuzzle = createPuzzle()
        display(newPuzzle)
        print()


if __name__ == "__main__":
    main()
