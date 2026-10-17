import qLearn
import matplotlib.pyplot as plt
from game import run_episode

n_train = 1500
# render_freq = 50

scores = []

for episode in range(n_train):
 
    render = True
    score = run_episode(qLearn, render=render, episode_num=episode+1)
    scores.append(score)
    qLearn.decay_exploration()
    print(f"Episode {episode+1}/{n_train} | Score: {score} | Exploration: {qLearn.exploration_prob:.3f}")
print(f"\nTraining complete!")
print(f"Best score: {max(scores)}")
print(f"Average score (last 50 episodes): {sum(scores[-50:]) / 50:.1f}")



"""
modify names of textfile and graphs
"""

# Save txt
with open("results_new_1500.txt", 'w') as f:
    f.write("Episode,Score\n")
    for i, s in enumerate(scores):
        f.write(f"{i+1},{s}\n")
    f.write(f"\nBest Score: {max(scores)}\n")
    f.write(f"Average Score: {sum(scores)/len(scores):.1f}\n")
    f.write(f"Average Last 50: {sum(scores[-50:])/50:.1f}\n")

# Save graph
window = 20
smoothed = [sum(scores[max(0,i-window):i+1])/len(scores[max(0,i-window):i+1]) for i in range(len(scores))]
plt.figure(figsize=(10,5))
plt.plot(scores, alpha=0.4, color='blue', label='Score per episode')
plt.plot(smoothed, color='red', linewidth=2, label='20-ep moving average')
plt.xlabel('Episode')
plt.ylabel('Score')
plt.title('New Hyperparameters (1500 episodes)')
plt.legend()
plt.savefig("graph_new_1500.png")
plt.close() 