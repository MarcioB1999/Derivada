
# Esta tarefa consiste em:
# 
# 1) Assistir ao vídeo https://www.youtube.com/watch?v=waNQ-7ckw0I
# 
# 2) Desenvolver as máscaras de derivada discutidas no vídeo
# 
# 3) Implementar o detector de bordas discutido no vídeo
# 
# 3.1) Ler uma imagem em escala de cinzas (ou ler imagem colorida e transformar para escala de cinzas)
# 
# 3.2) Ampliar a imagem para que ela tenha dois pixels a mais na direção horizontal (uma coluna de pixels à esquerda da imagem e uma coluna de pixels à direita da imagem) e dois pixels a mais na direção vertical (uma linha de pixels no topo da imagem e uma linha na base da imagem). Esses pixels adicionais terão valor de intensidade iguais a zero.
# 
# 3.3) usar uma máscara de derivada (abordagem central) e aplicá-la a cada pixel da imagem ampliada que não seja um pixel de borda. O resultado da aplicação da máscara sobre um pixel é copiado no pixel correspondente de uma imagem nova.
# 
# 3.4) Exibir a imagem original e a imagem nova.

# Inicia em 19/03/2020 às 00h00 e finaliza em 02/04/2020 às 23h59



import sys
import platform
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

def deriva(a, b):
    return (b-a)/2

def rgb_to_gray(rgb):
    #Y' = 0.2989 R + 0.5870 G + 0.1140 B 
    return np.dot(rgb[...], [0.2989, 0.5870, 0.1140])

def bordas_X(image):
    x, y = image.shape
    new_image = image.copy()
    
    for i in range(x-1):
        for j in range(y-1):
            new_image[i][j] = abs(deriva(image[i][j-1], image[i][j+1]))
            
    return new_image

def bordas_Y(image):
    x, y = image.shape
    new_image = image.copy()
    
    for i in range(x-1):
        for j in range(y-1):
            new_image[i][j] = abs(deriva(image[i-1][j], image[i+1][j]))
            
    return new_image

def bordas_XY(image):
    x, y = image.shape
    new_image = image.copy()
    
    for i in range(x-1):
        for j in range(y-1):
            new_image[i][j] = abs(deriva(image[i-1][j], image[i+1][j]) + deriva(image[i][j-1], image[i][j+1]))
            
    return new_image

def ler_imagem(img_name):
    img = io.imread(img_name)
    
    plt.figure(figsize=(12,12))
    plt.title('Imagem original',size='xx-large')
    plt.imshow(img)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    img = img[...,:3]
    img = rgb_to_gray(img)
    
    return img
    
def ampliar_imagem(img):
    new_img = np.zeros((img.shape[0]+2,img.shape[1]+2))
    new_img[1:img.shape[0]+1, 1:img.shape[1]+1] = img 
    
    return new_img

def plotar(f,img,img_name):
    conv=f(img)
    
    plt.figure(figsize=(12,12))
    plt.title(f.__name__,size='xx-large')
    plt.imshow(conv, cmap='gray')
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.savefig(img_name.split('.')[0] + '_bordas.png',cmap='gray')
    plt.show()


if __name__ == '__main__':
    if platform.system() == 'Linux':
        img_name=sys.argv[1]
    else:
        img_name=str(input('Digite o nome da imagem com a extensão'))
        
    f = bordas_XY
    #f=bordas_Y
    #f=bordas_X

    img = ler_imagem(img_name)
    new_img = ampliar_imagem(img)
    plotar(f,new_img,img_name)