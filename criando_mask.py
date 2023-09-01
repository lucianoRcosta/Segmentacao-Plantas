import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from clahe import Clahe
 
def contrast_check(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    histograma = cv2.calcHist([hsv], [2], None, [256], [0, 256])

    dispersao = np.max(histograma) - np.min(histograma)
    limite_dispersao = 14000

    if dispersao >= limite_dispersao:
        return Clahe(img)
    else:
        return img
    
#função temporária
def maior_contorno(contornos):
    maior_area = 0
    maior_contorno = None
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > maior_area:
            maior_area = area
            maior_contorno = contorno
    return maior_contorno


if __name__ == '__main__':
    # img = cv2.imread('dataset/0a2de4c5-d688-4f9d-9107-ace1d281c307___Com.G_TgS_FL 7941_180deg.JPG')

    pasta_imgs = 'dataset/'
    arquivos = os.listdir(pasta_imgs)

    for arq in arquivos:

        if arq.lower().endswith('jpg'):
            caminho_img = os.path.join(pasta_imgs, arq)
            img = cv2.imread(caminho_img)

            if img is not None:
                #recebe a função de checagem de contraste
                img_contrast_check = contrast_check(img)

                #aplicar borramento gaussiano para reduzir ruídos
                borrado_mask = cv2.GaussianBlur(img_contrast_check, (3, 3), 0) #mais pixels = menos ruído e mais imperfeições!

                #converte imagem para o espaço de cores hsv
                hsv = cv2.cvtColor(borrado_mask, cv2.COLOR_BGR2HSV)
                
                #limite inferior e superior 1 de matiz de tonalidade verde
                lower_green_1 = np.array([25, 20, 35])  
                upper_green_1 = np.array([90, 255, 255])

                mask1 = cv2.inRange(hsv, lower_green_1, upper_green_1)

                #processo morfológico de fechamento
                kernel = np.ones((3,3),np.uint8)
                fechamento = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel, iterations=2)   
                
                #findContours sendo aplicada ao fechamento
                contornos, _ = cv2.findContours(fechamento, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                contorno_final = maior_contorno(contornos)
                mascara_preta = np.zeros_like(img)
                
                #desenha contornos na máscara preta
                cv2.drawContours(mascara_preta, [contorno_final], -1, (255, 255, 255), thickness=cv2.FILLED)

                #processo morfológico de abertura
                # kernel = np.ones((2,2),np.uint8)
                # abertura = cv2.morphologyEx(fechamento, cv2.MORPH_OPEN, kernel, iterations=3)
                
                #FILTRO DE SOBEL
                #Aplicação do filtro
                sobelx = cv2.Sobel(fechamento, cv2.CV_64F, 1, 0, ksize=3)
                sobely = cv2.Sobel(fechamento, cv2.CV_64F, 0, 1, ksize=3)
                bordas = cv2.bitwise_or(np.absolute(sobelx), np.absolute(sobely))

                #junção borda com a máscara, uso o and pq as dimensões de mask e bordas são diferentes
                combinar = cv2.bitwise_and(bordas, bordas, mask=fechamento)

                cv2.imshow('Imagem original', img)
                cv2.imshow('Máscara da matiz', mask1)
                cv2.imshow('Bordas', bordas)
                cv2.imshow('Junção da Máscara e Bordas', combinar)
                # cv2.imshow('Abertura', abertura)
                cv2.imshow('Fechamento', fechamento)
                cv2.imshow('Máscara com Maior Contorno', mascara_preta)

                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print(f'Erro ao carregar imagem {arq}')