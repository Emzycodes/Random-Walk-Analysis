import matplotlib.pyplot as plt
from raandomwalks import RandomWalks

# Make a random walk
rw = RandomWalks()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig , ax = plt.subplots()
ax.scatter(rw.x_values,rw.y_values,s=15)
plt.savefig("img.png" ,bbox_inches='tight')
plt.show()