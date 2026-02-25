# Guessing-Game
🎯 Number Guessing Game (Python)

A simple and fun Python number guessing game where the player tries to guess a randomly selected number within a limited number of attempts. The game also includes sound effects for winning and losing on Windows systems.

📌 Features

Random number generated between 1 and 50

Maximum of 7 attempts

Input validation (only numbers allowed)

Hints after each guess (Too High / Too Low)

🎵 Sound effects on win and loss (Windows only)

🛠️ Technologies Used

Python 3

random module (for number generation)

winsound module (for sound effects – Windows only)

▶️ How to Run the Game

Make sure Python 3 is installed on your system.

Clone this repository or download the files.

Place the following sound files in the same directory:

win.wav

lose.wav

Run the program:

python guessing_game.py
🎮 How to Play

The program selects a secret number between 1 and 50.

You have 7 attempts to guess the correct number.

After each guess, the game will tell you:

Too High

Too Low

If you guess correctly, you win 🎉

If you fail within 7 attempts, you lose 😢

🧾 Sample Output
I have selected a number between 1 and 50.
You have 7 attempts.
Enter your guess: 25
Too Low!
Enter your guess: 40
Too High!
Enter your guess: 33

YOU WON!
You guessed the number in 3 attempts.
⚠️ Important Notes

winsound works only on Windows.

On Linux or macOS, remove or comment out the winsound lines to avoid errors.

Ensure the .wav files exist, otherwise sound playback will fail.

🚀 Future Enhancements

Difficulty levels (Easy / Medium / Hard)

Cross-platform sound support

GUI version using Tkinter or PyGame

Score tracking system

👨‍💻 Author

Samir Sahu
Beginner Python Project
Feel free to fork, modify, and improve!
