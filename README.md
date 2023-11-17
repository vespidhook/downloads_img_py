# Download de Imagens com Python

Este script Python simplificado permite baixar imagens da web usando a biblioteca `requests`. Você pode fornecer uma lista de URLs de imagens para baixar. O script cria um diretório chamado 'images' (se ainda não existir) e salva as imagens baixadas nesse diretório. 📸

## Pré-requisitos

Certifique-se de ter a biblioteca `requests` instalada antes de executar o script. Você pode instalá-la usando o seguinte comando: 🛠️

```bash
pip install requests
```

## Como usar

1. Clone este repositório ou copie o conteúdo do script para o seu ambiente.

2. Execute o script Python.

```python
python script.py
```

O script baixará cada imagem da lista de URLs fornecida e as salvará no diretório 'images'. 🚀

## Exemplo

```python
import requests
import os

def download_image(url, folder='images'):
    try:
        # Verifica se o diretório existe, se não, cria-o
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Obtém o nome do arquivo a partir da URL
        filename = os.path.join(folder, url.split('/')[-1])

        # Faz o download da imagem
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)

        print(f"Imagem baixada com sucesso: {filename} 🎉")

    except Exception as e:
        print(f"Erro ao baixar a imagem: {str(e)} ❌")

if __name__ == "__main__":
    # URLs das imagens
    image_urls = [  
        'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png',
        'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png',
        '...'
    ]

    # Baixa cada imagem
    for url in image_urls:
        download_image(url)
```

Certifique-se de substituir `'...'` na lista `image_urls` pelos URLs reais das imagens que deseja baixar. 🌐
