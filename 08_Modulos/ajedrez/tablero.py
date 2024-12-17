from PIL import Image
from ficha import ficha

class tablero:
    Lista_fichas = []
    def __init__(self,inicio):
        for i in inicio:
            self.Lista_fichas.append(ficha(i))
    
    def pintar_tablero(self):
        tablero_img = Image.open('images/tablero.png').convert("RGBA")
        for ficha in self.Lista_fichas:
            if ficha.visible:
                aux_img = Image.open(ficha.image_location()).convert("RGBA") 
                tablero_img.alpha_composite(aux_img, (ficha.X, ficha.Y))
            tablero_img.save("jugada.png")

    def cambiar_posicion_ficha(self,name1,name2):
        for ficha in self.Lista_fichas:
            if ficha.name == name1:
                ficha.name = name2
                ficha.setPos()
 
    def comer_ficha(self,name1,name2):
        for ficha in self.Lista_fichas:
            if (ficha.name[3:5] == name2[3:5] ):
                ficha.setVisible(False)       
        self.cambiar_posicion_ficha(name1,name1[:2]+"_"+name2[3:5])
    
