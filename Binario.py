import numpy as np

# deixa a imagem Binaria
def imagemEmBinario(image):
    imagemBinario = np.zeros(image.shape)
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i, j] != 0:
                imagemBinario[i, j] = 255
    
    resultado = np.copy(imagemBinario) 
    
    return resultado
