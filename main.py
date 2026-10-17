import qLearn
from game import run_episode
"""
Demo will render slower for eaiser presentation
"""
def watch_demo():
    qLearn.load_q_table('q_table_demo.pkl')
    qLearn.exploration_prob = 0.0
    try:
        while True:
            run_episode(qLearn, render=True, episode_num=0)
    except SystemExit:
        print("Game closed.")

def main():
    running = True
    while running:
        cmd = input("\nEnter command (play/quit): ").strip().lower()
        if cmd == "play":
            watch_demo()
        elif cmd == "quit":
            print("Goodbye!")
            running = False
        else:
            print("Unknown command. Type 'play' or 'quit'.")

if __name__ == "__main__":
    main()