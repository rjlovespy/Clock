import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np


"""
1 tick of hour hand = 12 ticks of minute hand = 720 ticks of second hand.
Therefore for every tick of hour hand, 
the hour, minute, second hands rotate by 6, 72, 4320 degrees respectively.
"""
t1 = np.linspace(-3*np.pi/2, -243*np.pi/2, 360)
t2 = np.linspace(-3*np.pi/2, -7*np.pi/2, 360)
t3 = np.linspace(-3*np.pi/2, -5*np.pi/3, 360)
x1 = 0.95*np.cos(t1)
y1 = 0.95*np.sin(t1)
x2 = 0.95*np.cos(t2)
y2 = 0.95*np.sin(t2)
x3 = 0.65*np.cos(t3)
y3 = 0.65*np.sin(t3)


fig = plt.figure()
ax = plt.axes(xlim=(-2,2),ylim=(-2,2))
second_hand = plt.Line2D((0,x1[0]),(0,y1[0]),color="crimson", lw=1)
minute_hand = plt.Line2D((0,x2[0]),(0,y2[0]),color="crimson", lw=2)
hour_hand = plt.Line2D((0,x3[0]),(0,y3[0]),color="crimson", lw=2)


def update(i):
    second_hand = plt.Line2D((0,x1[i]),(0,y1[i]),color="crimson", lw=1)
    minute_hand = plt.Line2D((0,x2[i]),(0,y2[i]),color="crimson", lw=2)
    hour_hand = plt.Line2D((0,x3[i]),(0,y3[i]),color="crimson", lw=2)
    ax.add_line(second_hand)
    ax.add_line(minute_hand)
    ax.add_line(hour_hand)
    return second_hand, minute_hand, hour_hand,


anime=ani.FuncAnimation(fig,update,frames=len(t1), interval=200,blit=True,repeat=True)
circle= plt.Circle((0,0),1.25,fc="lime",ec="purple",lw=35)
ax.add_patch(circle)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.set_facecolor("black")
fig.patch.set_facecolor("black")
plt.annotate("1",(np.cos(np.pi/3),np.sin(np.pi/3)),color="black")
plt.annotate("2",(np.cos(np.pi/6),np.sin(np.pi/6)),color="black")
plt.annotate("3",(np.cos(0),np.sin(0)),color="black")
plt.annotate("4",(np.cos(-np.pi/6),np.sin(-np.pi/6)),color="black")
plt.annotate("5",(np.cos(-np.pi/3),np.sin(-np.pi/3)),color="black")
plt.annotate("6",(np.cos(-np.pi/2),np.sin(-np.pi/2)),color="black")
plt.annotate("7",(np.cos(-2*np.pi/3),np.sin(-2*np.pi/3)),color="black")
plt.annotate("8",(np.cos(-5*np.pi/6),np.sin(-5*np.pi/6)),color="black")
plt.annotate("9",(np.cos(-np.pi),np.sin(-np.pi)),color="black")
plt.annotate("10",(np.cos(-7*np.pi/6),np.sin(-7*np.pi/6)),color="black")
plt.annotate("11",(np.cos(-4*np.pi/3),np.sin(-4*np.pi/3)),color="black")
plt.annotate("12",(np.cos(-3*np.pi/2),np.sin(-3*np.pi/2)),color="black")
plt.annotate("Courtesy of Rishikesh Jha",(1.5,-1.25),color="crimson")
plt.axis("equal")
# anime.save("clock.gif")
plt.show()
