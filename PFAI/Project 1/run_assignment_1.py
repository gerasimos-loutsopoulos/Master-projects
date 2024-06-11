'''
Define problem and start execution of search problems

Author: Tony Lindgren
'''

from missionaries_and_cannibals import MissionariesAndCannibals 
from node_and_search import SearchAlgorithm
from node_and_search import Node
from eight_puzzle import EightPuzzle

init_state = [[0, 0], 'r', [3, 3]] 
goal_state = [[3, 3], 'l', [0, 0]] 

initial_state_eight_puzzle = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
goal_state_eight_puzzle = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]

def main():
    # mc = MissionariesAndCannibals(init_state, goal_state)
    # sa = SearchAlgorithm(mc)
    # print('BFS')
    # print('Start state: ')
    # mc.pretty_print()
    # print('goal state: ')
    # sa.bfs().state.pretty_print()
    # solution = sa.bfs(statistics= True, verbose = False)  
    # solution.pretty_print_solution() 
    #  
    # print('DFS')
    # mc.pretty_print()
    # solution_dfs = sa.dfs(statistics=True, verbose = False)
    # solution_dfs.pretty_print_solution()   
    # print("hoera")
    # print('IDS')
    # mc.pretty_print()
    # solution_ids = sa.ids(statistics=True, verbose = False)
    # solution_ids.pretty_print_solution(verbose = True)  
    # print("hoeraaaaaaa!") 

    # Eight Puzzle

    # Greedy Search

    puzzle = EightPuzzle(initial_state_eight_puzzle, goal_state_eight_puzzle)
    sa = SearchAlgorithm(puzzle)

    # result = sa.greedy_search(heuristic=1, statistics = True, verbose = False)  # Change heuristic to 0 for h_1 or 1 for h_2
    # if result:
    #     print("Solution found:")
    #     sa.pretty_print_eight_puzzle(result)
    #     
    # else:
    #     print("No solution found.")

    # A Star

    # result = sa.a_star(heuristic=1, verbose = False, statistics = True)  # Change heuristic to 0 for h_1 or 1 for h_2
    # if result:
    #     print("Solution found:")
    #     sa.pretty_print_eight_puzzle(result)
    # else:
    #     print("No solution found.")


    result = sa.bfs(verbose = True, statistics = False)  # Change heuristic to 0 for h_1 or 1 for h_2
    if result:
        print("Solution found:")
        sa.pretty_print_eight_puzzle(result)
    else:
        print("No solution found.")

    

if __name__ == "__main__":
    main()