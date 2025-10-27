import requests

def get_data(url):
    """
    Função reutilizável para realizar requisições HTTP GET.
    Usa a biblioteca 'requests' para simplificar chamadas HTTP.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print(f"[INFO] GET {url} -> {response.status_code}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha na requisição: {e}")
        return None
