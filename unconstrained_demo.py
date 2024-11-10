from unconstrained_optimization import gradient_descent, steepest_descent, simplex
from grapher import graph, graph_simplex, graph_empty


# demo function and demo function gradient
# be careful when picking initial points for these functions
# as they grow out of hand very fast

def f(x, y):
    return -1/8*(x*y - (x**2)*y - x*(y**2))

def f_grad(x,y):
    vector = (-1/8*(y-2*x*y-(y**2)),-1/8*(x-(x**2)-2*x*y))
    return vector


X1 = (1,2)
X2 = (2/10, 1/10)


# uncomment to graph zoomed out empty plane of the function
# graph_empty(f, 2, 2)

# gradient descent
# first argument: marks the start point of the algorithm
# second argument: gradient of function to optimize
# third argument: number of iterations
# fourth optional argument: step modifier
result = gradient_descent(X1, f_grad, 10)
iteration_points = result[0]
graph(f, iteration_points[0], iteration_points[1])

# steepest descent (a type of variation of gradient descent)
# first argument: marks the start point of the algorithm
# second argument: function to optimize
# third argument: gradient of function to optimize
# fourth argument: number of iterations
result = steepest_descent(X1, f, f_grad, 10)
iteration_points = result[0]
graph(f, iteration_points[0], iteration_points[1])

# simplex
# first argument: marks the start point of the algorithm
# second argument: function to optimize
# third argument: initial simplex side length
# fourth argument: number of iterations
result = simplex(X2, f, 0.5, 10)
history = result[0]
graph_simplex(f, history)

