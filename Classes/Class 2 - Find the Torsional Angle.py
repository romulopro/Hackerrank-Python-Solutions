class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        

    def __sub__(self, n):
        return Points(self.x -n.x, self.y -n.y, self.z -n.z  )

    def dot(self, n):#escalar
         return self.x*n.x+self.y*n.y+self.z*n.z      

    def cross(self, n):#vetorial
         return Points(self.y*n.z - self.z*n.y, self.z*n.x - self.x*n.z, self.x*n.y - self.y*n.x)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)