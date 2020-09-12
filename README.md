# Learning to navigate
This project is aimed to train an agent to navigate using Reinforcement learning.

We use [Double DQN technique](https://arxiv.org/abs/1509.06461) to train the agent.

# Environment Setup

We utilize [Unity Machine Learning Agents](https://github.com/Unity-Technologies/ml-agents) plugin to interact with the environment. 
To set up your python environment to run the code in this repository, follow the instructions below:

1. Create (and activate) a new [Conda](https://docs.anaconda.com/anaconda/install/) environment with Python 3.6.

    ```bash
    conda create --name <env_name> python=3.6
    conda activate <env_name>
    ```


2. Clone the repository, and navigate to the python/ folder. Then, install several dependencies.

    ```bash
    git clone https://github.com/Akshai/navigation-rl.git
    cd navigation-rl/python
    pip install .
    ```

# Training

From the home path **navigation-rl**, run the following command to train the agent:

```bash
python train_navigation.py
```

# Visualization

From the home path **navigation-rl**, run the following command to visualize the trained agent:

```bash
python visualize_navigation.py <Path to your trained checkpoint>
```





