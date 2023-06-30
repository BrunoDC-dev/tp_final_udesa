import time
import threading
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as p3
from tkinter import Tk
from tkinter import ttk
from tkinter import Label
from PIL import ImageTk, Image
import tkinter
from communication.client.client import MountainClient
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import random
from matplotlib.lines import Line2D

class Dashboard:
    def __init__(self, client: MountainClient):
        self.root = Tk()
        self.root.title("Dashboard")
        self.root.geometry("1920x960")

        # Load and resize the background image
        background = Image.open("Mountainbg.jpg")
        background = background.resize((1920, 960), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(background)

        # Create a label widget and set the image as its background
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.client = client
        self.data = client.get_data()
        self.time_step = 500 # ms
        self.animations = [] # for animations to stay alive in memory
        self.figsize = (4.5, 3)
        self.filtro=None
        self.points_x = []
        self.points_y = []
        self.puntosy = {}
        self.puntosy2 = []
        self.puntos3d={}
        self.team_colors = {} 
        self.team_styles = {} 
        for equipo in self.data:
                if equipo not in self.team_styles:
                    marker = random.choice(['o', 's', '^', 'v', '*', 'x'])  # List of marker styles to choose from
                    self.team_styles[equipo] = marker
                marker = self.team_styles[equipo]
                if equipo not in self.team_styles:
                    marker = random.choice(['o', 's', '^', 'v', '*', 'x'])  # List of marker styles to choose from
                    self.team_styles[equipo] = marker
                if equipo not in self.team_colors:
                    self.team_colors[equipo] = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
                
        
        self.frame1=ttk.Frame(self.root)
        self.frame1.place(x=50,y=10)
        self.visualization_example(self.frame1)
        
        self.frame2=ttk.Frame(self.root)
        self.frame2.place(x=50,y=400)
        self.visualization_example2(self.frame2)
        
        self.frame3=ttk.Frame(self.root)
        self.frame3.place(x=600,y=400)
        self.visualization_example3(self.frame3)
        
        self.frame4=ttk.Frame(self.root)
        self.frame4.place(x=1100,y=10)
        self.visualization_example4(self.frame4)

        self.frame5=ttk.Frame(self.root)
        self.frame5.place(x=1000,y=400)
        self.visualization_example5(self.frame5)
        

        fig =plt.figure()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        toolbar = NavigationToolbar2Tk(self.canvas, self.root, pack_toolbar=False)
        toolbar.update()

        self.canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
        self.canvas.mpl_connect("key_press_event", key_press_handler)

        button = tkinter.Button(master=self.root, text="Quit", command=self.root.quit)
        data=self.data
        home = tkinter.Button(self.root, text="Inicio", command=lambda equipo=None: self.helloCallBack(None))
        home.pack(side=tkinter.TOP)

        if len(data) > 0:
            button_frame = tkinter.Frame(self.root)  # Create a frame to hold the buttons
            button_frame.pack(side=tkinter.TOP)

        for equipo in data:
            button = tkinter.Button(button_frame, text=equipo, command=lambda equipo=equipo: self.helloCallBack(equipo))
            button.pack(side=tkinter.LEFT)

    


    def helloCallBack(self,equipo):
        self.filtro= equipo

    def visualization_example(self, frame):
	    # Code for visualization plot
        fig=plt.figure()
        fig = plt.figure(facecolor="none")
        ax = fig.add_subplot()
        fig.set_size_inches(6,3)
        ax.set_xlim(-24000,24000)
        ax.set_ylim(-24000,24000)
        team_legend_handles = []
                # code for plo
        def animate(i):
                    # Clear the plot
            if self.filtro !=None:
                ax.clear() 
                new_points_x = []
                new_points_y = []
                for escalador in self.data[self.filtro]:
                    new_points_x.append(self.data[self.filtro][escalador]['x'])
                    new_points_y.append(self.data[self.filtro][escalador]['y'])
                marker = self.team_styles[self.filtro]
                color = self.team_colors[self.filtro]
                ax.scatter(new_points_x, new_points_y, c=color, marker=marker, alpha=0.5)
                if self.filtro not in team_legend_handles:
                        team_legend_handles.append(Line2D([0], [0], marker=marker, color='w', markerfacecolor=color, markersize=10, label=self.filtro))
            else:
                ax.clear() 
                for equipo in self.data:
                    new_points_x = []
                    new_points_y = []
                    for escalador in self.data[equipo]:
                        new_points_x.append(self.data[equipo][escalador]['x'])
                        new_points_y.append(self.data[equipo][escalador]['y'])
                    marker = self.team_styles[equipo]
                    color = self.team_colors[equipo]
                    ax.scatter(new_points_x, new_points_y, c=color, marker=marker)
                    if equipo not in team_legend_handles:
                        team_legend_handles.append(Line2D([0], [0], marker=marker, color='w', markerfacecolor=color, markersize=10, label=equipo))
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_title("Mapa de la montaña")
            fig.subplots_adjust(left=0.2, bottom=0.2) 
        # Update the points arrays
            self.points_x = new_points_x
            self.points_y = new_points_y
        # Plot the circle
            theta = np.linspace(0, 2 * np.pi, 100)
            x = 23000 * np.cos(theta)
            y = 23000 * np.sin(theta)
            ax.plot(x, y, color='r', linestyle='-', linewidth=2)

            
        self.animations.append(FuncAnimation(fig, func=animate, interval=self.time_step, blit=False))
        
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas._tkcanvas.pack()
     
    def visualization_example2(self, frame):
        
	    # Code for visualization plot
        fig=plt.figure()
        fig = plt.figure(facecolor='none')
        ax = fig.add_subplot()
        fig.set_size_inches(4,4)

                # code for plo

        def animate(i):
            if self.filtro !=None:
                ax.clear()
                top_promedio=0
                alturas = []
                for escalador in self.data[self.filtro]:
                    alturas.append(self.data[self.filtro][escalador]['z'])
                    color = self.team_colors[self.filtro]   
                    bar = ax.bar(escalador, self.data[self.filtro][escalador]['z'], label=escalador, color = color )
                self.puntosy[self.filtro]=sum(alturas)/len(alturas)
                if self.puntosy[self.filtro]>top_promedio:
                    top_promedio=self.puntosy[self.filtro] 
               
                ax.set_xlabel("Escaladores del equipo " + self.filtro)
                ax.set_ylabel("Alturas") 
                ax.set_title ("Alturas Actuales de escaladores")
            else:

                ax.clear()
                top_promedio=0
                for equipo in self.data:
                    alturas = []
                    for escalador in self.data[equipo]:
                        alturas.append(self.data[equipo][escalador]['z'])
                    self.puntosy[equipo]=sum(alturas)/len(alturas)
                    if self.puntosy[equipo]>top_promedio:
                        top_promedio=self.puntosy[equipo]
                    color = self.team_colors[equipo]    
                    bar = ax.bar(equipo,self.puntosy[equipo], label=equipo, color = color )
                    ax.set_xlabel("Equipos")
                    ax.set_ylabel("Alturas") 
                    ax.set_title ("Alturas promedio") 
            fig.subplots_adjust(left=0.2) 

        self.animations.append(FuncAnimation(fig, func=animate, interval=self.time_step, blit=False))
        
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas._tkcanvas.pack()

    def visualization_example3(self, frame):
	    # Code for visualization plot
        fig=plt.figure()
        fig = plt.figure(facecolor='none')
        ax = fig.add_subplot()
        fig.set_size_inches(4,4)

                # code for plo

        def animate(i):
            ax.clear() 
            top_altura=0
            for equipo in self.data:
                altura_antes = 0
                for escalador in self.data[equipo]:
                    if self.data[equipo][escalador]['z'] > altura_antes:
                        altura_antes = self.data[equipo][escalador]['z']
                color = self.team_colors[equipo]  
                if altura_antes>top_altura:
                    top_altura=altura_antes  
                bar = ax.bar(equipo,altura_antes, label=equipo, color = color )

            ax.set_xlabel("Equipos")
            ax.set_ylabel("Alturas") 
            ax.set_title ("Alturas maximas")  
            fig.subplots_adjust(left=0.2) 
        
        self.animations.append(FuncAnimation(fig, func=animate, interval=self.time_step, blit=False))
        
        canvas = FigureCanvasTkAgg(fig, frame)

        canvas._tkcanvas.pack()
    
    def visualization_example4(self, frame):
	    # Code for visualization plot
        fig=plt.figure()
        fig = plt.figure(facecolor='none')
        ax = fig.add_subplot()
        fig.set_size_inches(3,2)
        ganadores=[["Equipo","Escalador"]]
        table = ax.table(cellText=ganadores, loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1, 1)  
        ax.set_title ("Ganadores")  
        ax.axis('off')

                # code for plo
        self.ganadores_nombres=[]
        def animate(i):
            if len(ganadores)<10:
                for equipo in self.data:
                    for escalador in self.data[equipo]:
                        if self.data[equipo][escalador]['cima'] == True:
                            escalado_gano=False
                            for hiker in range(len(ganadores)):
                                if ganadores[hiker][0]==equipo and ganadores[hiker][1]==escalador:
                                    escalado_gano=True
                            if escalado_gano==False:
                                ganadores.append([equipo,escalador])
            table = ax.table(cellText=ganadores, loc='center')


            

        self.animations.append(FuncAnimation(fig, func=animate, interval=self.time_step, blit=False))
        
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas._tkcanvas.pack()
        
    def visualization_example5(self, frame):
	    # Code for visualization plot
        fig=plt.figure()
        fig = plt.figure(facecolor='none')
        ax = fig.add_subplot(projection='3d')
        fig.set_size_inches(6,4)
        def animate(i):
            if self.filtro !=None:
                ax.clear() 
                new_points_x = []
                new_points_y = []
                new_points_z = []
                for escalador in self.data[self.filtro]:
                    new_points_x.append(self.data[self.filtro][escalador]['x'])
                    new_points_y.append(self.data[self.filtro][escalador]['y'])
                    new_points_z.append(self.data[self.filtro][escalador]['z'])
                marker = self.team_styles[self.filtro]
                color = self.team_colors[self.filtro]
                ax.scatter(new_points_x, new_points_y,new_points_z ,c=color, marker=marker,s=100)
            else:
                ax.clear() 
                for equipo in self.data:
                    new_points_x = []
                    new_points_y = []
                    new_points_z=[]
                    for escalador in self.data[equipo]:
                        new_points_x.append(self.data[equipo][escalador]['x'])
                        new_points_y.append(self.data[equipo][escalador]['y'])
                        new_points_z.append(self.data[equipo][escalador]['z'])
                    marker = self.team_styles[equipo]
                    color = self.team_colors[equipo]
                    ax.scatter(new_points_x, new_points_y, c=color, marker=marker, s=100)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('z')
            ax.set_title("Mapa de la montaña 3D")
            ax.set_xlim(-24000,24000)
            ax.set_ylim(-24000,24000)

        self.animations.append(FuncAnimation(fig, func=animate, interval=self.time_step, blit=False))
        
        canvas = FigureCanvasTkAgg(fig, frame)
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
    client = MountainClient('localhost', 8080)
    d = Dashboard(client)
    d.start()



