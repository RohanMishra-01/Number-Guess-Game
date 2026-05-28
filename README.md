# Number Guessing Game

A simple command-line based Number Guessing Game built with Python. The user guesses a 4-digit number and it is checked against a randomly generated number by the computer. Guess it right and you win!

---

## Project Structure

    number-guessing-game/
    │
    ├── main.py               # Entry point — runs the main game loop
    ├── result.py             # Logic to compare user guess with computer's number
    └── computer_choice.py    # Randomly generates a 4-digit number (1000-9999)

---

## Features

- **Number Guessing** — User guesses a 4-digit number against the computer
- **Random Generation** — Computer picks a random number between 1000 and 9999
- **Result Display** — Shows the computer's number and whether the user won or lost
- **Input Validation** — Rejects numbers that are more than 4 digits

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository:

        git clone https://github.com/RohanMishra-01/number-guessing-game.git
        cd number-guessing-game

2. Run the program:

        python main.py

No external dependencies required — pure Python!

---

## Usage

On running `main.py`, you will see:

    --------------------MENU--------------------
    Kindly enter a number. It will be checked against the computer's
    random chosen 4 digit number. If it is the same you win, else you lose!

    Enter a 4 digit number:

After entering your number, the result is displayed like this:

    Computer's choice: 4782
    Congratulations you guessed the correct number!!

    (or)

    Computer's choice: 3921
    Your guess was wrong, try again!

---

## Game Rules

- Enter any 4-digit number between 1000 and 9999
- The computer randomly picks a number in the same range
- If your number matches the computer's number exactly, you win
- If it does not match, the game ends and you can run it again to retry

---

## Future Improvements

- [ ] Add a replay option without restarting the program
- [ ] Add hints like "too high" or "too low" for a better experience
- [ ] Track the number of attempts per session
- [ ] Allow the user to set the digit length (3-digit, 5-digit, etc.)
- [ ] Build a GUI using Tkinter

---

## Contributing

Contributions are welcome. Feel free to fork the repo and submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## Author

Developed by [Rohan Mishra](https://github.com/RohanMishra-01)
