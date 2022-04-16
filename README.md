# Mach Eight Sample Project

## Instructions

1. use `python3 -m venv ./env` to create a new virtual environment.
2. Run `source ./env/bin/activate` to activate the virtual environment.
3. Install program's requirements by running `pip3 install -r requirements.txt`.
4. Run `python3 project.py` and follow the instructions.

## Algorithm 

1. The program will ask the user for a height to match all the pairs of players whose height in inches adds up to the given number until he presses a non numeric key.

2. create a dictionary that will have a key for each different height of the NBA players, and the value for this keys is going to be
an array with all the players of this height. **Average time Complexity: O(n), Space Complexity: O(n)**.

3. While we insert the players to the hashmap, we validate if there is any key that added to the one that we just appended is equal
to the given target, and then we generate the pairs by putting together the player that was just appended with all the players in the other key.

4. Format the answer and print all the pairs. If theres none, the program will print 'No matches found'.


