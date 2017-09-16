import gym
import numpy as np

env = gym.make('CartPole-v0')
env.reset()
i = 0
done=False
while done==False:
    act  = env.action_space.sample()
    img = env.render(mode='rgb_array')
    o,r,done,_ = env.step(act)
    i+=1
    print i