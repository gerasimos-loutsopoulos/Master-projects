'''
Four in a row

Author: Tony Lindgren
'''
from copy import deepcopy

class FourInARow:
    def __init__(self, player, chip):
        new_board = []
        for _ in range(7):
            new_board.append([])
        self.board = new_board
        self.action = list(range(7))
        if chip != 'r' and chip != 'w':
            print('The provided value is not a valid chip (must be, r or w): ', chip)
        if player == 'human' and chip == 'w':
            self.ai_player = 'r'
        else:
            self.ai_player = 'w'
        self.curr_move = chip
    
    def to_move(self):
        return self.curr_move
    
    # Code
    #actions
    #TODO

    def actions(self):
        legal_actions = []
        for column in range(7):
            if len(self.board[column]) < 6:
                legal_actions.append(column)
        return legal_actions

    def result(self, action):                    
        dc = deepcopy(self)
        if self.to_move() == 'w':
            dc.curr_move = 'r'
            dc.board[action].append(self.to_move())   
        else:

            dc.curr_move = 'w'
            dc.board[action].append(self.to_move())    
        
        return dc
        
    #eval
    #TODO
    # Code Evaluation
    def eval(self):
        # Define a board position value matrix.
        position_values = [
            [3, 4, 5, 7, 5, 4, 3],
            [4, 6, 8, 10, 8, 6, 4],
            [5, 8, 11, 13, 11, 8, 5],
            [5, 8, 11, 13, 11, 8, 5],
            [4, 6, 8, 10, 8, 6, 4],
            [3, 4, 5, 7, 5, 4, 3]
        ]

        ai_player = self.ai_player
        player_chips = 0
        ai_chips = 0

        for col in range(7):
            for row in range(6):
                if len(self.board[col]) > row:
                    if self.board[col][row] == ai_player:
                        ai_chips += position_values[row][col]
                    else:
                        player_chips += position_values[row][col]

        # You can adjust the weights for the number of chips and positions as needed.
        # For example, you might want to give more weight to the number of chips.
        ai_score = ai_chips + ai_chips * (ai_chips / (ai_chips + player_chips))
        player_score = player_chips + player_chips * (player_chips / (ai_chips + player_chips))

        # Return the difference between AI's and player's scores.
        return ai_score - player_score

        
    def is_terminal(self):

        #check vertical
        for c in range(0, len(self.board)):
            count = 0
            curr_chip = None
            for r in range(0, len(self.board[c])):
                if curr_chip == self.board[c][r]:
                    count = count + 1
                    
                else:
                    curr_chip = self.board[c][r]
                    count = 1
                # print("C and R pairs", c,r)

                if count == 4:
                    if self.ai_player == curr_chip:        
                        print('Found vertical win')
                        return True, 100          #MAX ai wins positive utility
                    else:
                        print('Found vertical loss')
                        return True, -100         #MIN player wins negative utility
                    
            
                    
        # Code for Horizontal Win
        for r in range(0,6):
            count = 0
            curr_chip = None
            for c in range(0,len(self.board)):
                if(r < (len(self.board[c]))):
                    if curr_chip == self.board[c][r]:
                        count = count + 1
                    else:
                        curr_chip = self.board[c][r]
                        count = 1

                    if count == 4:
                        if self.ai_player == curr_chip:        
                            print('Found horizontal win')
                            return True, 100          #MAX ai wins positive utility
                        else:
                            print('Found horizontal loss')
                            return True, -100         #MIN player wins negative utility
                

        # Code            
        #check positive diagonal
        for c in range(7-3): 
            for r in range(6-3):    
                if len(self.board[c]) > r and len(self.board[c+1]) > r+1 and len(self.board[c+2]) > r+2 and len(self.board[c+3]) > r+3: #checks length
                    if self.ai_player == self.board[c][r] and self.ai_player == self.board[c+1][r+1] and self.ai_player == self.board[c+2][r+2] and self.ai_player == self.board[c+3][r+3]:  
                        print('Found positive diagonal win')
                        return True, 100
                    elif self.ai_player != self.board[c][r] and self.ai_player != self.board[c+1][r+1] and self.ai_player != self.board[c+2][r+2] and self.ai_player != self.board[c+3][r+3]:  
                        print('Found positive diagonal loss')
                        return True, -100
        # Code
        #check negative diagonal 
        for c in range(3,7):
            for r in range(6-3):
                if len(self.board[c]) > r and len(self.board[c-1]) > r+1 and len(self.board[c-2]) > r+2 and len(self.board[c-3]) > r+3: #checks length
                    if self.ai_player == self.board[c][r] and self.ai_player == self.board[c-1][r+1] and self.ai_player == self.board[c-2][r+2] and self.ai_player == self.board[c-3][r+3]:
                        print('Found negative diagonal win')
                        return True, 100
                    elif self.ai_player != self.board[c][r] and self.ai_player != self.board[c-1][r+1] and self.ai_player != self.board[c-2][r+2] and self.ai_player != self.board[c-3][r+3]:  
                        print('Found negative diagonal loss')
                        return True, -100  



    # Code
        #check draw
        draw_possible = all(len(self.board[c]) == 6 for c in range(len(self.board)))
        if draw_possible:
            return True, 0  # All columns are filled, it's a draw 
         
        return False, 0    


    # Code                                              
    def pretty_print(self):
        for row in range(5, -1, -1):
            for col in range(7):
                if len(self.board[col]) <= row:
                    print("_", end=" ")
                else:
                    print(self.board[col][row], end=" ")
            print()  # Move to the next row
