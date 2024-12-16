# Tic Tac Toe with Pygame and Prover9

A simple yet advanced implementation of the classic Tic Tac Toe game using Python and Pygame, with additional logic validation powered by Prover9.

## Features

- **Two-player interaction:**
  - The user plays as "X," and the computer plays as "O."
  - Alternating turns between the user and computer.

- **Winner detection:**
  - Uses Prover9, a theorem prover, to verify winning conditions logically.

- **Dynamic scoring system:**
  - Tracks the user's wins, the computer's wins, and ties across games.

- **Pop-up notifications:**
  - Displays messages when a game ends, indicating the winner or if it's a tie.

- **Smooth gameplay:**
  - The computer's move is delayed slightly to simulate "thinking."
  - Restart the game without freezing or interrupting the flow.

- **Interactive UI:**
  - Hover effects on the restart button and responsive design for gameplay.

## Technologies Used

- **Python**: Core programming language.
- **Pygame**: For rendering the game UI and handling interactions.
- **NumPy**: Efficiently manages the game grid.
- **Prover9**: Validates game logic and winning conditions.

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- Pygame library
- Prover9 installed on your system
- NumPy library

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/tic-tac-toe.git
   cd tic-tac-toe

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt

3. **Run the game**:
    ```bash
    python game.py

### How to Play

1. **Launch the game by running**:
    ```bash
    python game.py

2. **Take your turn**:
    - Click on an empty cell to place **"X"**.

3. **Computer's move**:

   - The computer will automatically place **"O"** in a random empty cell.

4. **Game progress**:

   - The game will continue until:
     - **Someone wins** (a pop-up will announce the winner), or
     - **All cells are filled**, resulting in a tie.

5. **Dynamic scoring**:

   - Scores for the **user**, **computer**, and **ties** are updated on the screen in real time.

6. **Restart the game**:

   - Click the **Restart button** or press the **R** key to reset the game and start fresh.

