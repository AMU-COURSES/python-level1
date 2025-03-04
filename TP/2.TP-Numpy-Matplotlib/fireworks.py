import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import math as m

"""
Generate Firework Explosions
"""

# Number of particles
num_particles = 100

# Initial position (center of explosion)
x = np.zeros(num_particles)
y = np.zeros(num_particles)

# Random explosion directions
angles = np.linspace(0, 2 * np.pi, num_particles)  # Spread evenly in a circle
speed = np.random.rand(num_particles) * 3  # Random speeds

"""
Use Mathematical Functions to Generate
"""

# Time step
time_step = 1
num_steps = 100
t = np.linspace(0, time_step, num_steps)

# Gravity
g = 9.81

# Update positions in a loop
timeit_start = time.time()
for p in range(num_particles):
    for i in range(num_steps):
        dx = speed[p] * m.cos(angles[p]) * t[i]
        dy = speed[p] * m.sin(angles[p]) * t[i] - 0.5 * g * t[i]**2
        x[p] += dx
        y[p] += dy
timeit_end = time.time()
print('Time taken to update positions in python loop:', timeit_end - timeit_start)

# Update positions using numpy
timeit_start = time.time()
# Compute velocities
vx = speed * np.cos(angles)
vy = speed * np.sin(angles)
for i in range(num_steps):
    x = x + vx * t[i]
    y = y + vy * t[i] - 0.5 * g * t[i]**2
timeit_end = time.time()
print('Time taken to update positions using numpy:', timeit_end - timeit_start)

"""
Visualize the Fireworks
"""

# Compute all positions using numpy
x_positions = np.outer(vx, t)  # x = velocity_x * time
y_positions = np.outer(vy, t) - 0.5 * 9.81 * t**2  # y = velocity_y * time - gravity

# Plot the fireworks
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
scat = ax.scatter(x, y, c="red")

# Update function for animation
def update(frame):
    scat.set_offsets(np.c_[x_positions[:, frame], y_positions[:, frame]])

# Animate the fireworks
ani = FuncAnimation(fig, update, frames=num_steps, interval=25) # interval in milliseconds
plt.show()

"""
Implement Bounding Box
"""

box_size = 10  # Box boundary size

# Define the box limits
x_min, x_max = -box_size, box_size
y_min, y_max = -box_size, box_size

# reinitialize the position of the particles
x = np.zeros(num_particles)
y = np.zeros(num_particles)
vx = speed * np.cos(angles)
vy = speed * np.sin(angles)

# reduce the time step (to slow down the animation)
time_step = 0.1

# Define the slowdown factor
slowdown_factor = 1

def update_positions():
    """ Update positions with bouncing effect at boundaries and slow down on impact. """
    global x, y, vx, vy, distribution_map

    # Update positions
    x += vx * time_step
    y += vy * time_step - 0.5 * g * time_step**2
    
    # Check for particle falling below the box floor
    y[y < y_min] = y_min
    
    # Detect collisions with box boundaries
    collision_x = (x <= x_min) | (x >= x_max)
    collision_y = (y <= y_min) | (y >= y_max)

    # Reverse velocity when hitting walls and apply slowdown
    vx[collision_x] *= -slowdown_factor
    vy[collision_y] *= -slowdown_factor

fig, ax = plt.subplots()
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Create scatter plot for the particles
scat = ax.scatter(x, y, c="red")

def update(frame):
    update_positions()
    scat.set_offsets(np.c_[x, y])

ani = FuncAnimation(fig, update, frames=num_steps, interval=25)
plt.show()

"""
Cumulative Distribution Map
"""

# reinitialize the position of the particles
x = np.zeros(num_particles)
y = np.zeros(num_particles)
vx = speed * np.cos(angles)
vy = speed * np.sin(angles)

# Create a 2D histogram to track cumulative particle distribution
distribution_map, x_edges, y_edges = np.histogram2d([], [], bins=50, range=[[x_min, x_max], [y_min, y_max]])

def update_positions():
    """ Update positions with bouncing effect at boundaries and slow down on impact. """
    global x, y, vx, vy, distribution_map

    # Update positions
    x += vx * time_step
    y += vy * time_step

    # Detect collisions with box boundaries
    collision_x = (x <= x_min) | (x >= x_max)
    collision_y = (y <= y_min) | (y >= y_max)

    # Reverse velocity when hitting walls and apply slowdown
    vx[collision_x] *= -slowdown_factor
    vy[collision_y] *= -slowdown_factor

    # Update cumulative distribution map
    hist, _, _ = np.histogram2d(x, y, bins=50, range=[[x_min, x_max], [y_min, y_max]])
    distribution_map += hist
    
fig, ax = plt.subplots()
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Initialize the cumulative distribution plot
heatmap = ax.imshow(distribution_map.T, origin='lower', extent=[x_min, x_max, y_min, y_max], cmap='inferno')
plt.colorbar(heatmap, label='Particle Density')

def update(frame):
    update_positions()
    heatmap.set_data(distribution_map.T)

ani = FuncAnimation(fig, update, frames=num_steps, interval=25)
plt.show()