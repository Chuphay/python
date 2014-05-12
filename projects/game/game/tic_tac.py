import random
import numpy as np
from brain import Network
import cPickle as pickle

favorite_color = np.arange(12).reshape(3,4)

pickle.dump( favorite_color, open( "save.p", "wb" ) )

favorite_color = pickle.load( open( "save.p", "rb" ) )
# favorite_color is now { "lion": "yellow", "kitty": "red" }
print favorite_color, type(favorite_color)

board = """
%s|%s|%s
-----
%s|%s|%s
-----
%s|%s|%s
"""


class Game(object):
    def __init__(self):
        self.__state__ = [i for i in range(9)]
        self.game_on = True
    def available(self):
        available = []
        for x in self.__state__:
            if type(x) == int:
                available.append(x)
        return available 
    def get(self,value):
        if value == 'X':
            out = []
            for i in self.__state__:
                if i == value:
                    out.append(1)
                else:
                    out.append(0)     
            return out        
        elif value == 'O':
            out = []
            for i in self.__state__:
                if i == value:
                    out.append(1)
                else:
                    out.append(0)
            return out        
        else:
            print 'error'       
    def state(self, show = False): 
        if show:   
            print board%tuple(self.__state__)
        return self.__state__
    def put(self,value, position):
        if self.game_on:
            self.__state__[position] = value 
            self.check_win()
        else:
            print 'game over...'
    def check_win(self):
        print 'checking for win'
        state = self.__state__
        for i in range(3):
            if (state[3*i] == state[3*i+1] == state[3*i+2]):
                print 'game over, %s wins' %state[3*i]
                self.game_on = False
            if (state[i] == state[i+3] == state[i+6]):
                print 'game over, %s wins' %state[i] 
                self.game_on = False 
        if (state[0] == state[4] == state[8]):
            print 'game over, %s wins' %state[0]
            self.game_on = False  
        if (state[2] == state[4] == state[6]):
            print 'game over, %s wins' %state[2] 
            self.game_on = False 
        if self.available() == [] and self.game_on:
            print "cat's game" 
            self.game_on = False                                   
 
def computer_turn(value):

    print 'computer is working ...'
    state = game.state()
    #print game.get('X')
    #print game.get('O')
    available = []
    for x in state:
        if type(x) == int:
            available.append(x)
    #print available
    random.shuffle(available)
    game.put(value,available[0])
    print value, ' on ', available[0] 
    



class computer_player(object):
    def __init__(self, array = None):

        if array == None:
            self.net  = [Network((18,18,1)) for i in range(9)]
            self.theta = [self.net[i].theta for i in range(9)]
        else:
            #s = np.array(array[0])
            #print s.shape
            #print len(array), len(array[0]), 'shapes'
            
            self.theta = array

            self.net = [Network((18,18,1),self.theta[i]) for i in range(9)]

    def get_move(self, array):
        """looking for np.array([[0,1],[1,0],[0,0],[0,0],[1,0],
        [0,0],[0,0],[0,0],[0,0]])
        where the first column is the X and the second column is the O
        and the 9 rows are obviously the 9 board positions
        """ 

        array = array.flatten().reshape(18,1) 

        temp = []
        theta = []
        for i in range(9):
            self.net[i].give_input(array)
            temp.append(self.net[i].get_output())
            theta.append(self.net[i].get_theta())            
        temp = np.array(temp)
        output = temp.argmax()
        theta = np.asarray(theta)    
        print temp , output, theta[0].shape

  
        
np.random.seed(123)
player1 = computer_player()
player1.get_move(np.array([[0,1],[1,0],[0,0],[0,0],[1,0],\
        [0,0],[0,0],[0,0],[0,0]]))
print player1.theta[0].shape, 'here'
#print player1.theta[0]

player2 = computer_player(player1.theta)
player2.get_move(np.array([[0,1],[1,0],[0,0],[0,0],[1,0],\
        [0,0],[0,0],[0,0],[0,0]]))        
print player1.theta == player2.theta
   
game = Game()
turn  = 1
player = False
while False:
    print 'turn: ', turn

    state = game.state(show = True)
    if player:
        choice = raw_input('q to quit, else, place an X \n>>> ')
        if choice == 'q':
            break
        available = []
        for x in state:
            if type(x) == int:
                available.append(x)
        if int(choice) in available:            
            game.put('X',int(choice))
        else:
            print 'erp.. try again'
            continue         
    #print 'yo', choice
    computer_turn('X')
    if game.game_on == False:
        print 'the game is over?'
        game.state(show = True)
        break    
    computer_turn('O')
    turn += 1
