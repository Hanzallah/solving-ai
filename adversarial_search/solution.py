"""
Original file is located at
    https://colab.research.google.com/drive/1_n3kw5ozMvO62aNw4qXwiRFyFBlW1cVM

# THINGS LEFT: Singlestepping statements, input formating.
# will do that tomorrow - 16/11/2020  
# But do please create few trees with different inputs (negative and postive integers)
# solve them and then try them out here. 
# IMP case: when two nodes are same but choice is done lexicographically 

#singleStepFlag = False ;
## notes :::  
# A = input("Enter Integer Values For A, B, C, D, E, F, G, H, I, separated by blank spaces: \n ")
#    By taking that one-time input and making it into a list - Leafs -  , we create the new tree

# Single stepping -- depends what he means, I emailed him and awaiting response 

leaves  = [5 ,3 , 1 , 2, 5 , 4 ,1, 3 , 3 ]
#leaves   = [5 ,2 , 2 , 5, 1 , 3 ,2, 4 , 2 ]
#leaves  = [1 ,3 , 4 , 1, 4 , 1 ,3, 5 , 3 ] 

# remaining -  take the node name, as in A or B etc, and append it to a list for pruned nodes -- done! 
"""

def minimax(leaves):
  L = min(leaves[0],leaves[1],leaves[2])
  M = min(leaves[3],leaves[4],leaves[5])
  R = min(leaves[6],leaves[7],leaves[8])

  Minimizer = [L, M, R]
  sortedIndex = sorted(range(len(Minimizer)), key=lambda k: Minimizer[k], reverse = True)
  Minimizer_dict = {0: "L"  ,1: "M"  , 2: "R" }

  if Minimizer[sortedIndex[0]] == Minimizer[sortedIndex[1]] or Minimizer[sortedIndex[0]] == Minimizer[sortedIndex[1]] == Minimizer[sortedIndex[2]]:
    max = Minimizer_dict[sortedIndex[0]]
  else:
    max = Minimizer_dict[sortedIndex[0]]
  # >>> I realized the if else statement here is the same  which is weird, probably sleep deprivation two days ago, test it, and I will look at it better tomorrow. << log:15-11
  # I need to get max and if two nodes have same value choose the earlier (from left, or lexicgrapgically using ascii order, ord())

  print("The move of the max player is :", max )

def alphabeta(leaves):
  Minimizer_dict = {0: "L"  ,1: "M"  , 2: "R" }
  A=leaves[0] 
  B=leaves[1] 
  C=leaves[2]
  D=leaves[3]
  E=leaves[4]
  F=leaves[5] 
  G=leaves[6] 
  H=leaves[7]
  I=leaves[8]  

  pruned = []  

  L = min(A,B,C)
  M_ceil = D
  R_ceil = G

  if L >= M_ceil:
    #prune nodes, >> append to list of pruned nodes, E and F here -- in alphab. order
    pruned.append('E')
    pruned.append('F')

  elif L < M_ceil:
    if M_ceil > E:
          M_ceil = E

    if L >= M_ceil:
        #prune F
          pruned.append('F')

    elif  M_ceil > F:
        M_ceil = F  
              #-------------- Now thrid , R node 
  if L >= R_ceil or M_ceil >= R_ceil :
      # prune H I 
      pruned.append('H')
      pruned.append('I')
  elif H < R_ceil:
          R_ceil = H
  elif L >= R_ceil or M_ceil >= R_ceil :
      #prune I
          pruned.append('I')
  elif I < R_ceil:
              R_ceil = I
  else :
          pass

  MaxinmizerLevel = [L ,M_ceil, R_ceil]
  sortedIndex = sorted(range(len(MaxinmizerLevel)), key=lambda k: MaxinmizerLevel[k], reverse = True)

  if MaxinmizerLevel[sortedIndex[0]] == MaxinmizerLevel[sortedIndex[1]] or MaxinmizerLevel[sortedIndex[0]] == MaxinmizerLevel[sortedIndex[1]] == MaxinmizerLevel[sortedIndex[2]]:
    max = Minimizer_dict[sortedIndex[0]]
  else:
    max = Minimizer_dict[sortedIndex[0]]

  # I need to get max and if two nodes have same value choose the earlier (from left, or lexicgrapgically using ascii order, ord())
  print("The move of the max player is :", max )
  print("The Pruned Nodes are :", pruned)
      
def main():
  # get the nine input values
  leaves = []
  leaves = input('Enter Integer Values For A, B, C, D, E, F, G, H, I, separated by blank spaces: \n').split()
  leaves = [int(x) for x in leaves]
  if (len(leaves)!= 9):
    print("Wrong input length")
  else:
    minimax(leaves)
    alphabeta(leaves)

if __name__ == '__main__':
  main()