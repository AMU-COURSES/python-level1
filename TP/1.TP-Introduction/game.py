import random

# Game settings

# Define the grid size
GRID_SIZE = (5, 5)  # 5x5 world

# Define player properties
player_position = [0, 0]  # Starting position (top-left corner)
inventory = {}  # Inventory as a dictionary

# Place items in the world
item_positions = {
    'cle': random.choices(range(5), k=2),
    'map': random.choices(range(5), k=2),
}

# Place the exit in the world
exit_position = random.choices(range(5), k=2)

"""
## Task 1: Implement the `display_world()` Function
- The function should print a **5x5 grid** where:
  - Empty spaces are represented by '.'
  - The player's position is represented by 'P'
  - The exit is represented by 'E'
- Example Output:
  ```
  . . . . .
  . . . . .
  . . P . .
  . . . . .Example
  . . . E .
  ```
"""
def display_world():
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            if [i, j] == player_position:
                print('P', end=' ')
            elif [i, j] == exit_position:
                print('E', end=' ')
            else:
                print('.', end=' ')
        print()

"""
## Task 2: Implement the `move_player(direction)` Function
- The function should move the player **up, down, left, or right** within the grid.
- It should prevent movement **outside the grid boundaries**.
- Example usage:
  ```python
  move_player('right')  # Moves the player one step to the right
  ```
"""
def move_player(direction):
    if direction[0] == "r":
        player_position[1] += 1
        if player_position[1] >= GRID_SIZE[1]:
            player_position[1] = 0
    elif direction[0] == "l":
        player_position[1] -= 1
        if player_position[1] <0 :
            player_position[1] = GRID_SIZE[1]-1
    elif direction[0] == "u":
        player_position[0] -= 1
        if player_position[0] <0:
            player_position[0] = GRID_SIZE[0]-1
    elif direction[0] == "d":
        player_position[0] += 1
        if player_position[0] >= GRID_SIZE[0]:
            player_position[0] = 0
    else:
        print("Wrong command, please use : right, left, up, down")
    return player_position 

"""
## Task 3: Implement the `collect_item(position)` Function
- The function should:
  - Check if an item exists at the given position.
  - Add the item to the inventory as a dictionary `{item_name: quantity}`.
  - If an item already exists, increase the quantity.
- Example usage:
  ```python
  collect_item([1, 1])  # Collects the key
"""
def collect_item():
    for item, item_position in item_positions.items():
        if player_position == item_position:
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
            print(f"Item collected: {item}")
            return

"""
## Task 4: Implement the map and the key

- Implement the `display_real_world()`, the exit should be hidden until the player collects the map.
- Implement the exit game logic, the player should collect the key before leaving the game.
- If the player reach the exit without the key, the game should print a message and the player should not be able to leave the game.
- If the player reach the exit with the key, the game should print the credits.
"""

def display_real_world():
    # if the player has the map, call display_world()
    if 'map' in inventory:
        display_world()
    else:
        for i in range(GRID_SIZE[0]):
            for j in range(GRID_SIZE[1]):
                if [i, j] == player_position:
                    print('P', end=' ')
                else:
                    print('.', end=' ')
            print()

def exit_game():
    if player_position == exit_position:
        if 'cle' in inventory:
            print("Congratulations! You've escaped the maze.")
            print("Credits: Game developed by Julien Zoubian")
            exit()
        else:
            print("You need the key to exit the game.")
            return

def main():
    while True:
        display_real_world()
        action = input("Enter your move: (up (u), down (d), left (l), right (r)): ")
        
        player_position = move_player(action)
        collect_item()
        exit_game()

if __name__ == "__main__":
    main()