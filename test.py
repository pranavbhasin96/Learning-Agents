import gym
env = gym.make('Breakout-v0')
env.reset()
for i in range(1000):
  env.render()
  _,d,r,_ = env.step(3)
