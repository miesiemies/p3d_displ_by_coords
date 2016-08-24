###############################
## Deformations Extractor    ##
## (c)2015 - Filippo Forlani ##
## gnugpl		     ##
## contact: filfor@gmail.com ##
###############################

#########
## usage:
## a. write a text file with points' coordinates to inspect
## b. launch server on plx 3d output on port 10001 (look for 'outputport' variable)
## c. run this program and catch output text file with name, phase, ux, uy, uz
## d. file is already to copy & paste to Excel or every spreadsheet
import string
import imp

plaxis_path = r'C:\Program Files (x86)\Plaxis\PLAXIS 3D'

found_module = imp.find_module('plxscripting', [plaxis_path])
plxscripting = imp.load_module('plxscripting', *found_module)
from plxscripting.easy import *

outputport = 10001
s_o, g_o = new_server('localhost', outputport)


stepids = [ ]
sz=[]
sztot=0
phasenames= []

class PlPoint(object):
    def __init__(self,name,x,y,z):
      self.name=name
      self.x=float(x)
      self.y=float(y)
      self.z=float(z)
    
pts=[]

fop=input('input filename [c:\pointsU.txt]:')
fot=input('output filename [c:\outputU.txt]:')

fase0=input('start phase [all] : ')
fase1=input('end phase [all] : ')
if not(fase0.isnumeric()): fase0=''
if not(fase1.isnumeric()): fase1=''

if fop=='': fop=r'c:\pointsU.txt'
if fot=='': fot=r'c:\outputU.txt'

fpoint=open(fop,"r")

while 1:
    in_line=fpoint.readline()
    if in_line=="":
        break
    print(in_line)
    [name,nx,ny,nz]=in_line.split('\t')
    pts.append(PlPoint(name,nx,ny,nz))

fpoint.close()

file=open(fot,"w")

if fase0=='' and fase1=='': iterate = g_o.Phases[:]
if fase0=='' and fase1!='': iterate = g_o.Phases[:int(fase1)]
if fase1!='' and fase1=='': iterate = g_o.Phases[int(fase0):]
if fase1!='' and fase1!='': iterate = g_o.Phases[int(fase0):int(fase1)]

iterate = g_o.Phases[:]
for phase in iterate:
    print(phase.Name.value)
    phasenames.append(phase.Name.value)

    for pt in pts:
        print(pt.x)
        ux=g_o.getsingleresult(phase, g_o.Soil.Ux, (pt.x, pt.y, pt.z))
        print('ux=',ux)

        uy = g_o.getsingleresult(phase, g_o.Soil.Uy,(pt.x, pt.y, pt.z))

        print('uy=', uy)
        uz=g_o.getsingleresult(phase, g_o.Soil.Uz, (pt.x, pt.y, pt.z))
        print('uz=',uz)
        print(pt.name, pt.x, pt.y, pt.z, ux, uy, uz)
        file.write("\t".join([ phase.Name.value, pt.name, str(pt.x), str(pt.y), str(pt.z), str(ux), str(uy), str(uz)])+'\n')
        print("\t".join([phase.Name.value, str(pt.name), str(pt.x), str(pt.y), str(pt.z), str(ux), str(uy), str(uz)]))
    print("end phase\n")
print("end")
file.close()



