import cv2
import numpy as np

#cria a máscara com as matizes verdes
def create_mask(img):
    #limite inferior e superior 1 de matiz de tonalidade verde
    intervalo_verde = (np.array([30, 20, 35]), np.array([100, 255, 255]))

    mask = cv2.inRange(img, *intervalo_verde)

    return mask

#função de checagem de contraste para aplicação de clahe
def contrast_check(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    histograma = cv2.calcHist([hsv], [2], None, [256], [0, 256])

    dispersao = np.max(histograma) - np.min(histograma)
    limite_dispersao = 10000

    if dispersao >= limite_dispersao:
        return clahe(img)
    else:
        return img

def clahe(img):
    #separação dos canais de cor da imagem
    canal_azul, canal_verde, canal_vermelho = cv2.split(img)

    #objeto clahe criado
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(3, 3))

    #clahe aplicado em cada canal
    clahe_azul = clahe.apply(canal_azul)
    clahe_verde = clahe.apply(canal_verde)
    clahe_vermelho = clahe.apply(canal_vermelho)
    
    #junção dos canais com clahe aplicado
    clahe_img = cv2.merge((clahe_azul, clahe_verde, clahe_vermelho))

    return clahe_img

#processo morfológico de fechamento
def fechamento(img):
    kernel = np.ones((3,3),np.uint8)
    fechamento = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=2) 

    return fechamento

#processo morfológico de abertura
def abertura(img):
    kernel = np.ones((2,2),np.uint8) # elemento estruturante
    abertura = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=3)

    return abertura

#função que encontra e desenha contornos
def find_draw_contours(img):
    #findContours sendo aplicada ao fechamento
    contornos, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contorno_final = maior_contorno(contornos)
    
    #cria máscara preta
    mascara_preta = np.zeros_like(img)
    
    #desenha contornos na máscara preta
    cv2.drawContours(mascara_preta, [contorno_final], -1, (255, 255, 255), thickness=cv2.FILLED)

    return mascara_preta
    
#função que encontra o maior contorno dentre a lista de contornos fornecida pela função findContours
def maior_contorno(contornos):
    maior_area = 0
    maior_contorno = None

    for contorno in contornos:
        area = cv2.contourArea(contorno)
    
        if area > maior_area:
            maior_area = area
            maior_contorno = contorno
    
    return maior_contorno

def filtro_de_sobel(img):
    #Aplicação do filtro
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    
    #operação or com os eixos x e y
    bordas = cv2.bitwise_or(np.absolute(sobelx), np.absolute(sobely))

    #junção borda com a máscara, uso do and porque as dimensões de mask e bordas são diferentes
    combinar = cv2.bitwise_and(bordas, bordas, mask=img)

    return bordas , combinar

#separação do fundo de imagem com a região de interesse
def background_separation(img1, img2, mask1):
    return cv2.bitwise_and(img1, img2, mask=mask1)