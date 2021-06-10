#!/usr/bin/python3

from datetime import date

class Persona:
  def __init__(self,año_nacimiento,sexo):
    self.año_nacimiento = año_nacimiento
    self.sexo = sexo
    self.edad = self.get_edad()

  def get_edad(self):
    return date.today().year - self.año_nacimiento

  def info(self):
    print(self.sexo,self.edad)

persona01 = Persona(1979,"Hombre")

persona01.info()
    
