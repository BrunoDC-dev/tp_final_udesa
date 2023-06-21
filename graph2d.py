import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from communication.client.client import MountainClient

c = MountainClient()

class RandomPointsAnimation:
    def __init__(self, radius=23000, num_points_per_frame=4, interval=200):
        self.radius = radius
        self.num_points_per_frame = num_points_per_frame
        self.interval = interval
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.points_x = []
        self.points_y = []
        self.circle = None
        self.animation = None
        self.stopped = False

    def add_points(self, frame):
        # Generate random points
        data = c.get_data()

        new_points_x = []
        new_points_y = []

        for equipo in data:
            for escalador in data[equipo]:
                new_points_x.append(data[equipo][escalador]['x'])
                new_points_y.append(data[equipo][escalador]['y'])

        # Update the points arrays
        self.points_x = new_points_x
        self.points_y = new_points_y

        # Clear the plot
        self.ax.clear()

        # Plot the points
        self.ax.scatter(self.points_x, self.points_y, c='r', marker='o', label='Random Points')

        # Plot the circle
        theta = np.linspace(0, 2 * np.pi, 100)
        x = self.radius * np.cos(theta)
        y = self.radius * np.sin(theta)
        self.ax.plot(x, y, color='b', label='Circle')

        # Set labels and legend
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.legend()

        # Check if stopping condition is met
        if self.stopped:
            self.animation.event_source.stop()

    def animate(self):
        self.animation = FuncAnimation(self.fig, self.add_points, interval=self.interval)
        plt.show()

    def stop_animation(self):
        self.stopped = True


# Create an instance of the RandomPointsAnimation class and start the animation
animation = RandomPointsAnimation(radius=23000, num_points_per_frame=4, interval=100)
animation.animate()
