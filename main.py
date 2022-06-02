from PIL import Image
import os

from modules.modules import addTextImage,  createBaseImage, overlayImage
from modules.sizes import sizesAndroid, sizesIos


def createImageHorizontal(url_image, fontSize, font):
    image = Image.open(url_image)
    logo = Image.open(route_logo)
    # calcular el tamaño del logo y centrarlo
    logo_resize = logo.resize(
        (int((image.height * 0.5) / 2), int((image.height * 0.5) / 2)))
    position = (int((image.width - logo_resize.width) / 2),
                int((image.height - logo_resize.height) * 0.7))
    overlayImage(logo_resize, position, url_image)
    # se añade el trecto a la imagen
    addTextImage(url_image, txt_one, fontSize, (255, 255, 255), 0.2, font)
    addTextImage(url_image, txt_version, fontSize, (255, 255, 255),  0.9, font)
    print('create image: ' + url_image)


def createImageVertical(url_image, fontSize, font):
    image = Image.open(url_image)
    logo = Image.open(route_logo)
    # calcular el tamaño del logo y centrarlo
    logo_resize = logo.resize(
        (int((image.width * 0.5) / 2), int((image.width * 0.5) / 2)))
    position = (int((image.width - logo_resize.width) / 2),
                int((image.height - logo_resize.height) * 0.7))
    overlayImage(logo_resize, position, url_image)
    # se añade el trecto a la imagen
    addTextImage(url_image, txt_one, fontSize, (255, 255, 255), 0.35, font)
    addTextImage(url_image, txt_version, fontSize, (255, 255, 255),  0.8, font)


def createImages(listSizes, font, isIos=False):

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
            createImageHorizontal(url_image,  size['fontSize'], font)
            print('create image horizontal: ' + url_image)

        # VERTICAL
        if size_x < size_y:
            createImageVertical(url_image,  size['fontSize'], font)
            print('create image vertical: ' + url_image)
    print('---------------- Finalizacion de la creacion de imagenes ----------------')


# datos de la imagen
font = "./fonts/Montserrat/static/Montserrat-ExtraBold.ttf"
txt_version = "V 3.0.2"
txt_one = 'Example play store \n loading.'
route_logo = './images/logo.png'


android = sizesAndroid()
createImages(android, font)
ios = sizesIos()
createImages(ios, font, True)
