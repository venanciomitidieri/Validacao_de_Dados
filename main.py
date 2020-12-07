import requests
from acesso_cep import BuscaEndereco

cep = 25065115
objeto_cep = BuscaEndereco(cep)
#print(objeto_cep)

#r = requests.get('https://viacep.com.br/ws/01001000/json/')
#print(type(r.text))

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(f'Bairro: {bairro},\nCidade: {cidade},\nUF: {uf}')
