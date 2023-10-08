<h1 align="center"> Projeto de segmentação de folhas de várias espécies</h1> <br>
    <p>
            Segmentações feitas com intuito de suprir a ausências de segmentações em um dataset de folhas, com o intuito de inserir a LBP para um método de classificação.
        Segue abaixo algumas técnicas utilizadas na segmentação:
    </p>

<h2 align="center">1 -> Criação da Máscara(create_mask)<h2> <br>    
    <p float="left">Captura de dois intervalos da matiz verde, após a transformação da imagem para formato HSV, e juntando os intervalos com a função bitwise_or do opencv.
    </p>
    <p float="center">
    <img alt="Máscara" title="Máscara" src="/etapas_dos_resultados/mask.png" width="400"> 
    </p>

<h2 align="center">2 -> Aplicação do Fechamento<h2> <br>    
    <p float="left">Aplicação da técnica do fechamento para diminuição de lacunas menores na máscara da folha.
    </p>
    <p float="center">
    <img alt="Fechamento" title="Fechamento" src="/etapas_dos_resultados/fechamento.png" width="400"> 
    </p>