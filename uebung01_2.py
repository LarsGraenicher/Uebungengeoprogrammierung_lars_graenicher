class WGS84Coord():
    def __init__(self,_longitude=0,_latitude=0):
        self._longitude=_longitude
        self._latitude=_latitude

    def setlongitude(self, wert):
        if wert <-180 or wert >180:
            print("Die Länge ist nicht im Wertebereich und wird korrigiert")
        while wert < -180:
            wert+=360
        
        while wert > 180:
            wert=wert-360
        self._longitude=wert

    def setlatitude(self, wert):
        if wert <-90 or wert >90:
            print("Die Breite ist nicht im Wertebereich und wird korrigiert, gegebenenfalls auch die Länge")
        klatittude=0
        counterlatitude=0
        counterlongitude=(wert+90)//180
        if counterlongitude%2==1:
            self.setlongitude(self._longitude*(-1))
        while wert>180:
            wert=wert-180
            counterlatitude+=1   
        if wert >90:
            klatittude=wert-90
            wert=90-klatittude
        if counterlatitude%2==1:
            wert= wert *(-1)
        while wert<-180:
            wert=wert+180
            counterlatitude+=1   
        if wert <-90:
            klatittude=wert+90
            wert=(-90)-klatittude
        if counterlatitude%2==1:
            wert= wert *(-1)
        self._latitude=wert
    
    def getlongitude(self):
        return self._longitude
    
    def getlatitude(self):
        return self._latitude
    longitude=property(getlongitude,setlongitude)
    latitude=property(getlatitude,setlatitude)
        
        
a=WGS84Coord()
a.longitude=190
a.latitude=2001    
print(a._longitude,a._latitude)
        


