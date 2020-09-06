# Learning to navigate
This project is aimed to train an agent to navigate using Reinforcement learning.

We use [Double DQN technique](https://arxiv.org/abs/1509.06461) to train the agent.

# Environment Setup

To set up your python environment to run the code in this repository, follow the instructions below.

Create (and activate) a new conda environment with Python 3.6.
```bash
conda create --name <env_name> python=3.6
conda activate <env_name>
pip install gym
```

Clone the repository, and navigate to the python/ folder. Then, install several dependencies.
```bash
git clone https://github.com/Akshai/navigation-rl.git
cd python
pip install .
```

# Training

```bash
python train_navigation.py
```

# Visualization
```bash
python visualize_navigation.py --model_path=<Path to your trained checkpoint>
```





