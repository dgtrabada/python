#!/usr/bin/python3

from datetime import date

class Persona:
  def __init__(self, año_nacimiento, sexo, nombre, apellido):
    self.año_nacimiento = año_nacimiento
    self.sexo = sexo
    self.edad = self.get_edad()
    self.nombre = nombre
    self.apellido = apellido

  def get_edad(self):
    return date.today().year - self.año_nacimiento

  def info(self):
    print("Nombre   : "+self.nombre)
    print("Apellido : "+self.apellido)
    print("Edad     : "+str(self.edad))
    print("Sexo     : "+self.sexo)

persona01 = Persona(1979,"Hombre","Manuel","López")

persona01.info()
#Nombre   : Manuel
#Apellido : López
#Edad     : 42
#Sexo     : Hombre

print("Año de nacimiento "+str(persona01.año_nacimiento))
#Año de nacimiento 1979

#herencia
class Estudiante(Persona): 
  def __init__(self, año_nacimiento, sexo, nombre, apellido, curso):
    super().__init__(año_nacimiento, sexo, nombre, apellido)
    self.curso = curso
  def info(self):
    super().info()
    print("Curso    : "+self.curso) 

estudiante01 = Estudiante(1981,"Mujer","María","Garcia","1DAM")

estudiante01.info()
#Nombre   : María
#Apellido : Garcia
#Edad     : 40
#Sexo     : Mujer


estudiante01.info()
#Nombre   : María
#Apellido : Garcia
#Edad     : 40
#Sexo     : Mujer
#Curso    : 1DAM

class Curso:
  def __init__(self, año, nombre , departamento,profesor):
    self.año = año
    self.nombre = nombre
    self.departamento = departamento
    self.profesor = profesor

#curso01 = Curso(1,"Python", "Informática"


