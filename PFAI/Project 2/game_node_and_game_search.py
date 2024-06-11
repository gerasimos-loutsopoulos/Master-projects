'''
Definitions for GameNode, GameSearch and MCTS

Author: Tony Lindgren
'''
from time import process_time
import random
import math
import time


class GameNode:
    '''
    This class defines game nodes in game search trees. It keep track of: 
    state
    '''
    def __init__(self, state, parent=None, move=None):
        self.state = state   
        # Node Definition Code
        self.parent = parent
        self.playouts = 0
        self.wins = 0
        self.successors = []
        self.move = move
        self.actions_left = state.actions()

    def is_fully_expanded(self):
        return len(self.actions_left) == 0
           
class GameSearch:
    '''
    Class containing different game search algorithms, call it with a defined game/node
    '''                 
    def __init__(self, game, depth=3, time = 0.2):
        self.state = game       
        self.depth = depth
        self.time = time
        self.elapsed_time = 0

    # Code

    def select(self, node):
        if not node.is_fully_expanded() or not node.actions_left:
            return node  # Choose unvisited node or node with available actions
        C = 1.0
        best_score = -float("inf")
        best_child = None

        for child in node.successors:
            exploit = child.wins / child.playouts
            explore = math.sqrt(math.log(node.playouts) / child.playouts)
            score = exploit + C * explore

            if score > best_score:
                best_score = score
                best_child = child

        if best_child:
            return self.select(best_child)  # Recursively select the best child
        else:
            return node  # All children have been visited or have no available actions return the current node
        
    def expand(self, node):
        if not node.is_fully_expanded():
            # Choose an untried action
            action = node.actions_left.pop()
            # Create a child node by applying the action
            new_state = node.state.result(action)
            child_node = GameNode(new_state, parent=node, move=action)

            # Update the parent's successors list
            node.successors.append(child_node)

            # If the new state is terminal return the child node with the terminal state
            is_terminal, value = new_state.is_terminal()
            if is_terminal:
                return child_node, value

            return child_node  # Return the new child node
        else:
            raise ValueError("Node is fully expanded. Cannot expand further.")
        
    def simulate(self, node):
       print("Node State:", node.state)
       state = node.state
       while True:
           legal_actions = state.actions()
           if not legal_actions:
               # The game is a draw
               return 0
           # Choose a random legal action
           random_action = random.choice(legal_actions)
           state = state.result(random_action)
           # Check if the game has reached a terminal state
           is_terminal, value = state.is_terminal()
           if is_terminal:
               if value == 100:  # AI wins
                   return 1
               elif value == -100:  # Player wins
                   return -1
               else:  # Draw
                   return 0
               
    def back_propagate(self, result, node):
        current_node = node
        while current_node is not None:
            current_node.playouts += 1
            if result == 1:
                if current_node.state.to_move() == self.state.ai_player:
                    current_node.wins += 1
            elif result == -1:
                if current_node.state.to_move() != self.state.ai_player:
                    current_node.wins += 1
            current_node = current_node.parent


    def actions(self, node):
        best_move = None
        best_score = -float("inf")

        for child in node.successors:
            if child.playouts > 0:
                score = child.wins / child.playouts
                if score > best_score:
                    best_score = score
                    best_move = child.move

        return best_move
    

    def mcts(self):                     
        start_time = process_time() 

        tree = GameNode(self.state)
        tree.actions_left = tree.state.actions()   
        elapsed_time = 0
        while elapsed_time < self.time:   
            leaf = self.select(tree)
            child = self.expand(leaf)   
            result = self.simulate(child) 
            self.back_propagate(result, child)         
            stop_time = process_time()
            elapsed_time = stop_time - start_time
        move = self.actions(tree)
        return move
    
    
    def minimax_search(self): 
        start_time = process_time() 
        _, move = self.max_value(self.state, self.depth, -float("inf"), float("inf"))  
        stop_time = process_time()
        self.elapsed_time = stop_time - start_time
        return move
    
    def max_value(self, state, depth, alpha, beta):
        move = None
        terminal, value = state.is_terminal()
        
        if terminal or depth == 0 or self.elapsed_time > self.time:
            return state.eval(), None
        
        v = -float("inf")
        actions = state.actions()
        for action in actions: 
            new_state = state.result(action)
            v2, _ = self.min_value(new_state, depth - 1, alpha, beta)
            if v2 > v:
                v = v2
                move = action
            alpha = max(alpha, v)
            if v >= beta:
                break  # Prune the rest of the branches
        return v, move
        
    def min_value(self, state, depth, alpha, beta):
        move = None
        terminal, value = state.is_terminal()
        if terminal or depth == 0:
            return state.eval(), None
        v = float("inf")
        actions = state.actions()
        for action in actions: 
            new_state = state.result(action)
            v2, _ = self.max_value(new_state, depth - 1, alpha, beta)
            if v2 < v:
                v = v2
                move = action
            beta = min(beta, v)
            if v <= alpha:
                break  # Prune the rest of the branches
        return v, move
    