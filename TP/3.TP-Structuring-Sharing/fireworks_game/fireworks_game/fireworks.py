import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class FireworksSimulation:
    def __init__(self, num_particles=100, num_steps=100, box_size=10, slowdown_factor=0.8, time_step=0.1):
        self.num_particles = num_particles
        self.num_steps = num_steps
        self.box_size = box_size
        self.slowdown_factor = slowdown_factor
        self.time_step = time_step
        self.g = 9.81  # Gravity constant

        # Initialize positions and velocities
        self.x = np.zeros(self.num_particles)
        self.y = np.zeros(self.num_particles)

        # Random explosion directions and speeds
        self.angles = np.random.uniform(0, 2 * np.pi, self.num_particles)
        self.speeds = np.random.uniform(1, 3, self.num_particles)

        # Compute velocity components
        self.vx = self.speeds * np.cos(self.angles)
        self.vy = self.speeds * np.sin(self.angles)

        # Box limits
        self.x_min, self.x_max = -self.box_size, self.box_size
        self.y_min, self.y_max = -self.box_size, self.box_size

        # Cumulative distribution map
        self.distribution_map, self.x_edges, self.y_edges = np.histogram2d(
            [], [], bins=50, range=[[self.x_min, self.x_max], [self.y_min, self.y_max]]
        )

        # Matplotlib setup
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(self.x_min, self.x_max)
        self.ax.set_ylim(self.y_min, self.y_max)
        self.heatmap = self.ax.imshow(
            self.distribution_map.T, origin='lower', extent=[self.x_min, self.x_max, self.y_min, self.y_max], cmap='inferno'
        )
        plt.colorbar(self.heatmap, label='Particle Density')

    def update_positions(self):
        """ Update positions with bouncing effect at boundaries and slow down on impact. """
        # Update positions
        self.x += self.vx * self.time_step
        self.y += self.vy * self.time_step

        # Detect collisions with box boundaries
        collision_x = (self.x <= self.x_min) | (self.x >= self.x_max)
        collision_y = (self.y <= self.y_min) | (self.y >= self.y_max)

        # Reverse velocity when hitting walls and apply slowdown
        self.vx[collision_x] *= -self.slowdown_factor
        self.vy[collision_y] *= -self.slowdown_factor

        # Update cumulative distribution map
        hist, _, _ = np.histogram2d(self.x, self.y, bins=50, range=[[self.x_min, self.x_max], [self.y_min, self.y_max]])
        self.distribution_map += hist

    def update(self, frame):
        self.update_positions()
        self.heatmap.set_data(self.distribution_map.T)

    def run(self):
        """ Run the animation. """
        ani = FuncAnimation(self.fig, self.update, frames=self.num_steps, interval=25)
        plt.show()

if __name__ == "__main__":
    simulation = FireworksSimulation()
    simulation.run()
