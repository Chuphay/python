import random
import numpy as np
from brain import Network
import cPickle as pickle
import copy
from pybrain.tools.shortcuts import buildNetwork
#when we pick the winners, we should pick them on correctness obviously, but also slimness of the parameters. It's a painful way to regularize
#this might only be really useful for a stochastic brain
#kind of stoned
favorite_color = np.arange(12).reshape(3,4)

pickle.dump( favorite_color, open( "save2.p", "wb" ) )

favorite_colors = pickle.load( open( "save2.p", "rb" ) )
# favorite_color is now { "lion": "yellow", "kitty": "red" }
print favorite_colors, type(favorite_colors)

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

        #print self.__state__
        self.game_on = True
    def available(self):
        available = []
        for x in self.__state__:
            if type(x) == int:
                available.append(x)
        #print available
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
    def machine_state(self):
        return (np.asarray([self.get('X'),self.get('O')])).T 
                       
    def state(self, show = False): 
        if show:   
            print board%tuple(self.__state__)
        return self.__state__
    def put(self,value, position):
        if self.game_on:
            if position in self.available():
                #print 'good to go'
                self.__state__[position] = value 
                self.check_win()
            else:
                raise IndexError("Index Error???")    
        else:
            print 'game over...'
    def check_win(self):
        #print 'checking for win'
        state = self.__state__
        for i in range(3):
            if (state[3*i] == state[3*i+1] == state[3*i+2]):
                #print 'game over, %s wins' %state[3*i]
                self.game_on = False
            if (state[i] == state[i+3] == state[i+6]):
                #print 'game over, %s wins' %state[i] 
                self.game_on = False 
        if (state[0] == state[4] == state[8]):
            #print 'game over, %s wins' %state[0]
            self.game_on = False  
        if (state[2] == state[4] == state[6]):
            #print 'game over, %s wins' %state[2] 
            self.game_on = False 
        if self.available() == [] and self.game_on:
            print "cat's game" 
            self.game_on = False                                   
 
def computer_turn(value,game,place = None):

    #print 'computer is working ...'

    if place == None:
        available = game.available()
        random.shuffle(available)
        place = available[0]

    #print value, ' on ', place
    try:
        game.put(value, place)
        return 0
    except IndexError:
        #print 'foul!'
        return 1    
     
    



class computer_player(object):
    def __init__(self, array = None):

        if array == None:
            ##self.net  = [Network((18,18,1)) for i in range(9)]
            ##self.theta = [self.net[i].theta for i in range(9)]
            self.net = buildNetwork(18,18,9)
            self.theta = self.net.params

        else:
            ##self.theta = array
            ##self.net = [Network((18,18,1),self.theta[i]) for i in range(9)]
            self.theta = array
            self.net = buildNetwork(18,18,9)
            self.net._params = self.theta

    def get_move(self, array):
        """looking for np.array([[0,1],[1,0],[0,0],[0,0],[1,0],
        [0,0],[0,0],[0,0],[0,0]])
        where the first column is the X and the second column is the O
        and the 9 rows are obviously the 9 board positions
        """ 

        array = array.flatten().reshape(18,)
        #print array
        ##temp = []
        ##for i in range(9):
        ##    self.net[i].give_input(array)
        ##    temp.append(self.net[i].get_output())         
        ##temp = np.array(temp)
        ##output = temp.argmax()
        ##return output
        #print self.net.activate(array).argmax()
        return self.net.activate(array).argmax()
        
    def make_a_child(self):

        return computer_player(self.theta + 0.01*np.random.randn(len(self.theta))) 
    def have_a_child(self,parent2):
        new_theta = (self.theta + parent2.theta)/2 

        return computer_player(new_theta)     
  
  
        

#np.random.seed(123)
player1 = computer_player()
player2 = computer_player(player1.theta)
print player2.theta == player1.theta   
#game = Game()
#theta = pickle.load( open( "theta1.p", "rb" ) )
#print (np.asarray([game.get('X'),game.get('O')])).T ,'X'
#print player1.get_move(game.machine_state())
player2 = player1.make_a_child()
#print player2.get_move(game.machine_state())
def play_a_game(player1, play = False):
    game = Game()
    turn  = 1
    count = 0
    while True and turn<10:

        if play:
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

        if game.game_on == False:
            break 

        move =  player1.get_move(game.machine_state())        
        foul = computer_turn('X',game,move)
        count += foul

        if game.game_on == False:
            #count -= 2
            break    
        computer_turn('O',game)
        
        turn += 1
    foul_count.append(count)
    
play = False
print "Starting Game Now"
foul_count = []
players = []
for i in range(500):
    players.append(computer_player())
for i in range(500):
    #print i
    player = players[i]
    play_a_game(player)


print foul_count
print sum(foul_count)

for times in range(500):

    zee = []
    new_players = []
    for i,e in enumerate(foul_count):
        if e == 0:
            new_players.append(players[i])
            new_players.append(players[i].make_a_child())
            new_players.append(players[i].make_a_child())
            new_players.append(players[i].make_a_child())
            new_players.append(players[i].make_a_child())
            zee.append(i)
    for i,e in enumerate(foul_count):
        if e == 1:
            #new_players.append(players[i])
            #new_players.append(players[i].make_a_child())
            zee.append(i)
    ##for i,e in enumerate(foul_count):
      ##  if e == 2:
            #new_players.append(players[i])
        ##    zee.append(i) 
    ##for i,e in enumerate(foul_count):
      ##  if e == 3:
        ##    zee.append(i)                
    
    foul_count = []
    for j in range(3):
        for i in zee:
            
            new_players.append(players[i])
            new_players.append(players[i].make_a_child())
            
            new_players.append(players[i].make_a_child())
            new_players.append(players[i].make_a_child())
            new_players.append(players[i].make_a_child())
            new_players.append(players[i].make_a_child())
            try:
                new_players.append(players[i].have_a_child(players[i+1]))
            except IndexError:
                pass  
            try:
                new_players.append(players[i].have_a_child(players[i+2]))
            except IndexError:
                pass 
            try:
                new_players.append(players[i].have_a_child(players[i+3]))
            except IndexError:
                pass  
            try:
                new_players.append(players[i].have_a_child(players[i+4]))
            except IndexError:
                pass  
            try:
                new_players.append(players[i].have_a_child(players[i+5]))
            except IndexError:
                pass 
            try:
                new_players.append(players[i].have_a_child(players[i+6]))
    
            except IndexError:
                pass               
        #new_players.append(players[i].make_a_child())

    players = new_players[:501]
    for i in range(500):
        player = players[i]
        play_a_game(player)

       
    print foul_count[:20]
    print sum(foul_count)
           

theta = players[0].theta 
pickle.dump(theta, open( "theta2.p", "wb" ) )   
    
