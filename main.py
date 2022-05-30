import cv2
from PIL import Image
import numpy as np
import os

from modules.modules import addTextImage,  createBaseImage, overlayImage
from modules.sizes import sizesAndroid, sizesIos


def createImageHorizontal(url_image, isIos):
    image = Image.open(url_image)
    logo = Image.open(route_logo)
    # calcular el tamaño del logo y centrarlo
    logo_resize = logo.resize(
        (int((image.height * 0.5) / 2), int((image.height * 0.5) / 2)))
    position = (int((image.width - logo_resize.width) / 2),
                int((image.height - logo_resize.height) * 0.7))
    overlayImage(logo_resize, position, url_image)
    # ejemplo de insercion de dos imagenes -- descomentarlas dos lineas siguientes para usar
    # position2 = (int(image.width * 0.2), int(image.height * 0.2))
    # overlayImage(logo_resize, position2, url_image)
    #  tamaño de letra por defecto
    fontSize = int(image.width * 0.0025)
    # grosor de letra por defecto
    fontWeigth = 6
    # tamaños y grosor personalizadas segun tamaño de imagen
    if isIos:
        if image.width == 2208:
            fontWeigth = 3
            fontSize = 2.8
        if image.width == 2436:
            fontWeigth = 3
            fontSize = 2.8
        if image.width == 1024:
            fontWeigth = 2
            fontSize = 1.7
        if image.width == 2048:
            fontWeigth = 3
            fontSize = 2.8
    else:
        if image.width == 1920:
            fontWeigth = 5
            fontSize = 2.5

        if image.width == 1280:
            fontWeigth = 3
            fontSize = 2

        if image.width == 800:
            fontWeigth = 2
            fontSize = 1

        if image.width == 480:
            fontWeigth = 1
            fontSize = 0.8

        if image.width == 320:
            fontWeigth = 1
            fontSize = 0.5

    img = cv2.imread(url_image)
    # se añade el trecto a la imagen
    addTextImage(img, txt_one, fontSize, (255, 255, 255), fontWeigth, 0.2)
    addTextImage(img, txt_version, fontSize,
                 (255, 255, 255), fontWeigth, 0.9)
    # se guarda la imagen
    cv2.imwrite(url_image, img)
    print('create image: ' + url_image)


def createImageVertical(url_image, isIos):
    image = Image.open(url_image)
    logo = Image.open(route_logo)
    # calcular el tamaño del logo y centrarlo
    logo_resize = logo.resize(
        (int((image.width * 0.5) / 2), int((image.width * 0.5) / 2)))
    position = (int((image.width - logo_resize.width) / 2),
                int((image.height - logo_resize.height) * 0.7))
    overlayImage(logo_resize, position, url_image)
    #  tamaño de letra por defecto
    fontSize = int(image.width * 0.0025)
    # grosor de letra por defecto
    fontWeigth = 6

    if isIos:
        if image.width == 640:
            fontWeigth = 2
            fontSize = 1
        if image.width == 750:
            fontWeigth = 2
            fontSize = 1.2
        if image.width == 1242:
            fontWeigth = 3
            fontSize = 2.5
        if image.width == 2436:
            fontWeigth = 3
            fontSize = 2.8
        if image.width == 2208:
            fontWeigth = 3
            fontSize = 2.8
        if image.width == 768:
            fontWeigth = 2
            fontSize = 1.2
    else:
        if image.width == 800:
            fontWeigth = 2
            fontSize = 1.5

        if image.width == 720:
            fontWeigth = 4
            fontSize = 1.5

        if image.width == 480:
            fontWeigth = 2
            fontSize = 1

        if image.width == 320:
            fontWeigth = 1
            fontSize = 0.6

        if image.width == 200:
            fontWeigth = 1
            fontSize = 0.4
    img = cv2.imread(url_image)
    addTextImage(img, txt_one,
                 fontSize, (255, 255, 255), fontWeigth, 0.35)
    addTextImage(img, txt_version, fontSize,
                 (255, 255, 255), fontWeigth, 0.8)
    cv2.imwrite(url_image, img)


def createImages(listSizes, isIos=False):

    for size in listSizes:
        # crear carpeta
        if isIos:
            path = "./ios"
            url_image = f"{path}/{size['name']}"
        else:
            path = f"./android/" + size['name']
            url_image = f"{path}/launch_screen.png"
        if not os.path.exists(path):
            os.makedirs(path)
        # create image size
        size_x = int(size['size'].split("x")[0])
        size_y = int(size['size'].split("x")[1])
        createBaseImage(size_y, size_x, url_image)
        # HORIZONTAL
        if size_x > size_y:
            createImageHorizontal(url_image, isIos)
            print('create image horizontal: ' + url_image)

        # VERTICAL
        if size_x < size_y:
            createImageVertical(url_image, isIos)
            print('create image vertical: ' + url_image)
    print('---------------- Finalizacion de la creacion de imagenes ----------------')


# datos de la imagen
txt_version = "V1.0.10"
txt_one = 'example play store \n cargando.'
route_logo = './images/logo.png'


android = sizesAndroid()
createImages(android)
ios = sizesIos()
createImages(ios, True)
