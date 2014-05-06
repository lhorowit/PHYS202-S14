
class Blob(object):
    
    def __init__(self):
        self.pixels = []
        
    def add(self,i,j):
        self.pixels.append((i,j))
        
    def mass(self):
        return len(self.pixels) 
        
    def centerofmass(self):
        sumX = 0
        sumY = 0
        for pixel in self.pixels:
            sumX += pixel[0]
            sumY += pixel[1]
            avg = (sumX/len(self.pixels), sumY/len(self.pixels))
        return avg
            
        
    def distanceTo(blob):
        D = ((self.centerofmass[0] - blob.centerofmass[0])**2 + (self.centerofmass[1] - blob.centerofmass[1])**2)**.5
        return round(D, 4)
    
    
def BlobFinder(picture, tau):
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
    xsize, ysize = picture.size
    temp = picture.load()
    result = 0
    for x in range(xsize):
        for y in range(ysize):
            if self.mass() >= P:
                result += 1
                Fill(picture)
    return result