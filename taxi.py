
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

print('You are facing East.')

print('Input an action.')

action = input()

if is_facing_east == True and action == action[0]:
    is_facing_east = False
    is_facing_north = True
    print("You are now facing North.")

if is_facing_east == True and action == actions[2]:
    x_coordinate += 1  
    print("X = " + str(x_coordinate))






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