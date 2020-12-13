'''
Used pseudocode from this website for the selection sort algorithm:
    https://www.geeksforgeeks.org/python-program-for-selection-sort/

We built the tree from the data taken from figure 19.2 of Winston book as instructed

The program will print the tree and ask you to enter width and height values.
You should enter two int values with a space in between.
'''

import math

# Selection Sort is used
def sortByWidth(points):
    for i in range(len(points)):
        min = i
        #  Find min
        for j in range(i+1, len(points)):
            if points[min][0] > points[j][0]:
                min = j
        #  Swap
        temp = points[i]
        points[i] = points[min]
        points[min] = temp
    return points  # Return sorted points by width


# Selection Sort is used
def sortByHeight(points):
    for i in range(len(points)):
        min = i
        #  Find min
        for j in range(i+1, len(points)):
            if points[min][1] > points[j][1]:
                min = j
        #  Swap
        temp = points[i]
        points[i] = points[min]
        points[min] = temp
    return points  # Return sorted points by height


# Find the median value according to width
def getMedianWidth(points):
    points = sortByWidth(points)
    n = len(points)/2
    median = (points[int(n)][0]+points[int(n-1)][0])/2
    return median


# Find the median value according to height
def getMedianHeight(points):
    points = sortByHeight(points)
    n = len(points)/2
    median = (points[int(n)][1]+points[int(n-1)][1])/2
    return median


# Establishing the tree, could have used a recursive method but it is not very
# necessary in this example
def getKDTree(points):
    conditions = []

    ''' Depth 0 --> height '''
    points = sortByHeight(points)
    conditions.append(getMedianHeight(points))
    no1 = []
    yes1 = []
    for i in range(0, len(points)):
        if points[i][1] >= conditions[0]:
            yes1.append(points[i])
        else:
            no1.append(points[i])
    ''' End of Depth 0 '''

    ''' Depth 1 --> weight '''
    points = sortByWidth(no1)
    conditions.append(getMedianWidth(points))
    no2 = []
    yes2 = []
    for i in range(0, len(points)):
        if points[i][0] >= conditions[1]:
            yes2.append(points[i])
        else:
            no2.append(points[i])

    points = sortByWidth(yes1)
    conditions.append(getMedianWidth(points))
    no3 = []
    yes3 = []
    for i in range(0, len(points)):
        if points[i][0] >= conditions[2]:
            yes3.append(points[i])
        else:
            no3.append(points[i])
    ''' End of Depth 1 '''

    ''' Depth 2 --> heigth '''
    points = sortByHeight(no2)
    conditions.append(getMedianHeight(points))
    no4 = []
    yes4 = []
    for i in range(0, len(points)):
        if points[i][1] >= conditions[3]:
            yes4.append(points[i])
        else:
            no4.append(points[i])

    points = sortByHeight(yes2)
    conditions.append(getMedianHeight(points))
    no5 = []
    yes5 = []
    for i in range(0, len(points)):
        if points[i][1] >= conditions[4]:
            yes5.append(points[i])
        else:
            no5.append(points[i])

    points = sortByHeight(no3)
    conditions.append(getMedianHeight(points))
    no6 = []
    yes6 = []
    for i in range(0, len(points)):
        if points[i][1] >= conditions[5]:
            yes6.append(points[i])
        else:
            no6.append(points[i])

    points = sortByHeight(yes3)
    conditions.append(getMedianHeight(points))
    no7 = []
    yes7 = []
    for i in range(0, len(points)):
        if points[i][1] >= conditions[6]:
            yes7.append(points[i])
        else:
            no7.append(points[i])
    ''' End of Depth 2 '''

    neighbourBoxesFromLeftToRight = [no4[0], yes4[0], no5[0], yes5[0], no6[0],
                                     yes6[0], no7[0], yes7[0]]

    ''' Finally return the parameters of the tree '''
    return neighbourBoxesFromLeftToRight, conditions


# This function is for displaying the tree
def displayTree(neighbourBoxesFromLeftToRight, conditions):
    print("----------------------------- THE COMPLETE K-D TREE -------------------------------")
    print(f"                                                         --NO--{neighbourBoxesFromLeftToRight[0]}")
    print(f"                              |--NO---- (Height > {conditions[3]})--|")
    print(f"                              |                          --YES--{neighbourBoxesFromLeftToRight[1]}")
    print(f"      |--NO-- (Width > {conditions[1]})--")

    print(f"      |                       |                           --NO--{neighbourBoxesFromLeftToRight[2]}")
    print(f"      |                       |--YES---- (Height > {conditions[4]})--|")
    print(f"      |                                                   --YES--{neighbourBoxesFromLeftToRight[3]}")
    print("      |         ")
    print(F"(Height > {conditions[0]}) ")
    print("      |        ")

    print(f"      |                                                   --NO--{neighbourBoxesFromLeftToRight[4]}")
    print(f"      |                       |--NO---- (Height > {conditions[5]})--|")
    print(f"      |                       |                           --YES--{neighbourBoxesFromLeftToRight[5]}")
    print(f"      |--YES-- (Width > {conditions[2]})--")

    print(f"                              |                            --NO--{neighbourBoxesFromLeftToRight[6]}")
    print(f"                              |--YES---- (8Height > {conditions[6]})--|")
    print(f"                                                           --YES--{neighbourBoxesFromLeftToRight[7]}")
    print("---------------------------------------------------------------------------------- ")


# The function that responsible for traversing the tree and outputting the
# every step while traversing
def getTheAnswer(neighbourBoxesFromLeftToRight, conditions, width, height,step):
    answer = ""
    if (step):
        print(f"Is the Height bigger than {conditions[0]}?")
    if height > conditions[0]:
        if (step):
            print("-YES")
            print(f"Is the Width bigger than {conditions[2]}?")
        if width > conditions[2]:
            if (step):
                print("-YES")
                print(f"Is the Height bigger than {conditions[6]}?")
            if height > conditions[6]:
                if (step):
                    print("-YES")
                answer = neighbourBoxesFromLeftToRight[7]
            else:
                if (step):
                    print("-NO")
                answer = neighbourBoxesFromLeftToRight[6]
        else:
            if (step):
                print("-NO")
                print(f"Is the Height bigger than {conditions[5]}?")
            if height > conditions[5]:
                if (step):
                    print("-YES")
                answer = neighbourBoxesFromLeftToRight[5]
            else:
                if (step):
                    print("-NO")
                answer = neighbourBoxesFromLeftToRight[4]
    else:
        if (step):
            print("-NO")
            print(f"Is the Width bigger than {conditions[1]}?")
        if width > conditions[1]:
            if (step):
                print("-YES")
                print(f"Is the Height bigger than {conditions[4]}?")
            if height > conditions[4]:
                if (step):
                    print("-YES")
                answer = neighbourBoxesFromLeftToRight[3]
            else:
                if (step):
                    print("-NO")
                answer = neighbourBoxesFromLeftToRight[2]
        else:
            if (step):
                print("-NO")
                print(f"Is the Height bigger than {conditions[3]}?")
            if height > conditions[3]:
                if (step):
                    print("-YES")
                answer = neighbourBoxesFromLeftToRight[1]
            else:
                if (step):
                    print("-NO")
                answer = neighbourBoxesFromLeftToRight[0]
    return answer

# Get user choice for single stepping
def get_step_flag():
  step = [2,2]
  
  while (len(step) != 1):
    step = input('Enter 0 to display only the final results - 1 for single-stepping option: ').split()
    step = [int(x) for x in step]

  if (step[0]):
    print()
    print('>> get_step_flag function takes input to decide Single-stepping option')
    print()
  return step[0]

# The MAIN function -------------------
def main():
    # get single stepping input
    step = get_step_flag()

    # Entering points in the figure 19.2 of winston book
    points = [(1, 2, "Red"), (2, 1, "Violet"), (2, 5, "Orange"),
              (2, 6, "Red"), (4, 2, "Blue"), (5, 6, "Yellow"),
              (6, 5, "Purple"), (6, 1, "Green")]

    # Establish the tree
    neighbourBoxesFromLeftToRight, conditions = getKDTree(points)

    if (step):
        # Print the tree
        displayTree(neighbourBoxesFromLeftToRight, conditions)

    # Get width and height from the console
    values = input("Please enter width and height int values with a space in between: ")
    width = int(values[0])
    height = int(values[2])
    # Get the answer by traversing through the tree
    answer = getTheAnswer(neighbourBoxesFromLeftToRight, conditions, width, height,step)
    # Print the answer
    print(f"*** The the answer is: {answer[2]} box at ({answer[0]}, {answer[1]}) ***")


if __name__ == "__main__":
    main()
