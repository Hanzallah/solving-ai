'''
# AI HW-HW04 Class precedence lists 
# We have modified the topological sort algorithm from Geekforgeeks to suit our purpose
# The original algorithm can be found at https://www.geeksforgeeks.org/topological-sorting/
# The algorithm was modified to perform top sort for each initially exposed element by creating a new graph
# In the recursive top_sort_util we also add to the stack before doing the recursion
'''
from itertools import chain

def top_sort_util(v, visited, stack, graph):
    keys = list(graph.keys())
    visited[v] = True
    
    stack.append(keys[v])

    for i in range(len(graph[keys[v]])):
        if visited[i] == False:
            top_sort_util(i, visited, stack, graph)
    

def top_sort(graph):
    exposed = []
    [exposed.append(i) for i in graph.keys() if i not in list(chain.from_iterable(graph.values()))]

    for item in exposed:
        mod_graph = dict()
        # create modified graph for each list
        for i in graph.keys():
            if i == item or i in graph[item] or i in list(chain.from_iterable(mod_graph.values())):
                mod_graph[i] = graph[i]

        # perform topological sort for each list
        visited = [False] * len(mod_graph.keys())
        stack = []
        for i in range(len(mod_graph.keys())):
            if (not visited[i]):
                top_sort_util(i, visited, stack, mod_graph)
        print(stack)                   

# Generate the inputs using adjacency lists
def create_inputs():
    input_A = {'fstream':['iostream'],'ifstream':['istream'],'iostream':['istream', 'ostream'],'ofstream':['ostream'],'istream':['ios'],'ostream':['ios'],'ios':[],}

    input_B = {'Consultant Manager': ['Consultant', 'Manager'], 'Director':['Manager'], 'Permanent Manager':['Manager', 'Permanent Employee'], 'Consultant':['Temporary Employee'], 'Manager':['Employee'], 'Temporary Employee': ['Employee'] , 'Permanent Employee': ['Employee'], 'Employee':[]}
    
    input_C = {'Crazy':['Professors', 'Hackers'], 'Professors':['Eccentrics','Teachers'], 'Hackers':['Eccentrics', 'Programmers'], 'Eccentrics':['Dwarfs'], 'Teachers':['Dwarfs'], 'Programmers':['Dwarfs'],  'Jacque':['Weightlifters', 'Shotputters', 'Athletes'], 'Weightlifters':['Athletes', 'Endomorpha'], 'Shotputters':['Athletes', 'Endomorpha'], 'Athletes':['Dwarfs'], 'Endomorpha':['Dwarfs'], 'Dwarfs':['Everything'],  'Everything':[]}

    return (input_A, input_B, input_C)

def main():
    input_A, input_B, input_C = create_inputs()
    print('\nTHE FIRST EXAMPLE')
    print('\nHIGHEST PRECEDENCE --> LOWEST PRECEDENCE')
    top_sort(input_A)
    print('\nTHE SECOND EXAMPLE')
    print('\nHIGHEST PRECEDENCE --> LOWEST PRECEDENCE')
    top_sort(input_B)
    print('\nTHE THIRD EXAMPLE')
    print('\nHIGHEST PRECEDENCE --> LOWEST PRECEDENCE')
    top_sort(input_C)

if __name__ == '__main__':
    main()