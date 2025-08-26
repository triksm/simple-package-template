# Dentro de package_name/file1_name.py

import numpy as np

def para_escala_de_cinza(imagem_colorida):
    """
    Converte uma imagem RGB para escala de cinza.
    """
    # Verifica se a imagem é colorida
    if imagem_colorida.ndim != 3 or imagem_colorida.shape[2] != 3:
        raise ValueError("A imagem de entrada deve ser colorida (RGB).")

    # Fórmula padrão para conversão para escala de cinza
    return np.dot(imagem_colorida[...,:3], [0.2989, 0.5870, 0.1140])