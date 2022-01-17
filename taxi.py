#movement variables 
actions = ['turn left', 'turn right', 'accelerate', 'reverse', 'view map', 'check position']

x_coordinate = 0
y_coordinate = 0

is_facing_east = True
is_facing_west = False
is_facing_south = False
is_facing_north = False 

#command functions
def view_map():
     print(""" 
        
                                    WATERFRONT DISTRICT 
@#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM#@   
@6       ________                                    ______                                         g@  
@6      |        |   _____     _______________      |      |      ________       ______   _____     g@
@6      |    1   |  |  2  |   |      3        |     |  4   |     |   5    |     |  6   | |  7  |    g@
@6      |________|  |_____|   |_______________|     |______|     |________|     |______| |_____|    g@
@6<<TO FINANCIAL DISTRICT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>TO HIGHWAY>>>g@
@6                                                                                                  g@
@<<<|   |<<<<<<<<<<<<<<<<|   |<<<<<<<<<<<<<<<|   |<<<<  <<<<<|   |<<<<<<<<<<<<<<<<<|   |>>>>>>>>>>>>g@
@6  |   | ____       ___ |   |          ___  |   |  __| |__  |   | ___    __| |__  |   | ___        g@
@6  |   ||    |     |___||   |___      |12 | |   |_|  ___  |_|   ||   |  |___17__| |   ||   |       g@
@6  |   || 8  |    |    ||   |11 |     |___| |    _  /   \  _    || 15|   >>>>>>>>>|   ||   |___    g@
@6  |   ||____|__  | 10 ||   |___|           |   | | \___/ | |   ||___|  |             ||  18   |   g@
@6  |   ||  9    | |____||   |   ___________ |   | |__   __| |   |  ____ |   |>>>>>>>>>>|_______|   g@
@6  |   ||_______|       |   |  |__13_______||   |    | | 14 |   | |_16_||   |  ___________________ g@
@6 _|   |>>>>>>>>>>>>>>>>|   |>>>>>>>>>>>>>>>|   |>>>>> >>>>>|   |>>>>>>>|   | |                   |g@
@6                                                                             |        20         |g@
@6 __START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|                   |g@                                                                                 
@6 ____________________________________________________________________________|___________________|g@
@6 ~~~~~~~~~~~~~~~~~~~~~~|______   19    _______________|~~~~~~~~~~~~~~~~~~~~~~~~~~~~|        |~~~~~g@
@6 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|       |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|        |~~~~~g@
QBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBQ
        
        
        """)



def control_taxi(action):
    
    global is_facing_east
    global is_facing_west
    global is_facing_south
    global is_facing_north

    global x_coordinate
    global y_coordinate 

    def check_position():
        if is_facing_east:
            print('You are facing East. At x: ' + str(x_coordinate) + ' and y: ' + str(y_coordinate) + '.')
        elif is_facing_west:
            print('You are facing West. At x: ' + str(x_coordinate) + ' and y: ' + str(y_coordinate) + '.')
        elif is_facing_south:
            print('You are facing South. At x: ' + str(x_coordinate) + ' and y: ' + str(y_coordinate) + '.')
        elif is_facing_north:
            print('You are facing North. At x: ' + str(x_coordinate) + ' and y: ' + str(y_coordinate) + '.') 

    if action == "check position":
        check_position()

    elif is_facing_east:
        match action:
            case 'turn left':
                is_facing_east = False
                is_facing_north = True
                print('You are facing North.')
            case 'turn right':
                is_facing_east = False
                is_facing_south = True
                print('You are facing South.')
            case 'accelerate':
                x_coordinate += 1
                print('x is now equal to ' + str(x_coordinate))
            case 'reverse':
                x_coordinate -= 1 
                print('x is now equal to ' + str(x_coordinate)) 
            case _:
                'Input a valid action.'    
                
    elif is_facing_west:
        match action:
            case 'turn left':
                is_facing_west = False
                is_facing_south = True
                print('You are facing South.')
            case 'turn right':
                is_facing_west = False
                is_facing_north = True 
                print('You are facing North.')
            case 'accelerate':
                x_coordinate -= 1
                print('x is now equal to ' + str(x_coordinate))
            case 'reverse':
                x_coordinate += 1 
                print('x is now equal to ' + str(x_coordinate))
            case _:
                'Input a valid action.'    

    elif is_facing_north:
        match action:
            case 'turn left':
                is_facing_north = False
                is_facing_west = True
                print('You are facing West.')
            case 'turn right':
                is_facing_north = False
                is_facing_east = True
                print('You are facing East.')
            case 'accelerate':
                y_coordinate += 1
                print('y is now equal to ' + str(y_coordinate))
            case 'reverse':
                y_coordinate -= 1
                print('y is now equal to ' + str(y_coordinate)) 
            case _:
                'Input a valid action.'     

    elif is_facing_south:
        match action:
            case 'turn left':
                is_facing_south = False
                is_facing_east = True
                print('You are facing East.')
            case 'turn right':
                is_facing_south = False
                is_facing_west = True
                print('You are facing West.')
            case 'accelerate':
                y_coordinate -= 1
                print('y is now equal to ' + str(y_coordinate))
            case 'reverse':
                y_coordinate += 1
                print('y is now equal to ' + str(y_coordinate))
            case _:
                'Input a valid action.' 



#game scripting

print("""

 ________  ______   _______   ________   __   ________   ________   __
|__    __||   ___| |   __  | |        | |  | |     |  | |   __   | |  |
   |  |   |   ___| |  |__  | |  |  |  | |  | |  |  |  | |  |__|  | |  |____
   |__|   |______| |__||__|  |__|__|__| |__| |__|_____| |__|  |__| |_______|
 ________  ________  ___   ___    __   _____________  _________
/__   __/ /  __    / \  \ /  /   /  /  ____________  /    \    \ 
  /  /   /  /__/  /   /     /   /  /   ________  ___/      \ ___\_________ 
 /__/   /__/  /__/   /__/ \__\ /__/    ______   /_________________________/
                                                    \__/         \__/ 

""")

print('Input an action.')
print('Possible actions are ' + str(actions))
print('You are facing East.')

i = 0

while i < 10:

    action = input()

    if action not in actions:
        print('Input a valid action. Possible actions are ' + str(actions))
    elif action == "view map":  
       view_map()
    else:
        control_taxi(action) 
        
           
                  


        
        




#rudimentary customer functionality -- will rework later

""" customer = {
    'name' : 'Joe',
    'directions' :  ['go straight', 'turn right', 'stop here'],
    'fare' : 0
}

print("These are the directions: " + str(customer['directions'][0]) + ", " + str(customer['directions'][1]) + ", " + str(customer['directions'][2]))

i = 0
while i < len(customer['directions']):

    direction = input()
    if direction == str(customer['directions'][i]):
        print("Great!")
        customer['fare'] += 1
    else:
        print("You went the wrong way!")

    i += 1

print('Thanks very much!' + ' You get ' + str(customer['fare']) + ' dollars.') """