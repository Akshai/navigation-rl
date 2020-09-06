from unityagents import UnityEnvironment
import numpy as np
from dqn_agent import Agent
import torch
import argparse

def process(args):
    env = UnityEnvironment(file_name="Banana.app")
    brain_name = env.brain_names[0]
    brain = env.brains[brain_name]
    env_info = env.reset(train_mode=False)[brain_name] # reset the environment
    state = env_info.vector_observations[0]            # get the current state
    score = 0                                          # initialize the score
    action_size = brain.vector_action_space_size
    state_size = len(state)

    agent = Agent(state_size, action_size,1, args.model_path)


    while True:
        action = agent.act(state, 0.0)                 # select an action
        env_info = env.step(action)[brain_name]        # send the action to the environment
        next_state = env_info.vector_observations[0]   # get the next state
        reward = env_info.rewards[0]                   # get the reward
        done = env_info.local_done[0]                  # see if episode has finished
        score += reward                                # update the score
        state = next_state                             # roll over the state to next time step
        if done:                                       # exit loop if episode finished
            break

    print("Score: {}".format(score))
    


def get_args():
    parser = argparse.ArgumentParser(description='Visualize the navigation of a trained model')
    parser.add_argument('model_path', help ='Path to the trained model')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    process(args)