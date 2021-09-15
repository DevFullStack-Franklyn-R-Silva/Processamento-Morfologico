# Processamento Morfológico

#### 🏫 Universidade Federal de Alagoas - UFAL *Ciência da Computação* - *Campus. Arapiraca*.

#### 📽 Projeto Final da disciplina de Processamento de Imagens
* Professor:
    👨‍🏫Tácito Trindade de Araújo Tiburtino Neves
* Aluno:
    👨‍🎓Franklyn Roberto da Silva

### 🔴Descrição geral do projeto
O objetivo principal do trabalho é avaliar de forma prática o entendimento dos conceitos apresentados.
Este projeto contém algorítmos operações morfológicas nas imagens que são: Dilatação, Erosão, Abertura e Fechamento.

Algumas coisas tem base nesse site: https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html

### ⚠Onde foi rodado o software❔
> Notebook
>
> Windows 10 Home, Versão: 21H1
>
> Fabricante do sistema: Dell Inc.
> 
> Modelo do sistema: Inspirion 3442
> 
> BIOS: A15
> 
> Versão do DirectX 12
> 
> Processador: Intel(R) Core(TM) i5-4210U CPU @ 1.70GHz (4 CPUs), 1.70 GHz
> 
> Placa de vídeo: NVIDIA GeForce 820M, VRAM 2 GB
> 
> Memória RAM: 8 Gb 

### ⚠O que precisa para rodar o algoritimo❔
* Ambiente Windows 10
* Python 3.9.5

Com o python instalado, precisa instalar uns pacotes para o projeto funcionar, que são:
> pip install numpy
> 
> pip install opencv-python
> 
> pip install pip install -U scikit-image

Após instalado os pacotes acima, execute o comando abaixo para inicializar o projeto.

>python .\Program.py

O algorítmos pode demorar um pouco, então aguarde exibir as telas com as imagens processadas.

⚠Obs: Toda implementação está nos respectivos arquivos no GitHub💢

### 🟠Como funciona o código❔
>O código permite a escolha de uma imagem como entrada,
e a saída do algoritmo será o resultado da aplicação das operações de morfologia: dilatação, erosão, abertura e fechamento.

### 🟢O funcionamento❕
Para realizar as operações de processamento morfológicos, na implementação é necessário ter uma imagem de preferência preto e branco, para obter o contorno dessa imagem de entrada.
Pois, no arquivo de entrada (Program.py) realiza-se estes pré-requisitos para garantir a execução correta dos algorítmos.

```python
"""
Imports omitidos
"""

imagem_original = cv.cvtColor(io.imread(caminho_imagens + "img01.png"), cv.COLOR_RGBA2GRAY)
imagem_binaria = binarizar(imagem_original)

img_contornada = gerar_imagem_contornada(imagem_binaria)

```






