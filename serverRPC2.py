import mysql.connector
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler



# Restringir a um determinado caminho

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Criando um Servidor

with SimpleXMLRPCServer(('192.168.0.122', 9000), # Definindo o IP da maquina servidor e a porta de conexao
		requestHandler=RequestHandler) as server:
	server.register_introspection_functions()

	def buscar_carro(nome):
			
		con = mysql.connector.connect(host='localhost',database='FIAT',user='root',password='102030hh')
		if con.is_connected():
			db_info = con.get_server_info()	
			print("Conectado ao servidor MySQL. v: ",db_info)
				
			cursor = con.cursor()
			cursor.execute("SELECT DATABASE();")
			linha = cursor.fetchone()
			print("Conectado ao banco de dados \n",linha)
				
			cursor.execute("SELECT modelo, preco FROM veiculos where modelo = '"+nome+"';")
			dados = cursor.fetchone()
			
			if dados == None: 
				error = "Veiculo nao encontrado na base de dados ", linha
				return error
			else: 
				print("Resultado da busca na base de dados VOLKS \n", dados)
				return dados
		if con.is_connected():
			cursor.close()
			con.close()
			print("Conexao ao MySQL foi finalizada")
				
	server.register_function(buscar_carro)

	server.serve_forever()
