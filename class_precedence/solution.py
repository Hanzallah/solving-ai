'''
# AI HW-HW04 Class precedence lists 
'''
from itertools import chain

def get_fish_hooks(graph):
    fish_hooks = dict()
    for key in graph.keys():
        fish_hooks[key] = []
        right = key
        for value in graph[key]:
            fish_hooks[key].append(right + '-' + value)
            right = value
    return fish_hooks

def get_precedence(graph):
    fish_hooks = get_fish_hooks(graph)
    precedence_list = []
    exposed = []
    [exposed.append(key) for key in graph.keys() if key not in list(chain.from_iterable(graph.values()))]

    while len(list(chain.from_iterable(fish_hooks.values()))) != 0:
        pass
  
    print(exposed)    

# Generate the inputs using adjacency lists
def create_inputs():
    input_A = {'fstream':['iostream'],'ifstream':['istream'],'iostream':['istream', 'ostream'],'ofstream':['ostream'],'istream':['ios'],'ostream':['ios'],'ios':[],}

    return input_A

def main():
    input_A = create_inputs()
    get_precedence(input_A)

if __name__ == '__main__':
    main()