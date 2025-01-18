import numpy as np
import matplotlib.pyplot as plt 
import skimage as ski 
from skimage import measure
import matplotlib.pyplot as plt
from skimage import measure
import stl
from stl import mesh
x=y= np.linspace(-1,1,100)
z=np.linspace(0,0.5,100)
x2d, y2d=np.meshgrid(x,y)
x3d,y3d,z3d= np.meshgrid(x,y,z)
f=((x3d**2+y3d**2) >= z3d)*((x3d**2+y3d**2) <= 1.5*z3d)#selon la logique de boole
f[:,:,0] = 0
f[:,:,-1 ]= 0
plt.pcolormesh(x2d,y2d,f[:,:,-1])
Verts, faces, normals, values,= measure.marching_cubes(f)
cts3d_image =mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i ,f in enumerate(faces):
 cts3d_image.vectors[i]=Verts[f]
#Enregister le fichier pour le visulaiser sous forme d'un fichier .stl
cts3d_image.save(filename='delta3.stl')





