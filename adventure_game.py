
class Player:
    def __init__(self):
        self.inventory = []
        self.health = 100

class Game:
    def __init__(self):
        self.player = Player()
        self.current_location = "start"

    def start_game(self):
        locations = {
            "start": {
                "description": "You wake up in a dimly lit room. There are two doors in front of you.",
                "choices": ["Open the left door", "Open the right door"]
            },
            "left_door": {
                "description": "You enter a dusty library. There's a mysterious book on the table.",
                "choices": ["Read the book", "Explore further"]
            },
            "right_door": {
                "description": "A cold breeze hits your face as you step outside. You're in a dense forest.",
                "choices": ["Follow a path", "Climb a tree"]
            },
            "hidden_cave": {
                "description": "You discovered a hidden cave. There's a treasure chest inside.",
                "choices": ["Open the chest", "Leave it alone"]
            },
            "game_over": {
                "description": "The game has ended.",
                "choices": []  # No choices here; game ends
            }
            # Add more locations and their descriptions and choices as the game progresses
        }

        while self.player.health > 0 and self.current_location != "game_over":
            print(locations[self.current_location]["description"])
            choices = locations[self.current_location]["choices"]
            for idx, choice in enumerate(choices):
                print(f"{idx + 1}. {choice}")

            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                if self.current_location == "start":
                    self.current_location = "left_door"
                # Add more conditional statements for different locations and choices
                elif self.current_location == "left_door":
                    self.current_location = "hidden_cave"
                # Add more conditional statements for different locations and choices
            elif user_choice == "2":
                if self.current_location == "start":
                    self.current_location = "right_door"
                # Add more conditional statements for different locations and choices
                elif self.current_location == "right_door":
                    self.current_location = "game_over"  # End game here
                # Add more conditional statements for different locations and choices

            # Update player stats, inventory, and location based on choices
            # Implement logic for different paths, storylines, and endings

        print("Game Over")

# Instantiate and start the game
game = Game()
game.start_game()
