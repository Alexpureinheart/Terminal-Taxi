
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


#movement scheme 
actions = ['turn left', 'turn right', 'accelerate', 'reverse']

is_facing_east = True
is_facing_west = False
is_facing_south = False
is_facing_north = False

x_coordinate = 0
y_coordinate = 0

print('Input an action.')
print('You are facing East.')



i = 0

while i < 10:
    

    action = input()

    if action == '':
        print('Input a valid action.')
    else:
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
                    i += 1
                    print('x is now equal to ' + str(x_coordinate))
                case 'reverse':
                    x_coordinate -= 1
                    i += 1 
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
                    i += 1
                    print('x is now equal to ' + str(x_coordinate))
                case 'reverse':
                    x_coordinate += 1 
                    i += 1
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
                    i += 1
                    print('y is now equal to ' + str(x_coordinate))
                case 'reverse':
                    y_coordinate -= 1
                    i += 1 
                    print('y is now equal to ' + str(x_coordinate)) 
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
                    i += 1
                    print('y is now equal to ' + str(x_coordinate))
                case 'reverse':
                    y_coordinate += 1
                    i += 1 
                    print('y is now equal to ' + str(x_coordinate))
                case _:
                    'Input a valid action.' 

           
                  


        
        






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