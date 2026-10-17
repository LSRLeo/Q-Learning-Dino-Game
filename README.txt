================================================================================
README.txt
Chrome Dino Game - Q-Learning AI Agent
Shirui (Leo) Liu
Introduction to Artificial Intelligence - Final Project
University of Denver
================================================================================

--------------------------------------------------------------------------------
PROJECT OVERVIEW
--------------------------------------------------------------------------------
This project implements a Q-Learning AI agent to play the Chrome Dinosaur Game.
The agent learns to jump over cacti and duck under birds by trial and error,
using a Q-table to store and update learned values over many episodes.

The game environment is built using Pygame, and the Q-learning agent is
implemented from scratch based on the Bellman equation.

--------------------------------------------------------------------------------
REQUIREMENTS
--------------------------------------------------------------------------------
Python 3.12 or later

Required libraries:
    pip3 install pygame
    pip3 install numpy
    pip3 install matplotlib

--------------------------------------------------------------------------------
FILE STRUCTURE
--------------------------------------------------------------------------------

Final_Project/
├── game.py              # Pygame Dino game environment (modified from open source)
├── qLearn.py            # Q-Learning agent (Q-table, epsilon-greedy, Bellman update)
├── train.py             # Training loop for experiments 1, 2, 3
├── demo.py        # Train agent for 2500 episodes and save Q-table
├── main.py              # Load saved Q-table and watch trained agent play
├── README.txt           # This file
└── Assets/
    ├── Dino/            # Dino sprite images
    ├── Cactus/          # Cactus sprite images
    ├── Bird/            # Bird sprite images
    └── Other/           # Background and cloud images

Generated output files:
    results_old_500.txt      # Experiment 1a scores
    results_new_500.txt      # Experiment 1b scores
    results_last_1500,txt    # Experiment 2a scores
    results_new_1500.txt     # Experiment 2b scores
    demo_result.txt          # Demo Training scores

    graph_old_500.png        # Experiment 1a learning curve
    graph_new_500.png        # Experiment 1b learning curve
    graph_last_1500.png      # Experiment 2a learning curve
    graph_new_1500.png       # Experiment 2b learning curve 
    graph_demo_2500          # Demo Traning learning curve

    q_table_demo.pkl         # Saved Q-table from demo training


--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------

--- OPTION 1: Run Experiments (train.py) ---

*You need to modify the paramter in qLearn.py manually 
See hyperparameters.txt for full list. Format:
learning_rate, discount_factor, exploration_prob, exploration_decay, exploration_min, episodes


Note: During each experiment, the game window pauses every 10 episodes.
      Press Enter to watch the agent play, then it continues automatically.

--- OPTION 2: Demo Training and Showcasing ---

Trains the agent for 2500 episodes and saves the Q-table.
Simply run the demo.py and run main.py



--------------------------------------------------------------------------------
GAME CONTROLS (during rendered episodes)
--------------------------------------------------------------------------------
Enter       — start watching a paused episode
Close window — stop current demo and return to prompt (demo.py only)

--------------------------------------------------------------------------------
STATE SPACE
--------------------------------------------------------------------------------
The agent observes three values each frame:
    dist_bin   — distance to next obstacle (0-19, 50px buckets)
    obs_type   — obstacle type (0=SmallCactus, 1=LargeCactus, 2=Bird, -1=None)
    speed_bin  — current game speed (0-9)

Total possible states: 20 x 4 x 10 = 800

--------------------------------------------------------------------------------
ACTIONS
--------------------------------------------------------------------------------
    0 — Run (do nothing)
    1 — Jump
    2 — Duck

--------------------------------------------------------------------------------
REWARD FUNCTION
--------------------------------------------------------------------------------
    +10          — jumping at the right time (dist_bin <= 2)
    -1           — jumping too early (dist_bin > 5)
    1 + score//100 — surviving each frame (increases with score)
    -100         — dying (collision with obstacle)

--------------------------------------------------------------------------------
Original Dino Game Pygame Implementation
--------------------------------------------------------------------------------

https://github.com/techwithtim/Chrome-Dino-Game-AI (base game code)
