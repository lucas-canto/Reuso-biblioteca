from http_module import get_data

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    data = get_data(url)
    if data:
        print("[SUCESSO] Dados recebidos:")
        for user in data[:3]:
            print(f"- {user['name']}")
