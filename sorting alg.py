import matplotlib.pyplot as plt
import random

def visualize(lst, fig, ax):
    ax.clear()
    ax.bar(range(len(lst)), lst)
    plt.pause(0.001)
    fig.canvas.draw()

def bubble_sort(lst, fig, ax):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            visualize(lst, fig, ax)

# Generate a list of random numbers
lst = random.sample(range(1, 100), 50)

# Create a figure and axis for the plot
fig, ax = plt.subplots()

visualize(lst, fig, ax)

# Sort the list and visualize the process
bubble_sort(lst, fig, ax)

plt.show()
