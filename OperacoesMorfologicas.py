import numpy as np
from ContornaImagem import imagemContornada



def erosao(imagem, oElementoEstruturante, contornosDeImagem):

    imagemQueIrarTerErosao = imagem

    correcao = int(len(oElementoEstruturante)/2)

    for i in range(len(imagemQueIrarTerErosao)):
        for j in range(len(imagemQueIrarTerErosao[0])):

            if contornosDeImagem[i, j] == 255:

                for k in range(len(oElementoEstruturante)):
                    for l in range(len(oElementoEstruturante[0])):

                        if oElementoEstruturante[k, l] != 0:
                            try:
                                imagemQueIrarTerErosao[i + k - correcao, j + k - correcao] = 0
                            except:
                                pass
    return imagemQueIrarTerErosao



def dilatar(imagem, oElementoEstruturante, contornosDeImagem):
    dilitarAImagem = imagem
    correcao = int(len(oElementoEstruturante)/2)

    for i in range(len(dilitarAImagem)):
        for j in range(len(dilitarAImagem[0])):
            if contornosDeImagem[i, j] == 255:
                for k in range(len(oElementoEstruturante)):
                    for l in range(len(oElementoEstruturante[0])):
                        if oElementoEstruturante[k, l] != 0:
                            try:
                                dilitarAImagem[i + k - correcao, j + k - correcao] = 255
                            except:
                                pass

    return dilitarAImagem





def abertura(imagem, oElementoEstruturante, contornosDeImagem):
    copiaDaImagem = np.copy(imagem)
    imagemComErosao = erosao(copiaDaImagem, oElementoEstruturante, contornosDeImagem)
    imagemComContornacao = imagemContornada(imagemComErosao)
    imagemComAbertura = dilatar(imagemComErosao, oElementoEstruturante, imagemComContornacao)

    return imagemComAbertura


def fechamento(imagem, oElementoEstruturante, contornosDeImagem):
    copiaDaImagem = np.copy(imagem)
    imagemComdilatacao = dilatar(copiaDaImagem, oElementoEstruturante, contornosDeImagem)
    imagemComContornacao = imagemContornada(imagemComdilatacao)
    imagemComFechamento = erosao(imagemComdilatacao, oElementoEstruturante, imagemComContornacao)

    return imagemComFechamento
