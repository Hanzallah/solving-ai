"""
# THINGS LEFT:
TESTING and checking for implementation errors 
maybe improve neatness of code and single-stepping statements
# IMP case: when two nodes are same but choice is done lexicographically 

https://colab.research.google.com/drive/1zSjoYYrPGdtvGINcS4EqpnLj2vyVajoz?usp=sharing <<<< Final work, COLAB notebook
"""

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

def get_algorithm(singleStepFlag):
  if (singleStepFlag) :
    print()
    print('>> Program function takes input to decide if Straight Minimaxing or w/ Alpha-beta Pruning')
    print(">> With alphabeta , we don't explicitly use the -inf,inf intial values, but that approach is implicitly implemented" )
    print()

  algorithm = []
  
  while (len(algorithm) != 1 or (algorithm[0] != 0 and algorithm[0] != 1)):
    algorithm = input('Enter 0 for Straight-Minimaxing Program - 1 for Minimax with Alphabeta Pruning: ').split()
    algorithm = [int(x) for x in algorithm]

  return algorithm[0]
   
def choose_input(singleStepFlag):
  if (singleStepFlag) :
    print()
    print('>> choose_input function takes input to Solve for the Assignment Trees OR user-inputted')
    print()

  chooseInput = [2, 2]
  
  while (len(chooseInput) != 1 or (chooseInput[0] != 0 and chooseInput[0] != 1)):
    chooseInput = input('Enter 0 for solving the Assignment-Given tree(s) - 1 for Keyboard Input: ').split()
    chooseInput = [int(x) for x in chooseInput]
  
  return chooseInput[0]

def minimax(leaves, singleStepFlag):
  L = min(leaves[0],leaves[1],leaves[2])
  M = min(leaves[3],leaves[4],leaves[5])
  R = min(leaves[6],leaves[7],leaves[8])
  if (singleStepFlag) :
    print("\n >>> 1a )  Take the sequence of values for leaves, and for L , M, R take min() of the the patches of 3 nodes left, middle and right , according to the tree structure" )

  Minimizer = [L, M, R]
  sortedIndex = sorted(range(len(Minimizer)), key=lambda k: Minimizer[k], reverse = True)
  Minimizer_dict = {0: "L"  ,1: "M"  , 2: "R" }
  if (singleStepFlag) :
    print("\n >>> 2a )  Sort the Minimizer level Nodes' values from Highest to Lowest value" )

  max = Minimizer_dict[sortedIndex[0]]
  if (singleStepFlag) :
    print("\n >>>  3a )   After sorting, the Final Output as required by assignment instructions is the L or M or R depedning on the sorting" )
    
  print("The move of the max player is :", max )

def alphabeta(leaves, singleStepFlag):

  if (singleStepFlag) :
    print("\n >>> 1b ) Take the sequence of values corrosponding to Tree leaves (terminal Nodes)  " )
    
  Minimizer_dict = {0: "L"  ,1: "M"  , 2: "R" }
  A = leaves[0] 
  B = leaves[1] 
  C = leaves[2]
  D = leaves[3]
  E = leaves[4]
  F = leaves[5] 
  G = leaves[6] 
  H = leaves[7]
  I = leaves[8]  

  pruned = []  
  if (singleStepFlag):
    print("\n >>> 2b ) Take min() of the the first 3 nodes, L = min (the 3-patch on the left), and initially assign D value to M node (as temporary ceiling) and G value to R node (as temporary ceiling)" )
  L = min(A,B,C)
  M_ceil = D
  R_ceil = G

  if L >= M_ceil:
    if (singleStepFlag) :
      print("\n >>> 3b )  Because  L >= M_ceil, append node E and F to pruned list -- in alphab. order " )
    pruned.append('E')
    pruned.append('F')
    
  elif L < M_ceil:
    if M_ceil > E:
      M_ceil = E
    if (singleStepFlag) :
        print("\n >>> 3b )  In case M_ceil is bigger that E node value, replace it on the minimizer level, M_ceil = E  " )
    
    if L >= M_ceil:
      if (singleStepFlag) :
         print("\n >>> 4b )  after the new value for M_ceil, we check to see it is indeed smaller than L, and thus prune F " )
      pruned.append('F')
    
    elif  M_ceil > F:
      M_ceil = F  
      if (singleStepFlag) :  
        print("\n >>> 4b )  No pruning Happens at M patch, i.e. middle  " )
    
    
  if L >= R_ceil or M_ceil >= R_ceil : #Now third , R node 
    if (singleStepFlag) :
      print("\n >>> 5b )  Because  L >= R_ceil, or M_ceil >= R_ceil, Prune H , I nodes -- in alphab. order " )
    pruned.append('H')
    pruned.append('I')
  elif H < R_ceil:
    R_ceil = H
    if (singleStepFlag) :
      print("\n >>> 5b )  In case R_ceil is bigger that H node value, replace it on the minimizer level, R_ceil = H  " )
    
  elif L >= R_ceil or M_ceil >= R_ceil :
    if (singleStepFlag) :  
      print("\n >>> 6b )  after the new value for R_ceil, we check to see it is indeed smaller than L or M_ceil, and thus prune I  " )
    pruned.append('I')
  elif I < R_ceil:
    R_ceil = I
    if (singleStepFlag) :  
      print("\n >>> 4b )  No pruning Happens at R patch, i.e. right node  " )    
    
  MaxinmizerLevel = [L ,M_ceil, R_ceil]
  sortedIndex = sorted(range(len(MaxinmizerLevel)), key=lambda k: MaxinmizerLevel[k], reverse = True)
  if (singleStepFlag) :  
    print("\n >>> 7b ) Sort minimizer level nodes, and choose max  " ) 
  max = Minimizer_dict[sortedIndex[0]]

  print("The move of the max player is :", max )
  print("The Pruned Nodes are : ", end='')
  [print(x, end=' ') for x in pruned]
      
def main():
  # get the nine input values
  leaves = []
  singleStepFlag = get_step_flag()
  
  algorithm = get_algorithm(singleStepFlag)
  get_input = choose_input(singleStepFlag)  


  if (get_input) == 0 and (not algorithm):
      print("\n- Minimax For tree with values of [5 ,3 , 1 , 2, 5 , 4 ,1, 3 , 3] corrosponding to A, B, C, D, E, F, G, H, I in respective order.")
      minimax([5 ,3 , 1 , 2, 5 , 4 ,1, 3 , 3], singleStepFlag)

  if (not get_input) and (algorithm):
    print('\n-------------------------------------------------------------------------------------------------')
    print("\n- Minimax with Alphabeta Pruning For tree with values of [5 ,3 , 1 , 2, 5 , 4 ,1, 3 , 3] corrosponding to A, B, C, D, E, F, G, H, I in respective order.")
    alphabeta([5 ,3 , 1 , 2, 5 , 4 ,1, 3 , 3], singleStepFlag)

    print('\n\n-------------------------------------------------------------------------------------------------')
    print("\n- Minimax with Alphabeta Pruning For tree with values of [5, 2, 2, 5, 1, 3, 2, 4, 2] corrosponding to A, B, C, D, E, F, G, H, I in respective order.")
    alphabeta([5, 2, 2, 5, 1, 3, 2, 4, 2], singleStepFlag)

    print('\n\n-------------------------------------------------------------------------------------------------')
    print("\n- Minimax with Alphabeta Pruning For tree with values of [1 ,3 ,4 ,1 ,4 ,1 ,3 ,5 ,3] corrosponding to A, B, C, D, E, F, G, H, I in respective order.")
    alphabeta([1 ,3 ,4 ,1 ,4 ,1 ,3 ,5 ,3], singleStepFlag)

  if get_input:  
      while (len(leaves)!= 9):
        leaves = input('Enter Integer Values For A, B, C, D, E, F, G, H, I, separated by blank spaces: \n').split()
        leaves = [int(x) for x in leaves]
      
      if not algorithm:
        minimax(leaves, singleStepFlag)
      elif algorithm:
        alphabeta(leaves, singleStepFlag)

if __name__ == '__main__':
  main()
