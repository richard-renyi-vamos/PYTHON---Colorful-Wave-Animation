import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

# Initialize empty plot objects
line, = ax.plot([], [], lw=4)  # Increased linewidth for thicker wave

# Function to initialize the plot
def init():
    line.set_data([], [])
    return line,

# Function to update the plot for each frame
def update(frame):
    x = np.linspace(0, 2*np.pi, 200)  # Increased number of points for smoother wave
    phase = frame / 5.0  # Adjusted frequency for faster animation
    y = np.sin(x + phase % (2*np.pi))  # Ensure smooth wrapping around at the end
    line.set_data(x, y)
    line.set_color(plt.cm.jet(frame/100.0))  # Add color based on frame number
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=30, init_func=init, blit=True)  # Increased number of frames

# Show the animation
plt.show()
