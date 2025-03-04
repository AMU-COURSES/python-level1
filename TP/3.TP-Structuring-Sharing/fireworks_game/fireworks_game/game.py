import random
from fireworks_game.fireworks import FireworksSimulation

class Game:
    """
    A class representing a simple grid-based game where a player moves, collects items, and tries to reach an exit.
    """
    def __init__(self, grid_size=(5, 5)):
        """
        Initializes the game with a grid, player position, items, and an exit.
        
        >>> game = Game((5,5))
        >>> game.grid_size
        (5, 5)
        >>> game.player_position
        [0, 0]
        """
        self.grid_size = grid_size
        self.player_position = [0, 0]  # Starting position (top-left corner)
        self.inventory = {}  # Inventory as a dictionary

        # Place items in the world
        self.item_positions = {
            'bomb': random.choices(range(grid_size[0]), k=2),
            'map': random.choices(range(grid_size[0]), k=2),
        }

        # Place the exit in the world
        self.exit_position = random.choices(range(grid_size[0]), k=2)

    def display_world(self):
        """Displays the game world with the player's position and exit visibility logic."""
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                if [i, j] == self.player_position:
                    print('P', end=' ')
                elif [i, j] == self.exit_position and 'map' in self.inventory:
                    print('E', end=' ')
                else:
                    print('.', end=' ')
            print()

    def move_player(self, direction):
        """
        Moves the player within the grid while ensuring no out-of-bound moves.
        
        >>> game = Game()
        >>> game.move_player('down')
        >>> game.player_position
        [1, 0]
        """
        movement_dict = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }
        if direction in movement_dict:
            new_x = self.player_position[0] + movement_dict[direction][0]
            new_y = self.player_position[1] + movement_dict[direction][1]

            if 0 <= new_x < self.grid_size[0] and 0 <= new_y < self.grid_size[1]:
                self.player_position = [new_x, new_y]

        self.collect_item()
        self.exit_game()

    def collect_item(self):
        """
        Checks if an item exists at the player's position and collects it.
        
        >>> game = Game()
        >>> game.item_positions['key'] = [0, 0]
        >>> game.collect_item()
        >>> 'key' in game.inventory
        True
        """
        for item, item_position in self.item_positions.items():
            if self.player_position == item_position:
                self.inventory[item] = self.inventory.get(item, 0) + 1
                print(f"Item collected: {item}")
                return

    def display_real_world(self):
        """Displays the world with hidden exit unless the player has the map."""
        if 'map' in self.inventory:
            self.display_world()
        else:
            for i in range(self.grid_size[0]):
                for j in range(self.grid_size[1]):
                    if [i, j] == self.player_position:
                        print('P', end=' ')
                    else:
                        print('.', end=' ')
                print()

    def exit_game(self):
        """
        Checks if the player reached the exit and has the key to win the game.
        
        >>> game = Game()
        >>> game.exit_position = [0, 0]
        >>> game.player_position = [0, 0]
        >>> game.inventory['key'] = 1
        >>> game.exit_game()
        """
        if self.player_position == self.exit_position:
            if 'bomb' in self.inventory:
                print("Take cover!")
                simulation = FireworksSimulation()  # Create fireworks simulation
                simulation.run()  # Run animation
                print("Credits: Game developed by Julien Zoubian")                
                exit()
            else:
                print("The door is locked. You need a key... or something more definitive.")

    def run(self):
        """Main game loop."""
        while True:
            self.display_real_world()
            action = input("Enter your move: (up, down, left, right, exit): ")
            if action in ['up', 'down', 'left', 'right']:
                self.move_player(action)
            elif action == 'exit':
                self.exit_game()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    game = Game()
    game.run()
