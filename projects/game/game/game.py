import random


board = """
%s|%s|%s
-----
%s|%s|%s
-----
%s|%s|%s
"""


#print board
class Player(object):
    def __init__(self,name = None, cities = [], resources = 100):
            self.resources = resources
            self.cities = cities
    
class City(object):
    def __init__(self, spot):
        resources_per_turn = 20
        cost_soldier = 60
        cost_new_city = 200
        cost_research = 60
        soldiers = 0
        research = 0
        self.spot = spot
class Game(object):
    def __init__(self):
        a = [i for i in range(1,10)]
        random.shuffle(a)
        self.board_string = ['%d'%i for i in range(1,10)]
        hero = a[0]
        enemy = a[1]
        self.board_string[hero-1] = 'X'
        self.board_string[a[2]-1] = 'X'
        self.board_string[enemy-1] = 'E'

        #print board%tuple(self.board_string)
        my_city = City(hero)
        my_second_city = City(a[2])
        me = Player('dave', [hero,a[2]])
        #print me.cities
        #print my_city.spot
        self.hero_city = me.cities
    def state(self):
        print board%tuple(self.board_string)
game = Game() 
def computer_turn():
    print 'computer did nothing'       

turn  = 1
while True:
    print 'turn: ', turn
    state = game.state()
    cities = game.hero_city
    length = len(cities)
    print cities
    choice = raw_input('0 to pass, 1 to buy a soldier, 2 to buy a city, 3 to research, 4 to send resources, 5 to send soldiers, 6 go to next city,q to quit ')
    if choice == 'q':
        break
    if choice == '0':
        pass 
    if choice == '1':
        print 'you bought a soldier'
        continue      
    print 'yo', choice
    computer_turn()
    turn += 1




  
        
        
        
        
        
        
        
        
        

