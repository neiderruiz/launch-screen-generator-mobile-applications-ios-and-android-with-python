import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import os

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
def addTextImage(url_image, text, fontSize, fontColor, marginTop, font):
    img = cv2.imread(url_image)
    width = img.shape[1]
    heigth = img.shape[0]
    font_extra = ImageFont.truetype(font, fontSize)
    # separar por saltos de linea
    for i, line in enumerate(text.split('\n')):
        text_formatter = line.strip()
        image = Image.open(url_image)
        draw = ImageDraw.Draw(im=image)
        textX = int((width) / 2)
        # imprimir primera linea
        if(i == 0):
            textY = int(heigth * marginTop)
        else:
            textY = int(heigth * marginTop) + \
                fontSize * i + int(fontSize * 0.8 * i)
        position = (textX, textY)
        draw.text(xy=position, text=text_formatter,
                  font=font_extra, fill=fontColor, anchor='mm')
        image.save(url_image)
