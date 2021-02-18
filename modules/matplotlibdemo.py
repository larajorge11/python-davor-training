import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [4566, 8765, 322, 4567]

legend = ["January", "February", "March", "April"]
plt.xticks(x, legend)

plt.plot(x, y)
plt.show()
