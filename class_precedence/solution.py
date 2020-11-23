'''
# AI HW-HW04 Class precedence lists 
# We have modified the topological sort algorithm from Geekforgeeks to suit our purpose
# The original algorithm can be found at https://www.geeksforgeeks.org/topological-sorting/
# The algorithm was modified to perform top sort for each initially exposed element by creating a new graph
# In the recursive top_sort_util we also add to the stack before doing the recursion
'''
from itertools import chain

# Recursive utility function for the topological sorting algorithm
def top_sort_util(step, v, visited, stack, graph):
    keys = list(graph.keys())
    visited[v] = True
    
    # add element to the class-precedence list
    if (step):
        print(">> appending value", keys[v], "to class precedence list")
        print()
        
    stack.append(keys[v])

    # visit the children of the element
    for i in range(len(graph[keys[v]])):
        if visited[i] == False:
            if (step):
                print(">> node not visited -- calling recursive topological sort utility")
                print(">> node is", list(graph[keys[v]])[i])
                print()
            top_sort_util(step, i, visited, stack, graph)
    
# Main topological sorting algorithm
def top_sort(step, graph):
    # get the list of initially exposed elements for which we will create the precedence lists
    if (step):
        print(">> getting the list of initially exposed element for which we calculate the precedence list")
    exposed = []
    [exposed.append(i) for i in graph.keys() if i not in list(chain.from_iterable(graph.values()))]
    if (step):
        print(">> The exposed list", exposed)
        print()

    for item in exposed:
        mod_graph = dict()
        # create modified graph for each list
        if (step):
            print(">> create modified graph for the current item in the exposed list")
            
        for i in graph.keys():
            if i == item or i in graph[item] or i in list(chain.from_iterable(mod_graph.values())):
                mod_graph[i] = graph[i]
        if (step):
            print(">> The modified graph for", item, ":", mod_graph)
            print()

        # perform topological sort for each list
        visited = [False] * len(mod_graph.keys())
        stack = []
        for i in range(len(mod_graph.keys())):
            if (not visited[i]):
                if (step):
                    print(">> node not visited -- calling recursive topological sort utility")
                    print(">> node is", list(mod_graph.keys())[i])
                    print()
                top_sort_util(step, i, visited, stack, mod_graph)
        print('\nHIGHEST PRECEDENCE --> LOWEST PRECEDENCE')
        print(stack)                   

# Generate the inputs using adjacency lists
def create_inputs(step):
    if (step):
        print(">> creating adjacency list for the first problem")
    input_A = {'fstream':['iostream'],'ifstream':['istream'],'iostream':['istream', 'ostream'],'ofstream':['ostream'],'istream':['ios'],'ostream':['ios'],'ios':[],}
    if (step):
        print(">> The adjacency list is", input_A)
        print()

    if (step):
        print(">> creating adjacency list for the second problem")
    input_B = {'Consultant Manager': ['Consultant', 'Manager'], 'Director':['Manager'], 'Permanent Manager':['Manager', 'Permanent Employee'], 'Consultant':['Temporary Employee'], 'Manager':['Employee'], 'Temporary Employee': ['Employee'] , 'Permanent Employee': ['Employee'], 'Employee':[]}
    if (step):
        print(">> The adjacency list is", input_B)
        print()

    if (step):
        print(">> creating adjacency list for the third problem")  
    input_C = {'Crazy':['Professors', 'Hackers'], 'Professors':['Eccentrics','Teachers'], 'Hackers':['Eccentrics', 'Programmers'], 'Eccentrics':['Dwarfs'], 'Teachers':['Dwarfs'], 'Programmers':['Dwarfs'],  'Jacque':['Weightlifters', 'Shotputters', 'Athletes'], 'Weightlifters':['Athletes', 'Endomorpha'], 'Shotputters':['Athletes', 'Endomorpha'], 'Athletes':['Dwarfs'], 'Endomorpha':['Dwarfs'], 'Dwarfs':['Everything'],  'Everything':[]}
    if (step):
        print(">> The adjacency list is", input_C)
        print()

    return (input_A, input_B, input_C)

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

def main():
    # get single stepping input
    step = get_step_flag()

    # get the homework inputs
    input_A, input_B, input_C = create_inputs(step)

    print('\nTHE FIRST EXAMPLE')
    top_sort(step, input_A)

    print('\nTHE SECOND EXAMPLE')
    top_sort(step, input_B)

    print('\nTHE THIRD EXAMPLE')
    top_sort(step, input_C)

if __name__ == '__main__':
    main()