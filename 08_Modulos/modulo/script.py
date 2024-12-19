import sys
import os
from geometry.dinamic import *

din=dinamic()

def print_help() :
  print (sys.argv[0], '-i <file xyz format>')

if len(sys.argv) == 1 :
  print_help()

for i in range(1,len(sys.argv)):
  if sys.argv[i] == '-i' :
    din.loadxyz(sys.argv[i+1])

for i in range(1,len(sys.argv)):
  if sys.argv[i] == '-d' :
    din.distancia(int(sys.argv[i+1]),int(sys.argv[i+2]))