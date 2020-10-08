'''
This code solves:
---There are 5 cannibals, 5 missionaries, and a boat holding 3---
'''
'''
Node represents the states.
List variable length is 5, it is in the form of:
[numberOfMissionaryOnTheWest, numberOfCannibalOnTheWest, Boatlocation(0 is West and 1 is East),  numberOfMissionaryOnTheEast, numberOfCannibalOnTheEast]
For instance [4, 4, 1, 1, 1] means 4 missionary and 4 cannibal on the west, boat is on the East, 1 missionary and 1 cannibal on the East
'''
class Node:
    def __init__(self, list):
        self.list = list
        self.misOnTheWest = list[0]
        self.canOnTheWest = list[1]
        self.misOnTheEast = list[3]
        self.canOnTheEast = list[4]
        if list[2] == 0:
            self.rowBoatLocation = "west"
        elif list[2] == 1:
            self.rowBoatLocation = "east"
        else:
            print("Wrong rowBoatLocation")

'''
This functions return all possible states that a given state can go to
Function automatically eliminates the invalid next states using isValidNode()
function
'''
def getAllPossibleNextNodes(node):
    nodeArray = node

    rowBoatLocation = None
    if nodeArray.list[2] == 0:
        rowBoatLocation = "west"
    elif nodeArray.list[2] == 1:
        rowBoatLocation = "east"
    else:
        print("Wrong rowBoatLocation")
        return

    possibleNodes = []
    if rowBoatLocation == "west":
        if isValidNode(nodeArray, Node([nodeArray.list[0]-0, nodeArray.list[1]-1, 1, nodeArray.list[3]+0, nodeArray.list[4]+1])):
            possibleNodes.append(Node([nodeArray.list[0]-0, nodeArray.list[1]-1, 1, nodeArray.list[3]+0, nodeArray.list[4]+1]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]-0, nodeArray.list[1]-2, 1, nodeArray.list[3]+0, nodeArray.list[4]+2])):
            possibleNodes.append(Node([nodeArray.list[0]-0, nodeArray.list[1]-2, 1, nodeArray.list[3]+0, nodeArray.list[4]+2]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]-0, nodeArray.list[1]-3, 1, nodeArray.list[3]+0, nodeArray.list[4]+3])):
            possibleNodes.append(Node([nodeArray.list[0]-0, nodeArray.list[1]-3, 1, nodeArray.list[3]+0, nodeArray.list[4]+3]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]-1, nodeArray.list[1]-0, 1, nodeArray.list[3]+1, nodeArray.list[4]+0])):
            possibleNodes.append(Node([nodeArray.list[0]-1, nodeArray.list[1]-0, 1, nodeArray.list[3]+1, nodeArray.list[4]+0]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]-1, nodeArray.list[1]-1, 1, nodeArray.list[3]+1, nodeArray.list[4]+1])):
            possibleNodes.append(Node([nodeArray.list[0]-1, nodeArray.list[1]-1, 1, nodeArray.list[3]+1, nodeArray.list[4]+1]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]-2, nodeArray.list[1]-0, 1, nodeArray.list[3]+2, nodeArray.list[4]+0])):
            possibleNodes.append(Node([nodeArray.list[0]-2, nodeArray.list[1]-0, 1, nodeArray.list[3]+2, nodeArray.list[4]+0]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]-2, nodeArray.list[1]-1, 1, nodeArray.list[3]+2, nodeArray.list[4]+1])):
            possibleNodes.append(Node([nodeArray.list[0]-2, nodeArray.list[1]-1, 1, nodeArray.list[3]+2, nodeArray.list[4]+1]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]-3, nodeArray.list[1]-0, 1, nodeArray.list[3]+3, nodeArray.list[4]+0])):
            possibleNodes.append(Node([nodeArray.list[0]-3, nodeArray.list[1]-0, 1, nodeArray.list[3]+3, nodeArray.list[4]+0]))
    else:
        if isValidNode(nodeArray, Node([nodeArray.list[0]+0, nodeArray.list[1]+1, 0, nodeArray.list[3]-0, nodeArray.list[4]-1])):
            possibleNodes.append(Node([nodeArray.list[0]+0, nodeArray.list[1]+1, 0, nodeArray.list[3]-0, nodeArray.list[4]-1]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]+0, nodeArray.list[1]+2, 0, nodeArray.list[3]-0, nodeArray.list[4]-2])):
            possibleNodes.append(Node([nodeArray.list[0]+0, nodeArray.list[1]+2, 0, nodeArray.list[3]-0, nodeArray.list[4]-2]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]+0, nodeArray.list[1]+3, 0, nodeArray.list[3]-0, nodeArray.list[4]-3])):
            possibleNodes.append(Node([nodeArray.list[0]+0, nodeArray.list[1]+3, 0, nodeArray.list[3]-0, nodeArray.list[4]-3]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]+1, nodeArray.list[1]+0, 0, nodeArray.list[3]-1, nodeArray.list[4]-0])):
            possibleNodes.append(Node([nodeArray.list[0]+1, nodeArray.list[1]+0, 0, nodeArray.list[3]-1, nodeArray.list[4]-0]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]+1, nodeArray.list[1]+1, 0, nodeArray.list[3]-1, nodeArray.list[4]-1])):
            possibleNodes.append(Node([nodeArray.list[0]+1, nodeArray.list[1]+1, 0, nodeArray.list[3]-1, nodeArray.list[4]-1]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]+2, nodeArray.list[1]+0, 0, nodeArray.list[3]-2, nodeArray.list[4]-0])):
            possibleNodes.append(Node([nodeArray.list[0]+2, nodeArray.list[1]+0, 0, nodeArray.list[3]-2, nodeArray.list[4]-0]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]+2, nodeArray.list[1]+1, 0, nodeArray.list[3]-2, nodeArray.list[4]-1])):
            possibleNodes.append(Node([nodeArray.list[0]+2, nodeArray.list[1]+1, 0, nodeArray.list[3]-2, nodeArray.list[4]-1]))

        if isValidNode(nodeArray, Node([nodeArray.list[0]+3, nodeArray.list[1]+0, 0, nodeArray.list[3]-3, nodeArray.list[4]-0])):
            possibleNodes.append(Node([nodeArray.list[0]+3, nodeArray.list[1]+0, 0, nodeArray.list[3]-3, nodeArray.list[4]-0]))
    return possibleNodes


'''
This function checks for the validity of a given functions
Cannibals should not outnumber the missionaries in West coast, East coast, also on
the boat as well
'''
def isValidNode(oldNode, newNode):
    misOnTheWest = newNode.list[0]
    canOnTheWest = newNode.list[1]
    misOnTheEast = newNode.list[3]
    canOnTheEast = newNode.list[4]

    if misOnTheWest < 0 or canOnTheWest < 0 or misOnTheEast < 0 or canOnTheEast < 0:
        return False
    elif misOnTheWest > 0 and canOnTheWest > misOnTheWest:
        return False
    elif misOnTheEast > 0 and canOnTheEast > misOnTheEast:
        return False
    else:
        return True


'''
Intiliziation of necessary lists for the BFS algorithm
Visited holds all of the previosly visited states
All possible states are added to queue only one time thanks to visited list
'''
visited = []
queue = []
finalList = []
'''
Breadth-first search (BFS) is an algorithm for traversing or searching state
diagrams. It starts from the root state (appended before the while loop) append
discovers all of the possible states and its proper neighbor nodes.
'''
def bfs():
    visited.append(Node([5, 5, 0, 0, 0]))
    queue.append(Node([5, 5, 0, 0, 0]))

    while queue:
        s = queue.pop(0)
        finalList.append(s.list)
        if s.list == [0, 0, 1, 5, 5]:
            break

        possibleNodes = getAllPossibleNextNodes(s)
        for i in range(0, len(possibleNodes)):
            flag = False
            for j in range(0, len(visited)):
                if possibleNodes[i].list == visited[j].list:
                    flag = True
            if flag is False:
                visited.append(possibleNodes[i])
                queue.append(possibleNodes[i])


bfs()
finalList.reverse()  # Final list contains all of the state Tree
result = []
# for j in range(0, len(finalList)):
#     print(finalList[j])
'''
We need to parse through the state tree and find a path between root state and
the finishing state. We look for it from finishing state to root state because of
that we need to reverse it first. Then we can from a new list named "result" append
our final state transitions to it.
'''
flag = True
for j in range(0, len(finalList)):  # We need to parse all of the tree
    tempList = []
    if finalList[j][2] == 1 and flag is True:  # This checks for West coast transition states
        for i in range(0, len(finalList)):

            tempList.append(finalList[j+i])  # we form a temporary list that contains one layers of states on the west bank
            k = None
            if (j+i+1) < len(finalList):  # We finish it if we reach at the end otherwise break and process the tempList
                k = j+i+1
            else:
                break
            if finalList[k][2] == 0:
                break
        if len(tempList) == 1:  # If there is only one state then we can just added it since every next states should be connected to it
            result.append(tempList[0])
            flag = False
        else:
            for i in range(0, len(tempList)):  # If there is more than one possible next state we choose a propers one tthat connects to our current state
                dif1 = result[-1][0] - tempList[i][0]
                dif2 = result[-1][0] - tempList[i][1]
                if dif1 >= 0 and dif2 >= 0 and (dif1+dif2) <= 3:
                    result.append(tempList[i])
                    flag = False

    elif finalList[j][2] == 0 and flag is False:  # This checks for East coast transition states

        for i in range(0, len(finalList)):
            tempList.append(finalList[j+i])  # we form a temporary list that contains one layers of states on the east coast
            k = None
            if (j+i+1) < len(finalList):   # We finish it if we reach at the end otherwise break and process the tempList
                k = j+i+1
            else:
                break
            if finalList[k][2] == 1:
                break
        if len(tempList) == 1:  # If there is only one state then we can just added it since every next states should be connected to it
            result.append(tempList[0])
            flag = True
        else:
            for i in range(0, len(tempList)):  # If there is more than one possible next state we choose a propers one tthat connects to our current state
                dif1 = result[-1][3] - tempList[i][3]
                dif2 = result[-1][4] - tempList[i][4]
                if dif1 >= 0 and dif2 >= 0 and (dif1+dif2) <= 3:
                    result.append(tempList[i])
                    flag = True


'''
We have the final result in the list named "Result", we just need to output
it to the console in a proper ways
'''
print("Structure of the list is : [numberOfMissionaryOnTheWest, numberOfCannibalOnTheWest, Boatlocation(0 is West and 1 is East),  numberOfMissionaryOnTheEast, numberOfCannibalOnTheEast]")
result.reverse()
for j in range(0, len(result)):
    print(result[j])
    print("        |", end=" ")
    if result[j][2] == 0 and (j+1) < len(result):
        print(f"SEND {result[j][0]-result[j+1][0]} Missionary and {result[j][1]-result[j+1][1]} Cannibal to the EAST")
    if result[j][2] == 1 and (j+1) < len(result):
        print(f"SEND {result[j][3]-result[j+1][3]} Missionary and {result[j][4]-result[j+1][4]} Cannibal to the WEST")
print("\n---The End", end="---")
