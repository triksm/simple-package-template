# Meu Pacote de Imagens

Este pacote é um exemplo para aprender a criar pacotes em Python. Ele contém funções para ler imagens e convertê-las para escala de cinza.

## Instalação

Use o gerenciador de pacotes pip para instalar:
```pip install seu-nome-de-pacote-unico```

## Uso

```python
# Importe as funções dos seus módulos
from package_name import file1_name, file2_name

# Leia uma imagem do seu computador
caminho = 'caminho/para/sua/imagem.jpg'
imagem = file2_name.ler_imagem(caminho)

# Converta para escala de cinza
imagem_cinza = file1_name.para_escala_de_cinza(imagem)

# Mostre o resultado
file2_name.mostrar_imagem(imagem_cinza, titulo='Resultado em Cinza')