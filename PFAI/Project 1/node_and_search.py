'''
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren
'''

import queue
import time
from typing import Any
from queue import LifoQueue
from queue import PriorityQueue
from dataclasses import dataclass, field


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


class Node:
    '''
    This class defines nodes in search trees. It keep track of: 
    state, cost, parent, action, and depth 
    '''
    search_cost = 0
    def __init__(self, state, cost=0, parent=None, action=None, direction=None):
        self.parent = parent
        self.state = state
        self.action = action
        self.direction = direction
        self.cost = cost
        self.depth = 0
        self.start_time = 0
        if parent:
            self.depth = parent.depth + 1 
    


 
    def pretty_print_solution(self, verbose=False):
        def print_recursive(node):            
            if node is None:
                return
            if verbose:
                node.state.pretty_print()
            if node.action:
                print("Action:", node.action)
            print_recursive(node.parent)

        print("Solution Path:")
        print_recursive(self)
        

    def goal_state(self):
        return self.state.check_goal()

    
    def successor(self):
        successors = queue.Queue()
        try: 
            for action in self.state.action:                     
                child = self.state.move(action)      
                if child != None:                                
                    childNode = Node(child, self.cost + 1, self, action)              
                    successors.put(childNode)
            return successors  
        except:
            for action in self.state.direction:                     
                child = self.state.move(self.state, self.direction)      
                if child != None:                                
                    childNode = Node(child, self.cost + 1, self, action)              
                    successors.put(childNode)
            return successors  

    
    def statistics(self):
        end_time = time.process_time()
        elapsed_time = end_time - self.start_time
        
        # Calculate the estimated effective branching factor
        n = Node.search_cost
        d = self.depth
        effective_branching_factor = n**(1/d) if d > 0 else 0
        
        print("----------------------------------------")
        print("Elapsed time (s):", elapsed_time)
        print("Solution found at depth:", self.depth)
        print("Number of nodes explored:", Node.search_cost)
        print("Cost of solution:", self.cost)
        print("Estimated effective branching factor:", effective_branching_factor)




             
class SearchAlgorithm:
    '''
    Class for search algorithms, call it with a defined problem 
    '''
    def __init__(self, problem):
        self.start = Node(problem)
        self.depth = 0        
        self.cost = 0
        
    def bfs(self, verbose = False, statistics = False):

        try:

            frontier = queue.Queue()
            already_visited = set()
            frontier.put(self.start)
            stop = False

            while not stop:

                if frontier.empty():
                    return None
                curr_node = frontier.get()
                Node.search_cost += 1

                if curr_node.state not in already_visited:
                    already_visited.add(curr_node.state) 

                    if curr_node.goal_state():
                        stop = True    
                        if statistics:
                            curr_node.statistics()
                            self.start_time = time.process_time()
                        return curr_node        


                    successor = curr_node.successor() 
                    while not successor.empty():                   
                    
                        frontier.put(successor.get())
        except:
            initial_state_eight_puzzle = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
            goal_state_eight_puzzle = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]
            frontier = queue.Queue()
            already_visited = set()
            frontier.put(initial_state_eight_puzzle)
            stop = False

            while not stop:

                if frontier.empty():
                    return None
                
                start_node = PrioritizedItem(self.h_1(initial_state_eight_puzzle), initial_state_eight_puzzle)
                frontier.put(start_node)
                curr_node = frontier.get()
                Node.search_cost += 1

                flat_child_state = self.flatten_state(child_state)
                if tuple(flat_child_state) not in explored:
                    already_visited.add(curr_node) 

                    if curr_node.goal_state():
                        stop = True    
                        if statistics:
                            curr_node.statistics()
                            self.start_time = time.process_time()
                        return curr_node        


                    successor = curr_node.successor() 
                    while not successor.empty():                   
                    
                        frontier.put(successor.get())
                    

 
    def dfs(self, depth_limit = None, verbose=False, statistics=False):
        frontier = queue.LifoQueue()  
        already_visited = []
        frontier.put(self.start)
        stop = False
        Node.search_cost = 0
        while not stop:          
            if depth_limit != None:
                if depth_limit < Node.search_cost:
                    curr_node.statistics()
                    return curr_node
                else:
                    if frontier.empty():                
                        return None
                    curr_node = frontier.get()
                    Node.search_cost += 1

                    if curr_node.state.state not in already_visited:

                        already_visited.append(curr_node.state.state)

                        if curr_node.goal_state():

                            stop = True
                            if statistics:
                                curr_node.statistics()
                                self.start_time = time.time()
                            return curr_node

                        successor = curr_node.successor()
                        while not successor.empty():
                            frontier.put(successor.get())
            else:
                if frontier.empty():                
                    return None
                curr_node = frontier.get()
                Node.search_cost += 1

                if curr_node.state.state not in already_visited:

                    already_visited.append(curr_node.state.state)

                    if curr_node.goal_state():

                        stop = True
                        if statistics:

                            curr_node.statistics()
                        return curr_node

                    successor = curr_node.successor()
                    while not successor.empty():

                        frontier.put(successor.get())

     
                
        


    def ids(self, depth_limit = 8,  verbose=False, statistics=False):
        
        while True:
            result = self.dfs(depth_limit, verbose, statistics)
            if result is not None:
                self.start_time = time.time()
                return result
            
    
            
    # ************Eight Puzzle Algorithm**************



    def pretty_print_eight_puzzle(self, state):
        # Implement a method to print the puzzle state in a readable format.
        for row in state:
            print(' '.join(map(str, row)))
        print()

    def check_goal_eight_puzzle(self, state, goal_state_eight_puzzle):
        # Implement a method to check if the current state is the goal state.
        return state == goal_state_eight_puzzle

    def move_eight_puzzle(self, state, direction):
        print("********", state)
        print("****************", direction)
        # Implement the move operation: move the 'e' and swap values.
        new_state = [row.copy() for row in state]
        empty_i, empty_j = None, None

        for i in range(3):
            for j in range(3):
                if new_state[i][j] == 'e':
                    empty_i, empty_j = i, j

        if direction == 'up' and empty_i > 0:
            new_state[empty_i][empty_j], new_state[empty_i - 1][empty_j] = new_state[empty_i - 1][empty_j], new_state[empty_i][empty_j]
        elif direction == 'down' and empty_i < 2:
            new_state[empty_i][empty_j], new_state[empty_i + 1][empty_j] = new_state[empty_i + 1][empty_j], new_state[empty_i][empty_j]
        elif direction == 'left' and empty_j > 0:
            new_state[empty_i][empty_j], new_state[empty_i][empty_j - 1] = new_state[empty_i][empty_j - 1], new_state[empty_i][empty_j]
        elif direction == 'right' and empty_j < 2:
            new_state[empty_i][empty_j], new_state[empty_i][empty_j + 1] = new_state[empty_i][empty_j + 1], new_state[empty_i][empty_j]

        return new_state


    def find_value_position(self, value, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == value:
                    return i, j
                
    def flatten_state(self, state):
        # Flatten the nested state list
        return [val for row in state for val in row]

    def print_statistics_eight_puzzle(self):
        end_time = time.process_time()
        start_time = 0
        elapsed_time = end_time - start_time
        
        # Calculate the estimated effective branching factor
        n = self.cost
        d = self.depth
        effective_branching_factor = n**(1/d) if d > 0 else 0
        
        print("----------------------------------------")
        print("Elapsed time (s):", elapsed_time)
        print("Solution found at depth:", self.cost)
        print("Number of nodes explored:", self.depth)
        print("Cost of solution:", self.cost)
        print("Estimated effective branching factor:", effective_branching_factor)
            
    def h_1(self, state):
        goal_state_eight_puzzle = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]
        # Implement the heuristic h_1: Number of tiles out of place.
        count = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != goal_state_eight_puzzle[i][j] and state[i][j] != 'e':
                    count += 1
        return count
    
    def h_2(self, state):
        # Implement the heuristic h_2: Manhattan distance.
        distance = 0
        goal_state_eight_puzzle = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]


        for i in range(3):
            for j in range(3):
                if state[i][j] != 'e':
                    value = state[i][j]
                    goal_i, goal_j = self.find_value_position(value, goal_state_eight_puzzle)
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance
    
    def greedy_search(self, heuristic=0, depth_limit=None, verbose=False, statistics=False):

        initial_state_eight_puzzle = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
        goal_state_eight_puzzle = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]

        frontier = PriorityQueue()
        start_node = PrioritizedItem(self.h_1(initial_state_eight_puzzle), initial_state_eight_puzzle)
        frontier.put(start_node)
        explored = set()
        step = 0  # Initialize step counter
        nodes_visited = 0
        depth = 0
        self.cost = 0
        self.search_cost = 0


        while not frontier.empty():
            current_node = frontier.get().item
            self.depth += 1
            self.search_cost += 1

            if self.check_goal_eight_puzzle(current_node, goal_state_eight_puzzle):
                # Goal state found
                return current_node

            if depth_limit is not None and depth_limit <= 0:
                continue

            nodes_visited += 1

         
            if verbose:
                print(f"Step {step}:")
                print(f"Current Frontier:")
                self.pretty_print_eight_puzzle(current_node)
            
            step += 1

            for direction in ['up', 'down', 'left', 'right']:
                child_state = self.move_eight_puzzle(current_node, direction)

                if child_state is not None:
                    flat_child_state = self.flatten_state(child_state)
                    if tuple(flat_child_state) not in explored:
                        if heuristic == 0:
                            child_priority = self.h_1(child_state)
                        
                        elif heuristic == 1:
                            child_priority = self.h_2(child_state)
                    
                        else:
                            # Default to h_1 if an invalid heuristic is provided
                            child_priority = self.h_1(child_state)

                        child_node = PrioritizedItem(child_priority, child_state)
                        frontier.put(child_node)
                        explored.add(tuple(flat_child_state))  # Convert to tuple before adding to set
                        self.cost += 1

                        if child_node.item == goal_state_eight_puzzle:
                            if statistics:
                                self.print_statistics_eight_puzzle()


                        
                        # successor = current_node.successor()
                        # while not successor.empty():
                        #     frontier.put(successor.get())
                
        return None
    

    def a_star(self, heuristic=0, depth_limit=None, verbose=False, statistics=False):

        initial_state_eight_puzzle = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
        goal_state_eight_puzzle = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]

        frontier = PriorityQueue()
        start_node = PrioritizedItem(0 + self.h_1(initial_state_eight_puzzle), initial_state_eight_puzzle)  # Initialize cost with 0 for the start node
        frontier.put(start_node)
        explored = set()
        step = 0  # Initialize step counter
        nodes_visited = 0
        depth = 0
        self.cost = 0

        while not frontier.empty():
            current_node = frontier.get()  # Get the current node directly from the PriorityQueue

            if self.check_goal_eight_puzzle(current_node.item, goal_state_eight_puzzle):  # Access the state using .item
                # Goal state found
                if statistics:
                    self.print_statistics_eight_puzzle()
                return current_node.item

            if depth_limit is not None and depth_limit <= 0:
                continue

            self.cost += 1

            if verbose:
                print(f"Step {step}:")
                print(f"Current Frontier:")
                self.pretty_print_eight_puzzle(current_node)
            
            step += 1

            for direction in ['up', 'down', 'left', 'right']:
                child_state = self.move_eight_puzzle(current_node.item, direction)  # Access the state using .item

                if child_state is not None:
                    flat_child_state = self.flatten_state(child_state)
                    if tuple(flat_child_state) not in explored:
                        if heuristic == 0:
                            child_priority = current_node.priority + 1 + self.h_1(child_state)  # Update priority using A* formula

                        elif heuristic == 1:
                            child_priority = current_node.priority + 1 + self.h_2(child_state)  # Update priority using A* formula

                        else:
                            # Default to h_1 if an invalid heuristic is provided
                            child_priority = current_node.priority + 1 + self.h_1(child_state)  # Update priority using A* formula

                        child_node = PrioritizedItem(child_priority, child_state)
                        frontier.put(child_node)
                        explored.add(tuple(flat_child_state))  # Convert to tuple before adding to set
                        self.depth += 1
                 

                        if current_node.item == goal_state_eight_puzzle:
                            if statistics:
                                self.print_statistics_eight_puzzle()

        return None


                        
        

        
