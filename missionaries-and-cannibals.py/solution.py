'''
A DFS search solution to the missionaries and cannibals problem
'''

class State():
    def __init__(self, c_left, m_left, c_right, m_right, boat_direction, boat_size):
        self.parent = None
        self.c_left = c_left
        self.m_left = m_left
        self.c_right = c_right
        self.m_right = m_right
        self.boat_direction = boat_direction
        self.boat_size = boat_size
        
    #  function to check if the goal state has been achieved
    def is_goal_state(self):
        return (self.c_left == 0 and self.m_left == 0)

    # validate the state under the problem constraints
    def validate(self):
        return (self.m_left == 0 or self.m_left >= self.c_left) and (self.m_right == 0 or self.m_right >= self.c_right) \
            and (self.m_left >= 0 and self.m_right >= 0) and (self.c_left >= 0 and self.c_right >= 0)

    # check if two states are equal
    def __eq__(self, other_state):
        return self.c_right == other_state.c_right and self.m_right == other_state.m_right \
            and self.c_left == other_state.c_left and self.m_left == other_state.m_left \
            and self.boat_direction == other_state.boat_direction and self.boat_size == other_state.boat_size

# TODO
def create_children(state):
    pass

'''
A depth-first search algorithm to find the goal state
'''
def dfs(c_left, m_left, c_right, m_right, boat_direction, boat_size):
    init_state = State(c_left, m_left, c_right, m_right, boat_direction, boat_size)

    if init_state.is_goal_state():
        return init_state()

    # create the visisted set and the stack
    visited = set()
    stack = list()
    stack.append(init_state)

    while stack:
        # remove and check the top state on the stack
        top_state = stack.pop()
        if (top_state.is_goal_state()):
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

# TODO
def print_path(solution):
    pass

def main():
    solution = dfs(5,5,0,0,'left',3)
    print_path(solution)

if __name__ == "__main__":
    main()
