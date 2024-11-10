import math
from typing import Callable

def half_elimination(fun: Callable[[float], float], start, end, min):

    def vidus(l, Xm, fXm, r):
        L = r - l
        X1 = l + L/4
        X2 = r - L/4
        fX1 = fun(X1)
        if(fX1 < fXm):
            r = Xm
            Xm = X1
            fXm = fX1
        else:
            fX2 = fun(X2)
            if(fX2 < fXm):
                l = Xm
                Xm = X2
                fXm = fX2
            else:
                l = X1
                r = X2
        
        L = r - l
        if(L < min):
            return (l,r)
        else:
            return vidus(l, Xm, fXm, r)
        
  
    Xm = (start + end)/2
    fXm = fun(Xm)

    return vidus(start, Xm, fXm, end)

def golden_section(fun:Callable[[float], float], start, end, min):

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
    
    L = end - start
    X1 = end - T * L
    X2 = start + T * L
    return vidus(start, X1, X2, end)     

def newton_method(funD:Callable[[float], float], funDD:Callable[[float], float], min, X0):  
    def vidus(X0):
        Xn = X0 - funD(X0)/funDD(X0)

        if(abs(X0 - Xn) < min):
            return Xn
        else:
            return vidus(Xn)
     
    return vidus(X0)