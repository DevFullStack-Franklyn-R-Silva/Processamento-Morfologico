import numpy as np
from skimage.measure import find_contours
import cv2 as cv

# gerar uma imagem contornada
def imagemContornada(imagem):
    contornosDaImagem = np.zeros(imagem.shape + (3, ), np.uint8)

    contornos = find_contours(imagem, 0)

    for contorno in contornos:

        contorno = contorno.astype(np.int).tolist()
        
        # Aqui desenhar linhas de contorno
        for idx, coords in enumerate(contorno[:-1]):
            y1, x1, y2, x2 = coords + contorno[idx + 1]
            contornosDaImagem = cv.line(contornosDaImagem, (x1, y1), (x2, y2),(0, 255, 0), 1)
        
    contornosDaImagem = contornosDaImagem[:,:,1]

    return contornosDaImagem

