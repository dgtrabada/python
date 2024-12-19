from  geometry.step import step
from  geometry.atom import atom
import math

class dinamic:
    
  def __init__(self):
    self.step=[]

  def append(self,step):
    self.step.append(step)
       
  def loadxyz(self,archivo,name=""):
    natoms = 0
    istep = 0
    text=open(archivo).readlines()
    nmaxlines=len(text)
    i=0
    while i < nmaxlines:
      line=text[i].split()
      bas=step()
      istep=istep+1
      if name != "":
        bas.name=name
      else:
        bas.name="step = "+str(istep)
      if i == 0 :
        natoms = int(line[0])
        i=i+1
      bas.line2=text[i]
      for j in range(natoms):
        i=i+1
        line=text[i].split()
        a=line[0]
        ra=[]
        ra.append(float(line[1]))
        ra.append(float(line[2]))
        ra.append(float(line[3]))     
        bas.append(atom(a,ra))
      i=i+1 #natom
      i=i+1 #line2
      self.append(bas)

  def distancia(self,atom1,atom2):
    for i in range(len(self.step)):
        r1 = self.step[i].atom[atom1-1].r
        r2 = self.step[i].atom[atom2-1].r 
        distance = math.sqrt((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2 + (r1[2] - r2[2])**2)
        print(f"d({atom1},{atom2}) = {distance}")
        