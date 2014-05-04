class Blob(object):
    
    def __init__(self, blob_list, x_list, y_list, mass, distance, centerofmass):
        self.mass = mass()
        self.distance = distanceTo(blob)
        self.centerofmass = centerofmass()
        self.x_list = []
        self.y_list = []
        self.blob_list = [self.x_list, self.y_list]
        
    def add(i,j):
        self.x_list.append(i)
        self.y_list.append(j)
        
               
    def mass():
        return len(self.x_list) 
        
    def centerofmass():
        mean_x = np.mean(x_list)
        mean_y = np.mean(y_list)
        mean_x1 = "%.4f" % mean_x 
        mean_y1 = "%.4f" % mean_y
        return (mean_x1, mean_y1)
        
    def distanceTo(blob):
        return ((blob.np.mean(x_list) - self.np.mean(x_list))**2 + (blob.np.mean(y_list) - self.np.mean(y_list))**2 )**.5    
    
def BlobFinder(picture, tau):
    """loops over the pixels in the loaded image, 
    replacing the RGB values of each with either 
    black or white depending on whether its total 
    luminance is above or below some threshold tau 
    passed in by the user"""
    black = (0, 0, 0)
    white = (255,255,255)
    xsize, ysize = picture.size
    temp = picture.load()
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if r+g+b <= threshold:
                temp[x,y] = black
            else:
                temp[x,y] = white
                
                

                
                
def Fill(picture):
    """keep a list of pixels that need to be looked at, 
    but haven't yet been filled in - a list of the (x,y) 
    coordinates of pixels that are neighbors of ones we have 
    already examined.  Keep looping until there's nothing 
    left in this list"""
    queue = [(0,0)]
    xsize, ysize = picture.size
    while queue:
        x,y,queue = queue[0][0], queue[0][1], queue[1:]
        r,g,b = picture[x,y]
        if (r,g,b) > BLACK:
            self.add(x,y)
            picture[x,y] = BLACK
            if x > 0:
                queue.append((x-1,y))
            if x < (xsize-1):
                queue.append((x+1,y))
            if y > 0:
                queue.append((x, y-1))
            if y < (ysize-1):
                queue.append((x, y+1))               
                
                
                
                
def countBeads(picture, P):
    """scan the image top to bottom and left to right using a nested loop.
    when non-black pixel is found, increment the count, then call the fill
    function to fill in all the pixels connected to that one.  
    
    Return the count"""
    xsize, ysize = picture.size
    temp = picture.load()
    result = 0
    for x in range(xsize):
        for y in range(ysize):
            if self.mass():
                result += 1
                Fill(picture)
    return result
