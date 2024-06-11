'''
Define game and start execution of game search

Author: Tony Lindgren
'''
from four_in_a_row import FourInARow
from game_node_and_game_search import GameSearch

    
def ask_ai(state0):
    gs = GameSearch(state0, depth=3, time = 5)
    move = gs.minimax_search()

    # gs = GameSearch(state0, depth=3, time=20)
    # move = gs.mcts()
    state1 = state0.result(move)
    print('--------')
    print('AI moves')
    print('--------')
    state1.pretty_print()  
    stop, value = state1.is_terminal() 
    if stop == True:
        if value > 0:
            print('AI won')     
            state1.pretty_print()  
                  
        else:
            print('Human won')
            state1.pretty_print()  

        return state1, True
    return state1, False 

# Code
def ask_player(state1):
    while True:
        answer = input('Enter your move (column 0-6): ')
        try:
            answer = int(answer)
            if answer not in FourInARow.actions(state1):
                print('You made an illegal move, choose another column.')
            else:
                break  # Break out of the loop if the input is valid
        except ValueError:
            print('Invalid input. Please enter a number between 0 and 6.')

    state0 = state1.result(answer)
    stop, value = state0.is_terminal()
    if stop:
        if value > 0:
            print('AI won')
        else:
            print('Human won')
        return state0, True
    return state0, False


 
def main():
    print('Welcome to play for-in-a-row!')
    answer = None
    while answer != 'y' and answer != 'n':
        answer = input('Would you like to start [y/n]: ')        
    if(answer == 'y'):  
        state0 = FourInARow('human', 'w') 
        stop = False
        while not stop:            
        #Ask player         
            state1, stop1 = ask_player(state0)
            if stop1:
                break
            else:
        #AI move
                state0, stop2 = ask_ai(state1)  

                if stop2:
                    break                
    else:
        state0 = FourInARow('ai','w') 
        stop = False
        while not stop: 
        #AI move
            state1, stop1 = ask_ai(state0)    
            if stop1:
                break
            else:  
        #Ask player
                state0, stop2 = ask_player(state1)    
                if stop2:
                    break               
       
if __name__ == "__main__":
    main()