print("s")
from PIL import Image 
import numpy as np 

img = Image.open("LHRNEA.png")
a = np.array(img)

print(a.shape)
# i dont think this ll work bcs i need to manipulate the specifics of the image to find out areas/ 
# boundaries that the object cannot pass thru 

# bail 
