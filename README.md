# BirdLens

Bem-vindo ao projeto BirdLens! Este projeto é dedicado à observação e identificação de aves utilizando técnicas de visão computacional.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/BirdLens.git
```
2. Navegue até o diretório do projeto:

```bash
cd BirdLens
```
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como usar

**Para usar vídeos próprios:** 
    
    Prepare seu vídeo de entrada (em formato MP4 ou outro suportado pelo OpenCV) e coloque-o na pasta 'bird_lens/data/'. No arquivo run.py, defina o caminho para o vídeo:

```python
VIDEO_PATH = os.path.join(BASE_DIR, 'bird_lens', 'data', 'seu_video.mp4')
```

**Para usar uma câmera / webcam:**

    Garanta acesso à câmera / webcam. No arquivo run.py, defina o caminho para o vídeo:

```python
VIDEO_PATH = -1
```

1. Execute o script:

```bash
python run.py
```

2. Para sair, basta pressionar Esc ou fechar a janela.