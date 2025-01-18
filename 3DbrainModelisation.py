import numpy as np
import matplotlib.pyplot as plt
from skimage import measure
import cv2
from stl import mesh
import os
# Chemin ....
Bath = '/Users/aisssamhamida/Desktop/3d'
images = []
# Fonction pour charger+vérifier+niveaux de gris
def get_data(path):
    for i in range(2, 81):  
        chemin = os.path.join(path, f"{i}.jpg")
        if os.path.exists(chemin):  
            img_arr = cv2.imread(chemin, cv2.IMREAD_GRAYSCALE)  
            if img_arr is not None:  
                images.append(img_arr)
            else:
                print(f"Erreur : impossible de lire {chemin}")
        else:
            print(f"Fichier introuvable : {chemin}")
get_data(Bath)
# les dimensions des images
image_shapes = [img.shape for img in images]
# Conversion en tableau,volume 3D
volume_data = np.stack(images, axis=0).astype(np.float32)  
# Normalisation 
if np.max(volume_data) > np.min(volume_data):  
    volume_data = (volume_data - np.min(volume_data)) / (np.max(volume_data) - np.min(volume_data))
else:
    print("Erreur : les images semblent être uniformes (min = max).")
    exit()

print(f"Dimensions du volume 3D : {volume_data.shape}")
spacing = (9, 2.0, 2.0) 
verts, faces, normals, values = measure.marching_cubes(volume_data, spacing=spacing) 
# objet STL à partir des surfaces
mesh_3d = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    mesh_3d.vectors[i] = verts[f]
    
output_file = 'mirleft1966.stl'
mesh_3d.save(filename=output_file)
print(f"Modèle 3D sauvegardé sous : {output_file}")

