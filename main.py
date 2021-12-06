import requests
import json

def busca_cep(cep):
    api_url = f"https://viacep.com.br/ws/{cep}/json/"
    request = requests.get(api_url)
    result = json.loads(request.content)
    cepnum = result['cep']
    endereco = result['logradouro']
    bairro = result['bairro']
    cidade = result['localidade']
    uf = result['uf']
    print(f"CEP: {cepnum}, Endereço: {endereco}, Bairro: {bairro}, Cidade: {cidade}, UF: {uf}")


cep = input("Digite o CEP: ")
busca_cep(cep)