import numpy as np
import matplotlib.pyplot as plt

# Generating uniform random number in the interval [A,B]
# A = 0
# B = 1
# u = np.random.rand()
# x = (B-A)*u + A
#
# # Changing the seed
# print("Setting the seed as 3")
# np.random.seed(seed=3)
# print(np.random.rand())
# print(np.random.rand())
# print(np.random.rand())
# print(np.random.rand())
# print("Setting the seed back to 3 again")
# np.random.seed(seed=3)
# print(np.random.rand())
# print(np.random.rand())
# print(np.random.rand())
# print(np.random.rand())
#
# # Simulate coin toss
# u = np.random.rand()
# if u < 0.5:
#     print("Heads")
# else:
#     print("Tails")
#
#
# Bernoulli and Multinoulli
# u = np.random.rand()
# p_success = 0.7
# if u < p_success:
#     print("Success")
# else:
#     print("Failure")

# Draw 3 balls with replacement
# no_red = 2.0
# no_blue = 4.0
# total = no_red + no_blue
# n_draws = 3
# for i in range(n_draws):
#     u = np.random.rand()
#     if u < (no_red/total):
#         print("Red")
#     else:
#         print("Blue")
#
# no_red = 2.0
# no_blue = 4.0
# no_green = 4.0
# total = no_red + no_blue + no_green
# no_draws = 3
# for i in range(no_draws):
#     u = np.random.rand()
#     if u < (no_red/total):
#         print("Red")
#     elif u < ((no_red+no_blue)/total):
#         print("Blue")
#     else:
#         print("Green")
#
# Binomial and multinomial
# n = 100
# p_success = 0.2
# no_success = 0
# for i in range(n):
#     u = np.random.rand()
#     if u < p_success:
#         no_success += 1
#     print("Number of success is %d" % no_success)
#
#
# # Draw 2 balls without replacement
# # Both number of balls and probabilities change after each draw
# no_red = 6.0
# no_blue = 5.0
# no_draw = 3
# for i in range(no_draw):
#     total = no_red + no_blue
#     u = np.random.rand()
#     if u < (no_red/total):
#         print("Red")
#         no_red -= 1
#     else:
#         print("Blue")
#         no_blue -= 1
#
#
# # # Drawing from standard Normal
# s = np.random.randn()
# # # Drawing from Gaussian distribution with mean mu and variance sigma
# sigma = 1.2
# mu = 5.2
# g = np.array([sigma * np.random.randn() + mu for i in range(1000)])
# print("Mean:%f and std:%f" % (np.mean(g), np.std(g)))
# #
# x = np.zeros(1000)
# for i in range(1000):
#     S = 0
#     for j in range(12):
#         S += np.random.rand()
#         z = S - 6  # standard normal
#     x[i] = sigma * z + mu
# print("Mean:%f and std: %f" % (np.mean(x), np.std(x)))
#
#
#Monte Carlo Experiment
N = 100000
cnt = 0
x_in = []
y_in = []
x_out = []
y_out = []
for i in range(N):
    x = np.random.rand()
    y = np.random.rand()
    if (x**2 + y**2) < 1:
        cnt += 1
        x_in.append(x)
        y_in.append(y)
    else:
        x_out.append(x)
        y_out.append(y)

print("Estimate for pi is %f" % (4*(float(cnt)/float(N))))

plt.figure()
plt.scatter(np.array(x_in), np.array(y_in), c='b', s=1)
plt.scatter(np.array(x_out), np.array(y_out), c='r', s=1)
plt.savefig('monte.png')
