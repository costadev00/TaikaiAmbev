# IT-IT Identificação e Transcrição de Imagens em Texto
## Visão Geral  
Reconhecimento de padrões de texto em imagens é um desafio amplamente abordado na literatura e existem diversas abordagens para esse problema. A utilização de sistemas de reconhecimento ópticos em processos de automação é muito positiva, pois utiliza informações extraídas de documentos, evitando re digitalização e melhorando a estabilidade do sistema. Todavia nem sempre esses sistemas possuem grande acurácia, recentemente na literatura foi proposto um framework que tem como objetivos agrupar dados utilizando estruturas de grafos, mesmo que estes dados não sejam originalmente redes e ele se mostrou mais eficiente que métodos clássicos de clustrering. Acreditamos que a utilização de uma estrategia similar para agrupar os trechos de documentos pode aumentar a acurácia dos sistemas de reconhecimento óptico. Dividiremos essa tarefa em duas sub tarefas a primeira reconhecer diferentes partes ou parágrafos dos documentos utilizando um algorítimo convolucional e o segundo classificar cada uma dessas partes.

[Link da Apresentação do Projeto](https://github.com/newGabriel/TaikaiAmbev/blob/main/Desenho%20da%20Arquitetura.png)

### Problema  
Empresas diferentes utilizam templates diferentes utilizam modelos diferentes de notas, também é comum que uma mesma empresa altere o layout de suas notas com o passar do tempo. Criar modelos de OCR eficazes para cada uma desses modelos é um trabalho exaustivo e que consome muito tempo, além disso esses modelos perdem a precisão mesmo com pequenas alterações nas notas. Reconhecimento de padrões de texto em imagens é um trabalho amplamente abordado na literatura e existem diversas abordagens para esse problema. Utilizar essas técnicas evita redigitação de informações e aumenta a estabilidade do sistema permitindo a extração das informações direto dos documentos de imagem.

### Proposta de solução  
Dado uma imagem de um formulário o sistema reconhecerá cada bloco, os isolará e rotulara baseado nas informações extraídas do mesmo. Utilizando grafos e reconhecimento de padrões, para a extração dos dados necessários.

# Informações Técnicas
## Gráfico explicativo  
![](https://github.com/newGabriel/TaikaiAmbev/blob/main/Desenho%20da%20Arquitetura.png)  
> Diagrama da Arquitetura

## Pré requisitos
- Linux (Qualquer Distro) 
- Python 3.9  
- Bibliotecas: PyX(Canvas,Path,Color), Scikit-Learn, Math, PIL(Image), Pytesseract

## Processo de instalação e execução
### Instalação das Bibliotecas 
- PyX : pip install pyx
- PIL : pip install pillow
- Pytesseract: pip install pytesseract
- Scikit-Learn : pip install scikit
- Poetry : pip install --user poetry
### Execução do Projeto
- py nome_do_projeto.py
         
# Time

| [<img src="https://avatars.githubusercontent.com/u/70163650?v=4" width="115"><br><sub>@zGummy</sub>](https://github.com/zGummy) | [<img src="https://avatars.githubusercontent.com/u/62945890?v=4" width="115"><br><sub>@newGabriel</sub>](https://github.com/newGabriel)
|[<img src="https://avatars.githubusercontent.com/u/65378419?v=4" width="115"><br><sub>@PauloHenriqueAS</sub>](https://github.com/PauloHenriqueAS) |
| :---: | :---: |