import cv2
import os
import numpy as np

# img = cv2.imread('dataset/0a2de4c5-d688-4f9d-9107-ace1d281c307___Com.G_TgS_FL 7941_180deg.JPG')

pasta_imgs = 'dataset/'
arquivos = os.listdir(pasta_imgs)

for arq in arquivos:

    if arq.lower().endswith('jpg'):
        caminho_img = os.path.join(pasta_imgs, arq)
        img = cv2.imread(caminho_img)

        if img is not None:
            #aplicar borramento gaussiano para reduzir ruídos
            borrado_mask = cv2.GaussianBlur(img, (3, 3), 0)
            borrado_sobel = cv2.GaussianBlur(img, (15, 15), 0)

            #converte imagem para o espaço de cores hsv
            hsv = cv2.cvtColor(borrado_mask, cv2.COLOR_BGR2HSV)

            #limite inferior e superior 1 de matiz de tonalidade verde
            lower_green_1 = np.array([35, 50, 50])  
            upper_green_1 = np.array([50, 255, 255])

             #limite inferior e superior 2 de matiz de tonalidade verde
            lower_green_2 = np.array([50, 50, 50])  
            upper_green_2 = np.array([85, 255, 255])

            mask1 = cv2.inRange(hsv, lower_green_1, upper_green_1)
            mask2 = cv2.inRange(hsv, lower_green_2, upper_green_2)

            mask = cv2.bitwise_or(mask1, mask2)

            #FILTRO DE SOBEL
            #Aplicação do filtro
            sobelx = cv2.Sobel(borrado_sobel, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(borrado_sobel, cv2.CV_64F, 0, 1, ksize=3)
            bordas = cv2.bitwise_or(np.absolute(sobelx), np.absolute(sobely))

            cv2.imshow('Imagem original', img)
            cv2.imshow('Máscara Binária', mask)
            cv2.imshow('Bordas', bordas)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print(f'Erro ao carregar imagem {arq}')