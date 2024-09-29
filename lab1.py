import matplotlib.pyplot as plt
import numpy as np
import math

##########################################################

def funkcija(x): 
    return ((x**2 - a)**2/b) - 1

def funkcijaD(x):
    return 4 *x *(x**2 - a)/b

def funkcijaDD(x):
    return 4*(3*x**2 - a)/b

a = 2
b = 1

intervalas = (0, 10)
e = 0.0001

##########################################################



def IntervaloDalijimasPusiau(fun, prad, pab, min, tikslof = 0, iter = 0):

    def vidus(l, Xm, fXm, r, tikslof, iter):
        L = r - l
        X1 = l + L/4
        X2 = r - L/4
        fX1 = fun(X1)
        tikslof += 1             ################
        if(fX1 < fXm):
            # plt.fill_between([Xm, r], [-5,-5], y2 = max(Ys) , color='red', alpha=0.3)
            # plt.scatter([Xm], [fun(Xm)], color='red')
            # plt.text(Xm, fun(Xm), f'{taskas}', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
            # taskas += 1
            r = Xm
            Xm = X1
            fXm = fX1
        else:
            fX2 = fun(X2)
            if(fX2 < fXm):
                tikslof += 1      #############
                # plt.fill_between([l, Xm], [-5,-5], y2 = max(Ys) , color='red', alpha=0.3)
                # plt.scatter([Xm], [fun(Xm)], color='red')
                # plt.text(Xm, fun(Xm), f'{taskas}', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
                # taskas += 1
                l = Xm
                Xm = X2
                fXm = fX2
            else:
                # plt.fill_between([l, X1], [-5,-5], y2 = max(Ys) , color='red', alpha=0.3)
                # plt.fill_between([X2, r], [-5,-5], y2 = max(Ys) , color='red', alpha=0.3)
                # plt.scatter([X1], [fun(X1)], color='red')
                # plt.scatter([X2], [fun(X2)], color='red')
                # plt.text(X1, fun(X1), f'{taskas}', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
                # plt.text(X2, fun(X2), f'{taskas}', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
                # taskas += 1
                l = X1
                r = X2
        
        L = r - l
        iter += 1     ######
        print(f"{iter} {tikslof} {(l,r)} {L}")   #######
        if(L < min):
            return (l,r)
        else:
            return vidus(l, Xm, fXm, r, tikslof, iter)
        
    # Xs = np.linspace(prad, pab, num = 1000)
    # Ys = [fun(y) for y in Xs]
    # fig, ax = plt.subplots() 
    # ax.plot(Xs, Ys)
  
    Xm = (prad + pab)/2
    fXm = fun(Xm)
    tikslof += 1
    rezultatas = vidus(prad, Xm, fXm, pab, tikslof, iter)
    print(tikslof)
    # plt.show()
    return rezultatas

def AuksinisPjuvis(fun, prad, pab, min):

    T = (math.sqrt(5) - 1)/2
    L = pab - prad
    X1 = pab - T * L
    X2 = prad + T * L

    def vidus(l, X1, X2, r, taskas = 1):
        if(fun(X2) < fun(X1)):
            plt.fill_between([l, X1], [-5,-5], y2 = max(Ys) , color='red', alpha=0.3)
            plt.scatter([X1], [fun(X1)], color='red')
            plt.text(X1, fun(X1), f'{taskas}', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
            taskas += 1
            l = X1
            X1 = X2
            L = r - l
            X2 = l + T * L
        else:
            plt.fill_between([r, X2], [-5,-5], y2 = max(Ys) , color='red', alpha=0.3)
            plt.scatter([X2], [fun(X2)], color='red')
            plt.text(X2, fun(X2), f'{taskas}', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
            taskas += 1
            r = X2
            L = r - l
            X2 = X1
            X1 = r - T * L

        if(L < min):
            return (l, r)
        else:
            return vidus(l, X1, X2, r, taskas)

    Xs = np.linspace(prad, pab, num = 1000)
    Ys = [fun(y) for y in Xs]
    fig, ax = plt.subplots() 
    ax.plot(Xs, Ys)
    rezultatas = vidus(prad, X1, X2, pab)
    plt.show()
    return rezultatas    

def NiutonoMetodas(fun, funD, funDD, prad, pab, min, X0):
    def vidus(X0, taskas = 1):
        Xn = X0 - funD(X0)/funDD(X0)
        plt.scatter([Xn], [fun(Xn)], color='red')
        plt.text(Xn, fun(Xn), f'{taskas}', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
        taskas += 1
        if(abs(X0 - Xn) < min):
            return Xn
        else:
            return vidus(Xn, taskas)
     
    Xs = np.linspace(prad, pab, num = 10000)
    Ys = [fun(y) for y in Xs]
    fig, ax = plt.subplots() 
    ax.plot(Xs, Ys)
    plt.scatter([X0], [fun(X0)], color='red')
    plt.text(X0, fun(X0), '0', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
    rezultatas = vidus(X0)
    plt.show()
    return rezultatas

IntervaloDalijimasPusiau(funkcija, intervalas[0], intervalas[1], e)
# AuksinisPjuvis(funkcija, intervalas[0], intervalas[1], e)
# NiutonoMetodas(funkcija, funkcijaD, funkcijaDD, intervalas[0], intervalas[1], e, 5)