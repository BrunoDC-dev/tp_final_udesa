import time
import threading
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
from communication.client.client import MountainClient


class Dashboard:
    def __init__(self, client: MountainClient):
        self.root = Tk()
        self.root.title("Dashboard")
        self.client = client
        self.data = client.get_data()
        self.time_step = 500 # ms
        self.animations = [] # for animations to stay alive in memory
        self.figsize = (4.5, 3)
        self.frame = Frame(self.root)
        self.visualization_example(self.frame)


    def visualization_example(self, frame):
	    # Code for visualization plot

# Create the figure and axis objects
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

# Define the circle parameters
        radius = 23
        theta = np.linspace(0, 2 * np.pi, 100)  # Angle values from 0 to 2*pi

# Generate the circle points
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)

# Plot the circle base
        circle = ax.plot(x, y, zs=0, zdir='z', label='Circle Base')

# Initialize empty arrays for points
        points_x = []
        points_y = []
        points_z = []

# Function to add points in each animation frame
        def add_points(frame):
    # Generate four random points
            new_points_x = np.random.uniform(-radius, radius, 4)
            new_points_y = np.random.uniform(-radius, radius, 4)
            new_points_z = np.random.rand(4) * 50

    # Add the new points to the existing arrays
            points_x.extend(new_points_x)
            points_y.extend(new_points_y)
            points_z.extend(new_points_z)

    # Plot all points
            ax.scatter(points_x, points_y, points_z, c='r', marker='o', label='Random Points')

# Set labels and legend
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()

# Create the animation
        self.animation = FuncAnimation(fig, add_points, frames=25, interval=200)
        
        canvas = FigureCanvasTkAgg(fig, frame)
        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()
        canvas._tkcanvas.pack()

    def start(self):
        # No modificar
        t = threading.Thread(target=self.update_data)
        t.start()
        self.root.mainloop()  

    def update_data(self):
        # No modificar
        while not self.client.is_over():
            self.data = self.client.get_data()
            time.sleep(self.time_step/1000)

    def stop(self):
        # No modificar
        self.root.quit()

if __name__ == "__main__":
    # No modificar
    client = MountainClient('localhost', 8080)
    d = Dashboard(client)
    d.start()
