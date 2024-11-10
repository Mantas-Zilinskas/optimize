import math

##########################################################

def funkcija(x, a = 2, b = 1): 
    return ((x**2 - a)**2/b) - 1

def funkcijaD(x, a = 2, b = 1): #pirmoji išvestinė
    return 4 *x *(x**2 - a)/b

def funkcijaDD(x, a = 2, b = 1): #antroji išvestinė
    return 4*(3*x**2 - a)/b


intervalas = (0, 10)
e = 0.0001

##########################################################



def IntervaloDalijimasPusiau(fun, prad, pab, min):

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
        
  
    Xm = (prad + pab)/2
    fXm = fun(Xm)

    return vidus(prad, Xm, fXm, pab)

def AuksinisPjuvis(fun, prad, pab, min):

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

def NiutonoMetodas(funD, funDD, min, X0):  
    def vidus(X0):
        Xn = X0 - funD(X0)/funDD(X0)

        if(abs(X0 - Xn) < min):
            return Xn
        else:
            return vidus(Xn)
     
    return vidus(X0)

print(IntervaloDalijimasPusiau(funkcija, intervalas[0], intervalas[1], e))
print(AuksinisPjuvis(funkcija, intervalas[0], intervalas[1], e))
print(NiutonoMetodas(funkcijaD, funkcijaDD, e, 5))