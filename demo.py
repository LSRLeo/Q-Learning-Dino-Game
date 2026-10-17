import qLearn
import matplotlib.pyplot as plt
from game import run_episode

def train(n_train, scores):
    for episode in range(n_train):
        episode_num = episode + 1
        score = run_episode(qLearn, render=True, episode_num=episode_num)
        scores.append(score)
        qLearn.decay_exploration()
        print(f"Episode {episode_num}/{n_train} | Score: {score} | Exploration: {qLearn.exploration_prob:.3f}")

    qLearn.save_q_table('q_table_demo.pkl')

    with open("demo_results.txt", 'w') as f:
        f.write("Episode,Score\n")
        for i, s in enumerate(scores):
            f.write(f"{i+1},{s}\n")
        f.write(f"\nBest Score: {max(scores)}\n")
        f.write(f"Average Score: {sum(scores)/len(scores):.1f}\n")
        f.write(f"Average Last 50: {sum(scores[-50:])/50:.1f}\n")

    window = 20
    smoothed = [sum(scores[max(0,i-window):i+1])/len(scores[max(0,i-window):i+1]) for i in range(len(scores))]
    plt.figure(figsize=(10,5))
    plt.plot(scores, alpha=0.4, color='blue', label='Score per episode')
    plt.plot(smoothed, color='red', linewidth=2, label='20-ep moving average')
    plt.xlabel('Episode')
    plt.ylabel('Score')
    plt.title('Demo Training (2500 episodes)')
    plt.legend()
    plt.savefig("graph_demo_2500.png")
    plt.close()

    print(f"\nTraining complete!")
    print(f"Best score: {max(scores)}")
    print(f"Average score (last 50 episodes): {sum(scores[-50:])/50:.1f}")

def main():
    n_train = 2500
    scores = []
    train(n_train, scores)

if __name__ == "__main__":
    main()