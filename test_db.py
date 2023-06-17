import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from communication.client.client import MountainClient
c=MountainClient()
class RandomPointsAnimation:
    def __init__(self, radius=23, num_points_per_frame=4, interval=200):
        self.radius = radius
        self.num_points_per_frame = num_points_per_frame
        self.interval = interval
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.points_x = []
        self.points_y = []
        self.points_z = []
        self.circle = None
        self.animation = None
        self.stopped = False

    def add_points(self, frame):
        # Generate random points
        data = c.get_data()
        print(data)
        
        new_points_x = []
        new_points_y = []
        new_points_z = []

        for equipo  in data:
            for escalador in data[equipo]:
                new_points_x.append(data[equipo][escalador]['x'])
                new_points_y.append(data[equipo][escalador]['y'])
                new_points_z.append(data[equipo][escalador]['z'])
        # Add the new points to the existing arrays
        self.points_x.extend(new_points_x)
        self.points_y.extend(new_points_y)
        self.points_z.extend(new_points_z)
        print(new_points_x)
        # Plot all points
        self.ax.scatter(self.points_x, self.points_y, self.points_z, c='r', marker='o', label='Random Points')

        # Check if stopping condition is met
        if self.stopped:
            self.animation.event_source.stop()

    def animate(self):
        # Define the circle parameters
        theta = np.linspace(0, 2 * np.pi, 100)  # Angle values from 0 to 2*pi

        # Generate the circle points
        x = self.radius * np.cos(theta)
        y = self.radius * np.sin(theta)

        # Plot the circle base
        self.circle = self.ax.plot(x, y, zs=0, zdir='z', label='Circle Base')

        # Set labels and legend
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.legend()

        # Create the animation
        self.animation = FuncAnimation(self.fig, self.add_points, interval=self.interval)

        # Show the 3D plot
        plt.show()

    def stop_animation(self):
        self.stopped = True


# Create an instance of the RandomPointsAnimation class and start the animation
animation = RandomPointsAnimation(radius=23, num_points_per_frame=4, interval=100)
animation.animate()

# Perform some actions or conditions to determine when to stop the animation
# For example, you can call the stop_animation method to stop the animation after a certain condition is met
# animation.stop_animation()
