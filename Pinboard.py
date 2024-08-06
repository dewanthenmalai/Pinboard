import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.widgets import Slider, Button

def generateLines(mod, mult):
    x = [j for i in range(mod) for j in (np.cos((i/mod)*2*np.pi),np.cos(mult*(i/mod)*2*np.pi))]
    y = [j for i in range(mod) for j in (np.sin((i/mod)*2*np.pi),np.sin(mult*(i/mod)*2*np.pi))]
    
    xx = np.vstack([x[0::2],x[1::2]])
    yy = np.vstack([y[0::2],y[1::2]])
    
    return xx, yy

fig = plt.figure()
ax = fig.add_subplot(111)

fig.subplots_adjust(bottom=0.25)
fig.canvas.manager.set_window_title("Pinboard")
ax.set_title('Multiplication Table Visualization')

# Circle for board
circle = plt.Circle((0,0), 1, edgecolor='black', facecolor='none')
ax.add_patch(circle)

# Inital values
mod_0 = 10
mult_0 = 2

x, y = generateLines(mod_0, mult_0)

lines = ax.plot(x, y, color='r')

# Modulus slider
mod_slider_ax = fig.add_axes([0.25, 0.15, 0.65, 0.03])
mod_slider = Slider(mod_slider_ax, 'Modulus', 10, 200, valinit=mod_0, valstep=1)

# Multiple slider
mult_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03])
mult_slider = Slider(mult_slider_ax, 'Multiple', 2, 100, valinit=mult_0, valstep=0.1)

# Event handler for changing sliders
def sliders_on_changed(val):
    global lines
    for line in lines: line.remove()
    new_x, new_y = generateLines(mod_slider.val, mult_slider.val)
    lines = ax.plot(new_x, new_y, color='r')
mod_slider.on_changed(sliders_on_changed)
mult_slider.on_changed(sliders_on_changed)

# Reset button
reset_button_ax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset', hovercolor='0.975')

# Event handler
def reset_button_on_clicked(mouse_event):
    mod_slider.reset()
    mult_slider.reset()
reset_button.on_clicked(reset_button_on_clicked)


plt.show()
