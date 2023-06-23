import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from communication.client.client import MountainClient
import random 
c = MountainClient()
class RandomPointsAnimation:
    def __init__(self, radius=23000, num_points_per_frame=4, interval=200):
        self.radius = radius
        self.num_points_per_frame = num_points_per_frame
        self.interval = interval
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(121)  # First subplot for current graph
        self.ax2 = self.fig.add_subplot(122)  # Second subplot for another random graph
        self.points_x = []
        self.points_y = []
        self.points_x2 = []
        self.points_y2 = []
        self.circle = None
        self.animation = None
        self.stopped = False

    def add_points(self, frame):
        # Generate random points for the current graph
        data = c.get_data()

        new_points_x = []
        new_points_y = []

        for equipo in data:
            for escalador in data[equipo]:
                new_points_x.append(data[equipo][escalador]['x'])
                new_points_y.append(data[equipo][escalador]['y'])

        # Update the points arrays for the current graph
        self.points_x = new_points_x
        self.points_y = new_points_y

        self.points_x2.append(random.random())
        self.points_y2.append(random.random())
        # Clear the plots
        self.ax1.clear()
        self.ax2.clear()

        # Plot the points for the current graph
        self.ax1.scatter(self.points_x, self.points_y, c='r', marker='o', label='Random Points')
        self.ax1.scatter(-5798.898261608745, 13939.77021944042551, c='b', marker='.', label='Flag')

        # Plot the circle for the current graph
        theta = np.linspace(0, 2 * np.pi, 100)
        x = self.radius * np.cos(theta)
        y = self.radius * np.sin(theta)
        self.ax1.plot(x, y, color='b', label='Circle')
        self.ax1.set_title('Current Graph')
        self.ax1.legend()
        print(self.points_x2)
        # Plot the points for the other graph
        self.ax2.plot(self.points_x2, self.points_y2)
        self.ax2.set_title('Other Random Graph')
        self.ax2.legend()

        # Check if stopping condition is met
        if self.stopped:
            self.animation.event_source.stop()

    def animate(self):
        self.animation = FuncAnimation(self.fig, self.add_points, interval=self.interval)
        plt.tight_layout()
        plt.show()

    def stop_animation(self):
        self.stopped = True

# Create an instance of the RandomPointsAnimation class and start the animation
animation = RandomPointsAnimation(radius=23000, num_points_per_frame=4, interval=100)
animation.animate()
