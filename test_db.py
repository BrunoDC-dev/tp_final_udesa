import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from communication.client.client import MountainClient

class RandomPointsAnimation:
    def __init__(self, radius=23000, num_points_per_frame=4, interval=200):
        self.radius = radius
        self.num_points_per_frame = num_points_per_frame
        self.interval = interval
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.circle = None
        self.animation = None
        self.stopped = False

    def add_points(self, frame):
        artists = []  # List to store the artists

        # Generate random points
        for equipo in self.data:
            for escalador in self.data[equipo]:
                x = self.data[equipo][escalador]['x']
                y = self.data[equipo][escalador]['y']
                z = self.data[equipo][escalador]['z']
                points = self.ax.scatter(x, y, z, c='r', marker='o', label='Random Points')
                artists.append(points)

        # Check if stopping condition is met
        if self.stopped:
            self.animation.event_source.stop()

        return artists  # Return the artists

    def animate(self, data):
        self.data = data

        # Define the circle parameters
        theta = np.linspace(0, 2 * np.pi, 100)  # Angle values from 0 to 2*pi

        # Generate the circle points
        x = self.radius * np.cos(theta)
        y = self.radius * np.sin(theta)

        # Clear previous plot
        self.ax.cla()

        # Plot the circle base
        self.ax.plot(x, y, zs=0, zdir='z', label='Circle Base')

        # Set labels and legend
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.legend()

        # Create the animation
        self.animation = FuncAnimation(self.fig, self.add_points, frames=1, blit=False)  # Disable blitting

        # Update the plot automatically
        plt.pause(0.001)

    def stop_animation(self):
        self.stopped = True

animation = RandomPointsAnimation(radius=23, num_points_per_frame=4)
c = MountainClient()

while not c.is_over():
    data = c.get_data()
    animation.animate(data)
