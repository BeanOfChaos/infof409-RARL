"""
Test file for gym python environment.
"""

import gym
from rllab.algos.trpo import TRPO
from rllab.baselines.linear_feature_baseline import LinearFeatureBaseline
from rllab.envs.box2d.cartpole_env import CartpoleEnv
from rllab.envs.normalized_env import normalize
from rllab.policies.gaussian_mlp_policy import GaussianMLPPolicy


def collect(env_name, nit=500):
    """Interface for easy data generation
       Should take whatever parameters are relevant (env name, number of iterations,...)
       And return an assessment of the result of the training
    """
    pass


# Tests calls to gym below

env = gym.make('InvertedPendulum-v2')
print(env.action_space)
print(env.observation_space)
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) #  random action selection
env.close()

env = gym.make('HalfCheetah-v2')
print(env.action_space)
print(env.observation_space)
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
env.close()

env = gym.make('Swimmer-v2')
print(env.action_space)
print(env.observation_space)
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
env.close()

env = gym.make('Hopper-v2')
print(env.action_space)
print(env.observation_space)
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
env.close()

env = gym.make('Walker2d-v2')
print(env.action_space)
print(env.observation_space)
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
env.close()
