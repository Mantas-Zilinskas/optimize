from unconstrained_optimization import gradient_descent, steepest_descent, simplex
from grapher import graph, graph_simplex

def f(x, y):
    return -1/8*(x*y - x**2*y - x*y**2)

def f_grad(x,y):
    vector = (-1/8*(y-2*x*y-y**2),-1/8*(x-x**2-2*x*y))
    return vector

X1 = (1,2)
X2 = (2/10, 1/10)

result = gradient_descent(X1, f_grad, 10)
iteration_points = result[0]
graph(f, iteration_points[0], iteration_points[1])

result = steepest_descent(X1, f, f_grad, 10)
iteration_points = result[0]
graph(f, iteration_points[0], iteration_points[1])

result = simplex(X2, f, 0.5, 10)
history = result[0]
graph_simplex(f, history)

