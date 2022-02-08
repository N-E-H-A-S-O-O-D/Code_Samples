import numpy as np
import math
import matplotlib.pyplot as plt
dt=0.1
tr= np.arange(0, 10+dt, dt)
V=np.zeros((np.shape(tr)))
Omega = np.zeros((np.shape(tr)))
def fr(x,u):
    return np.array([u[0] * np.cos(x[2]), u[0] * np.sin(x[2]), u[1]])
def main():
    for k in range(tr.shape[0]):
        if 0 <= tr[k] <=10:
            V[k]= 2
        else:
            V[k]=0
        if 3 <= tr[k] < 7:
            Omega[k]= -2*math.pi / 4
        else:
            Omega[k]=0
    #plotting speed signal
    plt.plot(tr, V)
    plt.xlabel('time')
    plt.ylabel('speed')
    plt.show()
    #plotting gyroscope signal
    plt.plot(tr, Omega)
    plt.xlabel('time')
    plt.ylabel('Gyroscope output')
    plt.show()
    x0 = np.array([0,0,math.pi/2])
    xr = np.zeros((tr.shape[0],3))
    cx = x0
    for k in range(1,tr.shape[0]):
        u  = np.array([V[k-1],Omega[k-1]])
        dt = tr[k] - tr[k-1]
        cx = cx + dt * fr(cx,u);
        xr[k,:] = cx;
    plt.clf()
    plt.plot(xr[:,0], xr[:,1] )
    plt.xlabel('px')
    plt.ylabel('py')
    plt.title('Position')
    plt.show()
main()