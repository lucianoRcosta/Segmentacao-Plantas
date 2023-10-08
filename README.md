<h1 align="center"> Projeto de segmentação de folhas de várias espécies</h1> <br>
    <p>
            Segmentações feitas com intuito de suprir a ausências de segmentações em um dataset de folhas, com o intuito de inserir a LBP para um método de classificação.
        Segue abaixo algumas técnicas utilizadas na segmentação:
    </p>

<h2 align="center">1 -> Criação da Máscara(create_mask)<h2> <br>    
    <p float="left">Captura de dois intervalos da cor vermelha utilizando após a transformação da imagem para formato HSV e juntando os intervalos com a função bitwise_or do opencv.
    </p>
    <p float="center">
    <img alt="Máscara" title="Máscara" src="/etapas_dos_resultados/mask.png" width="400"> 
    </p>