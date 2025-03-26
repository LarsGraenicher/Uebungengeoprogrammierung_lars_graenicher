import math

class Figur: 
    def __init__(self, name): 
        self.name = name
    def Umfang(self): 
        return 0 
    def __str__(self): 
        return self.name
    
class Punkt:
    def __init__(self, x, y):
        self.x=x
        self.y=y


class Kreis(Figur):
    def __init__(self, punkt ,radius):
        super().__init__("Kreis")
        
        self.punkt= punkt
        self.radius= radius

    def Umfang(self):
        return self.radius*math.pi*2
    
    def __str__(self):
        return f"{self.name} mit Zentrumskoordinaten ({self.punkt.x},{self.punkt.y}) und Radius {self.radius}"
    
k1=Kreis(Punkt(1,1),2)

print(k1.Umfang())

class Rechteck(Figur):
    def __init__(self, punkt1, punkt2):
        super().__init__("Rechteck")
        self.punkt1=punkt1
        self.punkt2=punkt2

    def Umfang(self):
        return 2*abs(self.punkt2.x-self.punkt1.x)+2*(abs(self.punkt2.y-self.punkt1.y))
    
    def __str__(self):
        return f"{self.name} ({self.punkt1.x},{self.punkt1.y}) - ({self.punkt2.x},{self.punkt2.y})"
    
r1= Rechteck(Punkt(1,1), Punkt(2,2))

print(r1.Umfang())

class Dreieck(Figur):
    def __init__(self, punkt1, punkt2, punkt3):
        super().__init__("Dreieck")
        self.punkt1=punkt1
        self.punkt2=punkt2
        self.punkt3=punkt3

    def Umfang(self):
        return math.sqrt(abs(self.punkt2.x-self.punkt1.x)**2+(abs(self.punkt2.y-self.punkt1.y))**2)+math.sqrt(abs(self.punkt3.x-self.punkt2.x)**2+(abs(self.punkt3.y-self.punkt2.y))**2)+math.sqrt(abs(self.punkt1.x-self.punkt3.x)**2+(abs(self.punkt1.y-self.punkt3.y))**2)
    
    def __str__(self):
        return f"{self.name} ({self.punkt1.x},{self.punkt1.y}) - ({self.punkt2.x},{self.punkt2.y}) - ({self.punkt3.x},{self.punkt3.y})"
        
d1=Dreieck(Punkt(1,1),Punkt(2,2), Punkt(1,2))

print(d1.Umfang())

class Polygon(Figur):
    def __init__(self, liste):
        super().__init__("Polygon")
        self.liste=liste

    def Umfang(self):
        result= math.sqrt((self.liste[len(self.liste)-1].x - self.liste[0].x)**2+(self.liste[len(self.liste)-1].y-self.liste[0].y)**2)
        for n in range(0,len(self.liste)-1):
            result += math.sqrt((self.liste[n].x - self.liste[n+1].x)**2+(self.liste[n].y-self.liste[n+1].y)**2)
    
        return result
    

    def __str__(self):
        text= f"{self.name} "
        for element in self.liste:
            text += f"- ({element.x},{element.y}) "

        return text
    
l=[Punkt(1,1),Punkt(2,2), Punkt(1,2)]

p1=Polygon(l)

print(p1.Umfang())
print(p1)