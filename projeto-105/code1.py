import os
import cv2 

imagens = "imagens/"
imgs = []

for imagem in os.listdir(imagens):
    name, extencao = os.path.splitext(imagem)
    if extencao == ".jpg":
        origem = imagens+imagem
        imgs.append(origem)

count = len(imgs)
frame = cv2.imread(imgs[0])
height, width, channels = frame.shape
size = (width, height)


video = cv2.VideoWriter("hyper_cars.mp4",  cv2.VideoWriter_fourcc(*"DIVX"), 0.5, size)
for i in range(0, count-1):
    frame = cv2.imread(imgs[i])
    video.write(frame)