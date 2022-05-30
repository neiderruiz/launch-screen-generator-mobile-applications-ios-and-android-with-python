import numpy as np
import cv2
from PIL import Image

# crear lienzo imagen
def createBaseImage(size_y, size_x, url_save):
    img = np.zeros((size_y, size_x, 3), np.uint8)
    cv2.imwrite(url_save, img)

# supoerponer imagen
def overlayImage(imgOverlap, position, url_image):
    image = Image.open(url_image)
    image.paste(imgOverlap, position, mask=imgOverlap)
    image.save(url_image)

# agregar texto a imagen
def addTextImage(img, text, fontSize, fontColor, fontWeigth, marginTop):
    font = cv2.FONT_HERSHEY_DUPLEX
    width = img.shape[1]
    heigth = img.shape[0]
    # separar por saltos de linea
    for i, line in enumerate(text.split('\n')):
        text_formatter = line.strip()
        textsize = cv2.getTextSize(
            text_formatter, font, fontSize, fontWeigth)[0]
        textX = int((width - textsize[0]) / 2)
        # imprimir primera linea
        if(i == 0):
            textY = int(heigth * marginTop)
        else:
            textY = int(heigth * marginTop) + \
                textsize[1] * i + int(textsize[1] * 0.8 * i)
        position = (textX, textY)
        cv2.putText(img, text_formatter, position, font,
                    fontSize, fontColor, fontWeigth)
