import cv2
import os
from functions import *

if __name__ == '__main__':
    # img = cv2.imread('dataset/0a2de4c5-d688-4f9d-9107-ace1d281c307___Com.G_TgS_FL 7941_180deg.JPG')

    pasta_imgs = 'dataset1/'
    arquivos = os.listdir(pasta_imgs)

    #loop que pega os arquivos na pasta dataset
    for arq in arquivos:
        #condição que checa se o arquivo termina com a extensão .jpg
        if arq.lower().endswith('jpg'):
            caminho_img = os.path.join(pasta_imgs, arq)
            img = cv2.imread(caminho_img)

            #condição que checa se img não está vazio
            if img is not None:           
                #recebe a função de checagem de contraste
                img_contrast_check = contrast_check(img)

                #aplicar borramento gaussiano para reduzir ruídos
                borrado_mask = cv2.GaussianBlur(img_contrast_check, (3, 3), 0) #mais pixels = menos ruído e mais imperfeições!

                # imagem_tons_de_cinza = cv2.cvtColor(borrado_mask, cv2.COLOR_BGR2GRAY)

                # _, binarized_image = cv2.threshold(imagem_tons_de_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

                # cv2.imshow("Otsu", binarized_image)

                # converte imagem para o espaço de cores hsv
                hsv = cv2.cvtColor(borrado_mask, cv2.COLOR_BGR2HSV)
                
                mask = create_mask(hsv)
                
                mask_fechamento = fechamento(mask)  
                
                mask_contornos = find_draw_contours(mask_fechamento)
                
                bordas, combinar = filtro_de_sobel(mask_contornos)

                cv2.imshow('Imagem original', img)
                cv2.imshow('Máscara da matiz', mask)
                cv2.imshow('Bordas', bordas)
                cv2.imshow('Junção da Máscara e Bordas', combinar)
                # cv2.imshow('Abertura', abertura)
                cv2.imshow('Fechamento', mask_fechamento)
                cv2.imshow('Maior Contorno', mask_contornos)

                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print(f'Erro ao carregar imagem {arq}')