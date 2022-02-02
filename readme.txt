 ________  ______   _______   ________   __   ________   ________   __
|__    __||   ___| |   __  | |        | |  | |     |  | |   __   | |  |
   |  |   |   ___| |  |__  | |  |  |  | |  | |  |  |  | |  |__|  | |  |____
   |__|   |______| |__||__|  |__|__|__| |__| |__|_____| |__|  |__| |_______|
 ________  ________  ___   ___    __   _____________  _________
/__   __/ /  __    / \  \ /  /   /  /  ____________  /    \    \ 
  /  /   /  /__/  /   /     /   /  /   ________  ___/      \ ___\_________ 
 /__/   /__/  /__/   /__/ \__\ /__/    ______   /_________________________/
                                                    \__/         \__/ 
Welcome to Terminal Taxi! The text-based taxi-simulation experience you 
never knew you wanted! The goal is simple, you must do your best to deliver
10 customers to their destinations safe and sound. In order to get all 10
customers to their destinations, you're going to have to drive carefully and
that means, no accidents see? This game takes place in the good ol' days so 
there's no fancy-shmancy smart phones. You'll have to figure out where you 
are by looking at a map the old-school way.

Here's what you need to know to play:

1. Type "accelerate", "reverse", "break", "turn left" or "turn right" to control your taxi. 
2. The taxi uses TANK CONTROLS, so it moves like a tank, just like a real taxi!
3. Type "view map" to see the map!
4. The map dosen't show your location cause it's an old-timey paper map, type "check position" to take
    in your surroundings and figure out where you are. 
5. From time to time customers will hail your taxi, if one does you can type "break" to pick them up.
6. Customers will pay their fares and brazenly leap from your taxi upon arrival at their destination.
7. If you forget where a customer wants to go type "ask for destination" to have them remind you.
8. The mayor of the town preemptively put up signs for a highway and a financial district, but they
    haven't actually been built yet. 
8. Type "exit" to exit the game.
9. Type "view commands" to view commands. 
10. Type "view instructions" to see this dialogue again.

This is the readme for my first portfolio project for the CS course in codecademy, wherein I am tasked with
making a terminal game using python.

Name: Terminal Taxi
Description: A text-based taxi driving simulator for terminal written in Python 3.10.1 
Installation: dunno yet . . .

Details:

1. Movement
-Movement uses tank controls, this is obviously unrealistic but I think it makes the game easier to play. 
-Boundaries and locations are objects which have set coordinants, every time the player moves x or y is incremented accordingly.
-Interactions happen based on whether or not player's coordinates match up to the location object's. 


2. Playspace and map
-The locations and boundaries have been mapped out using a grid system based on the map in game.
-The in-game map accurately represents the play space.  

3. Customer interactions
-Customers are randomly generated with first and last names and are randomly assigned a destination.  
 
4. Win/Fail conditions
-The game runs on a single while loop that is set to break when an event counter reaches 10 or higher players are then assessed and ranked.
-Delivering a customer counts as one event, while driving on to the sidewalk or into the harbor counts as 4. 
-Driving into the sea counts as 10, effectively ending the game.
-To get the highest rank you need to deliver all 10 customers without causeing any accidents. 
-The player can exit at anytime and will recieve an assessment based on how many customers they've delivered so far. 
