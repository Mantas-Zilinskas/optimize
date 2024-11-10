import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def graph_empty(func, x, y):
    x_lin = np.linspace( -abs(x),abs(x), 100)
    y_lin = np.linspace( -abs(y),abs(y), 100)
    x_lin, y_lin = np.meshgrid(x_lin, y_lin)
    z_lin = func(x_lin, y_lin)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d', computed_zorder= False)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.plot_surface(x_lin, y_lin, z_lin, cmap='viridis')

    plt.show()

def graph(func, x, y):
    x_buffer = (max(x)-min(x))*0.2
    y_buffer = (max(y)-min(y))*0.2
    x_lin = np.linspace(min(x) - x_buffer - 0.25, max(x) + x_buffer + 0.25, 100)
    y_lin = np.linspace(min(y) - y_buffer - 0.25, max(y) + y_buffer + 0.25, 100)
    x_lin, y_lin = np.meshgrid(x_lin, y_lin)
    z_lin = func(x_lin, y_lin)
    z = [func(x,y) for x, y in zip(x,y)]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d', computed_zorder= False)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.plot_surface(x_lin, y_lin, z_lin, cmap='viridis')
    ax.plot3D(x, y, z, color='red', linewidth=1, label='Optimization Path')
    points = list(zip(x, y, z))
    for i in range(len(points)):
        ax.text(points[i][0], points[i][1], points[i][2], f"{i}", color='brown')
        i += 1
    plt.plot(x,y,z, 'o')

    plt.show()

def graph_simplex(func, simplex:list[tuple[tuple[float, float],tuple[float, float],tuple[float, float]]]):
    xs=[]
    ys=[]
    for points in simplex:
        for point in points:
            xs.append(point[0])
            ys.append(point[1])

    x_buffer = (max(xs)-min(xs))*0.2
    y_buffer = (max(ys)-min(ys))*0.2
    x_lin = np.linspace(min(xs) - x_buffer - 0.25, max(xs) + x_buffer + 0.25, 100)
    y_lin = np.linspace(min(ys) - y_buffer - 0.25, max(ys) + y_buffer + 0.25, 100)
    x_lin, y_lin = np.meshgrid(x_lin, y_lin)
    z_lin = func(x_lin, y_lin)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d', computed_zorder= False)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.plot_surface(x_lin, y_lin, z_lin, cmap='viridis')

    
    p = simplex[0]
    x_p = [point[0] for point in p]
    y_p = [point[1] for point in p]
    x_p.append(p[0][0])
    y_p.append(p[0][1])
    z_p = func(np.array(x_p), np.array(y_p))
    ax.plot3D(x_p, y_p, z_p, color='red', linewidth=1)
    ax.scatter(x_p, y_p, z_p, color='blue', marker='o')
    ax.text(x_p[0], y_p[0], z_p[0], "00", color='pink')
    ax.text(x_p[1], y_p[1], z_p[1], "01", color='pink')
    ax.text(x_p[2], y_p[2], z_p[2], "02", color='pink')
    i=0
    for points in simplex[1::]:
        i += 1
        x_points = [point[0] for point in points]
        y_points = [point[1] for point in points]
        x_points.append(points[0][0])
        y_points.append(points[0][1])
        z_points = func(np.array(x_points), np.array(y_points))
        ax.plot3D(x_points, y_points, z_points, color='red', linewidth=1)
        ax.scatter(x_points, y_points, z_points, color='blue', marker='o')
        ax.text(x_points[0], y_points[0], z_points[0], f"{i}", color='pink')
    plt.show()




    
    

    

