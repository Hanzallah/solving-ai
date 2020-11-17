"""
# THINGS LEFT:
TESTING and checking for implementation errors 
maybe improve neatness of code and single-stepping statements

https://colab.research.google.com/drive/1zSjoYYrPGdtvGINcS4EqpnLj2vyVajoz?usp=sharing <<<< Final work, COLAB notebook
 
# IMP case: when two nodes are same but choice is done lexicographically 
## notes :::  
# A = input("Enter Integer Values For A, B, C, D, E, F, G, H, I, separated by blank spaces: \n ")
#    By taking that one-time input and making it into a list - Leafs -  , we create the new tree
# Single stepping -- depends what he means, I emailed him and awaiting response 
leaves  = [5 ,3 , 1 , 2, 5 , 4 ,1, 3 , 3 ]
leaves   = [5 ,2 , 2 , 5, 1 , 3 ,2, 4 , 2 ]
leaves  = [1 ,3 , 4 , 1, 4 , 1 ,3, 5 , 3 ] 
"""
singleStepFlag = SSF()

def SSF():
  SSF = []
  temp1 = True 

  while temp1 : 
    first = input('Enter 0 to display only the final results/ 1 for single-stepping option : \n').split()
    SSF = [int(x) for x in first]
    if (len(SSF)!= 1) or (SSF[0]!=1 and  SSF[0]!=0) : 
        print("\n *Only enter 0 or 1 , please!* \n " )
    else:
      #temp1 = False
      break
  singleStepFlag =  SSF[0]

  if singleStepFlag == 1 :
   print('\n >>> SSF function takes input to decide Singel-stepping option <<< \n ')
  #print('\n\n        --- SSF ---      \n\n ')
  return SSF[0]

def Program():
  Program = []
  temp2 = True 
  while temp2 : 
    Second = input(' \n Enter 1 for Straigt-Minimaxing Program / 2 for Minimax with Alphabeta Pruning : \n').split()
    Program = [int(x) for x in Second]
    if (len(Program)!= 1) or (Program[0]!=1 and  Program[0]!=2) : 
        print("\n *Only enter 0 or 1 , please!* \n " )
    else:
      #temp1 = False
      break
  if (singleStepFlag == 1 ) :
   print('\n >>> Program function takes input to decide if Straight Minimaxing or w/ Alpha-beta Pruning <<< \n ')
  print("\n\n >>> With alphabeta , we don't explicitly use the -inf,inf intial values, but that approach is implicitly implemented  <<< \n\n " )

  return Program[0]
   
def InputOrGiven():
  InputOrGiven = []
  temp3 = True 
  while temp3 : 
    Third = input('Enter 0 for solving the Assignment-Given tree(s) / 1 for Keyboard Input  \n').split()
    InputOrGiven = [int(x) for x in Third]
    if (len(InputOrGiven)!= 1) or (InputOrGiven[0]!=0 and  InputOrGiven[0]!=1) : 
        print("\n *Only enter 0 or 1 , please!* \n " )
    else:
      #temp1 = False
      break
  if (singleStepFlag == 1) :
   print('\n >>> InputOrGiven function takes input to Solve for the Assignment Trees OR user-inputted <<< \n ')
  return InputOrGiven[0]

def minimax(leaves):
  L = min(leaves[0],leaves[1],leaves[2])
  M = min(leaves[3],leaves[4],leaves[5])
  R = min(leaves[6],leaves[7],leaves[8])
  if (singleStepFlag == 1) :
    print("\n >>> 1a )  Take the sequence of values for leaves, and for L , M, R take min() of the the patches of 3 nodes left, middle and right , according to the tree structure <<< \n " )

  Minimizer = [L, M, R]
  sortedIndex = sorted(range(len(Minimizer)), key=lambda k: Minimizer[k], reverse = True)
  Minimizer_dict = {0: "L"  ,1: "M"  , 2: "R" }
  if (singleStepFlag == 1) :
    print("\n >>> 2a )  Sort the Minimizer level Nodes' values from Highest to Lowest value <<<\n " )
    
  # I need to get max and if 5 3 1 2 5 4 2 3 3 two nodes have same value choose the earlier (from left, or lexicgrapgically using ascii order, ord())
  max = Minimizer_dict[sortedIndex[0]]
  if (singleStepFlag == 1) :
    print("\n >>>  3a )   After sorting, the Final Output as required by assignment instructions is the L or M or R depedning on the sorting <<<\n " )
    
  print(" ---- Straight Minimaxing ----" )
  print("The move of the max player is :", max )

def alphabeta(leaves):

  if (singleStepFlag == 1) :
    print("\n >>> 1b ) Take the sequence of values corrosponding to Tree leaves (terminal Nodes)  <<< \n " )
    
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
  if (singleStepFlag == 1):
    print("\n >>> 2b ) Take min() of the the first 3 nodes, L = min (the 3-patch on the left), and initially assign D value to M node (as temporary ceiling) and G value to R node (as temporary ceiling)" )
  L = min(A,B,C)
  M_ceil = D
  R_ceil = G

  if L >= M_ceil:
    if (singleStepFlag == 1) :
      print("\n >>> 3b )  Because  L >= M_ceil, append node E and F to pruned list -- in alphab. order <<< \n " )
    pruned.append('E')
    pruned.append('F')
    
  elif L < M_ceil:
    if M_ceil > E:
      M_ceil = E
    if (singleStepFlag == 1) :
        print("\n >>> 3b )  In case M_ceil is bigger that E node value, replace it on the minimizer level, M_ceil = E  <<< \n " )
    
    if L >= M_ceil:
      if (singleStepFlag == 1) :
         print("\n >>> 4b )  after the new value for M_ceil, we check to see it is indeed smaller than L, and thus prune F <<< \n " )
      pruned.append('F')
    
    elif  M_ceil > F:
      M_ceil = F  
      if (singleStepFlag == 1) :  
        print("\n >>> 4b )  No pruning Happens at M patch, i.e. middle  <<< \n " )
    
    
  if L >= R_ceil or M_ceil >= R_ceil : #Now third , R node 
    if (singleStepFlag == 1) :
      print("\n >>> 5b )  Because  L >= R_ceil, or M_ceil >= R_ceil, Prune H , I nodes -- in alphab. order <<< \n " )
    pruned.append('H')
    pruned.append('I')
  elif H < R_ceil:
    R_ceil = H
    if (singleStepFlag == 1) :
      print("\n >>> 5b )  In case R_ceil is bigger that H node value, replace it on the minimizer level, R_ceil = H  <<< \n " )
    
  elif L >= R_ceil or M_ceil >= R_ceil :
    if (singleStepFlag == 1) :  
      print("\n >>> 6b )  after the new value for R_ceil, we check to see it is indeed smaller than L or M_ceil, and thus prune I  <<< \n " )
    pruned.append('I')
  elif I < R_ceil:
    R_ceil = I
    if (singleStepFlag == 1) :  
      print("\n >>> 4b )  No pruning Happens at R patch, i.e. right node  <<< \n " )    
    
  MaxinmizerLevel = [L ,M_ceil, R_ceil]
  sortedIndex = sorted(range(len(MaxinmizerLevel)), key=lambda k: MaxinmizerLevel[k], reverse = True)
  if (singleStepFlag == 1) :  
    print("\n >>> 7b ) Sort minimizer level nodes, and choose max  <<< \n " ) 
  max = Minimizer_dict[sortedIndex[0]]

  # I need to get max and if two nodes have same value choose the earlier (from left, or lexicgrapgically using ascii order, ord())
  print("------ Minimax with Alphabeta Pruning ------- " )
  print("The move of the max player is :", max )
  print("The Pruned Nodes are :", pruned)
      
def main():
  # get the nine input values
  leaves = []
  Program_instance = Program()
  InputOrGiven_instance = InputOrGiven()  
  
  if (InputOrGiven_instance) == 0 and (Program_instance == 1):
      print("\n Minimax For tree with values of [5 ,3 , 1 , 2, 5 , 4 ,1, 3 , 3] corrosponding to A, B, C, D, E, F, G, H, I in respective order.")
      minimax([5 ,3 , 1 , 2, 5 , 4 ,1, 3 , 3])

  if (InputOrGiven_instance == 0) and (Program_instance == 2):
    print("\n Minimax with Alphabeta Pruning For tree with values of [5 ,3 , 1 , 2, 5 , 4 ,1, 3 , 3] corrosponding to A, B, C, D, E, F, G, H, I in respective order.")
    alphabeta([5 ,3 , 1 , 2, 5 , 4 ,1, 3 , 3])

    print("\n Minimax with Alphabeta Pruning For tree with values of [5, 2, 2, 5, 1, 3, 2, 4, 2] corrosponding to A, B, C, D, E, F, G, H, I in respective order.")
    alphabeta([5, 2, 2, 5, 1, 3, 2, 4, 2])

    print("\n Minimax with Alphabeta Pruning For tree with values of [1 ,3 ,4 ,1 ,4 ,1 ,3 ,5 ,3] corrosponding to A, B, C, D, E, F, G, H, I in respective order.")
    alphabeta([1 ,3 ,4 ,1 ,4 ,1 ,3 ,5 ,3])

  if InputOrGiven_instance == 1:  
      leaves = input('Enter Integer Values For A, B, C, D, E, F, G, H, I, separated by blank spaces: \n').split()
      leaves = [int(x) for x in leaves]
  if (len(leaves)!= 9):
    print("Wrong input length")
    # don't we have to ask again for input here ? 
  elif Program_instance == 1:
        minimax(leaves)
  elif Program_instance == 2:
        alphabeta(leaves)
  else:
      pass

if __name__ == '__main__':
  main()
