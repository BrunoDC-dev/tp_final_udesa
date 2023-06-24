import numpy as np
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
        self.ax = self.fig.add_subplot(331)
        self.ax3 = self.fig.add_subplot(332)
        self.ax4 = self.fig.add_subplot(333)
        self.ax5 = self.fig.add_subplot(334)
        self.ax6 = self.fig.add_subplot(335)
        self.ax7 = self.fig.add_subplot(336)
        self.ax8 = self.fig.add_subplot(337)
        self.points_x = []
        self.points_y = []
        self.circle = None
        self.animation = None
        self.stopped = False
        self.puntosy = []
        self.puntosy2 = []
        self.puntosy3 = []
        self.puntosy4 = []
        self.puntosy5 = []
        self.puntosy6 = []

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
        buey = plt.imread('buey.png')
        self.ax.imshow(buey, extent=[-self.radius, self.radius, -self.radius, self.radius], aspect='auto')
        self.ax.plot(x, y, color='b', linestyle='')

        # Set labels and legend
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.legend()

        # Check if stopping condition is met
        if self.stopped:
            self.animation.event_source.stop()
        self.altura_promedio_equipo(data)
        self.altura_maxima_equipo(data)
        self.altura_escalador(data)
        

    def animate(self):
        self.animation = FuncAnimation(self.fig, self.add_points, interval=self.interval)
        plt.show()

    def stop_animation(self):
        self.stopped = True
    
    def altura_promedio_equipo(self, data):
        for equipo in data:
            alturas = []
            for escalador in data[equipo]:
                alturas.append(data[equipo][escalador]['z'])
            self.puntosy.append(sum(alturas)/len(alturas))
            print()
            self.ax3.plot(self.puntosy, color = 'r')
    
    def altura_maxima_equipo(self, data):
        for equipo in data:
            altura_antes = 0
            for escalador in data[equipo]:
                if data[equipo][escalador]['z'] > altura_antes:
                    altura_antes = data[equipo][escalador]['z']
            self.puntosy2.append(altura_antes)
            self.ax4.plot(self.puntosy2, color = 'b')
    
    def altura_escalador(self, data):
            esc1 = data['T1']['E1']['z']
            esc2 = data['T1']['E2']['z']
            esc3 = data['T1']['E3']['z']
            esc4 = data['T1']['E4']['z']
            self.puntosy3.append(esc1)
            self.puntosy4.append(esc2)
            self.puntosy5.append(esc3)
            self.puntosy6.append(esc4)
            self.ax5.plot(self.puntosy3, color = 'g')
            self.ax6.plot(self.puntosy4, color = 'y')
            self.ax7.plot(self.puntosy5, color = 'm')
            self.ax8.plot(self.puntosy6, color = 'r')

# Create an instance of the RandomPointsAnimation class and start the animation
animation = Animation(num_points_per_frame=4, interval=100)
animation.animate()
