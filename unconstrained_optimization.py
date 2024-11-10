import math
from typing import Callable

def gradient_descent(X0, grad_f: Callable[[float, float], tuple[float,float]], iters = 10, upsi = 1):
    
    xs:list[float]=[] 
    ys:list[float]=[] 
    xs.append(X0[0]) 
    ys.append(X0[1])

    for _ in range(iters):

        grad = grad_f(xs[-1],ys[-1])

        if grad[0] == 0 and grad[1] == 0:
            break

        xs.append(xs[-1] - upsi * grad[0]) 
        ys.append(ys[-1] - upsi * grad[1]) 

    return ((xs, ys), (xs[-1], ys[-1]))

def golden_opti(f: Callable[[float, float], float], grads, xy:tuple[float,float]):
    def golden_section(fun, prad, pab, min):
        T = (math.sqrt(5) - 1)/2

        def vidus(l, X1, X2, r, fX1 = None, fX2 = None): 
            if(fX1 is None):
                fX1 = fun(X1)   

            if(fX2 is None):
                fX2 = fun(X2)
            
            if(fX2 < fX1):
                l = X1
                X1 = X2
                fX1 = fX2 
                fX2 = None 
                L = r - l
                X2 = l + T * L
            else:
                r = X2
                L = r - l
                X2 = X1
                fX2 = fX1
                fX1 = None
                X1 = r - T * L
            if(L < min):
                return (l, r)
            else:
                return vidus(l, X1, X2, r, fX1, fX2) 
        
        L = pab - prad
        X1 = pab - T * L
        X2 = prad + T * L
        return vidus(prad, X1, X2, pab) 

    def g(upsi):
        return f(xy[0] - upsi * grads[0], xy[1] - upsi * grads[1])

    result = golden_section(g,0,5,0.0001)
    if result[0] == 0:
        return 0
    return ((result[0] + result[1])/2)

def steepest_descent(X0, f: Callable[[float, float],float], grad_f: Callable[[float, float], tuple[float,float]], iters = 10):
    
    xs=[] 
    ys=[] 
    xs.append(abs(X0[0])) 
    ys.append(abs(X0[1])) 

    for _ in range(iters):
    
        grad = grad_f(xs[-1],ys[-1])
        
        if(grad[0] == 0 and grad[1] == 0):
            break

        x_upsi = golden_opti(f, grad, (xs[-1], ys[-1]))

        if(x_upsi == 0):
            break
        xs.append(xs[-1] - x_upsi * grad[0])
        ys.append(ys[-1] - x_upsi * grad[1]) 

    return ((xs, ys), (xs[-1], ys[-1]))

def simplex(X0, f: Callable[[float, float], float], a=1, iters = 10):

    points = []
    best = None

    def get_deformation(p_new, p_old, p1, p2, squeeze = 0.5, reverse = -0.5, expand = 2):
        if(p1 < p2):
            if p_new < p_old and p_new > p1:
                return 1
            elif p_new < p1:
                return expand
            elif p_new > p_old:
                return reverse
            elif p2 < p_new and p_new < p_old:
                return squeeze
        else:
            if(p_new < p_old and p_new > p2):
                return 1
            elif p_new < p2:
                return expand
            elif p_new > p_old:
                return reverse
            elif p1 < p_new and p_new < p_old:
                return squeeze
            
        return 1
            
    def point_ref(reflectable, x1, x2, step = 1):
        x = reflectable[0] + (step + 1)*(((x1[0] + x2[0])/2) - reflectable[0])
        y = reflectable[1] + (step + 1)*(((x1[1] + x2[1])/2) - reflectable[1])
        return (x, y)

    b1 = a * (math.sqrt(2 + 1) + 1)/(2 * math.sqrt(2))
    b2 = a * (math.sqrt(2 + 1) - 1)/(2 * math.sqrt(2))
    x0 = X0
    x1 = (x0[0] + b1, x0[1] + b2)
    x2 = (x0[0] + b2, x0[1] + b1)
    points.append((x0,x1,x2))

    for _ in range(iters):
        

        p0 = f(x0[0],x0[1])
        p1 = f(x1[0],x1[1])
        p2 = f(x2[0],x2[1])

        if(p0 > p1 and p0 > p2):
            x3 = point_ref(x0, x1, x2)
            p3 = f(x3[0],x3[1])
            de = get_deformation(p3, p0, p1, p2)
            x3 = point_ref(x0, x1, x2, de)
            x0 = x3
        elif(p1 > p2):
            x3 = point_ref(x1, x0, x2)
            p3 = f(x3[0],x3[1])
            de = get_deformation(p3, p1, p2, p0)
            x3 = point_ref(x1, x0, x2, de)
            temp = x0
            x0 = x3
            x1 = temp
        else:
            x3 = point_ref(x2, x1, x0)
            p3 = f(x3[0],x3[1])
            de = get_deformation(p3, p2, p0, p1)
            x3 = point_ref(x2, x1, x0, de)
            temp = x0
            x0 = x3
            x2 = temp

        points.append((x0,x1,x2))
            
            
    shape = points[-1]
    final_point = ((shape[0][0] + shape[1][0] + shape[2][0])/3,(shape[0][1] + shape[1][1] + shape[2][1])/3)

    return (points, final_point)
