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

<h3 align="center">3 -> Aplicação do Maior Contorno(find_draw_contours e maior_contorno)<h3> <br>    
    <p float="left"> Utilização da função findContours do opencv e a utilização de uma função de comparação(maior_contorno), que compara os valores retornados por contourArea e procura o maior contorno.
    </p>
    <p float="center">
    <img alt="Fechamento" title="Fechamento" src="/etapas_dos_resultados/maior_contorno.png" width="400"> 
    </p>

<h4 align="center">4 -> Remoção do Fundo da Imagem(background_separation)<h4> <br>    
    <p float="left">Utilizando o bitwise_and, junto do maior contorno, separemos a folha do fundo da imagem.</p>
    <p float="center">
    <img alt="Fechamento" title="Fechamento" src="/etapas_dos_resultados/no_background.png" width="400"> 
    </p>