import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(10) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

for x in all_walks:
    print(x)

# # Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)
print(np_aw)
plt.plot(np_aw)
plt.show()
# # Clear the figure
plt.clf()
# # Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)
print(np_aw_t)
# # Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()
