"""
Reference: https://www.geeksforgeeks.org/machine-learning/q-learning-in-python/
"""

import numpy as np
import random
import pickle

# Hyperparameters
learning_rate = 0.4
discount_factor = 0.9
exploration_prob = 1.0
exploration_decay = 0.9985
exploration_min = 0.01


available_actions = 3

Q_table = {}


def get_q_values(state):
    # If state not seen before, initialize Q-values to zero
    if state not in Q_table:
        Q_table[state] = np.zeros(available_actions)
    return Q_table[state]


#Epsilon Greedy 
#This decides what action the dino should take for the current frame
def get_action(state):
    if np.random.rand() < exploration_prob: #explore - try random action
        return random.randint(0, available_actions- 1)   
    else:
        return np.argmax(get_q_values(state)) #exploit - look up Q-table using the state and pick the action with highest Q-value
    

def update(state, action, reward, next_state):
    current_q = get_q_values(state)[action] #return the q - value for the state
    next_max_q = np.max(get_q_values(next_state))#return the best/highest Q-value action for next_state
    Q_table[state][action] += learning_rate * (reward + discount_factor * next_max_q - current_q) #update state


 #I implemented decay for exploration so the dinasour utilize the leared Q-table
def decay_exploration():
    global exploration_prob
    exploration_prob = max(exploration_min, exploration_prob * exploration_decay)



def save_q_table(filename='q_table.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(Q_table, f)
    print(f"Q-table saved to {filename}")


def load_q_table(filename='q_table.pkl'):
    global Q_table
    with open(filename, 'rb') as f:
        Q_table = pickle.load(f)
    print(f"Q-table loaded from {filename}")