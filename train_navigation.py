from unityagents import UnityEnvironment
import numpy as np
from collections import deque
from dqn_agent import Agent
import torch
import matplotlib.pyplot as plt
import os
import argparse


env = UnityEnvironment(file_name="Banana.app")

# get the default brain
brain_name = env.brain_names[0]

def dqn(args, eps_start=1.0, eps_end=0.01, eps_decay=0.995):
    """Deep Q-Learning.
    
    Params
    ======
        args : command line arguments
        n_episodes (int): maximum number of training episodes
        max_t (int): maximum number of timesteps per episode
        eps_start (float): starting value of epsilon, for epsilon-greedy action selection
        eps_end (float): minimum value of epsilon
        eps_decay (float): multiplicative factor (per episode) for decreasing epsilon
    """
    scores = []                        # list containing scores from each episode
    scores_window = deque(maxlen=100)  # last 100 scores
    eps = eps_start                    # initialize epsilon
    state_size = 37
    action_size = 4
    agent = Agent(state_size, action_size,1)
    for i_episode in range(1, args.num_episodes+1):
        #resetting the environment for a new episode
        env_info = env.reset(train_mode=True)[brain_name]
        state = env_info.vector_observations[0]  
        score = 0
        cnt =0
        while True:
            action = agent.act(state, eps)
            env_info = env.step(action)[brain_name]        # send the action to the environment
            next_state = env_info.vector_observations[0]   # get the next state
            reward = env_info.rewards[0]                   # get the reward
            done = env_info.local_done[0]
            agent.step(state, action, reward, next_state, done)
            state = next_state
            score += reward
            cnt+=1
            if done:
                break
        scores_window.append(score)       # save most recent score in the 100 episode window
        scores.append(score)              # save most recent score
        eps = max(eps_end, eps_decay*eps) # decrease epsilon
        print('\rEpisode {}\tAverage Score in the last 100 episodes: {:.2f}'.format(i_episode, np.mean(scores_window)), end="")
        if i_episode % args.save_every == 0:
            print('\nSaving Checkpoint for {:d} episodes!\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_window)))
            torch.save(agent.qnetwork_local.state_dict(), os.path.join(args.save_checkpoint_path,'checkpoint_'+str(i_episode)+'.pth'))
    return scores


def process(args):
    # train dqn
    scores = dqn(args)
    # plot the scores
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(np.arange(len(scores)), scores)
    plt.ylabel('Score')
    plt.xlabel('Episode #')
    plt.savefig(os.path.join(args.reward_plot_path, 'reward_plot.png'))


def get_args():
    parser = argparse.ArgumentParser(description='Train a simple double DQN for navigation')
    parser.add_argument('--num_episodes', type=int, default=2000, help='Path to the folder of input images')
    parser.add_argument('--save_every', type=int, default=100, help='Frequency with which we are going to save the checkpoints')
    parser.add_argument('--reward_plot_path', type=str,  default="./", help='Path to store the reward plot')
    parser.add_argument('--save_checkpoint_path', default="./", help ='Path to store the trained model')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    process(args)