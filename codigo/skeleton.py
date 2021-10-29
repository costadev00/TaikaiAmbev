from pyx import canvas,path,color
from math import *
from random import random

from PIL import Image

import pytesseract

#pega oque ta na imagem e converte para string
tesseract =(pytesseract.image_to_box(Image.open('imagem.jpg')))

#tamanho da quantidade de pontos pegos pelo tesseract
npoints = len(tesseract)


radius = 0.05
scale = 5
beta1 = 1.1
beta2 = 0.9
theta1 = asin(1/beta1)
theta2 = pi - asin(beta2)

points = [(tesseract[i][0]*scale,tesseract[i][1]*scale) for i in range(npoints)]

def dot(p,q,r):
    return sum((p[i]-r[i])*(q[i]-r[i]) for i in [0,1])

def sharp(p,q):
    theta = 0.0
    for r in points:
        if r not in [p,q]:
            prq = acos(dot(p,q,r) / (dot(p,p,r)*dot(q,q,r))**0.5)
            theta = max(theta,prq)
    return theta

c = canvas.canvas()
 
def edge1(p,q):
    c.stroke(path.line(p[0],p[1],q[0],q[1]),
             [color.rgb.black])

def edge2(p,q):
    c.stroke(path.line(p[0],p[1],q[0],q[1]),
             [color.rgb.blue])

def point(p):
    c.fill(path.circle(p[0],p[1],radius),[color.rgb.red])

for p in points:
    for q in points:
        if p < q:
            theta = sharp(p,q)
            if theta < theta1:
                edge1(p,q)
            elif theta < theta2:
                edge2(p,q)

for p in points:
    point(p)

#retorna imagem do grafo
c.writePDFfile("Beta-skeleton")

#retorna os pontos de ligação do grafo
print(points)
