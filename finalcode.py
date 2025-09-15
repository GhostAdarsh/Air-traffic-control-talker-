print("hello world") 

# import modules here: 
from PIL import Image
import tkinter as tk 
from matplotlib import image 
from matplotlib import pyplot as plt 




#image show function 

def startup(): # adds background and 2D grid 
    print("x")
    # background: 
    img = Image.open('LondonHeathrowNEA.jpg')
    desired_dpi = 500

    # plotting points on grid
    t5A = plt.plot(365, 390, marker='x', color="green")
    t5B = plt.plot(365, 445, marker='x', color="blue")
    t5C = plt.plot(400, 425, marker='x', color="red")
    t5D = plt.plot(435, 450, marker='x', color="purple")
    t5E = plt.plot(463, 407, marker='x', color="brown")
    t5F = plt.plot(493, 424, marker='x', color="magenta")

    plt.imshow(img)
    plt.show()



startup() 


