import cv2
#caso uma forma adequada de aplicar seja encontrado
def Clahe(img):
    #separo os canais de cor da imagem
    canal_azul, canal_verde, canal_vermelho = cv2.split(img)

    #objeto clahe criado
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(2, 2))

    #clahe aplicado em cada canal
    clahe_azul = clahe.apply(canal_azul)
    clahe_verde = clahe.apply(canal_verde)
    clahe_vermelho = clahe.apply(canal_vermelho)
    
    clahe_img = cv2.merge((clahe_azul, clahe_verde, clahe_vermelho))

    return clahe_img