'''
A DFS search solution to the missionaries and cannibals problem
'''

class StateSearch():
    def __init__(self, cannibal_left, missionaries_left, boat_direction, boat_size):
        self.parent = None
        self.boat_direction = boat_direction
        self.boat_size = boat_size
        self.cannibal_left = cannibal_left
        self.missionaries_left = missionaries_left
    
    def goal_state(self):
        return (self.cannibal_left == 0 and self.missionaries_left == 0)

    def validate(self):
        pass

    def __eq__(self, other_state):
        return self.cannibal_left == other_state.cannibal_left and self.missionary_left == other_state.missionary_left \
            and self.boat_direction == other_state.boat_direction and self.boat_size == other_state.boat_size

def create_children(state):
    pass

'''
A depth-first search algorithm to find the goal state
'''
def dfs(cannibal_left, missionaries_left, boat_direction, boat_size):
    init_state = StateSearch(cannibal_left, missionaries_left, boat_direction, boat_size)

    if init_state.goal_state():
        return init_state()

    # create the visisted set and the stack
    visited = set()
    stack = list()
    stack.append(init_state)

    while stack:
        # remove and check the top state on the stack
        top_state = stack.pop()
        if (top_state.goal_state()):
            return top_state
        
        # if the top state is not the goal state then add it to the visisted set
        visited.add(top_state)

        # get the children of the top stack
        children = create_children(top_state)

        # add children to the stack if they haven't been visited
        for child in children:
            if (child not in visited) or (child not in stack):
                stack.append(child)
    return None

def print_path():
    pass

def main():
    solution = dfs(3,3,'left',2)
    print_path()

if __name__ == "__main__":
    main()
