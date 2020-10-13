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
        if (self.m_left == 0 or self.m_left >= self.c_left) and (self.m_right == 0 or self.m_right >= self.c_right) \
            and (self.m_left >= 0 and self.m_right >= 0) and (self.c_left >= 0 and self.c_right >= 0):
            return True
        else:
            return False

    # check if two states are equal
    def __eq__(self, other_state):
        return self.c_left == other_state.c_left and self.m_left == other_state.m_left \
            and  self.c_right == other_state.c_right and self.m_right == other_state.m_right \
            and self.boat_direction == other_state.boat_direction and self.boat_size == other_state.boat_size
    
    def __hash__(self):
        return hash((self.c_left, self.m_left, self.c_right, self.m_right, self.boat_direction, self.boat_size))

'''
Find the valid children of a node and return as a list
'''
def create_children(state):
    children = []
    if state.boat_direction == 'left':
        # only missionaries in boat
        for i in range(1,state.boat_size+1):
            check_state = State(state.c_left, state.m_left - i, state.c_right, state.m_right + i, 'right', state.boat_size)

            if check_state.validate():
                check_state.parent = state
                children.append(check_state)

        # equal numbers of both in boat
        for i in range(1, (state.boat_size)//2+1):
            check_state = State(state.c_left - i, state.m_left - i, state.c_right + i, state.m_right + i, 'right', state.boat_size)

            if check_state.validate():
                check_state.parent = state
                children.append(check_state)

        # more missionaries than cannibals in boat
        for i in range(state.boat_size//2+1,state.boat_size):
            check_state = State(state.c_left - (state.boat_size-i), state.m_left - i, state.c_right +  (state.boat_size-i), state.m_right + i, 'right', state.boat_size)

            if check_state.validate():
                check_state.parent = state
                children.append(check_state)

        # only cannibals in boat
        for i in range(1,state.boat_size+1):
            check_state = State(state.c_left - i, state.m_left, state.c_right + i, state.m_right, 'right', state.boat_size)

            if check_state.validate():
                check_state.parent = state
                children.append(check_state)
    else:
        # only missionaries in boat
        for i in range(1,state.boat_size+1):
            check_state = State(state.c_left, state.m_left + i, state.c_right, state.m_right - i, 'left', state.boat_size)

            if check_state.validate():
                check_state.parent = state
                children.append(check_state)

        # equal numbers of both in boat
        for i in range(1, (state.boat_size)//2+1):
            check_state = State(state.c_left + i, state.m_left + i, state.c_right - i, state.m_right - i, 'left', state.boat_size)

            if check_state.validate():
                check_state.parent = state
                children.append(check_state)

        # more missionaries than cannibals in boat
        check_state = State(state.c_left + (state.boat_size//2), state.m_left + (state.boat_size//2+1), state.c_right - (state.boat_size//2), state.m_right - (state.boat_size//2+1), 'left', state.boat_size)

        if check_state.validate():
            check_state.parent = state
            children.append(check_state)

        # only cannibals in boat
        for i in range(1,state.boat_size+1):
            check_state = State(state.c_left + i, state.m_left, state.c_right - i, state.m_right, 'left', state.boat_size)

            if check_state.validate():
                check_state.parent = state
                children.append(check_state)
    return children


'''
A depth-first search algorithm to find the goal state
'''
def dfs(c_left, m_left, c_right, m_right, boat_direction, boat_size):
    init_state = State(c_left, m_left, c_right, m_right, boat_direction, boat_size)

    if init_state.is_goal_state():
        return init_state

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
            if (child not in visited):
                stack.append(child)
    return None

'''
Print the path taken to find the solution
'''
def print_path(solution):
    path = []
    print(solution)
    path.append(solution)

    # create path by going up the tree using a node's parent
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent
    
    # print the path
    for i in range(len(path)):
        state = path.pop()
        print("Left Side -> " + "C: " + str(state.c_left) + " M: " + str(state.m_left))
        print("Right Side -> " + "C: " + str(state.c_right) + " M: " + str(state.m_right))
        print("Boat Direction -> " + str(state.boat_direction))
        print("---------------------------------------------------------------------------")

def main():
    solution = dfs(6,6,0,0,'left',5)
    print_path(solution)

if __name__ == "__main__":
    main()
