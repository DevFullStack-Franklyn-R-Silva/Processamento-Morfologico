import cv2 as cv
from skimage import io
from Binario import imagemEmBinario
from ContornaImagem import imagemContornada
from OperacoesMorfologicas import dilatar, erosao, abertura, fechamento

caminhoDaImagens = "./imagens/"

imagemOriginal = cv.cvtColor(io.imread(caminhoDaImagens + "imgPaint.png"), cv.COLOR_RGBA2GRAY)
imagemBinaria = imagemEmBinario(imagemOriginal)

#Exiber a imagem original
cv.imshow('Imagem Original', imagemBinaria)



imagemComContorno= imagemContornada(imagemBinaria)

oElementoEstruturante = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15,15))



# OPERAÇÕES DE EROSÃO E DILATAÇÃO
img_erodida = erosao(imagemBinaria, oElementoEstruturante, imagemComContorno)
cv.imshow('Imagem Erosão', img_erodida)

img_dilatada = dilatar(imagemBinaria, oElementoEstruturante, imagemComContorno)
cv.imshow('Imagem Dilatada', img_dilatada)


# OPERAÇÕES ABERTURA E FECHAMENTO

imagemComAbertura = abertura(imagemBinaria, oElementoEstruturante, imagemComContorno)
cv.imshow('Imagem Abertura', imagemComAbertura)

imagemComFechamento = fechamento(imagemBinaria, oElementoEstruturante, imagemComContorno)
cv.imshow('Imagem Fechamento', imagemComFechamento)

cv.waitKey(0)