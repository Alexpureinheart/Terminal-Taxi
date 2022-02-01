import random

#movement variables 
actions = ['turn left', 'turn right', 'accelerate', 'break', 'reverse', 'view map', 'check position', 'ask for destination']

x_coordinate = 2
y_coordinate = 4

is_facing_east = True
is_facing_west = False
is_facing_south = False
is_facing_north = False

has_customer = False
customer_exists = False

money = 0

customer_interaction_determiner = 0
customers_delivered = []

cardinal_direction = 'East'

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
        self.fare = 3.25


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

location_1 = Location("Bob's Books", [3, 4, 5], [10, 11, 12, 13, 14])
location_2 = Location('Pizza Palace', [6, 7, 8], [10, 11, 12, 13])
location_3 = Location('The Waterfront Library', [9, 10, 11, 12, 13], [10, 11, 12, 13])
location_4 = Location("Manuel the Dentist's", [15, 16, 17], [10, 11, 12, 13, 14])
location_5 = Location('Dope Beatz', [18, 19, 20, 21], [10, 11, 12, 13])
location_6 = Location('The Seashore Appartments', [22, 23, 24], [10, 11, 12, 13])
location_7 = Location('The Seashore Lofts', [25, 26, 27], [10, 11, 12, 13])
location_8 = Location('Burger Meister', [2, 3, 4, 5], [7, 8, 9])
location_9 = Location("Sally's Sweet Suites", [2, 3, 4, 5], [4, 5, 6])
location_10 = Location('Green Street Sports', [6, 7, 8, 9], [6, 7, 8])
location_11 = Location("N'ice! Cream'", [8, 9, 10], [7, 8])
location_12 = Location("Dante's Deck Chairs", [11, 12, 13, 14], [7, 8, 9])
location_13 = Location('Waterfront Bicycle Rentals', [9, 10, 11, 12, 13], [4, 5, 6])
location_14 = Location('St. Busta Park', [13, 14, 15, 16, 17, 18], [4, 5, 6, 7, 8, 9, 10])
location_15 = Location("Kyle's Curry Goat", [18, 19, 20], [7, 8, 9])
location_16 = Location("Shanty's Sea Shack", [19, 20, 21], [4, 5, 6])
location_17 = Location('Waterfront Post Office', [21, 22, 23, 24], [7, 8, 9, 10, 11])
location_18 = Location("Pop-in Shoppin'", [24, 25, 26, 27, 28], [6, 7, 8, 9])
location_19 = Location('The Waterfront Pier', [7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [2, 3, 4])
location_20 = Location('The Waterfront Harbor', [21, 22, 23, 24, 25, 26, 27], [1, 2, 3, 4, 5, 6, 7])

location_list = [location_1, location_2, location_3, location_4, location_5, location_6, location_7,
location_8, location_9, location_10, location_11, location_12, location_13, location_14, location_15,
location_16, location_17, location_18, location_19, location_20]

oak_street = Location('Oak Street', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], [11])
silver_street = Location('Silver Street', [2], [4,5,6,7,8,9,10,11])
green_road = Location('Green Road', [8], [4,5,6,7,8,9,10,11])
little_street = Location('Little Street', [13], [4,5,6,7,8,9,10,11])
saxon_way = Location('Saxon Way', [18], [4,5,6,7,8,9,10,11])
bond_ave_1 = Location('Bond Avenue', [21], [4, 5, 6, 7])
bond_ave_2 = Location('Bond Avenue', [21, 22, 23, 24], [7])
bond_ave_3 = Location('Bond Avenue', [24], [7, 8, 9, 10, 11])
sandy_boulevard = Location('Sandy Boulevard', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21], [4])

street_list = [oak_street, silver_street, green_road, little_street, saxon_way, bond_ave_1, bond_ave_2, bond_ave_3, sandy_boulevard]

boundary_top = Location('side walk', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], [12, 13])
boundary_bottom = Location('sea', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], [1, 2]) 
boundary_left = Location('side walk', [3, 4, 5, 6, 7], [5, 6, 7, 8, 9, 10])
boundary_middle_left = Location('side walk', [9, 10, 11, 12], [5, 6, 7, 8, 9, 10])
boundary_middle = Location('side walk', [14, 15, 16, 17], [5, 6, 7, 8, 9, 10])
boundary_middle_right_1 = Location('side walk', [19, 20], [5, 6, 7, 8, 9, 10])
boundary_middle_right_2 = Location('side walk', [21, 23], [8, 9])
boundary_right = Location('side walk', [25, 27], [6, 7, 8, 9, 10])
boundary_lower_right = Location('harbour', [22, 23, 24, 25, 26, 27, 28], [3, 4, 5, 6])

boundary_list = [boundary_top, boundary_bottom, boundary_left, boundary_middle_left, boundary_middle, boundary_middle_right_1,
boundary_middle_right_2, boundary_right, boundary_lower_right]



#command functions
def view_map():
     print(""" 
        
                                    WATERFRONT DISTRICT 
@#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM#@   
@6       ________                                    ______                                         g@  1. Bob's Books
@6      |        |   _____     _______________      |      |      ________       ______   _____     g@  2. Pizza Palace
@6      |    1   |  |  2  |   |      3        |     |  4   |     |   5    |     |  6   | |  7  |    g@  3. Waterfront Library
@6      |________|  |_____|   |_______________|     |______|     |________|     |______| |_____|    g@  4. Manuel the Dentist
@6<<TO FINANCIAL DISTRICT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>TO HIGHWAY>>>g@  5. Dope Beatz
@6                                    Oak St.                                                       g@  6. Seashore Appts.
@<<<| S |<<<<<<<<<<<<<<<<| G |<<<<<<<<<<<<<<<| L |<<<<  <<<<<| S |<<<<<<<<<<<<<<<<<|   |>>>>>>>>>>>>g@  7. Seashore Lofts 
@6  | i | ____       ___ | r |          ___  | i |  __| |__  | a | ___    __| |__  |   | ___        g@  8. Burger Meister
@6  | l ||    |     |___|| e |___      |12 | | t |_|  ___  |_| x ||   |  |___17__| |   ||   |       g@  9. Sally's Sweet Suites
@6  | v || 8  |    |    || e |11 |     |___| | t  _  /   \  _  o || 15|   >>>>>>>>>|   ||   |___    g@  10.Green Street Sports 
@6  | e ||____|__  | 10 || n |___|           | l | | \___/ | | n ||___|  | Bond Ave.   ||  18   |   g@  11.N'ice! Cream
@6  | r ||  9    | |____||   |   ___________ | e | |__   __| |   |  ____ |   |>>>>>>>>>>|_______|   g@  12.Dante's Deck Chairs 
@6  |   ||_______|       | R |  |__13_______||   |    | | 14 | W | |_16_||   |  ___________________ g@  13.Waterfront Bicycle Rentals 
@6 _| S |>>>>>>>>>>>>>>>>| d |>>>>>>>>>>>>>>>| S |>>>>> >>>>>| y |>>>>>>>|   | |                   |g@  14.St. Busta Park
@6    t                         Sandy Blvd.    t                               |        20         |g@  15.Kyle's Curry Goat
@6 __START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|                   |g@  16.Shanty's Sea Shack                                                                               
@6 ____________________________________________________________________________|___________________|g@  17.Waterfront Post Office 
@6 ~~~~~~~~~~~~~~~~~~~~~~|______   19    _______________|~~~~~~~~~~~~~~~~~~~~~~~~~~~~|        |~~~~~g@  18.Pop-in Shoppin'
@6 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|       |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|        |~~~~~g@  19.Waterfront Pier
QBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBQ  20.Waterfront Harbor
        
        
        """)


def check_position():
    
    global cardinal_direction

    global is_facing_east
    global is_facing_west
    global is_facing_south
    global is_facing_north

    global x_coordinate
    global y_coordinate 

    print_location(cardinal_direction)
    
    for i in range(len(location_list)):
        if x_coordinate in location_list[i].x_coordinates and y_coordinate in location_list[i].y_coordinates:
            print('You are at ' + location_list[i].name + '.')
         
def hit_the_break():
    print('You have stopped.')

def customer_interaction(customer):

    global x_coordinate
    global y_coordinate

    global event_count

    global customers_delivered
    global money
    
    print('The customer gets into your cab.')
    print('"Can you take me to ' + customer.destination.name +'"?')
    print('Possible responses: "Sorry", "Sure"')
    while True:
        response = input()
        action = format_action(response)   
        if response == "sorry":
            print('"Bummer."')
            print('The customer gets out.')
            customer_exists = False
            break  
        elif response == "sure":
            print('"Thanks!"')
            has_customer = True
            while has_customer == True:
                
                out_of_bound_fail_state()
                if event_count >= 10:
                    break 

                action = input()
                action = format_action(action)
                if action not in actions:
                    print('Input a valid action. Possible actions are ' + str(actions))
                elif action == "view map":  
                    view_map()
                elif action == "check position":
                    check_position()
                    print('The customer is sitting in the back seat.')
                elif action == "break":
                    hit_the_break()
                elif action == "ask for destination":
                    print("Please take me to " + customer.destination.name + ".") 
                else:
                    control_taxi(action)
                    customer.fare += 1.13
                    if x_coordinate in customer.destination.x_coordinates and y_coordinate in customer.destination.y_coordinates:
                        print('"Thanks! Let me out here!"')
                        print("The customer hands you " + "$" + str("{:.2f}".format(customer.fare)) + ".")
                        customers_delivered.append(customer)
                        money += customer.fare
                        event_count += 1
                        break
            break
        else:
            print('Please enter a valid response.') 

def print_location(cardinal_direction):
    

    try:
        on_street = []
        for i in range(len(street_list)):
            if x_coordinate in street_list[i].x_coordinates and y_coordinate in street_list[i].y_coordinates:
                on_street.append(street_list[i])
        if len(on_street) > 1:
            if on_street[0].name == on_street[1].name:
                print('You are facing ' + cardinal_direction + ' on ' + on_street[0].name + '.')
            else:
                print('You are facing ' + cardinal_direction + ' at the corner of ' + on_street[0].name + ' and '
            + on_street[1].name + '.')
        else: 
            print('You are facing ' + cardinal_direction + ' on ' + on_street[0].name + '.')
    except:
        out_of_bounds_handler()

    

def out_of_bounds_handler():
    for i in range(len(boundary_list)):
            if x_coordinate in boundary_list[i].x_coordinates and y_coordinate in boundary_list[i].y_coordinates:
                if boundary_list[i].name == 'side walk':
                    print('You are on the ' + boundary_list[i].name + '.')
                elif boundary_list[i].name == 'sea' or boundary_list[i].name == 'harbour':
                    print('You are in the ' + boundary_list[i].name + '.') 

def out_of_bound_fail_state():
    global event_count

    for i in range(len(boundary_list)):
            if x_coordinate in boundary_list[i].x_coordinates and y_coordinate in boundary_list[i].y_coordinates:
                if boundary_list[i].name == 'side walk':
                    event_count += 3
                    print('You hit a street sign!')
                if boundary_list[i].name == 'harbour':
                    event_count += 3
                    print('The harbour personnel are yelling at you.')
                    if event_count >= 10:
                        print('You drove off a pier.')
                elif boundary_list[i].name == 'sea':
                    event_count += 10
                    
def win_state():
    global money
    global customers_delivered

    print("Today, you delivered " + str(len(customers_delivered)) + " customers and made " + str("{:.2f}".format(money)) + " dollars.")
    if len(customers_delivered) >= 10:
        print("You're the best taxi driver on the road!")
    elif len(customers_delivered) > 7:
        print("Nice work today! Keep it up!")
    elif len(customers_delivered) > 5:
        print("Not to bad, but you need to be more careful.")
    elif len(customers_delivered) >= 3:
        print("I think you need to retake the licensing test buddy!")
    else:
        print("I don't think you're cut out for this.")
    

def format_action(action):
    action = action.lower()
    action = action.strip()
    return action       

def control_taxi(action):
    
    global is_facing_east
    global is_facing_west
    global is_facing_south
    global is_facing_north

    global x_coordinate
    global y_coordinate 

    global cardinal_direction

    if is_facing_east:
        match action:
            case 'turn left':
                cardinal_direction = 'North'
                is_facing_east = False
                is_facing_north = True
                print_location(cardinal_direction)
            case 'turn right':
                cardinal_direction = 'South'
                is_facing_east = False
                is_facing_south = True
                print_location(cardinal_direction)
            case 'accelerate':
                x_coordinate += 1
                print('x is now equal to ' + str(x_coordinate))
                print_location(cardinal_direction)
            case 'reverse':
                x_coordinate -= 1 
                print('x is now equal to ' + str(x_coordinate))
                print_location(cardinal_direction) 
            case _:
                'Input a valid action.'    
                
    elif is_facing_west:
        match action:
            case 'turn left':
                cardinal_direction = 'South'
                is_facing_west = False
                is_facing_south = True
                print_location(cardinal_direction) 
            case 'turn right':
                cardinal_direction = 'North'
                is_facing_west = False
                is_facing_north = True 
                print_location(cardinal_direction) 
            case 'accelerate':
                x_coordinate -= 1
                print('x is now equal to ' + str(x_coordinate))
                print_location(cardinal_direction) 
            case 'reverse':
                x_coordinate += 1 
                print('x is now equal to ' + str(x_coordinate))
                print_location(cardinal_direction) 
            case _:
                'Input a valid action.'    

    elif is_facing_north:
        match action:
            case 'turn left':
                cardinal_direction = 'West'
                is_facing_north = False
                is_facing_west = True
                print_location(cardinal_direction) 
            case 'turn right':
                cardinal_direction = 'East'
                is_facing_north = False
                is_facing_east = True
                print_location(cardinal_direction) 
            case 'accelerate':
                y_coordinate += 1
                print('y is now equal to ' + str(y_coordinate))
                print_location(cardinal_direction) 
            case 'reverse':
                y_coordinate -= 1
                print('y is now equal to ' + str(y_coordinate)) 
                print_location(cardinal_direction) 
            case _:
                'Input a valid action.'     

    elif is_facing_south:
        match action:
            case 'turn left':
                cardinal_direction = 'East'
                is_facing_south = False
                is_facing_east = True
                print_location(cardinal_direction) 
            case 'turn right':
                cardinal_direction = 'West'
                is_facing_south = False
                is_facing_west = True
                print_location(cardinal_direction) 
            case 'accelerate':
                y_coordinate -= 1
                print('y is now equal to ' + str(y_coordinate))
                print_location(cardinal_direction) 
            case 'reverse':
                y_coordinate += 1
                print('y is now equal to ' + str(y_coordinate))
                print_location(cardinal_direction) 
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
print_location('East')

#print('the length of location_list is ' + str(len(location_list)))

event_count = 0

while event_count < 3:


    customer_interaction_determiner = random.randint(1, 20)
    #print('customer interaction determiner = ' + str(customer_interaction_determiner))

    customer = customer_generator()
    #print(customer.first_name)
    #print(customer.last_name)
    #print(customer.destination.name) 

    
    if customer_interaction_determiner >= 17 and has_customer == False:
        print("A customer is hailing your taxi!")
        customer_exists = True

    action = input()
    action = format_action(action)

    if action not in actions:
        print('Input a valid action. Possible actions are ' + str(actions))
    elif action == "view map":  
       view_map()
    elif action == "check position":
        check_position()
    elif customer_exists == True and action == "break": 
        hit_the_break()
        customer_interaction(customer)      
    elif action == "break":
        hit_the_break()
    elif action == "ask for destination":
        print("Who are you talking to?")
    else:
        control_taxi(action) 
    
    
    out_of_bound_fail_state()
    

    for i in range(len(boundary_list)):
        if x_coordinate in boundary_list[i].x_coordinates and y_coordinate in boundary_list[i].y_coordinates and event_count >= 10:
            print('Game Over!')

win_state()
                  

