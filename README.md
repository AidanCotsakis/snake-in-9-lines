# Snake In 9 Lines Of Code

This project is a minimalist implementation of the classic Snake Game, written in Python with Pygame. This challenge-driven project achieves a functional Snake Game in as few lines of code as possible without using `exec()`. Despite its brevity, the game maintains essential features such as smooth movement, collision detection, and basic graphics for an engaging experience.

## **Features**

- **Smooth Movement and Direction Control**: Control the snake using `W`, `A`, `S`, and `D` keys.
- **Collision Detection**: Game resets on boundary collision or when the snake runs into itself.
- **Randomized Apple Placement**: Apple repositions on each successful "eating" by the snake, allowing for continuous play.
- **Compact Code Structure**: Built in a single loop with minimal code lines, optimizing Pygame functions for brevity.

## **Getting Started**

### **Prerequisites**
- **Python 3.x**
- **Pygame**: Install via pip if not already installed:
  ```bash
  pip install pygame
  ```

## **Running the Game**
1. Clone this repository:
2. Run the game:
    ```bash
    python smallSnake.py
    ```

## **Controls**
- Move Up: `W`
- Move Down: `S`
- Move Left: `A`
- Move Right: `D`

## **How It Works**
The game uses a single while loop with a compact control flow:

- **Direction Control**: Updates the direction of the snake based on keyboard inputs, while preventing direct reversal.
- **Apple Placement**: Checks for collisions between the snake's head and the apple, then generates a new apple position.
- **Collision and Boundary Checks**: Monitors the snake's head position to restart the game upon self-collision or boundary crossing.