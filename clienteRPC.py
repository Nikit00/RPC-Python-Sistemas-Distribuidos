import xmlrpc.client

s1 = xmlrpc.client.ServerProxy('http://192.168.0.121:9000')
s2 = xmlrpc.client.ServerProxy('http://192.168.0.122:9000')

nome = input("Digite o nome do carro: ")

print("VEICULO / PRECO \n", s1.buscar_carro(nome))
print("VEICULO / PRECO \n", s2.buscar_carro(nome))