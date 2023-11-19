# Pygame Pong Game

## Table of Contents

1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [How to Run](#how-to-run)
4. [Controls](#controls)
5. [Gameplay](#gameplay)
6. [Code Structure](#code-structure)
7. [Additional Information](#additional-information)

## 1. Overview

This is a simple implementation of the classic Pong game using the Pygame library. It features a basic player-versus-computer gameplay with a scoring system.

## 2. Dependencies

- Python 3.x
- Pygame

## 3. How to Run

1. Install Python: [Python Downloads](https://www.python.org/downloads/)
2. Install Pygame: Open a terminal and run `pip install pygame`
3. Run the game: Execute the script by running `python pong_game.py` in the terminal.

## 4. Controls

- UP Arrow Key: Move the player paddle up
- DOWN Arrow Key: Move the player paddle down

## 5. Gameplay

- The player competes against a computer-controlled opponent.
- The ball moves between the paddles, and the goal is to score points by making the ball pass the opponent's paddle.
- The game ends when one player reaches the maximum score.

## 6. Code Structure

- `pong_game.py`: Main script containing the game logic and setup.
- `pygame.freetype`: Used for rendering text on the screen.
- Game entities: Player paddle, computer-controlled paddle (bot), and the ball.

## 7. Additional Information

- The game runs at 60 frames per second.
- Scores are displayed at the top center of the screen.
- The game can be restarted by pressing any key after it ends.
- The maximum score required to win can be customized by changing the `max_score` variable in the code.
