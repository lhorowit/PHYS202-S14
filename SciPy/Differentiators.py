
def twoPtForwardDiff(x,y):
    """takes arrays x and y and returns dy/dx using a 2-point Foreward Difference"""
    
    
    dydxF = np.zeros(y.shape, float) 
    dydxF[0:-1] = np.diff(y)/np.diff(x)
    dydxF[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    
    return dydxF


        
def twoPtCenteredDiff(x,y):
    """takes arrays x and y and returns dy/dx using a 2-point Center Difference.
    This returns dy/dx using the slope of the given point and the next point in line """
    
    dydxC = np.zeros(y.shape, float) 
    dydxC[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2]) #center difference
    dydxC[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference
    dydxC[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) #backward difference
    
    return dydxC



def fourPtCenteredDiff(x,y):
    """takes arrays x and y and returns dy/dx using four point Center Difference"""
    
    dydx4 = np.zeros(y.shape, float) 
    dydx4[2:-2] = (y[0:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:])/(12*(x[1]-x[0])) #center difference
    dydx4[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference
    dydx4[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) #backward difference
    dydx4[1] = (y[2]-y[1])/(x[2]-x[1]) #forward difference
    dydx4[-2] = (y[-2] - y[-3])/(x[-2] - x[-3]) #backward difference
    return dydx4