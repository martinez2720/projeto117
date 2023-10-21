import cv2
import os

path = "Images"
images = []


for file in os.listdir(path):
  
    file_name, file_extension = os.path.splitext(file)
   
    if file_extension.lower() in ['.png', '.jpg', '.jpeg']:
        file_name = os.path.join(path, file_name + file_extension)
        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])

height, width, channels = frame.shape

size = (width, height)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)


for i in range(0, count):
    img = cv2.imread(images[i])
    out.write(img)


out.release()


print("Concluído")
