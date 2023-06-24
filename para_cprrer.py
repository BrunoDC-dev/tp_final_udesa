import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
def grafico_interactivo():
        t = np.arange(0.0, 2.0, 0.01)
        s0 = np.sin(2*np.pi*t)
        s1 = np.sin(4*np.pi*t)
        s2 = np.sin(6*np.pi*t)

        fig, ax = plt.subplots()
        l0, = ax.plot(t, s0, visible=False, lw=2, color='black', label='1 Hz')
        l1, = ax.plot(t, s1, lw=2, color='red', label='2 Hz')
        l2, = ax.plot(t, s2, lw=2, color='green', label='3 Hz')
        fig.subplots_adjust(left=0.2)

        lines_by_label = {l.get_label(): l for l in [l0, l1, l2]}
        line_colors = [l.get_color() for l in lines_by_label.values()]

        # Make checkbuttons with all plotted lines with correct visibility
        rax = fig.add_axes([0.05, 0.4, 0.1, 0.15])
        check = CheckButtons(
            ax=rax,
            labels=lines_by_label.keys(),
            actives=[l.get_visible() for l in lines_by_label.values()],
            label_props={'color': line_colors},
            frame_props={'edgecolor': line_colors},
            check_props={'facecolor': line_colors},
        )


        def callback(label):
            ln = lines_by_label[label]
            ln.set_visible(not ln.get_visible())
            ln.figure.canvas.draw_idle()

        check.on_clicked(callback)

        plt.show()
        print('nuevo 44')

grafico_interactivo()





"""

import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 1)
y1 = 2 * np.sin(2*np.pi*t)
y2 = 4 * np.sin(2*np.pi*2*t)

fig, ax = plt.subplots()
ax.set_title('Click on legend line to toggle line on/off')
line1, = ax.plot(t, y1, lw=2, label='1 Hz')
line2, = ax.plot(t, y2, lw=2, label='2 Hz')
leg = ax.legend(fancybox=True, shadow=True)

lines = [line1, line2]
lined = {}  # Will map legend lines to original lines.
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # Enable picking on the legend line.
    lined[legline] = origline


def on_pick(event):
    # On the pick event, find the original line corresponding to the legend
    # proxy line, and toggle its visibility.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Change the alpha on the line in the legend, so we can see what lines
    # have been toggled.
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()

fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()

y1 = data['T1']['E1']['z']
        y2 = data['T1']['E1']['z']

        fig, self.ax5= self.fig.add_subplot(224)
        self.ax5.set_title('Eliga el escalador al cual le quiera ver la altura')
        line1, = self.ax5.plot( y1, lw=2, label='1 Hz')
        line2, = self.ax5.plot( y2, lw=2, label='2 Hz')
        leg = self.ax5.legend(fancybox=True, shadow=True)

        lines = [line1, line2]
        lined = {}  # Will map legend lines to original lines.
        for legline, origline in zip(leg.get_lines(), lines):
            legline.set_picker(True)  # Enable picking on the legend line.
            lined[legline] = origline


        def on_pick(event):
            # On the pick event, find the original line corresponding to the legend
            # proxy line, and toggle its visibility.
            legline = event.artist
            origline = lined[legline]
            visible = not origline.get_visible()
            origline.set_visible(visible)
            # Change the alpha on the line in the legend, so we can see what lines
            # have been toggled.
            legline.set_alpha(1.0 if visible else 0.2)
            fig.canvas.draw()

        fig.canvas.mpl_connect('pick_event', on_pick)


        self.i += 1
        esc1 = data['T1']['E1']['z']
        esc2 = data['T1']['E2']['z']


        # Gráfico de líneas
        self.ax5.plot(esc1, color = 'm', label = "E1")
        self.ax5.plot(esc2, color = 'y', label = "E2")
        self.ax5.legend()
        




        color_linea = 1
        for escalador in data['T1']:
                color_linea += 1
                if color_linea%2==0: 
                    col = 'red' 
                    print('llego aca r')
                elif color_linea%3==0: 
                    col = 'green'
                elif color_linea%4==0: 
                    col = 'blue'
                elif color_linea%5==0: 
                    col = 'magenta'
                else: col = 'yellow'

                altura = data['T1'][escalador]['z']
                self.puntosy3.append(altura)
                self.ax5.plot(self.puntosy3, color = col, label = 'algo')



                t = np.arange(0.0, 2.0, 0.01)
            s0 = np.sin(2*np.pi*t)
            s1 = np.sin(4*np.pi*t)
            s2 = np.sin(6*np.pi*t)

            ax = self.ax
            l0, = self.ax.plot(t, s0, visible=False, lw=2, color='black', label='1 Hz')
            l1, = self.ax.plot(t, s1, lw=2, color='red', label='2 Hz')
            l2, = self.ax.plot(t, s2, lw=2, color='green', label='3 Hz')
            self.fig.subplots_adjust(left=0.2)

            lines_by_label = {l.get_label(): l for l in [l0, l1, l2]}
            line_colors = [l.get_color() for l in lines_by_label.values()]

            # Make checkbuttons with all plotted lines with correct visibility
            rax = self.fig.add_axes([0.05, 0.05, 0.1, 0.1])
            check = CheckButtons(
                ax=rax,
                labels=lines_by_label.keys(),
                actives=[l.get_visible() for l in lines_by_label.values()],
                label_props={'color': line_colors},
                frame_props={'edgecolor': line_colors},
                check_props={'facecolor': line_colors},
            )


            def callback(label):
                ln = lines_by_label[label]
                ln.set_visible(not ln.get_visible())
                ln.figure.canvas.draw_idle()
                self.fig.canvas.draw_idle()

            check.on_clicked(callback)
"""