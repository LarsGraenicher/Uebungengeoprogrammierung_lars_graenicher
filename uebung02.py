class Vector3:
    def __init__(self,x,y,z):
        self._x=x
        self._y=y
        self._z=z

    def setX(self, x):
        self.x=x

    def getX(self):
        return self._x
    
    def setY(self, y):
        self._y=y

    def getY(self):
        return self._y

    def setZ(self, z):
        self._z=z

    def getZ(self):
        return self._z

    x=property(getX,setX)   
    y=property(getY,setY)
    z=property(getZ,setZ)

    def __str__(self):
        return f"Der Vektor ist ({self._x},{self.y},{self.z})"
    
    def __add__(self, addVector):
        return Vector3(self.x+addVector.x, self.y+addVector.y, self.z+addVector.z)
    
    def __sub__(self, subVector):
        return Vector3(self.x-subVector.x,self.y-subVector.y,self.z-subVector.z)

    def __iadd__(self, addVector):
        return self.__add__(addVector)
    
    def __mul__(self, multiplicator):
        if type(multiplicator) == Vector3:
            return Vector3(self.x*multiplicator.x, self.y*multiplicator.y, self.z*multiplicator.z)
        if type(multiplicator) == int:
            return Vector3(self.x*multiplicator, self.y*multiplicator, self.z*multiplicator)
        if type(multiplicator) == float:
            return Vector3(self.x*multiplicator, self.y*multiplicator, self.z*multiplicator)

    def __rmul__(self, multiplicator):
        if type(multiplicator) == int:
            return Vector3(self.x*multiplicator, self.y*multiplicator, self.z*multiplicator)
        if type(multiplicator) == float:
            return Vector3(self.x*multiplicator, self.y*multiplicator, self.z*multiplicator)

    def cross(self, b):
        if not type(b) == Vector3:
            raise TypeError("Parameter has to be type Vector3")
        return Vector3(self.y*b.z-self.z*b.y, self.z*b.x-self.x*b.z,self.x*b.y-self.y*b.x)
    
    def dot(self, b):
        if not type(b) == Vector3:
            raise TypeError("Parameter has to be type Vector3")
        return self.x*b.x+self.y*b.y+self.z*b.z
    
    def normalize(self):
        lenself= (self.x**2+self.y**2+self.z**2)**0.5
        return Vector3(self.x/lenself, self.y/lenself, self.z/lenself)
    

v1=Vector3(1,0,0)
v2=Vector3(0,1,0)

print(v2*3.3)