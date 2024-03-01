import cv2
import numpy as np
import matplotlib.pyplot as plt

R = cv2.imread('Renault.png', cv2.IMREAD_GRAYSCALE)
A = cv2.imread('audi.png', cv2.IMREAD_GRAYSCALE)

_, tr = cv2.threshold(R, 240, 255, cv2.THRESH_BINARY)
_, ta = cv2.threshold(A, 240, 255, cv2.THRESH_BINARY)
contR, _ = cv2.findContours(tr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contA, _ = cv2.findContours(ta, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rx = []
ry = []


for contorno in contR:
    for punto in contorno:
        x, y = punto[0]
        rx.append(x)
        ry.append(y)

ax = []
ay = []
for contorno in contA:
    for punto in contorno:
        x, y = punto[0]
        ax.append(x)
        ay.append(y)
plt.figure(figsize=(18, 9))
plt.subplot(1, 2, 1)
plt.scatter(rx, ry, s=1, color='b')
plt.title('Contorno del logo de Renault')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.subplot(1, 2, 2)
plt.scatter(ax, ay, s=1, color='b')
plt.title('Contorno del logo de Audi')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.tight_layout()
plt.show()