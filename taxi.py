
customer = {
    'name' : 'Joe',
    'directions' :  ['go straight', 'turn right', 'stop here'],
    'fare' : 0
}

print("These are the directions: " + str(customer['directions'][0]) + ", " + str(customer['directions'][1]) + ", " + str(customer['directions'][2]))

direction_one = input()
if direction_one == str(customer['directions'][0]):
    print("Great!")
    customer['fare'] += 1
else:
    print("You went the wrong way!")

direction_two = input()
if direction_two == str(customer['directions'][1]):
    print("Awesome!")
    customer['fare'] += 1
else:
    print("You went the wrong way!")

direction_three = input()
if direction_three == str(customer['directions'][2]):
    print("Superb!")
    customer['fare'] += 1
else:
    print("You went the wrong way!")

print('Thanks very much!' + ' You get ' + str(customer['fare']) + ' dollars.')