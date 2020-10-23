'''
An A* search based solution for the E15 puzzle.
We used h1: number of misplaced tiles as the admissable heuristic
h1 is an admissible heuristic for the 15-puzzle, since every tile that is out
of position must be moved at least once
'''
import random
import copy

'''
Node class holds the puzzle as 2D list where -1 is denoting the empty tile and
other variables like estimated distance to goal (underestimate) and total esti-
mation which is  (h1 heuristic + distance between the current node and the start node)

Note that the ==, <, and > are overwritten in this class
'''
class Node:
    def __init__(self, puzzle, distanceFromInitPuzzle):
        self.puzzle = puzzle  # The puzzle itself which is represented by a 2D list where empty tile is -1
        self.estimatedDistanceToGoal = self.h1Heuristic()  # h1 admissable heuristic
        self.distanceFromInitPuzzle = distanceFromInitPuzzle  # Distance from the initial state
        self.totalCost = self.distanceFromInitPuzzle + self.estimatedDistanceToGoal  # Total estimation

    # Override EQUALS (==)
    def __eq__(self, other):  # checks for if puzzle is the same
        rows = len(self.puzzle)
        columns = len(self.puzzle[0])
        for i in range(0, rows):
            for j in range(0, columns):
                if self.puzzle[i][j] != other.puzzle[i][j]:
                    return False
        return True

    # Override LESS THAN (<)
    def __lt__(self, other):
        if self.totalCost < other.totalCost:
            return True
        else:
            return False

    # Override GREATER THAN (>)
    def __gt__(self, other):
        if self.totalCost > other.totalCost:
            return True
        else:
            return False

    # Find the admissable heuristic of this puzzle
    def h1Heuristic(self):
        h1 = 0
        rows = len(self.puzzle)
        columns = len(self.puzzle[0])
        finalState = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, -1]]  # The state we want to reach
        for i in range(0, rows):
            for j in range(0, columns):
                if (self.puzzle[i][j]-finalState[i][j]) != 0:  # Count the Number of misplaced tiles
                    h1 = h1 + 1
        return h1

    # Get the position of the empty tile [row, column]
    def getEmptyTilePosition(self):
        rows = len(self.puzzle)
        columns = len(self.puzzle[0])
        for i in range(0, rows):
            for j in range(0, columns):
                if self.puzzle[i][j] == -1:  # Looking for the position of the empty tile which is denoted by -1
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


# GET possible Nodes that we can go from the given node
def getAllNextPossibleNodes(currentNode):
    emptyTilePosition = currentNode.getEmptyTilePosition()
    emptyTileRow = emptyTilePosition[0]
    emptyTileCol = emptyTilePosition[1]

    nextNodes = []
    # ------ UP -------
    tempNode = copy.deepcopy(currentNode)  # Temp Node that will be tested if its valid next Node

    upTileRow = emptyTileRow - 1
    upTileCol = emptyTileCol
    if upTileRow >= 0:  # If UP shift is possible
        temp = tempNode.puzzle[upTileRow][upTileCol]
        tempNode.puzzle[upTileRow][upTileCol] = -1
        tempNode.puzzle[emptyTileRow][emptyTileCol] = temp

        tempNode.estimatedDistanceToGoal = tempNode.h1Heuristic()
        tempNode.distanceFromInitPuzzle = tempNode.distanceFromInitPuzzle + 1
        tempNode.totalCost = tempNode.distanceFromInitPuzzle + tempNode.estimatedDistanceToGoal
        nextNodes.append(tempNode)

    # -------- DOWN -------
    del tempNode
    tempNode = copy.deepcopy(currentNode)  # Temp Node that will be tested if its valid next Node

    downTileRow = emptyTileRow + 1
    downTileCol = emptyTileCol
    if downTileRow <= 3:  # If Down shift is possible
        temp = tempNode.puzzle[downTileRow][downTileCol]
        tempNode.puzzle[downTileRow][downTileCol] = -1
        tempNode.puzzle[emptyTileRow][emptyTileCol] = temp

        tempNode.estimatedDistanceToGoal = tempNode.h1Heuristic()
        tempNode.distanceFromInitPuzzle = tempNode.distanceFromInitPuzzle + 1
        tempNode.totalCost = tempNode.distanceFromInitPuzzle + tempNode.estimatedDistanceToGoal
        nextNodes.append(tempNode)

    # --------- RIGHT --------
    del tempNode
    tempNode = copy.deepcopy(currentNode)  # Temp Node that will be tested if its valid next Node

    rightTileRow = emptyTileRow
    rightTileCol = emptyTileCol + 1
    if rightTileCol <= 3:  # If RIGHT shift is possible
        temp = tempNode.puzzle[rightTileRow][rightTileCol]
        tempNode.puzzle[rightTileRow][rightTileCol] = -1
        tempNode.puzzle[emptyTileRow][emptyTileCol] = temp

        tempNode.estimatedDistanceToGoal = tempNode.h1Heuristic()
        tempNode.distanceFromInitPuzzle = tempNode.distanceFromInitPuzzle + 1
        tempNode.totalCost = tempNode.distanceFromInitPuzzle + tempNode.estimatedDistanceToGoal
        nextNodes.append(tempNode)

    # -------- LEFT -------
    del tempNode
    tempNode = copy.deepcopy(currentNode)  # Temp Node that will be tested if its valid next Node

    leftTileRow = emptyTileRow
    leftTileCol = emptyTileCol - 1
    if leftTileCol >= 0:  # If left shift is possible
        temp = tempNode.puzzle[leftTileRow][leftTileCol]
        tempNode.puzzle[leftTileRow][leftTileCol] = -1
        tempNode.puzzle[emptyTileRow][emptyTileCol] = temp

        tempNode.estimatedDistanceToGoal = tempNode.h1Heuristic()
        tempNode.distanceFromInitPuzzle = tempNode.distanceFromInitPuzzle + 1
        tempNode.totalCost = tempNode.distanceFromInitPuzzle + tempNode.estimatedDistanceToGoal
        nextNodes.append(tempNode)

    return nextNodes


# Puzzle Generator
# Just call this function and it returns distinct Puzzle
def createPuzzle():
    # Note -1 is the empty tile
    nd = copy.deepcopy(Node([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, -1]], 0))
    initState = nd.puzzle

    for i in range(10):  # The empty tile moves 10 times randomly
        index = nd.getEmptyTilePosition()
        emptyTileRow = index[0]
        emptyTileCol = index[1]
        temp = 0
        randomTileShift = random.randint(0, 1)  # 0 is vertical, 1 is horizontal
        if randomTileShift == 0:  # vertical
            randomTileShiftUporDown = random.randint(0, 1)  # Random 0 is UP, 1 is DOWN
            if randomTileShiftUporDown == 0:  # VERTICAL UP
                if index[0] == 0:  # Top line can't shift up one more times
                    temp = initState[emptyTileRow+1][emptyTileCol]
                    initState[emptyTileRow+1][emptyTileCol] = -1
                    initState[emptyTileRow][emptyTileCol] = temp
                else:
                    temp = initState[emptyTileRow-1][emptyTileCol]
                    initState[emptyTileRow-1][emptyTileCol] = -1
                    initState[emptyTileRow][emptyTileCol] = temp
            elif randomTileShiftUporDown == 1:  # VERTICAL DOWN
                if index[0] == 3:  # this line can't go DOWN
                    temp = initState[emptyTileRow-1][emptyTileCol]
                    initState[emptyTileRow-1][emptyTileCol] = -1
                    initState[emptyTileRow][emptyTileCol] = temp
                else:
                    temp = initState[emptyTileRow+1][emptyTileCol]
                    initState[emptyTileRow+1][emptyTileCol] = -1
                    initState[emptyTileRow][emptyTileCol] = temp
        elif randomTileShift == 1:  # horizontal
            randomTileShiftRightorLeft = random.randint(0, 1)  # Random RIGHT is 0, LEFT is 1
            if randomTileShiftRightorLeft == 0:  # HORIZONTAL RIGHT
                if index[1] == 3:
                    temp = initState[emptyTileRow][emptyTileCol-1]
                    initState[emptyTileRow][emptyTileCol-1] = -1
                    initState[emptyTileRow][emptyTileCol] = temp
                else:
                    temp = initState[emptyTileRow][emptyTileCol+1]
                    initState[emptyTileRow][emptyTileCol+1] = -1
                    initState[emptyTileRow][emptyTileCol] = temp
            elif randomTileShiftRightorLeft == 1:  # HORIZONTAL LEFT
                if index[1] == 0:
                    temp = initState[emptyTileRow][emptyTileCol+1]
                    initState[emptyTileRow][emptyTileCol+1] = -1
                    initState[emptyTileRow][emptyTileCol] = temp
                else:
                    temp = initState[emptyTileRow][emptyTileCol-1]
                    initState[emptyTileRow][emptyTileCol-1] = -1
                    initState[emptyTileRow][emptyTileCol] = temp

    return initState

# Selection Sort for the QUEUE
def sort(givenQueue):
    sortedQueue = givenQueue
    for i in range(0, len(sortedQueue)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(sortedQueue)):
            if sortedQueue[min_idx].totalCost > sortedQueue[j].totalCost:
                min_idx = j
        # Swap the found minimum element with
        # the first element
        sortedQueue[i], sortedQueue[min_idx] = sortedQueue[min_idx], sortedQueue[i]
    return sortedQueue


#  ----------A* algorithm with admissable heuristic ----------
def astar(initPuzzle):
    queue = []  # Initialize the Queue for the Nodes. This will hold array of puzzles which we can expand from the smallest total cost
    visited = []  # At the end this will be complete tree between start and end puzzle nodes
    queue.append(initPuzzle)  # Add starting ouzzle to the queue
    targetPuzzle = Node([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 5], [4, 5, 5, -1]], 0)  # Solved Puzzle
    maxLengthQueue = 1
    while len(queue) > 0:  # Loop until queue is empty or target is found
        sort(queue)  # We sort the queue every time so we can pop the smallest cost puzzle
        currentNode = queue.pop(0)
        visited.append(currentNode)  # Add current node to the visited list
        if len(queue) > maxLengthQueue:
            maxLengthQueue = len(queue)

        # Target Reached --> Backtrck and find the path
        if currentNode == targetPuzzle:
            finalPath = backtrack(visited)  # Backtrck Algorithm finds the path between start and end states
            finalPath.reverse()  # Path comes reversed from the backtrack() function, we fix it here
            return finalPath, maxLengthQueue  # Return the resulting path
            break

        childrenNodes = getAllNextPossibleNodes(currentNode)  # Get all of the possible next states
        for children in childrenNodes:
            for vis in visited:
                if children == vis:  # Check if we previously visited any of these new states
                    continue  # If visited before, just skip it
            for q in queue:
                if children == q:  # If we encounter a new state that is already in the queue
                    # We check if new states cost is bigger than the state in the queue
                    if children > q:  # This bigger than is overwritten in the Node class which checks for the cost
                        continue

            #print(children.distanceFromInitPuzzle)
            queue.append(children)

    return None


#  This function Traverses the final tree and finds the path between initial puzzle and the solved puzzle
def backtrack(visited):
    finalPath = []  # This will hold the final path between start and the end
    visited.reverse()  # Reverse the tree and parse it from END to START
    possiblePaths = getAllNextPossibleNodes(visited[0])  # Get all possible next nodes for the END state
    finalPath.append(visited[0])
    for i in range(1, len(visited)):
        for j in possiblePaths:
            if visited[i] == j:  # Search for the next suitable node
                finalPath.append(visited[i])  # When we foun the suitable next node, add it to the final path
                possiblePaths = getAllNextPossibleNodes(visited[i])  # Get the next possible paths for the newly found node
                break  # Break and look for the next Node

    return finalPath  # At the end return the backtracked path from END to START


# Main function that creates and solves 12 E15 puzzles
def main():
    for i in range(1, 13):
        print()
        print(f"------ Randomized E15 Puzzle S{i} ------")
        initState = Node(createPuzzle(), 0)  # Puzzle Generator
        print(f"------- Initial State of S{i} -------")
        initState.display()  # Display the scrambled first Puzzle
        print(f"-------- Solution of S{i} ----------")
        finalPath, maxQueueLength = astar(initState)  # Solve the puzzle with A* algorithm
        print(f"Max Queue Length = {maxQueueLength}")
        print(f"Solution Length = {len(finalPath)}")
        for j in finalPath:
            j.display()  # Display the moves needed to solve the puzzle
        print(f"-------- End of E15 Puzzle S{i} --------")


if __name__ == "__main__":
    main()
