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

        print(f"Imagem baixada com sucesso: {filename}")

    except Exception as e:
        print(f"Erro ao baixar a imagem: {str(e)}")

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
