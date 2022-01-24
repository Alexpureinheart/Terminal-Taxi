import random

#movement variables 
actions = ['turn left', 'turn right', 'accelerate', 'break', 'reverse', 'view map', 'check position']

x_coordinate = 2
y_coordinate = 4

is_facing_east = True
is_facing_west = False
is_facing_south = False
is_facing_north = False

has_customer = False
customer_exists = False

customer_interaction_determiner = 0

#game objects (dictionaries)
#customer system

first_names = ['Arandeep', 'Helen', 'Marianne', 'Madiha', 'Shazia', 'Rupert', 'Eleni', 'Tadhg', 'Tayyib',
'Ameer', 'Ihsan', 'Luna', 'Chase', 'Addie', 'Velma', 'Ayush', 'Rubi', 'Ariadne', 'Ziva', 'Lani']

last_names = ['Galloway', 'Dawe', 'Buchanan', 'Bush', 'Mcdowell', 'Guzman', 'Villanueva', 'Henson', 'Park',
 'Coates', 'Glover', 'Hicks', 'Barnes', 'Petersen', 'Hutchinson', 'Moyer', 'Holmes', 'Lennon', 'Pitt', 'Pearson']      

class Customer:
    def __init__(self, first_name, last_name, destination):
        self.first_name = first_name
        self.last_name = last_name
        self.destination = destination

def customer_generator():
    global first_names
    global last_names
    global location_list
    
    return Customer(first_names[random.randint(0, len(first_names) - 1)], last_names[random.randint(0, len(last_names) - 1)],
    location_list[random.randint(0, len(location_list) - 1)])
 

#locations

class Location:
    def __init__(self, name, x_coordinates, y_coordinates):
        self.name = name
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates 
    def get_name(self):
        return self._name
    def get_x_coordinate(self):
        return self._x_coordinates
    def get_y_coordinate(self):
        return self._y_coordinates

location_1 = Location('location 1', [3, 4, 5], [10, 11, 12, 13, 14])
location_2 = Location('location 2', [6, 7, 8], [10, 11, 12, 13])
location_3 = Location('location 3', [9, 10, 11, 12, 13], [10, 11, 12, 13])
location_4 = Location('location 4', [15, 16, 17], [10, 11, 12, 13, 14])
location_5 = Location('location 5', [18, 19, 20, 21], [10, 11, 12, 13])
location_6 = Location('location 6', [22, 23, 24], [10, 11, 12, 13])
location_7 = Location('location 7', [25, 26, 27], [10, 11, 12, 13])
location_8 = Location('location 8', [2, 3, 4, 5], [7, 8, 9])
location_9 = Location('location 9', [2, 3, 4, 5], [4, 5, 6])
location_10 = Location('location 10', [6, 7, 8, 9], [6, 7, 8])
location_11 = Location('location 11', [8, 9, 10], [7, 8])
location_12 = Location('location 12', [11, 12, 13, 14], [7, 8, 9])
location_13 = Location('location 13', [9, 10, 11, 12, 13], [4, 5, 6])
location_14 = Location('location 14', [13, 14, 15, 16, 17, 18], [4, 5, 6, 7, 8, 9, 10])
location_15 = Location('location 15', [18, 19, 20], [7, 8, 9])
location_16 = Location('location 16', [19, 20, 21], [4, 5, 6])
location_17 = Location('location 17', [21, 22, 23, 24], [7, 8, 9, 10, 11])
location_18 = Location('location 18', [24, 25, 26, 27, 28], [6, 7, 8, 9])
location_19 = Location('location 19', [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [2, 3, 4])
location_20 = Location('location 20', [21, 22, 23, 24, 25, 26, 27], [1, 2, 3, 4, 5, 6, 7])

location_list = [location_1, location_2, location_3, location_4, location_5, location_6, location_7,
location_8, location_9, location_10, location_11, location_12, location_13, location_14, location_15,
location_16, location_17, location_18, location_19, location_20]

oak_street = Location('Oak Street', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], [11])
silver_street = Location('Silver Street', [2], [4,5,6,7,8,9,10,11])
green_road = Location('Green Road', [8], [4,5,6,7,8,9,10,11])
litte_street = Location('Little Street', [13], [4,5,6,7,8,9,10,11])
saxon_way = Location('Saxon Way', [18], [4,5,6,7,8,9,10,11])
bond_ave_1 = Location('Bond Avenue', [21], [4,5,6,7])
bond_ave_2 = Location('Bond Avenue', [21, 22, 23, 24], [7])
bond_ave_3 = Location()




boundary_top = Location('side walk', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], [12, 13])
boundary_bottom = Location('sea', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], [1, 2]) 
boundary_left = Location('side walk', [3, 4, 5, 6, 7], [5, 6, 7, 8, 9, 10])
boundary_middle_left = Location('side walk', [9, 10, 11, 12], [5, 6, 7, 8, 9, 10])
boundary_middle = Location('side walk', [14, 15, 16, 17], [5, 6, 7, 8, 9, 10])
boundary_middle_right_1 = Location('side walk', [19, 20], [5, 6, 7, 8, 9, 10])
boundary_middle_right_2 = Location('side walk', [21, 23], [8, 9])
boundary_right = Location('side walk', [25, 27], [6, 7, 8, 9, 10])
boundary_lower_right = Location('harbor', [22, 23, 24, 25, 26, 27, 28], [3, 4, 5, 6])

boundary_list = [boundary_top, boundary_bottom, boundary_left, boundary_middle_left, boundary_middle, boundary_middle_right_1,
boundary_middle_right_2, boundary_right, boundary_lower_right]



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
@6                                    Oak St.                                                       g@
@<<<| S |<<<<<<<<<<<<<<<<| G |<<<<<<<<<<<<<<<| L |<<<<  <<<<<| S |<<<<<<<<<<<<<<<<<|   |>>>>>>>>>>>>g@
@6  | i | ____       ___ | r |          ___  | i |  __| |__  | a | ___    __| |__  |   | ___        g@
@6  | l ||    |     |___|| e |___      |12 | | t |_|  ___  |_| x ||   |  |___17__| |   ||   |       g@
@6  | v || 8  |    |    || e |11 |     |___| | t  _  /   \  _  o || 15|   >>>>>>>>>|   ||   |___    g@
@6  | e ||____|__  | 10 || n |___|           | l | | \___/ | | n ||___|  | Bond Ave.   ||  18   |   g@
@6  | r ||  9    | |____||   |   ___________ | e | |__   __| |   |  ____ |   |>>>>>>>>>>|_______|   g@
@6  |   ||_______|       | R |  |__13_______||   |    | | 14 | W | |_16_||   |  ___________________ g@
@6 _| S |>>>>>>>>>>>>>>>>| d |>>>>>>>>>>>>>>>| S |>>>>> >>>>>| y |>>>>>>>|   | |                   |g@
@6    t                         Sandy Blvd.    t                               |        20         |g@
@6 __START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|                   |g@                                                                                 
@6 ____________________________________________________________________________|___________________|g@
@6 ~~~~~~~~~~~~~~~~~~~~~~|______   19    _______________|~~~~~~~~~~~~~~~~~~~~~~~~~~~~|        |~~~~~g@
@6 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|       |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|        |~~~~~g@
QBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBQ
        
        
        """)


def check_position():
    
    global is_facing_east
    global is_facing_west
    global is_facing_south
    global is_facing_north

    global x_coordinate
    global y_coordinate 

    if is_facing_east:
        print('You are facing East.')
    elif is_facing_west:
        print('You are facing West.')
    elif is_facing_south:
        print('You are facing South.')
    elif is_facing_north:
        print('You are facing North.')
    print('At x: ' + str(x_coordinate) + ' and y: ' + str(y_coordinate) + '.')
    
    for i in range(len(location_list)):
        if x_coordinate in location_list[i].x_coordinates and y_coordinate in location_list[i].y_coordinates:
            print('You are at ' + location_list[i].name + '.')
         
def hit_the_break():
    print('You have stopped.')

def customer_interaction(customer):

    global x_coordinate
    global y_coordinate
    
    print('The customer gets into your cab.')
    print('"Can you take me to "' + customer.destination.name + '?')
    print('Possible responses: "Sorry.", "Sure!"')
    while True:
        response = input()   
        if response == "Sorry.":
            print('"Bummer."')
            print('The customer gets out.')
            customer_exists = False
            break  
        elif response == "Sure!":
            print('"Thanks!"')
            has_customer = True
            while has_customer == True:
                action = input()
                if action not in actions:
                    print('Input a valid action. Possible actions are ' + str(actions))
                elif action == "view map":  
                    view_map()
                elif action == "check position":
                    check_position()
                    print('The customer is sitting in the back seat.')
                elif action == "break":
                    hit_the_break() 
                else:
                    control_taxi(action)
                    if x_coordinate in customer.destination.x_coordinates and y_coordinate in customer.destination.y_coordinates:
                        print('"Thanks! Let me out here!"')
                        break
            break
        else:
            print('Please enter a valid response.') 

def control_taxi(action):
    
    global is_facing_east
    global is_facing_west
    global is_facing_south
    global is_facing_north

    global x_coordinate
    global y_coordinate 



    if is_facing_east:
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

print('the length of location_list is ' + str(len(location_list)))

i = 0

while i < 10:

    customer_interaction_determiner = random.randint(1, 10)
    print(customer_interaction_determiner)

    for i in range(len(boundary_list)):
        if x_coordinate in boundary_list[i].x_coordinates and y_coordinate in boundary_list[i].y_coordinates:
            if boundary_list[i].name == 'side walk':
                print('You drove onto the ' + boundary_list[i].name + '.')
            elif boundary_list[i].name == 'sea':
                print('You drove into the ' + boundary_list[i].name + '.')

    customer = customer_generator()
    print(customer.first_name)
    print(customer.last_name)
    print(customer.destination.name) 

    
    if customer_interaction_determiner >= 6 and has_customer == False:
        print("A customer is hailing your taxi!")
        customer_exists = True

    action = input()

    if action not in actions:
        print('Input a valid action. Possible actions are ' + str(actions))
    elif action == "view map":  
       view_map()
    elif action == "check position":
        check_position()
    elif customer_exists == True and action == "break": #this is the customer interaction code -- may wrap in function
        hit_the_break()
        customer_interaction(customer)      
    elif action == "break":
        hit_the_break() 
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