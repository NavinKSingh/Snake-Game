Snake Game with Pygame
Welcome to the Snake Game with Pygame! This game is a classic representation of the popular Snake game, built using the Pygame library in Python. The game features smooth gameplay, sound effects, and multiple background images.

Features
Dynamic Backgrounds: Multiple backgrounds that change during different game states (welcome screen, gameplay, and game over).
Sound Effects: Enjoy a variety of sound effects for game events such as eating fruit and game over scenarios.
High Score Tracking: The game tracks and saves the high score to a file.
Customizable Graphics: The game uses custom images for food and backgrounds.
Setup Instructions
Requirements
Python: Ensure you have Python installed. This code is compatible with Python 3.x.

Pygame: Install the Pygame library using pip if you haven’t already.
Files Needed
Make sure you have the following files in the same directory as your script:

image.jpg - Background image for gameplay.
image2.webp - Background image for the welcome screen.
image3.jpg - Background image for the game over screen.
apple.png - Image for the food.
music1.mp3 - Music for the main game loop.
music2.mp3 - Music for game over and wall collision.
music3.mp3 - Music for eating fruit.
music4.mp3 - Music for the welcome screen.
hiscore.txt - File to save and load the high score (created automatically if not present).
Running the Game
Place all the required image and audio files in the same directory as the script.

Run the script using Python:
python your_script_name.py
Enjoy the game! Press the Space Bar to start the game from the welcome screen. Use the arrow keys to control the snake and try to achieve the highest score possible.

Game Controls
Arrow Keys: Move the snake in the respective direction (Up, Down, Left, Right).
Space Bar: Start the game from the welcome screen.
Enter Key: Restart the game after a game over.
Troubleshooting
No Sound: Ensure that your sound files are correctly named and placed in the same directory as the script. Verify that your audio system is functioning properly.
Images Not Displaying: Confirm that the image files are correctly named and located in the same directory as the script.
