class ficha:
    abc="abcdefgh"    
    def __init__(self,name):
        self.name=name
        self.visible = True
        self.setPos()
  
    def load(self,tipo,x,y):
        self.name=tipo+x+y
        self.setPos()

    def setPos(self):
        rescal = 45
        self.X = self.getPosInt()[0] * rescal
        self.Y =  self.getPosInt()[1] * rescal
    
    def getPosInt(self):
        return int(self.abc.index(self.name[3])),(int(self.name[4])-1)
    
    def setVisible(self,visible):
        self.visible = visible 
        
    def image_location(self):
        return "images/"+self.name[:2]+".png"
    
    def info(self):
        print(self.name+" "+str(self.Y)+" "+str(self.X)+" "+self.image_location())#+" "+str(self.i)+" "+str(self.j))


    
