import argparse
from PIL import Image
import numpy as np

def process_image(img_path):
    # Carregar a imagem
    img = Image.open(img_path)

    # Converter a imagem para tons de cinza
    img_gray = img.convert('L')

    # Redimensionar a imagem para 8x8 pixels
    img_resized = img_gray.resize((8, 8))

    # Converter a imagem redimensionada para um array numpy
    img_array = np.array(img_resized)

    # Definir um limiar para distinguir quadrículas escuras (ajustável conforme necessário)
    threshold = 110

    # Criar o bitmap
    bitmap = (img_array < threshold).astype(int)

    # Converter o bitmap para uma lista para facilitar a visualização
    bitmap_list = bitmap.tolist()

    # Imprimir o bitmap
    for row in bitmap_list:
        print(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a 8x8 grid image to generate a bitmap.')
    parser.add_argument('img_path', type=str, help='Path to the image file')
    args = parser.parse_args()

    process_image(args.img_path)
