import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




# def f(x, y):
#     return 1/8*(x*y-x**2*y-x*y**2)

# # Define the grid of x and y
# x_lin = np.linspace(0, 0.5, 100)
# y_lin = np.linspace(0, 0.5, 100)
# x_lin, y = np.meshgrid(x_lin, y_lin)

# # Define the function z = f(x, y)
# z = f(x_lin,y)

# # Create the plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d', computed_zorder= False)


# # Plot the surface
# ax.plot_surface(x_lin, y, z, cmap='viridis')

# ax.plot3D([0.5,0.4,0.3], [0.5,0.4,0.3], [f(0.5,0.5),f(0.4,0.4),f(0.3,0.3)], color='red', linewidth=2, label='Optimization Path')


# Add labels
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# plt.show()


def graph(func, x, y):
    x_lin = np.linspace(min(x) - 1, max(x) + 1, 100)
    y_lin = np.linspace(min(y) - 1, max(y) + 1, 100)
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

    # x_lin = np.linspace(-10,10, 100)
    # y_lin = np.linspace(-10,10, 100)
    x_lin = np.linspace(min(xs) - 1, max(xs) + 1, 100)
    y_lin = np.linspace(min(ys) - 1, max(ys) + 1, 100)
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




    
    

    

