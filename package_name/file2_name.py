# Dentro de package_name/file2_name.py

from skimage import io
import matplotlib.pyplot as plt

def ler_imagem(caminho_do_arquivo):
    """
    Lê uma imagem a partir de um caminho e a retorna.
    """
    return io.imread(caminho_do_arquivo)


def mostrar_imagem(imagem, titulo='Imagem'):
    """
    Exibe uma imagem na tela.
    """
    # Define o mapa de cores como cinza para imagens em preto e branco
    io.imshow(imagem, cmap='gray')
    plt.title(titulo)
    plt.axis('off') # Remove os eixos x e y
    io.show()