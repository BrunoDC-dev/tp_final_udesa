import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from communication.client.client import MountainClient

c = MountainClient()

class Animation:
    def __init__(self, radius=23000, num_points_per_frame=4, interval=200):
        self.radius = radius
        self.num_points_per_frame = num_points_per_frame
        self.interval = interval
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(121)
        self.ax3 = self.fig.add_subplot(122)
        self.points_x = []
        self.points_y = []
        self.circle = None
        self.animation = None
        self.stopped = False
        self.puntosx = []
        self.puntosy = []
        self.i = 0

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
        self.ax.scatter(self.points_x, self.points_y, c='r', marker='o')

        # Plot the circle
        theta = np.linspace(0, 2 * np.pi, 100)
        x = self.radius * np.cos(theta)
        y = self.radius * np.sin(theta)
        self.ax.plot(x, y, color='b')

        # Set labels and legend
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.legend()

        # Check if stopping condition is met
        if self.stopped:
            self.animation.event_source.stop()
        self.altura_promedio_equipo(data)

    def animate(self):
        self.animation = FuncAnimation(self.fig, self.add_points, interval=self.interval)
        plt.show()

    def stop_animation(self):
        self.stopped = True
    
    def altura_promedio_equipo(self, data):
        self.i += 20
        for equipo in data:
            alturas = []
            for escalador in data[equipo]:
                alturas.append(data[equipo][escalador]['z'])
            self.puntosx.append(self.i)
            self.puntosy.append(sum(alturas)/len(alturas))
            self.ax3.plot(self.puntosx, self.puntosy, color = 'b')
      



# Create an instance of the RandomPointsAnimation class and start the animation
animation = Animation(num_points_per_frame=4, interval=100)
animation.animate()
