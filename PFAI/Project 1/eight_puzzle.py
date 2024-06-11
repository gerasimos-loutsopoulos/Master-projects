from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any
import time
from node_and_search import SearchAlgorithm
from node_and_search import Node

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)

class EightPuzzle:
    def __init__(self, initial_state, goal_state, cost=0, depth=0, search_cost=0):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.cost = cost
        self.depth = depth
        self.start_time = 0
        self.search_cost = 0
        self.direction = ['up','down','left','right'] 


    def move(self, state, direction):
        # Implement the move operation: move the 'e' and swap values.
        print("State:", state),
        print("Direction:", direction)
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
    

    def check_goal(self):  

        if self.initial_state == self.goal_state:        
            return True
        else:
            return False


if __name__ == "__main__":
    initial_state = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
    goal_state = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]
    
    # puzzle = EightPuzzle(initial_state, goal_state)
    # result = puzzle.greedy_search(heuristic=1, statistics = True, verbose = False)  # Change heuristic to 0 for h_1 or 1 for h_2
    # if result:
    #     print("Solution found:")
    #     puzzle.pretty_print(result)
    #     
    # else:
    #     print("No solution found.")

    # puzzle = EightPuzzle(initial_state, goal_state)
    # result = puzzle.a_star(heuristic=1)  # Change heuristic to 0 for h_1 or 1 for h_2
    # if result:
    #     print("Solution found:")
    #     puzzle.pretty_print(result)
    # else:
    #     print("No solution found.")